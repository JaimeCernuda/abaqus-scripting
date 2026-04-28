# Aurora — IN718 fatigue specimen — multi-objective topology optimization

Multi-load-case CPU+OpenMP run of the IN718 fatigue specimen on Aurora (ALCF). 3 load cases run as Plato MPMD performers, weighted-objective optimization, ROL trust-region solver.

## Problem

**IN718 fatigue specimen geometry** (146.17 × 64.60 × 25 mm) with 3 pin holes (Ø12.7 mm). The optimizer determines the material distribution that minimizes weighted compliance under three independent loading scenarios while respecting a volume constraint.

| Element | Value |
|---|---|
| Mesh | 9029 nodes, ~58k tet4 elements (h=3 mm) |
| Side sets | 5 (`fixed_left_yz`, `fixed_right_yz`, `load_upper`, `load_left_x`, `load_right_x`) |
| Material | Steel (linear elastic, E=200 GPa) |
| Filter | Helmholtz, radius=8 mm |
| Volume constraint | 68000 mm³ (~30% of design domain) |
| Objective | Weighted compliance: 0.5·LC1 + 0.25·LC2 + 0.25·LC3 |
| ROL | 50 trust-region iterations |
| MPMD ranks | 3 (one per load case, `number_of_processors=1` per `objective`) |

## Results

Both runs converged to **identical** values (deterministic optimization, same inputs):

| Run | Nodes | Ranks | Layout | Wall time | Compliance (start → end) |
|---|---|---|---|---|---|
| N=1 | 1 | 3 | 3 ranks/node | **1910 s** (31m50s) | 1793 → 439 (–76%) |
| N=2 | 2 | 3 | 1.5 ranks/node | **1993 s** (33m13s) | 1793 → 439 (–76%) |

### Why is N=2 slower than N=1?

This is the canonical failure mode of pure-ensemble scaling. The work is **3 independent load-case evaluations per ROL iteration**. With 3 ranks, that work parallelizes once across 3 LCs; spreading those 3 ranks across 2 nodes instead of 1 doesn't add any new parallelism — it only adds inter-node MPI latency for the master ↔ performer synchronization at every ROL step.

This run is a **multi-objective certification result** (the geometry survives all 3 load cases simultaneously) — it is not a strong-scaling result. For real strong-scaling on this geometry, each load case would need to decompose across multiple ranks (`number_of_processors > 1` per objective), which exposes a separate Plato MPMD bug we hit (see PORTING-AURORA.md).

## Renders (ParaView 6.0.0, headless)

`run-N{1,2}/in718_shape_iso.png` — solid-only thresholded topology
`run-N{1,2}/in718_density_3d.png` — full density colormap (Cool→Warm)
`run-N{1,2}/in718_shape_front.png` — front-on view of optimized shape
`run-N{1,2}/in718_midclip.png` — midplane density slice

## Files

| File | Purpose |
|---|---|
| `input.i` | Plato input deck — 3 objectives + volume constraint + ROL |
| `analyze_lc{1,2,3}.xml` | Plato Analyze problems for each load case |
| `analyze_volume.xml` | Volume criterion |
| `generate_mesh.py` | gmsh + netCDF4 mesh generation |
| `extract_results.py`, `render_matplotlib.py` | post-process |
| `run-aurora.sh` | PBS launcher (parameterized by `NODES`) |
| `run-N{1,2}/result.exo` | Optimized density field (Exodus II, 1.27 MB) |
| `run-N{1,2}/ROL_Optimizer.txt` | Per-iteration convergence log |
| `run-N{1,2}/run-N{1,2}.log` | Full PBS job output |

## Reproduction

```bash
qsub -l select=1                  -v NODES=1 run-aurora.sh
qsub -l select=2 -l place=scatter -v NODES=2 run-aurora.sh
```
