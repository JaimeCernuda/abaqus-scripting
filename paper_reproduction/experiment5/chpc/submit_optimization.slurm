#!/bin/bash
#SBATCH --job-name=exp5_tosca
#SBATCH --account=owner-gpu-guest
#SBATCH --partition=kingspeak
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --time=24:00:00
#SBATCH --mem=32G
#SBATCH -o exp5_tosca_%j.out
#SBATCH -e exp5_tosca_%j.err
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=${CHPC_EMAIL:-}

# ============================================================================
# Experiment 5: Topology Optimization on CHPC (full pipeline)
# ============================================================================

unset SLURM_GTIDS
export I_MPI_HYDRA_TOPOLIB=ipl

# Load Abaqus module
source /uufs/chpc.utah.edu/sys/installdir/abaqus/setup_ab_slurm.sh

# Set environment
export ABAQUS_MESH_SIZE=3.0
export ABAQUS_NUM_CPUS=$SLURM_NTASKS

cd $HOME/Abaqus/paper_reproduction/experiment5

echo "============================================"
echo "Experiment 5: Topology Optimization"
echo "Started: $(date)"
echo "Nodes: $SLURM_NNODES, Tasks: $SLURM_NTASKS"
echo "============================================"

# Step 1: Create design space
echo ""
echo "[1/6] Creating design space..."
abaqus cae noGUI=scripts/create_design_space.py
if [ $? -ne 0 ]; then
    echo "ERROR: Design space creation failed"
    exit 1
fi

# Step 2: Setup optimization
echo ""
echo "[2/6] Setting up optimization..."
abaqus cae noGUI=scripts/setup_optimization.py
if [ $? -ne 0 ]; then
    echo "ERROR: Optimization setup failed"
    exit 1
fi

# Step 3: Run topology optimization
echo ""
echo "[3/6] Running topology optimization..."
abaqus optimization job=Experiment5_TO cpus=$SLURM_NTASKS interactive
if [ $? -ne 0 ]; then
    echo "ERROR: Optimization run failed"
    exit 1
fi

# Step 4: Extract results
echo ""
echo "[4/6] Extracting results..."
abaqus python scripts/extract_results.py

# Step 5: Extract convergence history
echo ""
echo "[5/6] Extracting convergence history..."
abaqus python scripts/monitor_convergence.py || echo "WARNING: Convergence extraction failed"

# Step 6: Capture density contour screenshots
echo ""
echo "[6/6] Capturing screenshots..."
mkdir -p screenshots
if command -v xvfb-run &> /dev/null; then
    xvfb-run -a abaqus cae script=scripts/capture_to_results.py || echo "WARNING: Screenshot capture failed"
elif command -v Xvfb &> /dev/null; then
    Xvfb :99 -screen 0 1024x768x24 &
    XVFB_PID=$!
    export DISPLAY=:99
    sleep 2
    abaqus cae script=scripts/capture_to_results.py || echo "WARNING: Screenshot capture failed"
    kill $XVFB_PID 2>/dev/null
else
    echo "WARNING: No Xvfb available, skipping screenshots"
fi

echo ""
echo "============================================"
echo "Experiment 5: Topology Optimization Complete"
echo "Finished: $(date)"
echo "============================================"
