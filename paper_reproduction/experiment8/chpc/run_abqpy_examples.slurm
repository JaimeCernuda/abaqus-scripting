#!/bin/bash
#SBATCH --job-name=abqpy_ex
#SBATCH --account=notchpeak-shared-short
#SBATCH --partition=notchpeak-shared-short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=2:00:00
#SBATCH --mem=8G
#SBATCH -o abqpy_examples_%j.out
#SBATCH -e abqpy_examples_%j.err

# ============================================================================
# Run abqpy cantilever + skewExample in 3 modes:
#   1) noGUI (no display)
#   2) script= with Xvfb (virtual framebuffer)
#   3) noGUI with Xvfb DISPLAY set (in case noGUI checks for it)
# ============================================================================

module load abaqus/2025
unset SLURM_GTIDS

EXP_DIR=$HOME/Abaqus/paper_reproduction/experiment8
CANTILEVER=$EXP_DIR/scripts/abqpy_cantilever.py
SKEW=$EXP_DIR/scripts/abqpy_skewExample.py

echo "============================================"
echo "abqpy Examples Test Suite"
echo "Started: $(date)"
echo "Node: $(hostname)"
echo "============================================"

# Check what's available
echo ""
echo "--- Environment check ---"
which Xvfb 2>/dev/null && echo "Xvfb: found" || echo "Xvfb: NOT found"
which xvfb-run 2>/dev/null && echo "xvfb-run: found" || echo "xvfb-run: NOT found"
echo "DISPLAY=$DISPLAY"
rpm -q xorg-x11-server-Xvfb 2>/dev/null || echo "Xvfb rpm: not installed"

# ============================================================================
# TEST 1: Cantilever noGUI (baseline — we know this fails on 'mesh')
# ============================================================================
echo ""
echo "============================================"
echo "TEST 1: Cantilever - noGUI"
echo "============================================"

rm -rf $EXP_DIR/run_cantilever_nogui
mkdir -p $EXP_DIR/run_cantilever_nogui
cd $EXP_DIR/run_cantilever_nogui

abaqus cae noGUI=$CANTILEVER 2>&1
echo "Exit code: $?"
[ -f abaqus.rpy ] && tail -20 abaqus.rpy

# ============================================================================
# TEST 2: Cantilever script= with Xvfb
# ============================================================================
echo ""
echo "============================================"
echo "TEST 2: Cantilever - script= with Xvfb"
echo "============================================"

rm -rf $EXP_DIR/run_cantilever_xvfb
mkdir -p $EXP_DIR/run_cantilever_xvfb
cd $EXP_DIR/run_cantilever_xvfb

if command -v Xvfb &>/dev/null; then
    # Start Xvfb on a random display
    XDISPLAY=:$(( RANDOM % 900 + 100 ))
    Xvfb $XDISPLAY -screen 0 1024x768x24 &
    XVFB_PID=$!
    sleep 2
    export DISPLAY=$XDISPLAY
    echo "Xvfb started on $XDISPLAY (PID=$XVFB_PID)"

    abaqus cae script=$CANTILEVER 2>&1
    echo "Exit code: $?"

    kill $XVFB_PID 2>/dev/null
    unset DISPLAY
else
    echo "SKIPPED: Xvfb not available"
fi

[ -f abaqus.rpy ] && tail -30 abaqus.rpy
echo ""
echo "Files:"
ls -la

# ============================================================================
# TEST 3: Cantilever noGUI with DISPLAY set (Xvfb)
# ============================================================================
echo ""
echo "============================================"
echo "TEST 3: Cantilever - noGUI with DISPLAY set"
echo "============================================"

rm -rf $EXP_DIR/run_cantilever_nogui_display
mkdir -p $EXP_DIR/run_cantilever_nogui_display
cd $EXP_DIR/run_cantilever_nogui_display

if command -v Xvfb &>/dev/null; then
    XDISPLAY=:$(( RANDOM % 900 + 100 ))
    Xvfb $XDISPLAY -screen 0 1024x768x24 &
    XVFB_PID=$!
    sleep 2
    export DISPLAY=$XDISPLAY
    echo "Xvfb on $XDISPLAY, running noGUI..."

    abaqus cae noGUI=$CANTILEVER 2>&1
    echo "Exit code: $?"

    kill $XVFB_PID 2>/dev/null
    unset DISPLAY
else
    echo "SKIPPED: Xvfb not available"
fi

[ -f abaqus.rpy ] && tail -20 abaqus.rpy

# ============================================================================
# TEST 4: skewExample - script= with Xvfb (the full parametric + viz test)
# ============================================================================
echo ""
echo "============================================"
echo "TEST 4: skewExample - script= with Xvfb"
echo "============================================"

rm -rf $EXP_DIR/run_skew_xvfb
mkdir -p $EXP_DIR/run_skew_xvfb
cd $EXP_DIR/run_skew_xvfb

if command -v Xvfb &>/dev/null; then
    XDISPLAY=:$(( RANDOM % 900 + 100 ))
    Xvfb $XDISPLAY -screen 0 1024x768x24 &
    XVFB_PID=$!
    sleep 2
    export DISPLAY=$XDISPLAY
    echo "Xvfb on $XDISPLAY, running script=..."

    abaqus cae script=$SKEW 2>&1
    echo "Exit code: $?"

    kill $XVFB_PID 2>/dev/null
    unset DISPLAY
else
    echo "SKIPPED: Xvfb not available"
fi

[ -f abaqus.rpy ] && tail -40 abaqus.rpy
echo ""
echo "Files:"
ls -la

# ============================================================================
# TEST 5: skewExample - noGUI (expect failures from viz calls)
# ============================================================================
echo ""
echo "============================================"
echo "TEST 5: skewExample - noGUI (no display)"
echo "============================================"

rm -rf $EXP_DIR/run_skew_nogui
mkdir -p $EXP_DIR/run_skew_nogui
cd $EXP_DIR/run_skew_nogui

abaqus cae noGUI=$SKEW 2>&1
echo "Exit code: $?"
[ -f abaqus.rpy ] && tail -40 abaqus.rpy

echo ""
echo "============================================"
echo "All tests finished: $(date)"
echo "============================================"
