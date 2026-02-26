#!/bin/bash
#SBATCH --job-name=cantilever
#SBATCH --account=notchpeak-shared-short
#SBATCH --partition=notchpeak-shared-short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=1:00:00
#SBATCH --mem=8G
#SBATCH -o cantilever_%j.out
#SBATCH -e cantilever_%j.err

# ============================================================================
# Run the exact abqpy cantilever example in both noGUI and script= modes
# ============================================================================

module load abaqus/2025
unset SLURM_GTIDS

EXP_DIR=$HOME/Abaqus/paper_reproduction/experiment8
SCRIPT=$EXP_DIR/scripts/abqpy_cantilever.py

# --- Test 1: noGUI mode ---
echo "============================================"
echo "Test 1: abaqus cae noGUI=cantilever.py"
echo "Started: $(date)"
echo "============================================"

rm -rf $EXP_DIR/run_cantilever_nogui
mkdir -p $EXP_DIR/run_cantilever_nogui
cd $EXP_DIR/run_cantilever_nogui

abaqus cae noGUI=$SCRIPT 2>&1
echo "noGUI exit code: $?"
echo ""
echo "Files:"
ls -la
echo ""
if [ -f abaqus.rpy ]; then
    echo "=== abaqus.rpy ==="
    cat abaqus.rpy
fi

# --- Test 2: script= mode (loads GUI layer, no display needed) ---
echo ""
echo "============================================"
echo "Test 2: abaqus cae script=cantilever.py"
echo "Started: $(date)"
echo "============================================"

rm -rf $EXP_DIR/run_cantilever_script
mkdir -p $EXP_DIR/run_cantilever_script
cd $EXP_DIR/run_cantilever_script

abaqus cae script=$SCRIPT 2>&1
echo "script= exit code: $?"
echo ""
echo "Files:"
ls -la
echo ""
if [ -f abaqus.rpy ]; then
    echo "=== abaqus.rpy ==="
    cat abaqus.rpy
fi

echo ""
echo "============================================"
echo "Both tests finished: $(date)"
echo "============================================"
