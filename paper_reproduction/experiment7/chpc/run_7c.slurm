#!/bin/bash
#SBATCH --job-name=exp7c
#SBATCH --account=notchpeak-shared-short
#SBATCH --partition=notchpeak-shared-short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=1:00:00
#SBATCH --mem=8G
#SBATCH -o exp7c_%j.out
#SBATCH -e exp7c_%j.err

# ============================================================================
# Experiment 7c: Import airbeam_vol.inp + setup TO + writeParAndInputFiles()
#
# Tests whether we can correctly recreate the airbeam_vol.par optimization
# setup using the CAE Python API, and generate a matching .par file.
# ============================================================================

module load abaqus/2025
unset SLURM_GTIDS

EXP_DIR=$HOME/Abaqus/paper_reproduction/experiment7

echo "============================================"
echo "Experiment 7c: Import + TO Setup + writePar"
echo "Started: $(date)"
echo "Node: $(hostname)"
echo "============================================"

# Clean and prepare working directory
rm -rf $EXP_DIR/run_7c
mkdir -p $EXP_DIR/run_7c
cp $EXP_DIR/examples/airbeam_vol.inp $EXP_DIR/run_7c/
cd $EXP_DIR/run_7c

echo "CWD: $(pwd)"
echo "Files: $(ls)"
echo ""

abaqus cae noGUI=$EXP_DIR/scripts/run_7c.py 2>&1
EXIT_CODE=$?

echo ""
echo "============================================"
echo "Exit code: $EXIT_CODE"
echo "Finished: $(date)"
echo "============================================"

echo ""
echo "Files in run_7c/:"
ls -la

# Abaqus noGUI sends print output to abaqus.rpy — dump it
if [ -f abaqus.rpy ]; then
    echo ""
    echo "=== abaqus.rpy (script output) ==="
    cat abaqus.rpy
fi

# Show any generated .par files
for par in $(find . -name "*.par" 2>/dev/null); do
    echo ""
    echo "=== $par ==="
    cat "$par"
done
