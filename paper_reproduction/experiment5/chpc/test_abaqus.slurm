#!/bin/bash
#SBATCH --job-name=test_abaqus
#SBATCH --account=hochhalter
#SBATCH --partition=kingspeak
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --time=1:00:00
#SBATCH --mem=8G
#SBATCH -o test_abaqus_%j.out
#SBATCH -e test_abaqus_%j.err

# ============================================================================
# Stage 1: Prove Abaqus runs — geometry + mesh creation
# Screenshots are captured separately on Frisco nodes (see CHPC_GUIDE.md)
# ============================================================================

unset SLURM_GTIDS
export I_MPI_HYDRA_TOPOLIB=ipl

source /uufs/chpc.utah.edu/sys/installdir/abaqus/setup_ab_slurm.sh

export ABAQUS_MESH_SIZE=3.0

cd $HOME/Abaqus/paper_reproduction/experiment5

echo "============================================"
echo "Stage 1: Abaqus Geometry + Mesh Test"
echo "Started: $(date)"
echo "============================================"

# Create design space (geometry + mesh)
echo ""
echo "[1/1] Creating design space..."
abaqus cae noGUI=scripts/create_design_space.py
if [ $? -ne 0 ]; then
    echo "FAILED: Geometry creation failed"
    exit 1
fi

# Verify outputs
if [ -f "Experiment5_TO.cae" ]; then
    echo "PASSED: Experiment5_TO.cae created"
else
    echo "FAILED: Experiment5_TO.cae not found"
    exit 1
fi

echo ""
echo "============================================"
echo "Stage 1 Complete: $(date)"
echo "NOTE: Capture screenshots on Frisco with:"
echo "  vglrun -c proxy abaqus cae script=scripts/capture_geometry.py"
echo "============================================"
