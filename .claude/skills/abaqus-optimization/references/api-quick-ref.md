# Optimization API Quick Reference

## TopologyTask

```python
model.TopologyTask(
    name='TaskName',
    region=MODEL,                           # or specific region
    materialInterpolationTechnique=SIMP,    # or RAMP
    materialInterpolationPenalty=3.0,       # Higher = sharper boundaries
    freezeBoundaryConditionRegions=ON,      # Preserve BC areas
    freezeLoadRegions=ON,                   # Preserve load areas
    objectiveFunctionDeltaStopCriteria=0.001  # Convergence tolerance
)
```

## Design Responses

```python
task = model.optimizationTasks['TaskName']

# Volume
task.SingleTermDesignResponse(name='volume', region=MODEL, identifier=VOLUME)

# Strain energy (stiffness)
task.SingleTermDesignResponse(name='energy', region=MODEL,
                               identifier=STRAIN_ENERGY, stepOptions=LAST_STEP)

# Compliance
task.SingleTermDesignResponse(name='compliance', region=MODEL, identifier=COMPLIANCE)

# Mass
task.SingleTermDesignResponse(name='mass', region=MODEL, identifier=MASS)

# Eigenfrequency (modes)
task.SingleTermDesignResponse(name='frequency', region=MODEL,
                               identifier=EIGENFREQUENCY, modes=(1,))

# Displacement at a point
task.SingleTermDesignResponse(name='disp', region=assembly.sets['Point'],
                               identifier=DISPLACEMENT, dof=2)

# Stress (von Mises)
task.SingleTermDesignResponse(name='stress', region=MODEL,
                               identifier=STRESS, stressComponent=MISES, operation=MAXIMUM)
```

## Objective Function

```python
task.ObjectiveFunction(
    name='Objective',
    objectives=((designResponse, targetType, weight, referenceValue),)
)

# targetType options:
# - MINIMIZE_MAXIMUM  (minimize the max value - good for compliance)
# - MAXIMIZE_MINIMUM  (maximize the min value - good for frequency)
# - MINIMIZE          (minimize the response)
# - MAXIMIZE          (maximize the response)
```

## Optimization Constraints

```python
task.OptimizationConstraint(
    name='Constraint',
    designResponse='volume',
    restrictionMethod=RELATIVE_LESS_THAN_EQUAL,  # Relative to original
    restrictionValue=0.3  # 30% of original
)

# restrictionMethod options:
# - RELATIVE_LESS_THAN_EQUAL    (fraction of original, e.g., 0.3 = 30%)
# - RELATIVE_EQUAL
# - ABSOLUTE_LESS_THAN_EQUAL    (absolute value, e.g., 250 MPa)
# - ABSOLUTE_EQUAL
```

## Frozen Regions

```python
# Keep material in specific regions
task.FrozenArea(name='Frozen', region=assembly.sets['KeepSolid'])

# Or freeze BC and load regions automatically via TopologyTask parameters
```

## Manufacturing Constraints

```python
# Minimum member size (prevents thin features)
task.GeometricRestriction(
    name='MinMember',
    technique=MEMBER_SIZE,
    region=MODEL,
    minSize=5.0  # mm
)

# Symmetry constraint
task.GeometricRestriction(
    name='SymY',
    symmetric=SYMMETRIC,
    axis=AXIS_2  # Y-axis symmetry
)

# Draw direction (for casting/molding)
task.GeometricRestriction(
    name='DrawDir',
    technique=STAMP,
    region=MODEL,
    stampDirection=((0, 0, 0), (0, 1, 0))  # Pull direction +Y
)
```

## Run Optimization Process

```python
opt = mdb.OptimizationProcess(
    name='OptProcess',
    model='ModelName',
    task='TaskName',
    maxDesignCycle=50,
    dataSaveFrequency=OPT_DATASAVE_EVERY_CYCLE
)
opt.submit()
opt.waitForCompletion()
```
