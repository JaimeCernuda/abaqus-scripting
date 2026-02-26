#!/bin/bash
#SBATCH --job-name=exp7e
#SBATCH --account=notchpeak-shared-short
#SBATCH --partition=notchpeak-shared-short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=2:00:00
#SBATCH --mem=8G
#SBATCH -o exp7e_%j.out
#SBATCH -e exp7e_%j.err

# ============================================================================
# Experiment 7e: Own geometry + topology optimization + submit()
#
# Builds a simple block model from scratch (like experiment 6) and runs
# topology optimization using patterns confirmed by 7c/7d.
# ============================================================================

module load abaqus/2025
unset SLURM_GTIDS

EXP_DIR=$HOME/Abaqus/paper_reproduction/experiment7

echo "============================================"
echo "Experiment 7e: Own Geometry + TO + submit()"
echo "Started: $(date)"
echo "Node: $(hostname)"
echo "============================================"

# Clean and prepare working directory
rm -rf $EXP_DIR/run_7e
mkdir -p $EXP_DIR/run_7e
cd $EXP_DIR/run_7e

echo "CWD: $(pwd)"
echo ""

abaqus cae noGUI=$EXP_DIR/scripts/run_7e.py 2>&1
EXIT_CODE=$?

echo ""
echo "============================================"
echo "Exit code: $EXIT_CODE"
echo "Finished: $(date)"
echo "============================================"

echo ""
echo "Files in run_7e/:"
ls -la

# Abaqus noGUI sends print output to abaqus.rpy — dump it
if [ -f abaqus.rpy ]; then
    echo ""
    echo "=== abaqus.rpy (script output) ==="
    cat abaqus.rpy
fi

# Show optimization output directory if it exists
for dir in $(find . -maxdepth 1 -type d ! -name "."); do
    echo ""
    echo "=== Contents of $dir/ ==="
    ls -la "$dir/" | head -30
    count=$(ls "$dir/" 2>/dev/null | wc -l)
    if [ "$count" -gt 30 ]; then
        echo "  ... and $((count - 30)) more files"
    fi
done
