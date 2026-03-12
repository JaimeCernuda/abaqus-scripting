# Interaction Troubleshooting

## Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "Contact not detected" | Surfaces too far apart | Use adjust=ON or check initial gap |
| "Overclosure too large" | Initial penetration | Adjust geometry or use interference fit |
| "Convergence failure" | Contact instability | Use stabilization, smaller increments |
| "Tie failed" | Non-matching surfaces | Check surface definitions |
| "Severe discontinuity" | Contact chattering | Add contact stabilization |
| "Negative eigenvalue" | Improper master/slave | Swap master and slave surfaces |
| "Zero pivot" | Unconstrained rigid body | Check BCs, add contact stabilization |

## Master/Slave Selection Rules

- **Master**: stiffer, coarser mesh
- **Slave**: softer, finer mesh
- Smaller surface should typically be slave
- Analytical rigid surfaces must be master

## Contact Convergence Issues

### Symptoms
- Analysis terminates with "Too many attempts"
- Severe discontinuity warnings
- Contact opening/closing repeatedly

### Solutions

1. **Add contact stabilization**
```python
model.SurfaceToSurfaceContactStd(
    name='Contact',
    createStepName='Step-1',
    master=master_surf,
    slave=slave_surf,
    interactionProperty='PropName',
    contactControls='StabilizationControl'
)

# Create stabilization control
model.ContactStabilization(
    name='StabilizationControl',
    zeroDistance=0.0,
    reductionFactor=0.1,
    stabilizationFactor=0.0001
)
```

2. **Use smaller time increments**
```python
model.StaticStep(
    name='Step-1',
    previous='Initial',
    initialInc=0.01,
    maxInc=0.05,
    minInc=1e-10,
    maxNumInc=1000
)
```

3. **Enable automatic stabilization**
```python
model.StaticStep(
    name='Step-1',
    previous='Initial',
    stabilizationMagnitude=0.0002,
    stabilizationMethod=DISSIPATED_ENERGY_FRACTION
)
```

## Initial Penetration/Overclosure

### Detect Overclosure
Run a datacheck to identify initial overclosure:
```bash
abaqus job=ModelName datacheck
```

### Fix Options

1. **Adjust slave nodes (default)**
```python
model.Tie(name='Tie', master=master, slave=slave, adjust=ON)
```

2. **Use shrink fit for interference**
```python
model.SurfaceToSurfaceContactStd(
    ...,
    interferenceType=SHRINK_FIT,
    interferenceDirectionType=COMPUTED
)
```

3. **Modify geometry to eliminate gap/overlap**

## Friction Coefficient Guidelines

| Material Pair | Static mu | Kinetic mu |
|---------------|-----------|------------|
| Steel on steel (dry) | 0.5-0.8 | 0.4-0.6 |
| Steel on steel (lubricated) | 0.1-0.2 | 0.05-0.15 |
| Aluminum on steel | 0.4-0.6 | 0.3-0.5 |
| Rubber on concrete | 0.6-0.9 | 0.5-0.8 |
| Plastic on metal | 0.3-0.4 | 0.2-0.3 |

## Tie Constraint Issues

### "Tie constraint has no matched nodes"
- Surfaces are too far apart
- Check `positionTolerance` value
- Ensure surfaces are correctly defined

### Fix
```python
model.Tie(
    name='Tie',
    master=master_surf,
    slave=slave_surf,
    positionTolerance=1.0,  # Increase tolerance
    positionToleranceMethod=SPECIFIED,
    adjust=ON
)
```

## Contact Pressure Singularities

### Sharp edges causing unrealistic stress
- Use finer mesh at contact edges
- Add small fillet/chamfer to geometry
- Check if results converge with mesh refinement

## Explicit vs Implicit Contact

| Feature | Implicit (Standard) | Explicit |
|---------|---------------------|----------|
| Best for | Static, slow dynamic | Fast dynamic, impact |
| Contact algorithm | Newton iteration | Penalty method |
| Convergence | Can fail | Always completes |
| Time increment | Automatic | CFL condition |
| Self-contact | Possible | Easy to set up |

## Debugging Contact

1. **Check contact status in ODB**
```python
# In post-processing
odb = openOdb('Job.odb')
step = odb.steps['Step-1']
frame = step.frames[-1]
contact_status = frame.fieldOutputs['CSTATUS']
```

2. **Request contact outputs**
```python
model.FieldOutputRequest(
    name='ContactOutputs',
    createStepName='Step-1',
    variables=('CSTRESS', 'CDISP', 'CSTATUS', 'CFORCE')
)
```
