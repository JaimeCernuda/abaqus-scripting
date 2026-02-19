#!/bin/bash
#SBATCH --job-name=exp5_tosca
#SBATCH --account=hochhalter
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
# Uses writeParAndInputFiles() + abaqus optimization CLI (avoids submit()
# segfault in noGUI/script= mode).
# ============================================================================

unset SLURM_GTIDS
export I_MPI_HYDRA_TOPOLIB=ipl

# Load Abaqus module
source /uufs/chpc.utah.edu/sys/installdir/abaqus/setup_ab_slurm.sh

# Set environment
export ABAQUS_MESH_SIZE=3.0
export ABAQUS_NUM_CPUS=$SLURM_NTASKS
export ABAQUS_MAX_CYCLES=50

cd $HOME/Abaqus/paper_reproduction/experiment5

echo "============================================"
echo "Experiment 5: Topology Optimization"
echo "Started: $(date)"
echo "Nodes: $SLURM_NNODES, Tasks: $SLURM_NTASKS"
echo "Max design cycles: $ABAQUS_MAX_CYCLES"
echo "============================================"

# Step 1: Create design space
echo ""
echo "[1/5] Creating design space..."
abaqus cae noGUI=scripts/create_design_space.py
if [ $? -ne 0 ]; then
    echo "ERROR: Design space creation failed"
    exit 1
fi

# Step 2: Setup optimization (generates .par file via writeParAndInputFiles)
echo ""
echo "[2/5] Setting up optimization..."
abaqus cae noGUI=scripts/setup_optimization.py
if [ $? -ne 0 ]; then
    echo "ERROR: Optimization setup failed"
    exit 1
fi

# Find the .par file
PAR_FILE=$(find . -name "*.par" -type f 2>/dev/null | head -1)
if [ -z "$PAR_FILE" ]; then
    echo "ERROR: No .par file generated"
    exit 1
fi
echo "  .par file: $PAR_FILE"

# Step 3: Run Tosca via CLI
echo ""
echo "[3/5] Running Tosca optimization via CLI..."
abaqus optimization task="$PAR_FILE" job=Experiment5_TO cpus=$SLURM_NTASKS interactive 2>&1
OPT_EXIT=$?

if [ $OPT_EXIT -ne 0 ]; then
    echo "  First attempt failed (exit $OPT_EXIT), retrying without cpus..."
    abaqus optimization task="$PAR_FILE" job=Experiment5_TO interactive 2>&1
    OPT_EXIT=$?
fi

if [ $OPT_EXIT -ne 0 ]; then
    echo "ERROR: Tosca optimization failed"
    exit 1
fi

# Step 4: Extract results
echo ""
echo "[4/5] Extracting results..."
abaqus python scripts/extract_results.py

# Step 5: Extract convergence history
echo ""
echo "[5/5] Extracting convergence history..."
abaqus python scripts/monitor_convergence.py || echo "WARNING: Convergence extraction failed"

echo ""
echo "============================================"
echo "Experiment 5: Topology Optimization Complete"
echo "Finished: $(date)"
echo "============================================"
