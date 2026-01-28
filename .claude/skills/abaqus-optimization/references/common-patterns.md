# Common Optimization Patterns

## Maximize Stiffness at 30% Volume

The most common topology optimization setup: minimize strain energy (maximize stiffness) while using only 30% of the original volume.

```python
task = model.optimizationTasks['TopoTask']

# Define design responses
task.SingleTermDesignResponse(name='vol', region=MODEL, identifier=VOLUME)
task.SingleTermDesignResponse(name='energy', region=MODEL,
                               identifier=STRAIN_ENERGY, stepOptions=LAST_STEP)

# Objective: minimize strain energy (maximize stiffness)
task.ObjectiveFunction(name='MinEnergy',
    objectives=((task.designResponses['energy'], MINIMIZE_MAXIMUM, 1.0, 0.0),))

# Constraint: volume <= 30% of original
task.OptimizationConstraint(name='VolConstraint', designResponse='vol',
    restrictionMethod=RELATIVE_LESS_THAN_EQUAL, restrictionValue=0.3)
```

## Minimize Mass with Stress Constraint

Lightweight design: remove as much material as possible while keeping stress below allowable.

```python
task = model.optimizationTasks['TopoTask']

# Define design responses
task.SingleTermDesignResponse(name='mass', region=MODEL, identifier=MASS)
task.SingleTermDesignResponse(name='stress', region=MODEL,
                               identifier=STRESS, stressComponent=MISES, operation=MAXIMUM)

# Objective: minimize mass
task.ObjectiveFunction(name='MinMass',
    objectives=((task.designResponses['mass'], MINIMIZE, 1.0, 0.0),))

# Constraint: von Mises stress <= 250 MPa
task.OptimizationConstraint(name='StressLimit', designResponse='stress',
    restrictionMethod=ABSOLUTE_LESS_THAN_EQUAL, restrictionValue=250.0)
```

## Maximize First Natural Frequency

Vibration-critical design: maximize the first eigenfrequency to avoid resonance.

```python
task = model.optimizationTasks['TopoTask']

# Define design responses
task.SingleTermDesignResponse(name='vol', region=MODEL, identifier=VOLUME)
task.SingleTermDesignResponse(name='freq', region=MODEL,
                               identifier=EIGENFREQUENCY, modes=(1,))

# Objective: maximize first frequency
task.ObjectiveFunction(name='MaxFreq',
    objectives=((task.designResponses['freq'], MAXIMIZE_MINIMUM, 1.0, 0.0),))

# Constraint: volume <= 40%
task.OptimizationConstraint(name='VolConstraint', designResponse='vol',
    restrictionMethod=RELATIVE_LESS_THAN_EQUAL, restrictionValue=0.4)
```

## Minimize Compliance with Displacement Limit

Stiffness optimization with a hard displacement constraint at a critical point.

```python
task = model.optimizationTasks['TopoTask']

# Define design responses
task.SingleTermDesignResponse(name='vol', region=MODEL, identifier=VOLUME)
task.SingleTermDesignResponse(name='compliance', region=MODEL, identifier=COMPLIANCE)
task.SingleTermDesignResponse(name='disp', region=assembly.sets['CriticalPoint'],
                               identifier=DISPLACEMENT, dof=2)  # U2

# Objective: minimize compliance
task.ObjectiveFunction(name='MinComp',
    objectives=((task.designResponses['compliance'], MINIMIZE, 1.0, 0.0),))

# Constraints
task.OptimizationConstraint(name='VolConstraint', designResponse='vol',
    restrictionMethod=RELATIVE_LESS_THAN_EQUAL, restrictionValue=0.3)
task.OptimizationConstraint(name='DispConstraint', designResponse='disp',
    restrictionMethod=ABSOLUTE_LESS_THAN_EQUAL, restrictionValue=1.0)  # Max 1mm
```

## Design for Additive Manufacturing

Topology optimization with manufacturing constraints suitable for 3D printing.

```python
# Create task with frozen regions
model.TopologyTask(
    name='TopoTask',
    region=MODEL,
    materialInterpolationTechnique=SIMP,
    materialInterpolationPenalty=3.0,
    freezeBoundaryConditionRegions=ON,
    freezeLoadRegions=ON
)

task = model.optimizationTasks['TopoTask']

# Standard stiffness optimization
task.SingleTermDesignResponse(name='vol', region=MODEL, identifier=VOLUME)
task.SingleTermDesignResponse(name='energy', region=MODEL,
                               identifier=STRAIN_ENERGY, stepOptions=LAST_STEP)
task.ObjectiveFunction(name='MinEnergy',
    objectives=((task.designResponses['energy'], MINIMIZE_MAXIMUM, 1.0, 0.0),))
task.OptimizationConstraint(name='VolConstraint', designResponse='vol',
    restrictionMethod=RELATIVE_LESS_THAN_EQUAL, restrictionValue=0.3)

# Manufacturing constraints for printability
task.GeometricRestriction(
    name='MinMember',
    technique=MEMBER_SIZE,
    region=MODEL,
    minSize=2.0  # Min feature size 2mm
)

# Optional: overhang constraint for support-free printing
task.GeometricRestriction(
    name='Overhang',
    technique=OVERHANG,
    region=MODEL,
    overhangAngle=45.0,  # degrees from vertical
    pullDirection=((0, 0, 0), (0, 0, 1))  # Build direction +Z
)
```

## Run Optimization

After setting up the task, design responses, objective, and constraints:

```python
opt = mdb.OptimizationProcess(
    name='OptProcess',
    model='Model-1',
    task='TopoTask',
    maxDesignCycle=50,
    dataSaveFrequency=OPT_DATASAVE_EVERY_CYCLE
)
opt.submit()
opt.waitForCompletion()
```
