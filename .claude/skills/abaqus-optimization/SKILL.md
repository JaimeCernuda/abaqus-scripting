---
name: abaqus-optimization
description: Execute topology optimization via Tosca CLI. Use when user mentions running optimization, tosca optimize, check run, SLURM job, post-processing optimization results, smoothing, STL export, or validation run.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
  - Bash(tosca:*)
  - Bash(sbatch:*)
---

# Tosca CLI Workflow Skill

This skill covers **executing** topology optimization via the Tosca CLI. For **authoring** the `.par` file (design responses, objectives, constraints, frozen regions), see the tosca skill. For the **complete end-to-end topology optimization workflow** (geometry through results), see `/abaqus-topology-optimization`.

## When to Use This Skill

**Route here when user mentions:**
- "run optimization", "tosca optimize", "start tosca"
- "check run", "test run", "test1"
- "SLURM job", "submit to cluster", "CHPC", "sbatch"
- "optimization report", "convergence", "post-processing results"
- "smoothing", "STL export", "iso smoothing"
- "validation run", "run FEA on optimized design"
- "flatten inp", "renumber RP nodes"
- Debugging Tosca CLI errors (segfault, license, stale files)

**Route elsewhere:**
- Writing `.par` file content (DV_TOPO, DRESP, CONSTRAINT, etc.) -> tosca skill
- Complete topology optimization workflow -> `/abaqus-topology-optimization`
- Building the FEA model (geometry, mesh, BCs, loads) -> module skills
- CAE-based optimization API (TopologyTask, ObjectiveFunction) -> valid alternative for Abaqus built-in optimization; see `/abaqus-topology-optimization` for correct usage

## Two Optimization Paths

### Path A: CAE API (Abaqus built-in optimization)

The CAE optimization API (`TopologyTask`, `ObjectiveFunction`, `OptimizationProcess`) works correctly when used with the proper tuple format. The key pitfall: `ObjectiveFunction.objectives` must use **4-tuples** `(suppress, designResponse, weight, referenceValue)`. Passing a 5-tuple (e.g., with a trailing empty string) corrupts C++ state and causes segfaults/KeyErrors.

See `/abaqus-topology-optimization` for correct CAE API usage patterns.

### Path B: Tosca CLI (primary workflow for this project)

For Tosca-specific features or standalone Tosca execution, the hybrid pipeline is used:

```
CAE Python API (noGUI)          Tosca CLI
--------------------------      ---------
1. Build geometry
2. Mesh
3. Material + section
4. Assembly, step, BCs, loads
5. noPartsInputFile=ON -------> 6. Generate .par file (hand-written)
   + writeInput()                7. tosca optimize -p file.par -s abaqus
                                 8. Output: ISO_SMOOTHING.stl
```

**Note:** Tosca `.par` files must be hand-written. CAE generates `.par` for its own optimization system, not for standalone Tosca.

## Prerequisites

Before running Tosca CLI:
1. A flat `.inp` file (use `noPartsInputFile=ON` before `writeInput()`)
2. A `.par` parameter file referencing the flat `.inp`
3. Full Abaqus license with Tosca module (not Learning Edition)
4. Tosca on PATH (`tosca` command available or `abaqus tosca`)

## Workflow: Running Optimization

### Step 1: Generate Flat .inp File

Tosca requires flat `.inp` files without `*Part`/`*Instance`/`*Assembly` hierarchy. Use `noPartsInputFile=ON` before `writeInput()`:

```python
mdb.models['Model-1'].setValues(noPartsInputFile=ON)
mdb.jobs[job_name].writeInput()
```

This produces a flat `.inp` directly — no manual flattening or RP node renumbering needed.

**Legacy approach:** If `noPartsInputFile` is not available, the `.inp` can be flattened manually. See `references/common-patterns.md` Pattern 1 and Pattern 2 for the legacy flattening code.

### Step 2: Check Run (Test Before Optimizing)

```bash
ToscaStructure --job JOBNAME --solver abaqus --type test1
```

