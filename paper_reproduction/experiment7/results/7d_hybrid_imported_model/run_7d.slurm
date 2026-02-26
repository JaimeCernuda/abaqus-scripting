#!/bin/bash
#SBATCH --job-name=exp7d
#SBATCH --account=notchpeak-shared-short
#SBATCH --partition=notchpeak-shared-short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=2:00:00
#SBATCH --mem=8G
#SBATCH -o exp7d_%j.out
#SBATCH -e exp7d_%j.err

# ============================================================================
# Experiment 7d: Import airbeam_vol.inp, setup in CAE, hybrid optimization
#
# Hybrid approach: CAE for model import + writeInput(), manual .par generation,
# Tosca CLI for optimization. Workaround for writeParAndInputFiles()/submit() bugs.
# ============================================================================

module load abaqus/2025
unset SLURM_GTIDS

EXP_DIR=$HOME/Abaqus/paper_reproduction/experiment7

echo "============================================"
echo "Experiment 7d: Hybrid TO (import + CLI)"
echo "Started: $(date)"
echo "Node: $(hostname)"
echo "which tosca: $(which tosca)"
echo "============================================"

# Clean and prepare working directory
rm -rf $EXP_DIR/run_7d
mkdir -p $EXP_DIR/run_7d
cp $EXP_DIR/examples/airbeam_vol.inp $EXP_DIR/run_7d/
cd $EXP_DIR/run_7d

echo "CWD: $(pwd)"
echo "Files: $(ls)"
echo ""

abaqus cae noGUI=$EXP_DIR/scripts/run_7d.py 2>&1
EXIT_CODE=$?

echo ""
echo "============================================"
echo "Exit code: $EXIT_CODE"
echo "Finished: $(date)"
echo "============================================"

echo ""
echo "Files in run_7d/:"
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
