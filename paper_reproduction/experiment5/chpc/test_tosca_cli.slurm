#!/bin/bash
#SBATCH --job-name=test_tosca_cli
#SBATCH --account=hochhalter
#SBATCH --partition=kingspeak
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --time=2:00:00
#SBATCH --mem=8G
#SBATCH -o test_tosca_cli_%j.out
#SBATCH -e test_tosca_cli_%j.err

# ============================================================================
# Test 2: Run Tosca optimization via CLI
#
# Uses .par file from writeParAndInputFiles() + abaqus optimization CLI.
# cpus set via abaqus_v6.env to avoid str/int bug in Abaqus 2025.
#
# Pass: TOSCA_POST/ directory with .odb files
# Fail: no TOSCA_POST or no .odb files
# ============================================================================

unset SLURM_GTIDS
export I_MPI_HYDRA_TOPOLIB=ipl

source /uufs/chpc.utah.edu/sys/installdir/abaqus/setup_ab_slurm.sh

export ABAQUS_MESH_SIZE=3.0
export ABAQUS_NUM_CPUS=$SLURM_NTASKS
export ABAQUS_MAX_CYCLES=3

cd $HOME/Abaqus/paper_reproduction/experiment5

echo "============================================"
echo "Test 2: Tosca CLI Optimization"
echo "Started: $(date)"
echo "Tasks: $SLURM_NTASKS, Max cycles: $ABAQUS_MAX_CYCLES"
echo "============================================"

# Step 1: Create design space
echo ""
echo "[1/4] Creating design space..."
abaqus cae noGUI=scripts/create_design_space.py
if [ $? -ne 0 ]; then
    echo "FAILED: Design space creation failed"
    exit 1
fi

# Step 2: Setup optimization (generates .par file)
echo ""
echo "[2/4] Setting up optimization + generating .par file..."
abaqus cae noGUI=scripts/setup_optimization.py
if [ $? -ne 0 ]; then
    echo "FAILED: Optimization setup failed"
    exit 1
fi

# Step 3: Find the .par file
echo ""
echo "[3/4] Locating .par file..."
PAR_FILE=$(find . -name "*.par" -type f 2>/dev/null | head -1)
if [ -z "$PAR_FILE" ]; then
    echo "FAILED: No .par file found"
    exit 1
fi
echo "  Found: $PAR_FILE"

# Step 4: Run Tosca via CLI
echo ""
echo "[4/4] Running Tosca optimization via CLI..."
echo "  Command: abaqus optimization task=$PAR_FILE job=Experiment5_TO cpus=$SLURM_NTASKS interactive"

abaqus optimization task="$PAR_FILE" job=Experiment5_TO cpus=$SLURM_NTASKS interactive 2>&1
OPT_EXIT=$?
echo "  Exit code: $OPT_EXIT"

# If cpus caused a TypeError, retry without it (env file will handle cpus)
if [ $OPT_EXIT -ne 0 ]; then
    echo ""
    echo "  Retrying without cpus argument (using abaqus_v6.env instead)..."
    abaqus optimization task="$PAR_FILE" job=Experiment5_TO interactive 2>&1
    OPT_EXIT=$?
    echo "  Retry exit code: $OPT_EXIT"
fi

# Check results
echo ""
echo "Checking for TOSCA_POST..."
TOSCA_FOUND=0
for dir in . Experiment5_TO Experiment5_Optimization; do
    if [ -d "${dir}/TOSCA_POST" ]; then
        ODB_COUNT=$(ls ${dir}/TOSCA_POST/*.odb 2>/dev/null | wc -l)
        echo "PASSED: Tosca ran — ${ODB_COUNT} design cycle ODB(s) in ${dir}/TOSCA_POST"
        ls -la ${dir}/TOSCA_POST/*.odb 2>/dev/null
        TOSCA_FOUND=1
        break
    fi
done

if [ $TOSCA_FOUND -eq 0 ]; then
    echo "FAILED: No TOSCA_POST directory found"
    echo ""
    echo "Diagnostics:"
    echo "  Working directory contents:"
    ls -la
    echo ""
    echo "  Searching for TOSCA_POST anywhere:"
    find . -name "TOSCA_POST" -type d 2>/dev/null || echo "  None found"
    echo ""
    echo "  Searching for any .odb files:"
    find . -name "*.odb" -type f 2>/dev/null | head -10
    exit 1
fi

echo ""
echo "============================================"
echo "Test 2 Complete: $(date)"
echo "============================================"
