#!/bin/bash
#SBATCH --job-name=exp10_prod
#SBATCH --account=hochhalter
#SBATCH --partition=kingspeak
#SBATCH --qos=kingspeak
#SBATCH -M kingspeak
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --time=48:00:00
#SBATCH --mem=120G
#SBATCH -o exp10_%j.out
#SBATCH -e exp10_%j.err

# ============================================================================
# Experiment 10: Production run (1mm mesh, 75 cycles)
# Usage: sbatch chpc/run_exp10_production.slurm
# ============================================================================

module load abaqus/2025
unset SLURM_GTIDS
export I_MPI_HYDRA_TOPOLIB=ipl

EXP_DIR=$HOME/Abaqus/paper_reproduction/experiment10
WORK_DIR=$EXP_DIR/run

export ABAQUS_MESH_SIZE=1.0
export ABAQUS_NUM_CPUS=8
export ABAQUS_MAX_CYCLES=75
export ABAQUS_STRESS_LIMIT=800.0

echo "============================================"
echo "Experiment 10: PRODUCTION Stress-Constrained TO"
echo "Started: $(date)"
echo "Node: $(hostname)"
echo "Mesh size: $ABAQUS_MESH_SIZE mm"
echo "CPUs: $ABAQUS_NUM_CPUS"
echo "Max cycles: $ABAQUS_MAX_CYCLES"
echo "Stress limit: $ABAQUS_STRESS_LIMIT MPa"
echo "============================================"

# --- Environment check ---
echo ""
echo "--- Environment ---"
which abaqus 2>/dev/null && echo "abaqus: $(abaqus information=release 2>&1 | head -1)" || echo "abaqus: NOT found"
which tosca 2>/dev/null && echo "tosca: found" || echo "tosca: NOT found (will try 'abaqus tosca')"
which Xvfb 2>/dev/null && echo "Xvfb: found" || echo "Xvfb: NOT found (visualization will be skipped)"

# ============================================================================
# STEP 1: Build model + flatten .inp + generate .par + run Tosca (noGUI)
# ============================================================================
echo ""
echo "============================================"
echo "STEP 1: Optimization pipeline (noGUI)"
echo "============================================"

# Clean working directory
rm -rf $WORK_DIR
mkdir -p $WORK_DIR
cd $WORK_DIR

abaqus cae noGUI=$EXP_DIR/scripts/exp10_optimize.py 2>&1
STEP1_EXIT=$?
echo ""
echo "Step 1 exit code: $STEP1_EXIT"

# Check for output
echo ""
echo "--- Files in work directory ---"
ls -la $WORK_DIR/
echo ""

if [ -d $WORK_DIR/exp10_tosca ]; then
    echo "--- Tosca output directory ---"
    ls -la $WORK_DIR/exp10_tosca/ | head -20
    TOSCA_FILES=$(ls $WORK_DIR/exp10_tosca/ 2>/dev/null | wc -l)
    echo "Total files in exp10_tosca/: $TOSCA_FILES"
fi

# Check for STL
STL_COUNT=$(find $WORK_DIR -name "*.stl" 2>/dev/null | wc -l)
echo ""
echo "STL files found: $STL_COUNT"
find $WORK_DIR -name "*.stl" -exec ls -la {} \;

# ============================================================================
# STEP 2: Visualization (optional, requires Xvfb)
# ============================================================================
if command -v Xvfb &>/dev/null; then
    echo ""
    echo "============================================"
    echo "STEP 2: Visualization (Xvfb)"
    echo "============================================"

    # Start Xvfb
    XDISPLAY=:$(( RANDOM % 900 + 100 ))
    Xvfb $XDISPLAY -screen 0 1024x768x24 &
    XVFB_PID=$!
    sleep 2
    export DISPLAY=$XDISPLAY
    echo "Xvfb started on $XDISPLAY (PID=$XVFB_PID)"

    cd $WORK_DIR
    timeout 300 abaqus cae script=$EXP_DIR/scripts/exp10_visualize.py 2>&1
    STEP2_EXIT=$?

    kill $XVFB_PID 2>/dev/null
    unset DISPLAY

    echo ""
    echo "Step 2 exit code: $STEP2_EXIT"
    if [ $STEP2_EXIT -eq 124 ]; then
        echo "WARNING: Visualization timed out (300s)"
    fi
else
    echo ""
    echo "Skipping visualization (Xvfb not available)"
fi

# ============================================================================
# RESULTS SUMMARY
# ============================================================================
echo ""
echo "============================================"
echo "RESULTS SUMMARY"
echo "============================================"

echo ""
echo "--- Optimization outputs ---"
for ext in inp par; do
    for f in $WORK_DIR/*.$ext; do
        [ -f "$f" ] && echo "  $(basename $f): $(wc -c < $f) bytes"
    done
done

echo ""
echo "--- Visualization images ---"
IMG_COUNT=0
for f in $WORK_DIR/*.png; do
    if [ -f "$f" ]; then
        echo "  $(basename $f): $(wc -c < $f) bytes"
        IMG_COUNT=$((IMG_COUNT + 1))
    fi
done
echo "  Images: $IMG_COUNT"

echo ""
echo "--- STL outputs ---"
find $WORK_DIR -name "*.stl" -exec echo "  {}" \; 2>/dev/null

echo ""
echo "--- Optimization convergence ---"
if [ -f $WORK_DIR/exp10_tosca/optimization_report.csv ]; then
    echo "  First 5 and last 5 iterations:"
    head -7 $WORK_DIR/exp10_tosca/optimization_report.csv
    echo "  ..."
    tail -5 $WORK_DIR/exp10_tosca/optimization_report.csv
fi

echo ""
echo "============================================"
echo "Experiment 10 PRODUCTION finished: $(date)"
echo "Step 1 (optimization) exit: $STEP1_EXIT"
echo "============================================"
