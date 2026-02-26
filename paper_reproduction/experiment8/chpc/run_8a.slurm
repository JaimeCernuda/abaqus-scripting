#!/bin/bash
#SBATCH --job-name=exp8a
#SBATCH --account=notchpeak-shared-short
#SBATCH --partition=notchpeak-shared-short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=1:00:00
#SBATCH --mem=8G
#SBATCH -o exp8a_%j.out
#SBATCH -e exp8a_%j.err

# ============================================================================
# Experiment 8a: Validate model + static analysis in noGUI mode
# ============================================================================

module load abaqus/2025
unset SLURM_GTIDS

EXP_DIR=$HOME/Abaqus/paper_reproduction/experiment8

echo "============================================"
echo "Experiment 8a: Model Validation + Static FEA"
echo "Started: $(date)"
echo "Node: $(hostname)"
echo "============================================"

rm -rf $EXP_DIR/run_8a
mkdir -p $EXP_DIR/run_8a
cd $EXP_DIR/run_8a

echo "CWD: $(pwd)"
echo ""

abaqus cae noGUI=$EXP_DIR/scripts/exp8a_model_and_analysis.py 2>&1
EXIT_CODE=$?

echo ""
echo "============================================"
echo "Exit code: $EXIT_CODE"
echo "Finished: $(date)"
echo "============================================"

echo ""
echo "Files in run_8a/:"
ls -la

if [ -f abaqus.rpy ]; then
    echo ""
    echo "=== abaqus.rpy (script output) ==="
    cat abaqus.rpy
fi

if [ -f Block_Analysis.dat ]; then
    echo ""
    echo "=== Block_Analysis.dat (last 50 lines) ==="
    tail -50 Block_Analysis.dat
fi

if [ -f Block_Analysis.msg ]; then
    echo ""
    echo "=== Block_Analysis.msg (last 30 lines) ==="
    tail -30 Block_Analysis.msg
fi
