#!/bin/bash
#SBATCH --job-name=test_tosca
#SBATCH --account=hochhalter
#SBATCH --partition=kingspeak
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --time=2:00:00
#SBATCH --mem=16G
#SBATCH -o test_tosca_%j.out
#SBATCH -e test_tosca_%j.err

# ============================================================================
# Stage 2: Prove Tosca license works — run topology optimization
# Uses writeParAndInputFiles() + abaqus optimization CLI (avoids submit()
# segfault in noGUI/script= mode).
# ============================================================================

unset SLURM_GTIDS
export I_MPI_HYDRA_TOPOLIB=ipl

source /uufs/chpc.utah.edu/sys/installdir/abaqus/setup_ab_slurm.sh

export ABAQUS_MESH_SIZE=3.0
export ABAQUS_NUM_CPUS=$SLURM_NTASKS
export ABAQUS_MAX_CYCLES=3

cd $HOME/Abaqus/paper_reproduction/experiment5

echo "============================================"
echo "Stage 2: Tosca License Test"
echo "Started: $(date)"
echo "Nodes: $SLURM_NNODES, Tasks: $SLURM_NTASKS"
echo "Max design cycles: $ABAQUS_MAX_CYCLES"
echo "============================================"

# Step 1: Create design space
echo ""
echo "[1/3] Creating design space..."
abaqus cae noGUI=scripts/create_design_space.py
if [ $? -ne 0 ]; then
    echo "FAILED: Design space creation failed"
    exit 1
fi

# Step 2: Setup optimization (generates .par file via writeParAndInputFiles)
echo ""
echo "[2/3] Setting up optimization..."
abaqus cae noGUI=scripts/setup_optimization.py
if [ $? -ne 0 ]; then
    echo "FAILED: Optimization setup failed"
    exit 1
fi

# Find the .par file
PAR_FILE=$(find . -name "*.par" -type f 2>/dev/null | head -1)
if [ -z "$PAR_FILE" ]; then
    echo "FAILED: No .par file generated"
    exit 1
fi
echo "  .par file: $PAR_FILE"

# Step 3: Run Tosca via CLI
echo ""
echo "[3/3] Running Tosca optimization via CLI..."
abaqus optimization task="$PAR_FILE" job=Experiment5_TO cpus=$SLURM_NTASKS interactive 2>&1
OPT_EXIT=$?

if [ $OPT_EXIT -ne 0 ]; then
    echo "  First attempt failed (exit $OPT_EXIT), retrying without cpus..."
    abaqus optimization task="$PAR_FILE" job=Experiment5_TO interactive 2>&1
    OPT_EXIT=$?
fi

# Check that TOSCA_POST was created
TOSCA_FOUND=0
for dir in . Experiment5_TO Experiment5_Optimization; do
    if [ -d "${dir}/TOSCA_POST" ]; then
        ODB_COUNT=$(ls ${dir}/TOSCA_POST/*.odb 2>/dev/null | wc -l)
        echo "PASSED: Tosca ran — ${ODB_COUNT} design cycle ODBs in ${dir}/TOSCA_POST"
        TOSCA_FOUND=1
        break
    fi
done

if [ $TOSCA_FOUND -eq 0 ]; then
    echo "WARNING: TOSCA_POST directory not found in expected locations"
    echo "  Checking alternate locations..."
    find . -name "TOSCA_POST" -type d 2>/dev/null
fi

echo ""
echo "============================================"
echo "Stage 2 Complete: $(date)"
echo "============================================"
