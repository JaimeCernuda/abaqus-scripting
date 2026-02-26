#!/bin/bash
#SBATCH --job-name=exp8d
#SBATCH --account=notchpeak-shared-short
#SBATCH --partition=notchpeak-shared-short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=4:00:00
#SBATCH --mem=16G
#SBATCH -o exp8d_%j.out
#SBATCH -e exp8d_%j.err

# ============================================================================
# Experiment 8d: Full submit() pipeline with systematic variations
# ============================================================================

module load abaqus/2025
unset SLURM_GTIDS

EXP_DIR=$HOME/Abaqus/paper_reproduction/experiment8

echo "============================================"
echo "Experiment 8d: Full submit() Pipeline"
echo "Started: $(date)"
echo "Node: $(hostname)"
echo "============================================"

rm -rf $EXP_DIR/run_8d
mkdir -p $EXP_DIR/run_8d
cd $EXP_DIR/run_8d

echo "CWD: $(pwd)"
echo ""

abaqus cae noGUI=$EXP_DIR/scripts/exp8d_submit.py 2>&1
EXIT_CODE=$?

echo ""
echo "============================================"
echo "Exit code: $EXIT_CODE"
echo "Finished: $(date)"
echo "============================================"

echo ""
echo "Files in run_8d/:"
ls -la

if [ -f abaqus.rpy ]; then
    echo ""
    echo "=== abaqus.rpy (script output) ==="
    cat abaqus.rpy
fi

# Show optimization output directories
for dir in $(find . -maxdepth 1 -type d ! -name "."); do
    echo ""
    echo "=== Contents of $dir/ ==="
    ls -la "$dir/" | head -30
    count=$(ls "$dir/" 2>/dev/null | wc -l)
    if [ "$count" -gt 30 ]; then
        echo "  ... and $((count - 30)) more files"
    fi
done

# Check for TOSCA.OUT
if [ -f TOSCA.OUT ]; then
    echo ""
    echo "=== TOSCA.OUT (last 50 lines) ==="
    tail -50 TOSCA.OUT
fi
