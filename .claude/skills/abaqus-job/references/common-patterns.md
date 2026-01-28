# Common Job Patterns

## Standard Submit and Wait
```python
mdb.saveAs('Model.cae')
job = mdb.Job(name='Analysis', model='Model')
job.submit()
job.waitForCompletion()
print(f"Job completed with status: {job.status}")
```

## Parallel Processing
```python
job = mdb.Job(name='Analysis', model='Model', numCpus=4, numDomains=4)
job.submit()
job.waitForCompletion()
```

## Input File Only (for HPC submission)
```python
job = mdb.Job(name='Analysis', model='Model')
job.writeInput()  # Creates Analysis.inp
# Then submit via: abaqus job=Analysis cpus=8
```

## Data Check (verify model without solving)
```python
job = mdb.Job(name='Check', model='Model', type=DATACHECK)
job.submit()
job.waitForCompletion()
```

## Multiple Jobs (Parameter Study)
```python
for load in [100, 200, 300]:
    # Modify model...
    model.loads['Force'].setValues(magnitude=load)
    mdb.saveAs(f'Model_Load{load}.cae')

    job = mdb.Job(name=f'Load_{load}', model='Model')
    job.submit()
    job.waitForCompletion()

    if job.status == COMPLETED:
        print(f"Load {load} N completed successfully")
```

## Monitor Job Progress
```python
import time

job = mdb.Job(name='LongAnalysis', model='Model')
job.submit()

while job.status not in (COMPLETED, ABORTED):
    print(f"Status: {job.status}")
    time.sleep(10)

if job.status == COMPLETED:
    print("Analysis completed successfully!")
else:
    print("Analysis failed - check .msg file for errors")
```

## Submit Without Waiting (Background)
```python
job.submit()
# Returns immediately - job runs in background
# Check status later with job.status
```

## Optimization Process
```python
opt_process = mdb.OptimizationProcess(
    name='TopologyOpt',
    model='Model',
    task='OptTask',
    maxDesignCycle=50
)
opt_process.submit()
opt_process.waitForCompletion()
```

## Restart Analysis
```python
# Continue from a previous job
job = mdb.Job(
    name='Continue',
    model='Model',
    type=RESTART,
    restartJob='OriginalJob',
    restartStep='Step-1',
    restartIncrement=STEP_END
)
job.submit()
job.waitForCompletion()
```

## User Subroutine
```python
job = mdb.Job(
    name='WithUMAT',
    model='Model',
    userSubroutine='umat.for'
)
job.submit()
job.waitForCompletion()
```

## High Memory Job
```python
job = mdb.Job(
    name='LargeModel',
    model='Model',
    numCpus=8,
    numDomains=8,
    memory=95,
    memoryUnits=PERCENTAGE,
    scratch='D:/scratch'
)
job.submit()
job.waitForCompletion()
```

## Command Line Alternatives

```bash
# Run interactively (wait for completion)
abaqus job=MyJob interactive

# Run in background
abaqus job=MyJob

# With parallel processing
abaqus job=MyJob cpus=4 mp_mode=threads

# From input file
abaqus job=NewJob input=model.inp

# Double precision
abaqus job=MyJob double=both

# With user subroutine
abaqus job=MyJob user=umat.for
```
