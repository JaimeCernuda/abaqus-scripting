---
name: plato-job
description: Submit and monitor Plato jobs on NCSA Delta via SLURM. Generates batch scripts, handles spack environment loading.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
---

# Plato Job — SLURM Submission

Submit Plato optimization and analysis jobs on NCSA Delta.

## CRITICAL: NEVER Run on Login Nodes

Delta login nodes are shared. Automated scripts will kill Plato processes.
**ALL** Plato execution must go through SLURM (`sbatch` or `srun`).

## When to Use

- User says run, submit, execute, start the optimization
- After mesh + XML + .i files are ready

## What to Ask User

### Required
- Confirmation that input files are ready

### Optional (with defaults)
- **MPI ranks**: Default 4 (scale: 1 rank per ~50k elements)
- **Wall time**: Default 2 hours
- **Memory**: Default 32 GB
- **Partition**: Default `cpu` (48hr max) or `cpu-interactive` (1hr, for testing)

## Batch Script Template

```bash
#!/bin/bash
#SBATCH --job-name=plato-opt
#SBATCH --account=bekn-delta-cpu
#SBATCH --partition=cpu
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=1
#SBATCH --mem=32g
#SBATCH --time=02:00:00
#SBATCH --output=plato-%j.out
#SBATCH --error=plato-%j.err

# Load Plato environment
source /projects/bekn/jcernuda/plato/spack/share/spack/setup-env.sh
spack env activate /projects/bekn/jcernuda/plato

# Set library paths for cray-mpich
export LD_LIBRARY_PATH="/opt/cray/pe/mpich/8.1.32/ofi/gnu/11.2/lib:/opt/cray/libfabric/1.22.0/lib64:/opt/cray/pe/lib64:${LD_LIBRARY_PATH}"

echo "=== Plato job started at $(date) ==="
echo "=== Node: $(hostname), Tasks: ${SLURM_NTASKS} ==="

# Run Plato
srun plato input.i

echo "=== Plato job completed at $(date) ==="
```

## Interactive Testing (short runs)

```bash
srun --account=bekn-delta-cpu --partition=cpu-interactive \
  --time=00:30:00 --ntasks=4 --mem=16g --pty bash -c '
  source /projects/bekn/jcernuda/plato/spack/share/spack/setup-env.sh
  spack env activate /projects/bekn/jcernuda/plato
  export LD_LIBRARY_PATH="/opt/cray/pe/mpich/8.1.32/ofi/gnu/11.2/lib:/opt/cray/libfabric/1.22.0/lib64:/opt/cray/pe/lib64:${LD_LIBRARY_PATH}"
  srun plato input.i
'
```

## Monitoring

```bash
squeue -u $USER                    # Check job status
tail -f plato-<jobid>.out          # Watch output
scancel <jobid>                    # Cancel job
sacct -j <jobid> --format=JobID,State,ExitCode,Elapsed,MaxRSS  # Post-mortem
```

## Scaling Guidelines

| Mesh Size (elements) | MPI Ranks | Wall Time (50 iter) | Memory |
|---|---|---|---|
| < 10k | 1-2 | 10-30 min | 8 GB |
| 10k-50k | 4 | 30-60 min | 16 GB |
| 50k-200k | 8-16 | 1-4 hr | 32 GB |
| 200k+ | 16-32 | 4-12 hr | 64 GB |

## Working Directory

All input files (mesh.exo, analyze.xml, input.i) must be in the same directory.
Submit from that directory:

```bash
cd /path/to/problem/
sbatch run_plato.sh
```

## Validation

- [ ] All input files exist in working directory (mesh.exo, *.xml, input.i)
- [ ] SLURM account is correct (bekn-delta-cpu)
- [ ] Enough wall time for the problem size
- [ ] Output files appear after job starts (Iteration*.exo)

## Troubleshooting

| Issue | Cause | Fix |
|---|---|---|
| "command not found: plato" | Spack env not loaded | Add source/activate lines to batch script |
| MPI error | Wrong ntasks | Ensure ntasks >= sum of all service number_processors |
| Job killed (TIME) | Wall time too short | Increase --time |
| Job killed (OOM) | Not enough memory | Increase --mem |
| "Cannot find mesh" | Wrong working directory | cd to dir with mesh.exo before srun |
| Immediate exit, no output | Input file syntax error | Run `plato --check input.i` first |
