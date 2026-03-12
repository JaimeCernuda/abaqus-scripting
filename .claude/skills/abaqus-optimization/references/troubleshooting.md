# Tosca CLI Troubleshooting

## "tosca: command not found"

**Cause:** Tosca is not on PATH.

**Solutions:**

1. On HPC clusters, load the module first:
   ```bash
   module load abaqus/2025    # loads both Abaqus and Tosca
   ```

2. Try alternative command names:
   ```bash
   tosca optimize ...           # Direct tosca command
   abaqus tosca optimize ...    # Via Abaqus launcher
   abaqus optimization ...      # Older Abaqus versions
   ```

3. Find the Tosca install path and add to PATH:
   ```bash
   # Typical locations:
   # Linux: /opt/SIMULIA/Tosca/2025/linux_a64/code/command/
   # Windows: C:\SIMULIA\Tosca\2025\win_b64\code\command\
   export PATH=$PATH:/opt/SIMULIA/Tosca/2025/linux_a64/code/command
   ```

4. Use the full path to the start script:
   ```bash
   /path/to/ToscaStructure.sh --job JOBNAME --solver abaqus
   # or on Windows:
   "C:\path\to\ToscaStructure.bat" --job JOBNAME --solver abaqus
   ```

## Segfault from OptimizationProcess.submit()

**Cause:** The `ObjectiveFunction.objectives` parameter was passed a **5-tuple** instead of the correct **4-tuple**. The trailing element (typically an empty string `''`) corrupts internal C++ state, causing a null pointer dereference.

**Error looks like:**
```
Abaqus Error: cae exited with an error.
```
Or simply a crash with no error message and a core dump.

**Solution:** Fix the `ObjectiveFunction.objectives` tuple format:

```python
# WRONG — 5-tuple corrupts C++ state, causes segfault:
model.optimizationTasks['Task'].ObjectiveFunction(
    name='ObjFunc',
    objectives=((OFF, 'DR_StrainEnergy', 1.0, 0.0, ''),))  # 5 elements!

# CORRECT — 4-tuple (suppress, designResponse, weight, referenceValue):
model.optimizationTasks['Task'].ObjectiveFunction(
    name='ObjFunc',
    objectives=((OFF, 'DR_StrainEnergy', 1.0, 0.0),))  # 4 elements
```

**Alternative:** If using the Tosca CLI path, bypass the CAE optimization API entirely and write the `.par` file manually.

## KeyError from writeParAndInputFiles()

**Cause:** Typically a downstream consequence of corrupted C++ state from a wrong tuple format in `ObjectiveFunction`. The prototype job reference becomes invalid in the internal C++ map.

**Error looks like:**
```
KeyError: 'JobName'
```

**Solution:** Fix the `ObjectiveFunction.objectives` tuple format (must be 4-tuple). If the error persists after fixing the tuple, use `writeInput()` + manual `.par` as an alternative:

```python
# Fix the tuple format first:
objectives=((OFF, 'DR_StrainEnergy', 1.0, 0.0),)  # 4-tuple

# If still failing, use writeInput() + manual .par for Tosca CLI:
mdb.models['Model-1'].setValues(noPartsInputFile=ON)
mdb.jobs[job_name].writeInput()
# ... write .par file manually ...
```

## Hierarchical .inp Not Readable by Tosca

**Cause:** By default, `writeInput()` produces hierarchical `.inp` with `*Part`/`*Instance`/`*Assembly` wrappers that Tosca cannot parse.

**Solution:** Set `noPartsInputFile=ON` before calling `writeInput()`:

```python
mdb.models['Model-1'].setValues(noPartsInputFile=ON)
mdb.jobs[job_name].writeInput()
```

This produces a flat `.inp` directly — no manual flattening needed.

## Solver License Errors

**Error looks like:**
```
Error in TOSCA.OUT: CRITICAL - FE solver failed
```
Or in `authorization.log`:
```
License not available for Tosca_Structure
```

**Solutions:**

1. Verify license server is reachable:
   ```bash
   abaqus licensing lmstat -a
   ```

2. Check that both Abaqus and Tosca licenses are available:
   ```bash
   abaqus information=release    # Should show version info
   tosca --help                   # Should show help text
   ```

3. On CHPC/HPC, ensure the correct module is loaded:
   ```bash
   module list                    # Check loaded modules
   module load abaqus/2025        # Load if missing
   ```

4. Check `JOBNAME/authorization.log` for detailed license diagnostics.

## CHPC Module Loading

**Problem:** Tosca or Abaqus commands fail on HPC cluster.

**Required setup for CHPC (University of Utah):**

```bash
module load abaqus/2025
unset SLURM_GTIDS                    # MANDATORY: prevents Abaqus MPI hangs
export I_MPI_HYDRA_TOPOLIB=ipl       # Intel MPI topology for multi-CPU
```

