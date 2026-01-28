---
name: abaqus-job
description: Create and manage Abaqus jobs - job creation, submission, monitoring, and input file generation.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
---

# Abaqus Job Skill

## When to Use This Skill

**USE when you need to:**
- Create and submit an analysis job
- Write input file (.inp) without running
- Configure parallel processing (CPUs)
- Set memory allocation
- Monitor job progress
- Create restart jobs
- Submit optimization processes

**Do NOT use for:**
- Extracting results after job completes → use `/abaqus-odb`
- Setting up the model → use other module skills
- Post-processing or visualization → use `/abaqus-odb`

## Key Decisions

### 1. Submit or Write Input Only?

| Goal | Method |
|------|--------|
| Run analysis | `job.submit()` |
| Generate INP file only | `job.writeInput()` |
| Run from command line | `abaqus job=Name` |

### 2. Parallel Processing

| Setting | When |
|---------|------|
| numCpus=1 | Small models, Learning Edition |
| numCpus=N | Large models, multi-core |
| mp_mode=THREADS | Shared memory (single node) |
| mp_mode=MPI | Distributed memory (cluster) |

## Required Inputs

| Input | Required | Default |
|-------|----------|---------|
| Job name | YES | - |
| Model name | YES | - |
| CPUs | NO | 1 |
| Memory | NO | 90% |

## Common Patterns

### Basic Job Submission
```python
# Save model first
mdb.saveAs(pathName='MyModel.cae')

# Create and submit job
job = mdb.Job(name='MyJob', model='MyModel')
job.submit()
job.waitForCompletion()
```

### Parallel Job
```python
job = mdb.Job(
    name='ParallelJob',
    model='MyModel',
    numCpus=4,
    numDomains=4,
    memory=90,
    memoryUnits=PERCENTAGE
)
job.submit()
job.waitForCompletion()
```

### Write Input Only (No Run)
```python
job = mdb.Job(name='MyJob', model='MyModel')
job.writeInput(consistencyChecking=OFF)
# Creates MyJob.inp
```

### Submit Without Waiting
```python
job.submit()
# Returns immediately - job runs in background
```

### Monitor Job Status
```python
import time

job.submit()
while job.status != COMPLETED:
    print(f"Status: {job.status}")
    time.sleep(10)

if job.status == COMPLETED:
    print("Success!")
elif job.status == ABORTED:
    print("Failed - check .msg file")
```

### Job from Input File
```python
job = mdb.JobFromInputFile(
    name='FromINP',
    inputFileName='existing_model.inp',
    numCpus=4
)
job.submit()
```

### Optimization Job
```python
opt_process = mdb.OptimizationProcess(
    name='TopologyOpt',
    model='MyModel',
    task='TopoTask',
    maxDesignCycle=50
)
opt_process.submit()
opt_process.waitForCompletion()
```

### Restart Job
```python
job = mdb.Job(
    name='RestartJob',
    model='MyModel',
    type=RESTART,
    restartJob='OriginalJob',
    restartStep='Step-1',
    restartIncrement=10
)
```

## Command Line Submission

```bash
# Run interactively (wait for completion)
abaqus job=MyJob interactive

# Run in background
abaqus job=MyJob

# With parallel
abaqus job=MyJob cpus=4 mp_mode=threads

# From input file
abaqus job=NewJob input=model.inp

# Optimization
abaqus optimization job=OptJob
```

## Output Files

| Extension | Content |
|-----------|---------|
| .odb | Results database |
| .dat | Printed output |
| .msg | Solver messages (check for errors) |
| .sta | Status (increment progress) |
| .inp | Input file |
| .cae | Model database |
| .lck | Lock file (job running) |

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Job aborted" | Analysis error | Check .msg file |
| "License not available" | No tokens | Wait or check license server |
| "Disk full" | Large output | Clear scratch, reduce output |
| "Memory error" | Model too large | Increase memory or coarsen mesh |
| ".lck file exists" | Previous job not cleaned up | Delete .lck if job is done |

## API Reference

For detailed parameters: [Job API](../../docs/abaqus-api/modules/job.md)
