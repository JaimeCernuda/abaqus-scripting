# NCSA Delta Quick Reference

## Login
```bash
ssh jcernuda@login.delta.ncsa.illinois.edu
```
Login nodes: `dt-login01` through `dt-login04`

**CRITICAL: This is a shared cluster. DO NOT run computation on login nodes.**
- CPU limit: ~16 cores per user
- Memory limit: 37 GB soft / 62 GB hard per user
- Automated scripts will kill offending processes
- Use `srun` or `sbatch` for ALL real work

## Accounts & Allocations

| Account | Balance | Project |
|---|---|---|
| `bekn-delta-cpu` | 4,152 hrs | iowarp |
| `bekn-delta-gpu` | 216 hrs | iowarp |

Check with: `accounts`

## Storage

| Path | Quota | Backed Up? | Notes |
|---|---|---|---|
| `/u/jcernuda` | 100 GB | Yes (daily snapshots, 30 days) | Home directory |
| `/projects/bekn` | 500 GB | TBA | Shared project space |
| `/work/nvme/bekn` | 500 GB | No | Fast NVMe scratch |
| `/work/hdd/bekn` | 1 TB | No | HDD scratch |
| `/tmp` (node-local) | 740 GB–1.5 TB | No | Deleted after job ends |

Check with: `quota`

Snapshots: `~/.snapshot/snapshot-daily-YYYY-MM-DD_HH_mm_ss_UTC/`

## Partitions

| Partition | Nodes | Max Time | Charge Factor |
|---|---|---|---|
| `cpu` | 128-core AMD Milan, 256 GB | 48 hr | 1.0 |
| `cpu-interactive` | same | 1 hr | 2.0 |
| `gpuA100x4` | 64-core, 4x A100 40GB, 256 GB | 48 hr | 1.0 |
| `gpuA100x4-interactive` | same | 1 hr | 2.0 |
| `gpuA40x4` | 64-core, 4x A40 48GB, 256 GB | 48 hr | 0.6 |
| `gpuA40x4-interactive` | same | 1 hr | 1.2 |
| `gpuA100x8` | 128-core, 8x A100 40GB, 2 TB | 48 hr | 4.0 |
| `gpuH200x8` | 128-core, 8x H200 141GB, 2 TB | 48 hr | 3.0 |
| `gpuMI100x8` | 128-core, 8x MI100 32GB, 2 TB | 48 hr | 1.5 |

Preemptible variants (`*-preempt`) available at same time limits.

## SLURM Job Submission

### Interactive Sessions
```bash
# CPU interactive
srun --account=bekn-delta-cpu --partition=cpu-interactive \
  --time=00:30:00 --mem=32g --pty bash

# GPU interactive
srun --account=bekn-delta-gpu --partition=gpuA100x4-interactive \
  --time=00:30:00 --mem=64g --gpus-per-node=1 --pty bash
```

### Batch Job Template (CPU)
```bash
#!/bin/bash
#SBATCH --job-name=my_job
#SBATCH --account=bekn-delta-cpu
#SBATCH --partition=cpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=64g
#SBATCH --time=01:00:00
#SBATCH --output=%x-%j.out

module load modtree/cpu
srun ./my_program
```

### Batch Job Template (GPU)
```bash
#!/bin/bash
#SBATCH --job-name=my_gpu_job
#SBATCH --account=bekn-delta-gpu
#SBATCH --partition=gpuA100x4
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=64g
#SBATCH --time=01:00:00
#SBATCH --gpus-per-node=1
#SBATCH --gpus-per-task=1
#SBATCH --gpu-bind=verbose,per_task:1
#SBATCH --output=%x-%j.out

module load modtree/gpu
srun ./my_program
```

### Required SBATCH Directives
- `--partition=` — which queue
- `--account=` — your allocation (`bekn-delta-cpu` or `bekn-delta-gpu`)
- `--time=` — wall time (HH:MM:SS)

## Useful Commands

```bash
accounts                    # List allocations and balances
quota                       # Check storage usage
squeue -u $USER             # Your running/pending jobs
sinfo --summarize           # Partition availability
scontrol show job <JOBID>   # Detailed job info
scancel <JOBID>             # Cancel a job
module avail                # List available modules
module spider <name>        # Search for a module
module load <name>          # Load a module
module list                 # Show loaded modules
```

## Modules (Lmod)

Default loaded: `gcc-native/13.2`, `PrgEnv-gnu`, `cray-mpich`, `cudatoolkit/25.3_12.8`

```bash
module load modtree/gpu     # GPU environment (default)
module load modtree/cpu     # CPU-only environment
```

## Data Transfer

- **Small files:** `scp`, `rsync`
- **Large transfers:** Globus (endpoints: "NCSA Delta" or "ACCESS Delta")

## Documentation

https://docs.ncsa.illinois.edu/systems/delta/en/latest/
