#!/bin/bash
#SBATCH --job-name=exp7_tosca
#SBATCH --account=notchpeak-shared-short
#SBATCH --partition=notchpeak-shared-short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=1:00:00
#SBATCH --mem=8G
#SBATCH -o exp7_%j.out
#SBATCH -e exp7_%j.err

# ============================================================================
# Experiment 7: Run built-in Tosca airbeam_vol example
#
# 7a: tosca optimize (standalone Tosca CLI)
# 7b: abaqus optimization (Abaqus CLI wrapper)
#
# Tests whether Tosca optimization works at all on CHPC,
# independent of any CAE Python API issues.
# ============================================================================

module load abaqus/2025
unset SLURM_GTIDS

EXP_DIR=$HOME/Abaqus/paper_reproduction/experiment7

echo "============================================"
echo "Experiment 7: Built-in Tosca Example"
echo "Started: $(date)"
echo "Node: $(hostname)"
echo "which tosca: $(which tosca)"
echo "which abaqus: $(which abaqus)"
echo "============================================"

# ---- 7a: tosca optimize ----
echo ""
echo "============================================"
echo "[7a] tosca optimize"
echo "============================================"

rm -rf $EXP_DIR/run_7a
mkdir -p $EXP_DIR/run_7a
cp $EXP_DIR/examples/airbeam_vol.inp $EXP_DIR/examples/airbeam_vol.par $EXP_DIR/run_7a/
cd $EXP_DIR/run_7a

echo "  CWD: $(pwd)"
echo "  Files: $(ls)"
echo ""

tosca optimize -j airbeam_tosca -p airbeam_vol.par -s abaqus -scpus 1 2>&1
EXIT_7A=$?

echo ""
echo "  7a exit code: $EXIT_7A"
echo "  Files after run:"
ls -la
if [ -d airbeam_tosca ]; then
    echo "  airbeam_tosca/ contents:"
    ls -la airbeam_tosca/
fi

# ---- 7b: abaqus optimization ----
echo ""
echo "============================================"
echo "[7b] abaqus optimization"
echo "============================================"

rm -rf $EXP_DIR/run_7b
mkdir -p $EXP_DIR/run_7b
cp $EXP_DIR/examples/airbeam_vol.inp $EXP_DIR/examples/airbeam_vol.par $EXP_DIR/run_7b/
cd $EXP_DIR/run_7b

echo "  CWD: $(pwd)"
echo "  Files: $(ls)"
echo ""

abaqus optimization task=airbeam_vol.par job=airbeam_abq interactive 2>&1
EXIT_7B=$?

echo ""
echo "  7b exit code: $EXIT_7B"
echo "  Files after run:"
ls -la
if [ -d airbeam_abq ]; then
    echo "  airbeam_abq/ contents:"
    ls -la airbeam_abq/
fi

# ---- Summary ----
echo ""
echo "============================================"
echo "Summary"
echo "  7a (tosca optimize):      exit $EXIT_7A"
echo "  7b (abaqus optimization): exit $EXIT_7B"
echo "Finished: $(date)"
echo "============================================"
