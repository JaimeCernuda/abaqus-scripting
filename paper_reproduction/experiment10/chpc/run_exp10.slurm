#!/bin/bash
#SBATCH --job-name=exp10_TO
#SBATCH --account=notchpeak-shared-short
#SBATCH --partition=notchpeak-shared-short
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --time=4:00:00
#SBATCH --mem=16G
#SBATCH -o exp10_%j.out
#SBATCH -e exp10_%j.err

# ============================================================================
# Experiment 10: IN718 Stress-Constrained Topology Optimization
#
# Usage:
#   # Test run (~30 min, 3mm mesh, 20 cycles)
#   sbatch chpc/run_exp10.slurm
#
#   # Production run (~24-48h, 1mm mesh, 75 cycles)
#   sbatch --export=ABAQUS_MESH_SIZE=1.0,ABAQUS_MAX_CYCLES=75,ABAQUS_NUM_CPUS=8,ABAQUS_STRESS_LIMIT=800.0 \
#          --time=48:00:00 --mem=64G --ntasks=8 chpc/run_exp10.slurm
# ============================================================================

module load abaqus/2025
unset SLURM_GTIDS
export I_MPI_HYDRA_TOPOLIB=ipl

EXP_DIR=$HOME/Abaqus/paper_reproduction/experiment10
WORK_DIR=$EXP_DIR/run

# Pass through environment variables (use defaults if not set)
export ABAQUS_MESH_SIZE=${ABAQUS_MESH_SIZE:-3.0}
export ABAQUS_NUM_CPUS=${ABAQUS_NUM_CPUS:-$SLURM_NTASKS}
export ABAQUS_MAX_CYCLES=${ABAQUS_MAX_CYCLES:-20}
export ABAQUS_STRESS_LIMIT=${ABAQUS_STRESS_LIMIT:-800.0}

echo "============================================"
echo "Experiment 10: Stress-Constrained TO"
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
    timeout 180 abaqus cae script=$EXP_DIR/scripts/exp10_visualize.py 2>&1
    STEP2_EXIT=$?

    kill $XVFB_PID 2>/dev/null
    unset DISPLAY

    echo ""
    echo "Step 2 exit code: $STEP2_EXIT"
    if [ $STEP2_EXIT -eq 124 ]; then
        echo "WARNING: Visualization timed out (180s)"
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
echo "============================================"
echo "Experiment 10 finished: $(date)"
echo "Step 1 (optimization) exit: $STEP1_EXIT"
echo "============================================"
