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

# Volume (identifier is a plain string in Abaqus 2025)
task.SingleTermDesignResponse(name='volume', region=MODEL, identifier='VOLUME')

# Strain energy (stiffness)
task.SingleTermDesignResponse(name='energy', region=MODEL, identifier='STRAIN_ENERGY')

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
# Abaqus 2025 requires a 5-element tuple:
# (suppress, designResponseName, weight, referenceValue, stepName)
task.ObjectiveFunction(
    name='Objective',
    objectives=((OFF, 'strain_energy', 1.0, 0.0, ''),),
    target=MINIMIZE
)

# target options: MINIMIZE, MAXIMIZE
# suppress: OFF (active) or ON (suppressed)
# stepName: '' for default, or specific step name
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
# 1. Create a prototype Job first (required as FEA template)
mdb.Job(name='ModelName', model='ModelName', numCpus=4, numDomains=4)

# 2. Create OptimizationProcess with prototypeJob (required in Abaqus 2025)
opt = mdb.OptimizationProcess(
    name='OptProcess',
    model='ModelName',
    task='TaskName',
    prototypeJob='ModelName',
    maxDesignCycle=50
)

# 3. Submit from within CAE (do NOT use 'abaqus optimization task=X' CLI)
opt.submit(validate=False)
opt.waitForCompletion()
```

### Abaqus 2025 Notes

- **`prototypeJob`** is required — it references a regular `mdb.Job` that serves as the FEA template
- **`task=` CLI flag** expects a Tosca `.par` parameter file, NOT a CAE task name — use `OptimizationProcess.submit()` from within CAE instead
- **ObjectiveFunction tuple** needs 5 elements: `(suppress, designResponse, weight, referenceValue, stepName)`
- **`identifier`** for `SingleTermDesignResponse` is a plain string (`'STRAIN_ENERGY'`, `'VOLUME'`), not a symbolic constant
