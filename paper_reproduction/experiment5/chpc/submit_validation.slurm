#!/bin/bash
#SBATCH --job-name=exp5_validate
#SBATCH --account=owner-gpu-guest
#SBATCH --partition=kingspeak
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --time=4:00:00
#SBATCH --mem=16G
#SBATCH -o exp5_validate_%j.out
#SBATCH -e exp5_validate_%j.err

# ============================================================================
# Experiment 5: Validation - Re-analyze optimized geometry under all load cases
# Run AFTER topology optimization completes
# ============================================================================

unset SLURM_GTIDS
export I_MPI_HYDRA_TOPOLIB=ipl

source /uufs/chpc.utah.edu/sys/installdir/abaqus/setup_ab_slurm.sh

export ABAQUS_NUM_CPUS=$SLURM_NTASKS

cd $HOME/Abaqus/paper_reproduction/experiment5

echo "============================================"
echo "Experiment 5: Validation"
echo "Started: $(date)"
echo "============================================"

# Run validation (compares optimized vs Experiment 4 baseline)
abaqus python scripts/run_validation.py

echo ""
echo "============================================"
echo "Validation Complete: $(date)"
echo "============================================"
