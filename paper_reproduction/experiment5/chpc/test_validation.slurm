#!/bin/bash
#SBATCH --job-name=test_validate
#SBATCH --account=owner-gpu-guest
#SBATCH --partition=kingspeak
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --time=2:00:00
#SBATCH --mem=16G
#SBATCH -o test_validate_%j.out
#SBATCH -e test_validate_%j.err

# ============================================================================
# Stage 3: Prove density-filtered validation works (20 kN only)
# Requires: Stage 2 to have completed (TOSCA_POST exists)
# ============================================================================

unset SLURM_GTIDS
export I_MPI_HYDRA_TOPOLIB=ipl

source /uufs/chpc.utah.edu/sys/installdir/abaqus/setup_ab_slurm.sh

export ABAQUS_NUM_CPUS=$SLURM_NTASKS
export VALIDATION_LOADS=20    # Only test 20 kN (quick)

cd $HOME/Abaqus/paper_reproduction/experiment5

echo "============================================"
echo "Stage 3: Validation Test (20 kN only)"
echo "Started: $(date)"
echo "============================================"

# Check prerequisite: TOSCA_POST must exist from Stage 2
if [ ! -d "Experiment5_TO/TOSCA_POST" ] && [ ! -d "TOSCA_POST" ]; then
    echo "FAILED: No optimization results found"
    echo "  Run Stage 2 (test_tosca.slurm) first"
    exit 1
fi

# Step 1: Create and run 20 kN validation job
echo ""
echo "[1/3] Setting up density-filtered validation (20 kN)..."
abaqus cae noGUI=scripts/setup_validation_jobs.py
if [ $? -ne 0 ]; then
    echo "FAILED: Validation job creation failed"
    exit 1
fi

# Verify ODB was created
if [ -f "Validation_20kN.odb" ]; then
    echo "PASSED: Validation_20kN.odb created"
else
    echo "FAILED: Validation_20kN.odb not found"
    exit 1
fi

# Step 2: Run comparison (will show 20 kN only, skip missing 60/100)
echo ""
echo "[2/3] Running comparison against Experiment 4 baseline..."
abaqus python scripts/run_validation.py || echo "WARNING: Comparison had issues (Exp4 baseline may not exist yet)"

# Step 3: Capture validation screenshots
echo ""
echo "[3/3] Capturing validation screenshots..."
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

echo ""
echo "============================================"
echo "Stage 3 Complete: $(date)"
echo "============================================"

# Summary
echo ""
echo "--- Output files ---"
for f in Validation_20kN.odb validation_results.txt validation_comparison.csv; do
    if [ -f "$f" ]; then
        echo "  [OK] $f"
    else
        echo "  [  ] $f (not found)"
    fi
done
ls screenshots/val_*.png 2>/dev/null && echo "  [OK] Validation screenshots" || echo "  [  ] No validation screenshots"
