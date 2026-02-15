#!/bin/bash
#SBATCH --job-name=test_slurm
#SBATCH --account=owner-gpu-guest
#SBATCH --partition=kingspeak
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:05:00
#SBATCH --mem=1G
#SBATCH -o test_slurm_%j.out
#SBATCH -e test_slurm_%j.err

# ============================================================================
# Stage 0: Smoke test — prove SLURM accepts and runs jobs
# ============================================================================

echo "============================================"
echo "SLURM Smoke Test"
echo "============================================"
echo ""
echo "Hostname: $(hostname)"
echo "Date:     $(date)"
echo "User:     $USER"
echo "Job ID:   $SLURM_JOB_ID"
echo "Partition: $SLURM_JOB_PARTITION"
echo "Nodes:    $SLURM_NNODES"
echo "Tasks:    $SLURM_NTASKS"
echo "CWD:      $(pwd)"
echo ""
echo "--- Loaded modules ---"
module list 2>&1
echo ""
echo "--- Disk space (home) ---"
df -h "$HOME" 2>/dev/null || echo "df not available"
echo ""
echo "SLURM works"
echo "============================================"
