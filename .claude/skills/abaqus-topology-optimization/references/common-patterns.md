# Common Topology Optimization Patterns

## Maximize Stiffness at 30% Volume (Most Common)

```python
# Abaqus 2025: identifier is a string, ObjectiveFunction uses 5-tuple
task.SingleTermDesignResponse(name='vol', region=MODEL, identifier='VOLUME')
task.SingleTermDesignResponse(name='SE', region=MODEL, identifier='STRAIN_ENERGY')
task.ObjectiveFunction(name='Obj',
    objectives=((OFF, 'SE', 1.0, 0.0, ''),),
    target=MINIMIZE)
task.OptimizationConstraint(name='VolCon', designResponse='vol',
    restrictionMethod=RELATIVE_LESS_THAN_EQUAL, restrictionValue=0.3)
```

## With Minimum Member Size

```python
task.GeometricRestriction(
    name='MinMember',
    technique=MEMBER_SIZE,
    region=MODEL,
    minSize=5.0
)
```

## Freeze Specific Regions

```python
task.FrozenArea(name='KeepSolid', region=assembly.sets['MountingHoles'])
```

## With Draw Direction (Casting)

```python
task.GeometricRestriction(
    name='DrawDir',
    technique=DEMOLD_CONTROL,
    region=MODEL,
    pullDirection=((0, 0, 0), (0, 0, 1))  # Z-direction pull
)
```

## Symmetry Constraint

```python
task.GeometricRestriction(
    name='Symmetry',
    technique=PLANAR_SYMMETRY,
    masterRegion=MODEL,
    axis=AXIS_1  # X-axis symmetry
)
```

## Multi-Load Case

```python
# Create multiple static steps, each with different load
model.StaticStep(name='LoadCase1', previous='Initial')
model.StaticStep(name='LoadCase2', previous='LoadCase1')

# Apply different loads in each step
model.ConcentratedForce(name='Force1', createStepName='LoadCase1', ...)
model.ConcentratedForce(name='Force2', createStepName='LoadCase2', ...)

# Optimization considers all load cases automatically
task.SingleTermDesignResponse(name='SE', region=MODEL,
                              identifier=STRAIN_ENERGY,
                              stepOptions=ALL_STEPS)
```

## Weight Minimization with Stress Constraint

```python
task.SingleTermDesignResponse(name='vol', region=MODEL, identifier=VOLUME)
task.SingleTermDesignResponse(name='stress', region=MODEL,
                              identifier=STRESS_MEASURE,
                              measure=VON_MISES)

task.ObjectiveFunction(name='MinWeight',
    objectives=((task.designResponses['vol'], MINIMIZE_MAXIMUM, 1.0, 0.0),))

task.OptimizationConstraint(name='StressCon', designResponse='stress',
    restrictionMethod=ABSOLUTE_LESS_THAN_EQUAL,
    restrictionValue=250.0)  # Max 250 MPa
```

## SIMP Parameters

```python
model.TopologyTask(
    name='TopoTask',
    region=MODEL,
    materialInterpolationTechnique=SIMP,
    materialInterpolationPenalty=3.0,  # Standard: 3.0, increase for sharper 0/1
    densityMoveLimit=0.25,             # Default 0.25, reduce for stability
    objectiveFunctionDeltaStopCriteria=0.001
)
```

## Complete Workflow: Setup + Submit from CAE Script

```python
# 1. Define task, design responses, objective, constraints (see patterns above)
# ...

# 2. Save the model
mdb.saveAs(pathName='MyModel.cae')

# 3. Create prototype job (required by OptimizationProcess)
mdb.Job(name='MyModel', model='MyModel', numCpus=4, numDomains=4)

# 4. Create and submit optimization process
opt_process = mdb.OptimizationProcess(
    name='MyOptimization',
    model='MyModel',
    task='TopoTask',
    prototypeJob='MyModel',
    maxDesignCycle=50)
opt_process.submit(validate=False)
opt_process.waitForCompletion()
```

**WARNING:** Do NOT use `abaqus optimization task=X` directly from the CLI.
The `task=` flag expects a Tosca `.par` parameter file, not a CAE task name.
Always use `OptimizationProcess.submit()` from within a CAE script instead.
