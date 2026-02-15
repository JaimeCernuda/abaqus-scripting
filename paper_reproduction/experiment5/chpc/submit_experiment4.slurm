#!/bin/bash
#SBATCH --job-name=exp4_refined
#SBATCH --account=owner-gpu-guest
#SBATCH --partition=kingspeak
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --time=8:00:00
#SBATCH --mem=16G
#SBATCH -o exp4_refined_%j.out
#SBATCH -e exp4_refined_%j.err

# ============================================================================
# Re-run Experiment 4 with refined mesh on CHPC (full license, no node limit)
# ============================================================================

unset SLURM_GTIDS
export I_MPI_HYDRA_TOPOLIB=ipl

source /uufs/chpc.utah.edu/sys/installdir/abaqus/setup_ab_slurm.sh

export ABAQUS_MESH_SIZE=3.0
export ABAQUS_NUM_CPUS=$SLURM_NTASKS

cd $HOME/Abaqus/paper_reproduction/experiment4

echo "============================================"
echo "Experiment 4: Refined Mesh (3mm, full license)"
echo "Started: $(date)"
echo "Nodes: $SLURM_NNODES, Tasks: $SLURM_NTASKS"
echo "============================================"

# Step 1: Create geometry + meshed model
echo ""
echo "[1/6] Creating model with refined mesh..."
abaqus cae noGUI=scripts/create_model.py
if [ $? -ne 0 ]; then
    echo "ERROR: Model creation failed"
    exit 1
fi

# Step 2: Setup and run 20 kN
echo ""
echo "[2/6] Setting up 20 kN load case..."
abaqus cae noGUI=scripts/setup_20kN.py
echo "[2/6] Running 20 kN analysis..."
abaqus job=Job_20kN cpus=$SLURM_NTASKS interactive

# Step 3: Setup and run 60 kN
echo ""
echo "[3/6] Setting up 60 kN load case..."
abaqus cae noGUI=scripts/setup_60kN.py
echo "[3/6] Running 60 kN analysis..."
abaqus job=Job_60kN cpus=$SLURM_NTASKS interactive

# Step 4: Setup and run 100 kN
echo ""
echo "[4/6] Setting up 100 kN load case..."
abaqus cae noGUI=scripts/setup_100kN.py
echo "[4/6] Running 100 kN analysis..."
abaqus job=Job_100kN cpus=$SLURM_NTASKS interactive

# Step 5: Extract results
echo ""
echo "[5/6] Extracting results..."
abaqus python scripts/extract_20kN_results.py
abaqus python scripts/extract_60kN_results.py
abaqus python scripts/extract_100kN_results.py

# Step 6: Verify
echo ""
echo "[6/6] Verifying final results..."
abaqus python scripts/verify_final_results.py

echo ""
echo "============================================"
echo "Experiment 4 (Refined): Complete"
echo "Finished: $(date)"
echo "============================================"
