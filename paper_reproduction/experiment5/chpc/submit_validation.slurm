#!/bin/bash
#SBATCH --job-name=exp5_validate
#SBATCH --account=owner-gpu-guest
#SBATCH --partition=kingspeak
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --time=4:00:00
#SBATCH --mem=16G
#SBATCH -o exp5_validate_%j.out
#SBATCH -e exp5_validate_%j.err
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=${CHPC_EMAIL:-}

# ============================================================================
# Experiment 5: Validation - Density-filtered analysis under all load cases
# Run AFTER topology optimization completes
# ============================================================================

unset SLURM_GTIDS
export I_MPI_HYDRA_TOPOLIB=ipl

source /uufs/chpc.utah.edu/sys/installdir/abaqus/setup_ab_slurm.sh

export ABAQUS_NUM_CPUS=$SLURM_NTASKS

cd $HOME/Abaqus/paper_reproduction/experiment5

echo "============================================"
echo "Experiment 5: Validation"
echo "Started: $(date)"
echo "============================================"

# Step 1: Create and run validation jobs (density-filtered, 20/60/100 kN)
echo ""
echo "[1/3] Creating and running validation analysis jobs..."
abaqus cae noGUI=scripts/setup_validation_jobs.py
if [ $? -ne 0 ]; then
    echo "ERROR: Validation job creation failed"
    exit 1
fi

# Step 2: Compare optimized vs Experiment 4 baseline
echo ""
echo "[2/3] Running comparison against baseline..."
abaqus python scripts/run_validation.py

# Step 3: Capture validation stress screenshots
echo ""
echo "[3/3] Capturing validation screenshots..."
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
echo "Validation Complete: $(date)"
echo "============================================"

# Summary
echo ""
echo "--- Output files ---"
for f in Validation_20kN.odb Validation_60kN.odb Validation_100kN.odb \
         validation_results.txt validation_comparison.csv; do
    if [ -f "$f" ]; then
        echo "  [OK] $f"
    else
        echo "  [  ] $f"
    fi
done
