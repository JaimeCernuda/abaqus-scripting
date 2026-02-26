#!/bin/bash
#SBATCH --job-name=exp8c
#SBATCH --account=notchpeak-shared-short
#SBATCH --partition=notchpeak-shared-short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=2:00:00
#SBATCH --mem=8G
#SBATCH -o exp8c_%j.out
#SBATCH -e exp8c_%j.err

# ============================================================================
# Experiment 8c: writeParAndInputFiles() test with systematic variations
# ============================================================================

module load abaqus/2025
unset SLURM_GTIDS

EXP_DIR=$HOME/Abaqus/paper_reproduction/experiment8

echo "============================================"
echo "Experiment 8c: writeParAndInputFiles() Test"
echo "Started: $(date)"
echo "Node: $(hostname)"
echo "============================================"

rm -rf $EXP_DIR/run_8c
mkdir -p $EXP_DIR/run_8c
cd $EXP_DIR/run_8c

echo "CWD: $(pwd)"
echo ""

abaqus cae noGUI=$EXP_DIR/scripts/exp8c_write_par.py 2>&1
EXIT_CODE=$?

echo ""
echo "============================================"
echo "Exit code: $EXIT_CODE"
echo "Finished: $(date)"
echo "============================================"

echo ""
echo "Files in run_8c/:"
ls -la

if [ -f abaqus.rpy ]; then
    echo ""
    echo "=== abaqus.rpy (script output) ==="
    cat abaqus.rpy
fi

# Show any .par files
for f in *.par; do
    if [ -f "$f" ]; then
        echo ""
        echo "=== $f ==="
        cat "$f"
    fi
done

# Show any .inp files (first 50 lines)
for f in *.inp; do
    if [ -f "$f" ]; then
        echo ""
        echo "=== $f (first 50 lines) ==="
        head -50 "$f"
        echo "..."
        wc -l "$f"
    fi
done