This validates the FE model and `.par` file without running a full optimization. Always do this first.

### Step 3: Run Optimization

```bash
tosca optimize -j JOBNAME -p PARFILE -s abaqus -scpus N
```

Or equivalently:
```bash
ToscaStructure --job JOBNAME --solver abaqus
```

The `.par` file must reference the flattened `.inp` via `FILE = flat.inp` in its `FEM_INPUT` block. Both files must be in the current working directory or use absolute paths.

### Step 4: Monitor Progress

- Watch `JOBNAME/TOSCA.OUT` for CRITICAL/ERROR/WARNING messages
- Check `optimization_report.csv` for per-cycle objective and constraint values
- Check `optimization_status_all.csv` for extended convergence metrics

### Step 5: Generate Report and Smooth Results

```bash
# Generate postprocessing report (.vtfx for visualization)
ToscaStructure --job JOBNAME --report

# Smooth results for CAD export (STL)
ToscaStructure --job JOBNAME --smooth
```

### Step 6: Validation Run (FEA on Optimized Design)

Tosca deletes per-cycle ODB files. To visualize stress/displacement on the optimized design, run Abaqus FEA on the last-cycle `.inp` from `SAVE.inp/<N>/`:

```bash
cd JOBNAME/SAVE.inp/<last_cycle>/
abaqus job=Optimized input=flat.inp cpus=N interactive
```

The last-cycle `.inp` includes `tosca_distribution.inp` with per-element density values (SIMP penalties), so the FEA runs on the actual optimized topology.

## Key CLI Flags

| Flag | Meaning |
|------|---------|
| `-j JOBNAME` | Job name; Tosca creates a directory with this name |
| `-p PARFILE` | Path to the `.par` parameter file |
| `-s abaqus` | FE solver to use |
| `-scpus N` | Number of CPUs for the FE solver |
| `--loglevel DEBUG` | Verbose logging to `TOSCA.OUT` |
| `--loglevel_stdout INFO` | Show more detail on stdout |
| `--type test1` | Check run (validate without optimizing) |
| `--report` | Generate postprocessing data |
| `--smooth` | Smooth results for CAD transfer |

## SLURM Integration

For HPC clusters, see `references/common-patterns.md` Pattern 3 for a complete SLURM script. Key considerations:

- `module load abaqus/2025` (loads both Abaqus and Tosca)
- `unset SLURM_GTIDS` (prevents Abaqus MPI issues)
- `export I_MPI_HYDRA_TOPOLIB=ipl` (Intel MPI topology)
- Set `ABAQUS_NUM_CPUS`, `ABAQUS_MESH_SIZE`, etc. as environment variables
- Use `Xvfb` for visualization steps on headless nodes

## Validation Checklist

After optimization completes:
- [ ] `TOSCA.OUT` shows no CRITICAL or ERROR messages
- [ ] `optimization_report.csv` shows objective converging
- [ ] Constraints satisfied in final cycle
- [ ] STL file produced (if SMOOTH block in `.par`)
- [ ] Validation FEA runs on last-cycle `.inp` without errors
- [ ] Stress/displacement results are physically reasonable

## Troubleshooting

See `references/troubleshooting.md` for detailed error resolution.

| Problem | Quick Fix |
|---------|-----------|
| `tosca: command not found` | Check PATH, try `abaqus tosca` or load module |
| Segfault from `submit()` | Check ObjectiveFunction tuple format — must be 4-tuple, not 5-tuple |
| KeyError from `writeParAndInputFiles()` | Caused by corrupted C++ state from wrong tuple format; fix ObjectiveFunction 4-tuple |
| Stale `.onf`/`.db` files | Delete `JOBNAME/` directory before re-running |
| RP node collision | Renumber RP nodes with offset (see Pattern 2) |

## Code Patterns

For actual code from the working experiments, see:
- [CLI Reference](references/cli-reference.md)
- [Common Patterns](references/common-patterns.md)
- [Troubleshooting Guide](references/troubleshooting.md)
