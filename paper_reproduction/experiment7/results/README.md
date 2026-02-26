# Experiment 7: Topology Optimization on CHPC

**Date**: 2026-02-19
**Platform**: CHPC (University of Utah), Abaqus 2025 + Tosca Structure R2025x
**Cluster**: notchpeak-shared-short

## Summary

Five sub-experiments testing different approaches to run Tosca topology optimization on CHPC.

| Experiment | Approach | Model | Result | Cycles |
|---|---|---|---|---|
| **7a** | `tosca optimize` CLI | airbeam (built-in example) | PASS | 80 (converged ~26) |
| **7b** | `abaqus optimization` CLI | airbeam (built-in example) | PASS | 80 (converged ~26) |
| **7c** | CAE Python API (`writeParAndInputFiles`/`submit`) | airbeam (imported) | FAIL (Abaqus bug) | N/A |
| **7d** | Hybrid: CAE API + Tosca CLI | airbeam (imported) | PASS | 54 (converged ~26) |
| **7e** | Hybrid: CAE API + Tosca CLI | Custom 100x40x20 block | PASS | 7 (converged ~6) |

## Key Finding

`OptimizationProcess.writeParAndInputFiles()` and `OptimizationProcess.submit()` are broken in Abaqus 2025 noGUI mode. The prototype job is registered at the Python level but not in the C++ optimization subsystem, causing a KeyError or segfault (signal 11).

**Working workaround**: Use the CAE Python API for model creation and `Job.writeInput()`, then generate a Tosca `.par` file manually and run `tosca optimize` via the command line.

---

## Folder Contents

### 7a_tosca_cli/
Baseline: runs the built-in airbeam example directly with `tosca optimize` CLI.
- `airbeam_vol.inp` / `airbeam_vol.par` -- input files
- `optimization_report.csv` -- per-cycle objective/constraint values
- `TOSCA.OUT` -- full Tosca log
- `ISO_SMOOTHING_0_3.stl` -- smoothed optimized geometry (iso-value 0.3)
- `VOLUME_SMOOTHING_0_4.stl` -- smoothed geometry (volume-based, 0.4)
- `*.vtfx` -- 3D visualization files (viewable in 3DEXPERIENCE or GLview)
- `*.tab` -- tabular design response data per cycle
- `slurm_output.out` -- SLURM job log

### 7b_abaqus_cli/
Same as 7a but uses `abaqus optimization` wrapper instead of `tosca optimize` directly.
Produces identical results, confirming both CLI paths work.

### 7c_cae_api_diagnostic/
Diagnostic experiment that proves the CAE Python API bug. No optimization output.
- `run_7c.py` -- Python script (runs in `abaqus cae noGUI`)
- `run_7c.slurm` -- SLURM submission script
- `slurm_output.out` -- log showing KeyError on `writeParAndInputFiles()` and segfault on `submit()`

### 7d_hybrid_imported_model/
Imports the airbeam .inp into CAE, generates .par manually, runs Tosca CLI.
- `run_7d.py` / `run_7d.slurm` -- scripts
- `airbeam_vol.inp` -- original flat-format input (used by Tosca)
- `airbeam_FEA.inp` -- CAE-regenerated input (for reference only)
- `airbeam_7d.par` -- manually generated Tosca parameter file
- `optimization_report.csv` -- per-cycle data
- `TOSCA.OUT` -- full log (54 cycles)
- `ISO_SMOOTHING.stl` -- optimized geometry
- `slurm_output.out` -- SLURM log

### 7e_hybrid_custom_geometry/
Builds a 100x40x20 mm block from scratch in CAE, meshes it, applies BCs/loads,
flattens the .inp, generates .par, and runs Tosca optimization.
- `run_7e.py` / `run_7e.slurm` -- scripts
- `Block_FEA.inp` -- CAE-generated input (with *Part/*Instance structure)
- `Block_FEA_flat.inp` -- flattened input (Tosca-compatible)
- `Block_7e.par` -- Tosca parameter file
- `optimization_report.csv` -- per-cycle data
- `TOSCA.OUT` -- full log (7 cycles)
- `ISO_SMOOTHING.stl` -- optimized geometry
- `slurm_output.out` -- SLURM log

**Model**: 100 x 40 x 20 mm steel block, encastre on x=0 face, 1 MPa pressure on x=100 face.
**Optimization**: Minimize strain energy, volume <= 50%, frozen elements near BC face.
**Mesh**: 165 nodes, 80 C3D8R elements (10 mm seed size).

---

## How to View Results

- **STL files**: Open in any 3D viewer (MeshLab, ParaView, Blender, etc.)
- **VTFX files**: Open in 3DEXPERIENCE GLview or Ceetron GLview
- **CSV/TAB files**: Open in Excel or any spreadsheet tool
- **TOSCA.OUT**: Plain text log, open in any text editor

## How to Reproduce

```bash
# On CHPC:
module load abaqus/2025
cd experiment7/
sbatch chpc/run_7e.slurm   # or run_7d.slurm, etc.
```