**Why `unset SLURM_GTIDS` is mandatory:** SLURM sets `SLURM_GTIDS` which conflicts with how Abaqus initializes MPI. Without unsetting it, Abaqus will hang during solver startup.

## Stale .onf/.db Files from Previous Runs

**Problem:** Re-running optimization fails with errors about existing files or corrupted state.

**Error looks like:**
```
ERROR: Job directory already exists
```
Or unexpected results from a "resumed" run instead of a fresh start.

**Solution:** Delete the entire job output directory before re-running:

```bash
rm -rf JOBNAME/
tosca optimize -j JOBNAME -p file.par -s abaqus
```

In a SLURM script:
```bash
rm -rf $WORK_DIR
mkdir -p $WORK_DIR
cd $WORK_DIR
```

## Memory/CPU Configuration for Parallel Runs

**Problem:** Out of memory or solver crashes on large models.

**Configuration checklist:**

| Parameter | Where to Set | Example |
|-----------|-------------|---------|
| Solver CPUs | `-scpus N` on CLI | `-scpus 8` |
| SLURM memory | `#SBATCH --mem=120G` | 120G for ~100k elements |
| SLURM CPUs | `#SBATCH --ntasks=8` | Match `-scpus` |
| Wall time | `#SBATCH --time=48:00:00` | 48h for production |

**Rules of thumb:**
- Memory: ~1 GB per 10k elements for C3D10 meshes
- CPUs: 4-8 is typical; diminishing returns above 8 for most models
- Time: 1mm mesh with 75 cycles on IN718 specimen takes ~12-24 hours

## RP Node Collision in Flattened .inp

**Problem:** Tosca crashes or gives wrong results because assembly-level reference point (RP) nodes have IDs (1, 2, 3) that collide with mesh node IDs.

**Error looks like:**
```
ERROR: Duplicate node definition
```
Or silent incorrect results (loads applied to wrong nodes).

**Solution:** Renumber RP nodes during flattening. Add `max_mesh_node` as offset to all RP node IDs:

```python
rp_offset = max_mesh_node  # e.g., 50000
rp_node_map = {}
for old_id in rp_nodes:
    rp_node_map[old_id] = old_id + rp_offset
# old_id=1 -> new_id=50001, old_id=2 -> new_id=50002, etc.
```

See `references/common-patterns.md` Patterns 1-2 for the full implementation.

## Tosca Cannot Read Hierarchical .inp

**Problem:** Tosca fails to parse the `.inp` file written by Abaqus CAE.

**Error looks like:**
```
ERROR: Unknown keyword *PART
```
Or:
```
ERROR: Instance not found
```

**Cause:** Abaqus CAE writes `.inp` files with `*Part`/`*Instance`/`*Assembly` hierarchy by default. Tosca expects flat `.inp` files.

**Solution:** Use `noPartsInputFile=ON` before `writeInput()` to produce a flat `.inp` directly:

```python
mdb.models['Model-1'].setValues(noPartsInputFile=ON)
mdb.jobs[job_name].writeInput()
```

**Alternative:** Tosca can auto-flatten hierarchical `.inp` during its data check, but set names get prefixed with `<assembly>_<instance>_`.

**Legacy:** Manual flattening code is in `references/common-patterns.md` Patterns 1-2.

## TOSCA.OUT Error Analysis

When optimization fails, always check `JOBNAME/TOSCA.OUT` first:

```bash
# Search for errors
grep -i "CRITICAL\|ERROR\|WARNING" JOBNAME/TOSCA.OUT

# Check the DB_ERROR directory (created automatically on failure)
ls -la JOBNAME/DB_ERROR/
```

The `DB_ERROR/` directory contains:
- Protocol files from the FE solver
- The initial model and parameter file
- All files and macros needed to reproduce the error

## Optimization Not Converging

**Problem:** Objective oscillates or does not improve after many cycles.

**Solutions:**

1. Relax constraints (increase volume fraction or stress limit):
   ```
   # In .par file:
   CONSTRAINT
     LE_VALUE = 1000.0    # was 800.0
   END_
   ```

2. Increase max iterations:
   ```
   STOP
     ITER_MAX = 100       # was 50
   END_
   ```

3. Adjust filter radius (typically 2-4x mesh size):
   ```
   OPT_PARAM
     TOPO_FILTER_RADIUS = 6.0    # was 3.0
   END_
   ```

4. Check `optimization_report.csv` to see if constraints are being violated or if the objective is plateauing.

## Result File Errors

**Problem:** Tosca stops because the FE solver result file is invalid.

**Common causes (from Tosca docs):**
- No node stresses written in the result file (check output requests)
- Solver cannot perform FEA due to numerical problems
- Element twisting from missing BCs or too-large displacements
- Rigid body motion in the model

**Solution:** Run a standalone static analysis first (`abaqus job=test input=flat.inp interactive`) to verify the FEA model works before optimization.
