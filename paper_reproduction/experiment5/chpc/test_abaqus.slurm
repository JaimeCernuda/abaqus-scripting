#!/bin/bash
#SBATCH --job-name=test_abaqus
#SBATCH --account=owner-gpu-guest
#SBATCH --partition=kingspeak
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --time=1:00:00
#SBATCH --mem=8G
#SBATCH -o test_abaqus_%j.out
#SBATCH -e test_abaqus_%j.err

# ============================================================================
# Stage 1: Prove Abaqus runs and screenshot capture works
# ============================================================================

unset SLURM_GTIDS
export I_MPI_HYDRA_TOPOLIB=ipl

source /uufs/chpc.utah.edu/sys/installdir/abaqus/setup_ab_slurm.sh

export ABAQUS_MESH_SIZE=3.0

cd $HOME/Abaqus/paper_reproduction/experiment5

echo "============================================"
echo "Stage 1: Abaqus Geometry + Screenshot Test"
echo "Started: $(date)"
echo "============================================"

# Step 1: Create design space (geometry + mesh)
echo ""
echo "[1/2] Creating design space..."
abaqus cae noGUI=scripts/create_design_space.py
if [ $? -ne 0 ]; then
    echo "FAILED: Geometry creation failed"
    exit 1
fi
echo "PASSED: Experiment5_TO.cae created"

# Step 2: Capture screenshot (test xvfb-run)
echo ""
echo "[2/2] Capturing geometry screenshot..."
mkdir -p screenshots

if command -v xvfb-run &> /dev/null; then
    echo "  Using xvfb-run for headless rendering..."
    xvfb-run -a abaqus cae script=scripts/capture_geometry.py
elif command -v Xvfb &> /dev/null; then
    echo "  Using manual Xvfb..."
    Xvfb :99 -screen 0 1024x768x24 &
    XVFB_PID=$!
    export DISPLAY=:99
    sleep 2
    abaqus cae script=scripts/capture_geometry.py
    kill $XVFB_PID 2>/dev/null
else
    echo "  WARNING: No Xvfb available, trying direct (may fail)..."
    abaqus cae script=scripts/capture_geometry.py
fi

if [ -f screenshots/geometry_mesh.png ]; then
    echo "PASSED: Screenshot captured"
else
    echo "WARNING: Screenshot not captured (xvfb may not be available)"
    echo "  Geometry creation still succeeded — Abaqus works."
fi

echo ""
echo "============================================"
echo "Stage 1 Complete: $(date)"
echo "============================================"
