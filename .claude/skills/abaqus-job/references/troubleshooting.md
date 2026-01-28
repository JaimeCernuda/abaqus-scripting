# Job Troubleshooting

## Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "Job aborted" | Model errors | Check .msg and .dat files |
| "License not available" | License issue | Wait or check license server |
| "Memory exceeded" | Too fine mesh | Increase memory or coarsen mesh |
| "Too many increments" | Convergence issue | Check model, reduce load |
| "Element distortion" | Large deformation | Enable nlgeom, refine mesh |
| "Negative eigenvalue" | Instability | Check BCs, add stabilization |
| ".lck file exists" | Previous job running | Delete .lck if job is done |
| "Disk full" | Large output | Clear scratch, reduce output |

## Output Files

| Extension | Content | When to Check |
|-----------|---------|---------------|
| `.odb` | Results database | Post-processing |
| `.msg` | Solver messages | **First place for errors** |
| `.dat` | Printed output | Warnings, summaries |
| `.sta` | Status file | Increment progress |
| `.inp` | Input file | Model verification |
| `.cae` | Model database | Backup |
| `.lck` | Lock file | Indicates running job |
| `.log` | Log file | Solver progress |
| `.com` | Command file | Execution commands |

## Common Status Messages

| Status | Meaning |
|--------|---------|
| SUBMITTED | Job queued, waiting to start |
| RUNNING | Actively solving |
| COMPLETED | Finished successfully |
| ABORTED | Failed (check .msg file) |

## Debugging Workflow

1. **Check job status**
   ```python
   print(job.status)
   ```

2. **Read message file**
   ```python
   with open('JobName.msg', 'r') as f:
       print(f.read())
   ```

3. **Common .msg file warnings**
   - "WARNING: The system matrix has X negative eigenvalues"
   - "WARNING: Element X is distorted"
   - "WARNING: Contact pair X-Y not converged"

4. **Check .sta file for progress**
   ```
   STEP   INC  ATT  SEVERE  EQUIL  TOTAL    TIME/LPF
     1     1    1     0      1       1      0.100
   ```

## Performance Tips

- Use `numCpus=4` or more for large models
- Set `memory=90` (percentage) for adequate memory
- Use scratch directory for temp files on fast drive
- Enable `echoPrint=OFF` to reduce .dat file size
- Use element output reduction (`OUTPUT=SELECTED`)

## Convergence Issues

### Static Analysis Not Converging
```python
# Try smaller initial increment
model.StaticStep(
    name='Load',
    previous='Initial',
    initialInc=0.01,
    maxInc=0.1,
    minInc=1e-10,
    maxNumInc=1000
)
```

### Contact Not Converging
```python
# Add stabilization
model.StaticStep(
    name='Contact',
    previous='Initial',
    stabilizationMethod=DAMPING_FACTOR,
    continueDampingFactors=True,
    adaptiveDampingRatio=0.05
)
```

### Large Deformation Issues
```python
# Enable geometric nonlinearity
model.StaticStep(
    name='Load',
    previous='Initial',
    nlgeom=ON
)
```

## Memory Management

```python
# Check estimated memory before running
job = mdb.Job(name='Test', model='Model')
job.writeInput()  # Creates .inp file

# Run data check first
job_check = mdb.Job(name='Check', model='Model', type=DATACHECK)
job_check.submit()
job_check.waitForCompletion()
# Check .dat file for memory estimate
```

## Learning Edition Limits

- Maximum 1000 nodes
- No parallel processing
- No Tosca optimization

If you exceed node limit:
```python
# Increase mesh size
part.seedPart(size=10.0)  # Larger = fewer elements
part.generateMesh()
```

## Cleaning Up After Failed Jobs

```python
import os

job_name = 'FailedJob'
extensions = ['.lck', '.023', '.mdl', '.prt', '.res', '.stt']

for ext in extensions:
    filepath = f'{job_name}{ext}'
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Deleted {filepath}")
```
