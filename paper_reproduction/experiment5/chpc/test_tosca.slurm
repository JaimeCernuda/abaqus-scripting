#!/bin/bash
#SBATCH --job-name=test_tosca
#SBATCH --account=owner-gpu-guest
#SBATCH --partition=kingspeak
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --time=2:00:00
#SBATCH --mem=16G
#SBATCH -o test_tosca_%j.out
#SBATCH -e test_tosca_%j.err

# ============================================================================
# Stage 2: Prove Tosca license works — run 3-iteration optimization
# ============================================================================

unset SLURM_GTIDS
export I_MPI_HYDRA_TOPOLIB=ipl

source /uufs/chpc.utah.edu/sys/installdir/abaqus/setup_ab_slurm.sh

export ABAQUS_MESH_SIZE=3.0
export ABAQUS_NUM_CPUS=$SLURM_NTASKS

cd $HOME/Abaqus/paper_reproduction/experiment5

echo "============================================"
echo "Stage 2: Tosca License Test (3 iterations)"
echo "Started: $(date)"
echo "Nodes: $SLURM_NNODES, Tasks: $SLURM_NTASKS"
echo "============================================"

# Step 1: Create design space
echo ""
echo "[1/4] Creating design space..."
abaqus cae noGUI=scripts/create_design_space.py
if [ $? -ne 0 ]; then
    echo "FAILED: Design space creation failed"
    exit 1
fi

# Step 2: Setup optimization
echo ""
echo "[2/4] Setting up optimization..."
abaqus cae noGUI=scripts/setup_optimization.py
if [ $? -ne 0 ]; then
    echo "FAILED: Optimization setup failed"
    exit 1
fi

# Step 3: Run 3-iteration topology optimization (quick test)
echo ""
echo "[3/4] Running topology optimization (3 iterations only)..."
abaqus optimization job=Experiment5_TO cpus=$SLURM_NTASKS interactive maxDesignCycle=3
OPT_EXIT=$?

if [ $OPT_EXIT -ne 0 ]; then
    echo "FAILED: Optimization failed (exit code: $OPT_EXIT)"
    echo "  Check if Tosca license is available:"
    echo "  abaqus licensing lmstat -a"
    exit 1
fi

# Check that TOSCA_POST was created
if [ -d "Experiment5_TO/TOSCA_POST" ]; then
    ODB_COUNT=$(ls Experiment5_TO/TOSCA_POST/*.odb 2>/dev/null | wc -l)
    echo "PASSED: Tosca ran — ${ODB_COUNT} design cycle ODBs in TOSCA_POST"
else
    echo "WARNING: TOSCA_POST directory not found"
    echo "  Checking alternate locations..."
    find . -name "TOSCA_POST" -type d 2>/dev/null
fi

# Step 4: Capture density screenshot
echo ""
echo "[4/4] Capturing density contour screenshots..."
mkdir -p screenshots

if command -v xvfb-run &> /dev/null; then
    xvfb-run -a abaqus cae script=scripts/capture_to_results.py
elif command -v Xvfb &> /dev/null; then
    Xvfb :99 -screen 0 1024x768x24 &
    XVFB_PID=$!
    export DISPLAY=:99
    sleep 2
    abaqus cae script=scripts/capture_to_results.py
    kill $XVFB_PID 2>/dev/null
else
    echo "WARNING: No Xvfb available, skipping screenshots"
fi

if ls screenshots/density_*.png 1>/dev/null 2>&1; then
    echo "PASSED: Density screenshots captured"
else
    echo "WARNING: No density screenshots (Tosca still passed)"
fi

echo ""
echo "============================================"
echo "Stage 2 Complete: $(date)"
echo "============================================"
