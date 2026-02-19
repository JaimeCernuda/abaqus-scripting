# Topology Optimization Error Summary

Record of errors encountered while attempting to run Abaqus Tosca topology optimization on CHPC (University of Utah HPC cluster).

## Environment

- **Abaqus version**: 2025
- **Clusters tested**: kingspeak, notchpeak
- **Module**: `module load abaqus/2025`
- **License server**: ls1.chpc.utah.edu (extended token licensing)

---

## Error 1: `abaqus: command not found` (SLURM jobs)

**Symptom**: SLURM jobs fail immediately with `abaqus: command not found` (exit code 127).

**Root cause**: The CHPC setup script `setup_ab_slurm.sh` does NOT add `abaqus` to PATH. It only:
1. Runs `srun hostname` to build a host list
2. Writes MPI configuration to `abaqus_v6.env`
3. Unsets `SLURM_GTIDS`

**Fix**: Add `module load abaqus/2025` before sourcing the setup script.

```bash
# Correct order:
module load abaqus/2025                    # adds abaqus to PATH
source /uufs/.../abaqus/setup_ab_slurm.sh # configures MPI (optional for single-CPU)
```

**Affected experiments**: 6 (notchpeak run), job 11006048.

---

## Error 2: `OptimizationProcess.submit()` segfault (signal 11)

**Symptom**: Abaqus CAE crashes with signal 11 (SIGSEGV) when calling `opt_process.submit(validate=False)` in noGUI mode.

```
*** ABAQUS/ABQcaeK rank 0 terminated by signal 11
*** ERROR CATEGORY:  CAE
Abaqus Error: cae exited with an error code -11 (-0XB)
```

The `.exception` file shows:
```
ABAQUS/ABQcaeK rank 0 encountered a SEGMENTATION VIOLATION referencing location (nil)
```

**Observed on**:
- kingspeak (multiple runs during experiment 5/6 development)
- notchpeak (experiment 6, job 11006052 on notch309)

**What works before the crash**: The entire model builds successfully — geometry, material, mesh, optimization task, design responses, objective function, constraints, prototype job, and OptimizationProcess creation all complete. The `.cae` file is saved. The crash occurs specifically at the `submit()` call.

**What we tried**:
- `submit(validate=False)` — segfaults
- `submit(validate=True)` — not tested (validate=True means validate-only, doesn't run)
- Single CPU (`numCpus=1`) — segfaults
- Both kingspeak and notchpeak — segfaults on both

**Conclusion**: `submit()` appears broken in noGUI/headless mode in Abaqus 2025 on CHPC. The workaround is to use the Tosca CLI instead.

---

## Error 3: `writeParAndInputFiles()` KeyError (Abaqus 2025)

**Symptom**: Calling `opt_process.writeParAndInputFiles()` throws a `KeyError` in some configurations.

**Workaround**: Catch the KeyError and fall back to:
1. `mdb.jobs['...'].writeInput()` — generates the `.inp` file
2. Manually write a `.par` file using the Tosca parameter file format

**Status**: Intermittent. Sometimes works, sometimes throws KeyError. The fallback pipeline was built in experiment 5.

---

## Error 4: `setup_ab_slurm.sh` overwrites `abaqus_v6.env`

**Symptom**: Custom `abaqus_v6.env` settings (like `cpus = int(...)` to fix the str/int bug) are lost.

**Root cause**: `setup_ab_slurm.sh` unconditionally writes:
```bash
echo "" > abaqus_v6.env     # destroys existing file
echo "mp_mpi_implementation = IMPI" >> abaqus_v6.env
echo "mp_host_list=..." >> abaqus_v6.env
echo "mp_mpirun_path=..." >> abaqus_v6.env
```

**Fix**: Either:
- Skip `setup_ab_slurm.sh` entirely for single-CPU jobs
- Re-create `abaqus_v6.env` AFTER sourcing the setup script

---

## Error 5: `mpirun` not found

**Symptom**: `.err` file shows `/usr/bin/which: no mpirun in (...)`.

**Root cause**: `setup_ab_slurm.sh` calls `$(which mpirun)` but Intel MPI is not loaded. The script writes an empty path to `abaqus_v6.env`.

**Impact**: Low for single-CPU jobs (MPI not needed). For multi-CPU jobs, Intel MPI module may need to be loaded separately.

---

## Error 6: Abaqus 2025 `cpus` str/int type bug

**Symptom**: Abaqus 2025 fails when `cpus` in `abaqus_v6.env` is a string instead of an integer.

**Fix**: Use Python expression in `abaqus_v6.env`:
```python
import os
cpus = int(os.environ.get('ABAQUS_NUM_CPUS', '1'))
```

---

## Planned Resolution: Experiment 7

Experiment 7 will rebuild topology optimization from scratch using:
- **abqpy** (https://github.com/haiiliin/abqpy) as API reference
- **Built-in CHPC Tosca examples** (`/uufs/.../abaqus/2025/.../examples/topo/`) as working references
- **Tosca CLI** (`tosca optimize` or `abaqus optimization task=X.par`) instead of `submit()`
- **Incremental stages**: (A) FEA only, (B) TO setup, (C) TO + run
- Correct environment: `module load abaqus/2025`, no `setup_ab_slurm.sh` for single-CPU

### Key Discovery: Tosca CLI

CHPC has a `tosca` command with built-in examples:
```bash
tosca example airbeam_vol -s ABAQUS -scpus 1
```

The correct CLI for custom optimization:
```bash
tosca optimize -j JobName -par file.par -s ABAQUS -scpus 1
```

Or via the Abaqus wrapper:
```bash
abaqus optimization task=file.par job=JobName interactive
```
