# Job API Quick Reference

## Job Creation
```python
job = mdb.Job(
    name='JobName',
    model='ModelName',
    type=ANALYSIS,              # or RESTART, DATACHECK
    numCpus=4,                  # Parallel processing
    numDomains=4,               # For domain decomposition
    memory=90,                  # Memory percentage
    memoryUnits=PERCENTAGE,
    scratch=''                  # Scratch directory
)
```

## Job Submission
```python
job.submit()                    # Submit (non-blocking)
job.waitForCompletion()         # Wait for finish

# Or submit interactively
job.submit(consistencyChecking=OFF)
job.waitForCompletion()
```

## Job Status
```python
job.status                      # Check status
# Values: SUBMITTED, RUNNING, COMPLETED, ABORTED
```

## Input File Operations
```python
job.writeInput()                # Generate .inp file only
job.writeInput(consistencyChecking=OFF)  # Skip checks
```

## Batch Command (external)
```bash
abaqus job=JobName interactive
abaqus job=JobName cpus=4
abaqus datacheck job=JobName
```

## Full Job Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| name | str | Job name (required) |
| model | str | Model name (required) |
| type | SymbolicConstant | ANALYSIS, RESTART, DATACHECK |
| numCpus | int | Number of CPUs (default 1) |
| numDomains | int | Domain decomposition (for MPI) |
| memory | int | Memory allocation |
| memoryUnits | SymbolicConstant | PERCENTAGE or MEGA_BYTES |
| scratch | str | Scratch directory path |
| userSubroutine | str | Path to user subroutine |
| explicitPrecision | SymbolicConstant | SINGLE, DOUBLE |
| echoPrint | Boolean | Print input echo |
| modelPrint | Boolean | Print model data |
| contactPrint | Boolean | Print contact info |
| historyPrint | Boolean | Print history output |

## Restart Job Parameters

```python
job = mdb.Job(
    name='RestartJob',
    model='ModelName',
    type=RESTART,
    restartJob='OriginalJob',     # Previous job name
    restartStep='Step-1',          # Step to restart from
    restartIncrement=10            # Increment number
)
```

## JobFromInputFile

```python
job = mdb.JobFromInputFile(
    name='FromINP',
    inputFileName='model.inp',
    numCpus=4,
    numDomains=4,
    memory=90,
    memoryUnits=PERCENTAGE
)
```
