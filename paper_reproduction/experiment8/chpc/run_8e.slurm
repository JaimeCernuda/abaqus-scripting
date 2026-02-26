#!/bin/bash
#SBATCH --job-name=exp8e
#SBATCH --account=notchpeak-shared-short
#SBATCH --partition=notchpeak-shared-short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=4:00:00
#SBATCH --mem=16G
#SBATCH -o exp8e_%j.out
#SBATCH -e exp8e_%j.err

# ============================================================================
# Experiment 8e: writeParAndInputFiles() -> Tosca CLI
# ============================================================================

module load abaqus/2025
unset SLURM_GTIDS

EXP_DIR=$HOME/Abaqus/paper_reproduction/experiment8

echo "============================================"
echo "Experiment 8e: API -> Tosca CLI"
echo "Started: $(date)"
echo "Node: $(hostname)"
echo "============================================"

rm -rf $EXP_DIR/run_8e
mkdir -p $EXP_DIR/run_8e
cd $EXP_DIR/run_8e

echo "CWD: $(pwd)"
echo ""

abaqus cae noGUI=$EXP_DIR/scripts/exp8e_par_to_tosca.py 2>&1
EXIT_CODE=$?

echo ""
echo "============================================"
echo "Exit code: $EXIT_CODE"
echo "Finished: $(date)"
echo "============================================"

echo ""
echo "Files in run_8e/:"
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

# Check for STL output
find . -name "*.stl" -exec echo "STL found: {}" \;

# Check for TOSCA.OUT
find . -name "TOSCA.OUT" -exec sh -c 'echo "=== {} (last 50 lines) ===" && tail -50 "{}"' \;
