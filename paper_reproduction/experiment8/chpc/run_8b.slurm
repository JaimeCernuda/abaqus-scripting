#!/bin/bash
#SBATCH --job-name=exp8b
#SBATCH --account=notchpeak-shared-short
#SBATCH --partition=notchpeak-shared-short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=1:00:00
#SBATCH --mem=8G
#SBATCH -o exp8b_%j.out
#SBATCH -e exp8b_%j.err

# ============================================================================
# Experiment 8b: Optimization setup validation (no run)
# ============================================================================

module load abaqus/2025
unset SLURM_GTIDS

EXP_DIR=$HOME/Abaqus/paper_reproduction/experiment8

echo "============================================"
echo "Experiment 8b: Optimization Setup Validation"
echo "Started: $(date)"
echo "Node: $(hostname)"
echo "============================================"

rm -rf $EXP_DIR/run_8b
mkdir -p $EXP_DIR/run_8b
cd $EXP_DIR/run_8b

echo "CWD: $(pwd)"
echo ""

abaqus cae noGUI=$EXP_DIR/scripts/exp8b_optimization_setup.py 2>&1
EXIT_CODE=$?

echo ""
echo "============================================"
echo "Exit code: $EXIT_CODE"
echo "Finished: $(date)"
echo "============================================"

echo ""
echo "Files in run_8b/:"
ls -la

if [ -f abaqus.rpy ]; then
    echo ""
    echo "=== abaqus.rpy (script output) ==="
    cat abaqus.rpy
fi
