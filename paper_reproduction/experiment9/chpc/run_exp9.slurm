#!/bin/bash
#SBATCH --job-name=exp9_fea_viz
#SBATCH --account=notchpeak-shared-short
#SBATCH --partition=notchpeak-shared-short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=2:00:00
#SBATCH --mem=8G
#SBATCH -o exp9_%j.out
#SBATCH -e exp9_%j.err

# ============================================================================
# Experiment 9: FEA + Visualization Image Capture
#   Step 1: Build model + run FEA (noGUI mode)
#   Step 2: Open ODB + capture images (script= mode with Xvfb)
# ============================================================================

module load abaqus/2025
unset SLURM_GTIDS

EXP_DIR=$HOME/Abaqus/paper_reproduction/experiment9
WORK_DIR=$EXP_DIR/run

echo "============================================"
echo "Experiment 9: FEA + Visualization"
echo "Started: $(date)"
echo "Node: $(hostname)"
echo "============================================"

# --- Environment check ---
echo ""
echo "--- Environment ---"
which Xvfb 2>/dev/null && echo "Xvfb: found" || echo "Xvfb: NOT found"
which abaqus 2>/dev/null && echo "abaqus: found" || echo "abaqus: NOT found"

# ============================================================================
# STEP 1: Build model + run FEA (noGUI — no display needed)
# ============================================================================
echo ""
echo "============================================"
echo "STEP 1: Build model and run FEA (noGUI)"
echo "============================================"

# Clean working directory
rm -rf $WORK_DIR
mkdir -p $WORK_DIR
cd $WORK_DIR

abaqus cae noGUI=$EXP_DIR/scripts/exp9_build_and_solve.py 2>&1
STEP1_EXIT=$?
echo ""
echo "Step 1 exit code: $STEP1_EXIT"

# Check if ODB was created
if [ ! -f $WORK_DIR/Job_20kN.odb ]; then
    echo "ERROR: Job_20kN.odb not found. Step 1 failed."
    echo "Files in work dir:"
    ls -la $WORK_DIR/
    echo ""
    echo "Aborting — cannot proceed to visualization without ODB."
    exit 1
fi

echo "ODB created: $(ls -la $WORK_DIR/Job_20kN.odb)"

# ============================================================================
# STEP 2: Visualization + image capture (script= mode with Xvfb)
# ============================================================================
echo ""
echo "============================================"
echo "STEP 2: Open ODB and capture images (Xvfb)"
echo "============================================"

if ! command -v Xvfb &>/dev/null; then
    echo "ERROR: Xvfb not available. Cannot capture images."
    exit 1
fi

# Start Xvfb on a random display
XDISPLAY=:$(( RANDOM % 900 + 100 ))
Xvfb $XDISPLAY -screen 0 1024x768x24 &
XVFB_PID=$!
sleep 2
export DISPLAY=$XDISPLAY
echo "Xvfb started on $XDISPLAY (PID=$XVFB_PID)"

cd $WORK_DIR

# Run visualization script with timeout (3 min should be plenty)
# script= mode keeps CAE open, but sys.exit(0) in the script should close it.
# timeout is a safety net in case sys.exit doesn't work.
timeout 180 abaqus cae script=$EXP_DIR/scripts/exp9_visualize.py 2>&1
STEP2_EXIT=$?

# Clean up Xvfb
kill $XVFB_PID 2>/dev/null
unset DISPLAY

echo ""
echo "Step 2 exit code: $STEP2_EXIT"
if [ $STEP2_EXIT -eq 124 ]; then
    echo "WARNING: Step 2 timed out (180s). Script may have hung."
fi

# ============================================================================
# RESULTS SUMMARY
# ============================================================================
echo ""
echo "============================================"
echo "RESULTS SUMMARY"
echo "============================================"

echo ""
echo "--- FEA outputs ---"
for ext in odb dat msg sta; do
    f=$WORK_DIR/Job_20kN.$ext
    [ -f "$f" ] && echo "  $ext: $(ls -la $f | awk '{print $5}') bytes"
done

echo ""
echo "--- Visualization images ---"
IMG_COUNT=0
for f in $WORK_DIR/*.png; do
    if [ -f "$f" ]; then
        echo "  $(basename $f): $(ls -la $f | awk '{print $5}') bytes"
        IMG_COUNT=$((IMG_COUNT + 1))
    fi
done

if [ $IMG_COUNT -ge 3 ]; then
    echo ""
    echo "SUCCESS: $IMG_COUNT images captured."
elif [ $IMG_COUNT -gt 0 ]; then
    echo ""
    echo "PARTIAL: $IMG_COUNT of 3 expected images captured."
else
    echo ""
    echo "FAILED: No images captured."
fi

echo ""
echo "--- All files in work directory ---"
ls -la $WORK_DIR/

echo ""
echo "============================================"
echo "Experiment 9 finished: $(date)"
echo "============================================"
