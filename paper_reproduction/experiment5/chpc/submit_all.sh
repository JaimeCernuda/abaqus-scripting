#!/usr/bin/env bash
# Submit the complete Experiment 5 pipeline with SLURM dependency chaining.
# Validation auto-starts only after optimization succeeds.
#
# Usage: bash chpc/submit_all.sh

set -euo pipefail

cd "$HOME/Abaqus/paper_reproduction/experiment5"

echo "Submitting Experiment 5 pipeline..."
echo ""

# Submit topology optimization
OPT_JOBID=$(sbatch --parsable chpc/submit_optimization.slurm)
echo "  Optimization: SLURM job ${OPT_JOBID}"

# Submit validation (starts after optimization succeeds)
VAL_JOBID=$(sbatch --parsable --dependency=afterok:${OPT_JOBID} chpc/submit_validation.slurm)
echo "  Validation:   SLURM job ${VAL_JOBID} (after ${OPT_JOBID})"

echo ""
echo "Pipeline submitted. Monitor with:"
echo "  squeue -u \$USER"
echo "  bash chpc/monitor.sh --watch"
echo "  tail -f exp5_tosca_${OPT_JOBID}.out"
