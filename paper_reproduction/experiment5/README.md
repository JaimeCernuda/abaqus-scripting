# Experiment 5: Topology Optimization of IN718 Fatigue Specimen

## Objective

Optimize the material distribution of the IN718 fatigue specimen from Experiment 4
using Tosca topology optimization. The goal is to minimize compliance (maximize stiffness)
while reducing volume to 40% of the original, keeping pin hole regions frozen.

## Prerequisites

- Full Abaqus license with Tosca optimization module
- Experiment 4 baseline results (for validation comparison)
- CHPC cluster access (kingspeak partition)

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/create_design_space.py` | Creates geometry, partitions frozen regions, meshes with C3D10 |
| `scripts/setup_optimization.py` | Configures SIMP topology optimization (penalty=3.0, vol<=40%) |
| `scripts/extract_results.py` | Post-processes: density field, convergence, summary CSV |
| `scripts/setup_validation_jobs.py` | Density-filtered validation: assigns void/solid materials, runs 20/60/100 kN |
| `scripts/run_validation.py` | Compares validation results against Experiment 4 baseline |
| `scripts/monitor_convergence.py` | Extracts per-iteration strain energy + density to CSV |
| `scripts/capture_geometry.py` | Screenshots of meshed geometry (requires GUI/xvfb) |
| `scripts/capture_to_results.py` | Screenshots of density contours + validation stress (requires GUI/xvfb) |
| `scripts/plot_convergence.py` | Matplotlib convergence plot (Python 3, runs locally) |

## CHPC Batch Scripts

| Script | Purpose |
|--------|---------|
| `chpc/submit_optimization.slurm` | Full TO pipeline: create + setup + optimize + extract + screenshots |
| `chpc/submit_validation.slurm` | Density-filtered validation: create jobs + compare + screenshots |
| `chpc/submit_experiment4.slurm` | Re-run Experiment 4 with refined 3mm mesh |
| `chpc/submit_all.sh` | Submit optimization + validation with SLURM dependency chain |
| `chpc/deploy.sh` | rsync scripts from local machine to cluster |
| `chpc/monitor.sh` | Cluster-side status dashboard (iteration count, logs, errors) |
| `chpc/download_results.sh` | Pull results (CSVs, screenshots, logs) to local machine |

### Test Scripts (staged deployment)

| Script | Stage | Purpose |
|--------|-------|---------|
| `chpc/test_slurm.slurm` | 0 | Trivial job to prove SLURM works |
| `chpc/test_abaqus.slurm` | 1 | Geometry creation + screenshot capture |
| `chpc/test_tosca.slurm` | 2 | 3-iteration TO to verify Tosca license |
| `chpc/test_validation.slurm` | 3 | Single-load (20 kN) density-filtered validation |

## Staged Deployment

Deploy incrementally — verify each stage before proceeding:

```bash
# Stage 0: Prove SLURM works
sbatch chpc/test_slurm.slurm

# Stage 1: Prove Abaqus runs + screenshots work
sbatch chpc/test_abaqus.slurm

# Stage 2: Prove Tosca license works (3 iterations)
sbatch chpc/test_tosca.slurm

# Stage 3: Prove density-filtered validation works (20 kN only)
sbatch chpc/test_validation.slurm

# Stage 4: Full pipeline
bash chpc/submit_all.sh
bash chpc/monitor.sh --watch
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `ABAQUS_MESH_SIZE` | `3.0` | Element seed size in mm |
| `ABAQUS_NUM_CPUS` | `1` | Number of CPUs for analysis jobs |
| `DENSITY_THRESHOLD` | `0.5` | Density cutoff for solid/void classification |
| `VALIDATION_LOADS` | `20,60,100` | Comma-separated load cases (kN) to validate |
| `CHPC_EMAIL` | (empty) | Email for SLURM job notifications |

## Optimization Parameters

- Method: SIMP (Solid Isotropic Material with Penalization)
- Penalty: 3.0
- Volume constraint: <= 40% of original
- Objective: Minimize strain energy (maximize stiffness)
- Primary load: 20 kN vertical (design load case)
- Frozen regions: Upper pin, lower left pin, lower right pin
- Manufacturing constraint: Minimum member size = mesh size
- Max iterations: 50
- Convergence: delta objective < 0.001

## Validation Approach

After optimization, validation re-analyzes the optimized topology under all load cases:
- Elements with density >= 0.5 keep full IN718 stiffness (E=200 GPa)
- Elements with density < 0.5 get near-zero stiffness (E=0.001 MPa)
- Three load cases (20/60/100 kN) are run and compared against Experiment 4 baseline

## Expected Results

- Clear load paths connecting upper pin to lower pins
- Optimized geometry retains material along primary stress paths
- Volume reduction from 100% to ~40%
- Stress concentration may increase at transitions between frozen and design regions
- Validation should show increased stress but maintained load paths vs Experiment 4

## Output Files

After full pipeline:
- `Experiment5_TO.cae` — Model database
- `Experiment5_TO/TOSCA_POST/*.odb` — Per-iteration results
- `optimization_summary.csv` — Key metrics
- `optimization_report.txt` — Detailed text report
- `convergence_history.csv` — Per-iteration strain energy and density
- `convergence_plot.png` — Convergence visualization
- `Validation_20kN.odb`, `Validation_60kN.odb`, `Validation_100kN.odb` — Validation results
- `validation_results.txt` — Comparison vs Experiment 4
- `validation_comparison.csv` — Tabular comparison data
- `screenshots/*.png` — Density contours and stress contour images
