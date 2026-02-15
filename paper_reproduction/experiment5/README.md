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
| `scripts/run_validation.py` | Re-analyzes optimized shape at 20/60/100 kN, compares to Exp4 |

## SLURM Batch Scripts

| Script | Purpose |
|--------|---------|
| `chpc/submit_optimization.slurm` | Full TO pipeline (create + setup + optimize + extract) |
| `chpc/submit_validation.slurm` | Post-TO validation (run after optimization completes) |
| `chpc/submit_experiment4.slurm` | Re-run Experiment 4 with refined 3mm mesh |

## Running on CHPC

```bash
# 1. Run topology optimization
sbatch chpc/submit_optimization.slurm

# 2. After TO completes, run validation
sbatch chpc/submit_validation.slurm
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `ABAQUS_MESH_SIZE` | `3.0` | Element seed size in mm |
| `ABAQUS_NUM_CPUS` | `1` | Number of CPUs for analysis jobs |

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

## Expected Results

- Clear load paths connecting upper pin to lower pins
- Optimized geometry retains material along primary stress paths
- Volume reduction from 100% to ~40%
- Stress concentration may increase at transitions between frozen and design regions
- Validation should show increased stress but maintained load paths vs Experiment 4

## Output Files

After optimization:
- `Experiment5_TO.cae` — Model database
- `Experiment5_TO/TOSCA_POST/*.odb` — Per-iteration results
- `optimization_summary.csv` — Key metrics
- `optimization_report.txt` — Detailed text report
- `validation_results.txt` — Comparison vs Experiment 4
- `validation_comparison.csv` — Tabular comparison data
