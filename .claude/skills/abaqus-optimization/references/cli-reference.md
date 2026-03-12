# Tosca CLI Reference

## Primary Commands

### Start Optimization

```bash
tosca optimize -j JOBNAME -p PARFILE -s abaqus [-scpus N]
```

| Flag | Required | Description |
|------|----------|-------------|
| `-j JOBNAME` | Yes | Job name. Tosca creates a directory `JOBNAME/` for all outputs. |
| `-p PARFILE` | Yes | Path to the `.par` parameter file. |
| `-s abaqus` | Yes | FE solver name. Use `abaqus` for Abaqus. |
| `-scpus N` | No | Number of CPUs for the FE solver (default: 1). |

The `.par` file must reference the flattened `.inp` via `FILE = flat_input.inp` in its `FEM_INPUT` block.

Alternative syntax (equivalent):
```bash
ToscaStructure --job JOBNAME --solver abaqus
```

### Check Run (Test Before Optimizing)

```bash
ToscaStructure --job JOBNAME --solver abaqus --type test1
```

Validates the FE model and `.par` file without running a full optimization. The `.par` and `.inp` files must already exist in the working directory. Always run this before a production optimization to catch errors early.

### Generate Postprocessing Report

```bash
ToscaStructure --job JOBNAME --report
```

Calls Tosca Structure.REPORT, which generates a `.vtfx` file in `JOBNAME/TOSCA_POST/` after a successful optimization. The `.vtfx` file contains visualization sequences and convergence graphs.

### Smooth Results for CAD Export

```bash
ToscaStructure --job JOBNAME --smooth
```

Calls Tosca Structure.SMOOTH, which prepares optimization results for transfer to CAD. If the `.par` file contains a `SMOOTH` block with `FORMAT = stl`, this produces an STL file.

### View Results

```bash
ToscaStructure --view JOBNAME/TOSCA_POST/file.vtfx
```

Opens Tosca Structure.view for interactive visualization of optimization results (animation over iterations).

### Get Help

```bash
ToscaStructure --help
```

## Logging

Logging is always written to `JOBNAME/TOSCA.OUT`. Control verbosity with these flags:

```bash
ToscaStructure --loglevel LEVEL --loglevel_stdout LEVEL ...
```

| Level | Description |
|-------|-------------|
| `WARNING` | Only warnings and errors (not recommended). |
| `NOTICE` | Default stdout output. Most important messages only. |
| `INFO` | Default log file output. Standard detail. |
| `DEBUG` | Very verbose. Useful for support/troubleshooting. |
| `TRACE` | Extremely verbose. Major performance loss. Developers only. |

`--loglevel` must be equal to or more verbose than `--loglevel_stdout`.

Example: INFO on stdout, DEBUG in log file:
```bash
ToscaStructure --loglevel_stdout INFO --loglevel DEBUG --job JOBNAME --solver abaqus
```

## Output Files and Directories

After optimization, the `JOBNAME/` directory contains:

| File/Directory | Description |
|----------------|-------------|
| `TOSCA.OUT` | Main log file. Search for CRITICAL, ERROR, WARNING. |
| `optimization_report.csv` | Per-cycle objective and constraint values. |
| `optimization_status_all.csv` | Extended status with convergence metrics. |
| `SAVE.inp/` | Directory with per-cycle `.inp` files (for validation FEA). |
| `SAVE.inp/<N>/` | Cycle N directory with modified `.inp` and `tosca_distribution.inp`. |
| `TOSCA_POST/` | Postprocessing data (created by `--report`). |
| `DB_ERROR/` | Created on failure; contains all files needed to diagnose the error. |
| `authorization.log` | License and configuration information. |
| `*.stl` | Smoothed geometry (if SMOOTH block in `.par` with `FORMAT = stl`). |

## Environment Variables

| Variable | Description |
|----------|-------------|
| `FED_OMP_NUM_THREADS` | OpenMP threads for Tosca (not the solver). |
| `SLURM_GTIDS` | Must be **unset** on SLURM clusters (`unset SLURM_GTIDS`). |
| `I_MPI_HYDRA_TOPOLIB` | Set to `ipl` for Intel MPI on HPC. |

## Finding the Tosca Command

Tosca may be available under different names depending on installation:

```python
# Priority order for finding Tosca
tosca_cmds = ['tosca', 'abaqus tosca', 'abaqus optimization']

for candidate in tosca_cmds:
    try:
        cmd_parts = candidate.split()
        test = subprocess.Popen(cmd_parts + ['--help'],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out, _ = test.communicate()
        if test.returncode == 0:
            print("Found Tosca via: '{}'".format(candidate))
            break
    except OSError:
        continue
```

On HPC systems, load the module first:
```bash
module load abaqus/2025    # loads both Abaqus and Tosca
```

## .par File Constraints (for CLI usage)

- One line must not exceed **160 characters**.
- Save with **UTF-8** encoding (mandatory for Unicode characters).
- `FEM_INPUT` block must reference the **flattened** `.inp` (no Part/Instance/Assembly hierarchy).
- Both `.par` and `.inp` files should be in the working directory, or use absolute paths.
