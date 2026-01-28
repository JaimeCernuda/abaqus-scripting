---
name: abaqus-optimization
description: Configure topology and shape optimization in Abaqus using Tosca - design responses, objectives, constraints, and manufacturing restrictions.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
---

# Abaqus Optimization Skill

## When to Use This Skill

**USE when you need to:**
- Create a TopologyTask for material distribution optimization
- Define design responses (volume, strain energy, frequency, stress)
- Set optimization objectives (minimize compliance, maximize frequency)
- Add optimization constraints (volume fraction, displacement limit)
- Define frozen regions (where material must stay)
- Add manufacturing constraints (member size, symmetry, draw direction)

**Do NOT use for:**
- Complete TO workflow (use `/abaqus-topology-optimization` instead)
- Shape optimization workflow (use `/abaqus-shape-optimization`)
- Running the optimization (use `/abaqus-job` with OptimizationProcess)

**Note:** Requires full Abaqus license with Tosca module.

## Key Decisions

### 1. Objective Selection

| Goal | Response | Objective |
|------|----------|-----------|
| Maximum stiffness | strain_energy | MINIMIZE_MAXIMUM |
| Minimum weight | volume | MINIMIZE |
| Maximum frequency | eigenfrequency | MAXIMIZE_MINIMUM |
| Minimum stress | stress | MINIMIZE_MAXIMUM |

### 2. Common Constraint Combinations

| Scenario | Objective | Constraint |
|----------|-----------|------------|
| Stiffness with weight limit | Min compliance | Volume ≤ 30% |
| Weight with stiffness | Min volume | Compliance ≤ X |
| Weight with stress limit | Min volume | Stress ≤ σ_allow |

### 3. Manufacturing Constraints

| Constraint | Purpose | Value |
|------------|---------|-------|
| Min member size | Prevent thin features | 3-5mm |
| Max member size | Limit thick sections | 10-20mm |
| Draw direction | Enable mold extraction | Vector |
| Symmetry | Mirror geometry | Plane |

## Required Inputs

| Input | Required |
|-------|----------|
| Task type | YES (Topology or Shape) |
| Design region | YES (MODEL or specific set) |
| Objective | YES |
| Volume constraint | Typically YES |

## Common Patterns

### Create Topology Task
```python
model.TopologyTask(
    name='TopoTask',
    region=MODEL,
    materialInterpolationTechnique=SIMP,
    materialInterpolationPenalty=3.0,
    freezeBoundaryConditionRegions=ON,
    freezeLoadRegions=ON,
    objectiveFunctionDeltaStopCriteria=0.001
)
```

### Design Responses

```python
task = model.optimizationTasks['TopoTask']

# Volume response
task.SingleTermDesignResponse(
    name='volume',
    region=MODEL,
    identifier=VOLUME
)

# Strain energy (compliance)
task.SingleTermDesignResponse(
    name='strain_energy',
    region=MODEL,
    identifier=STRAIN_ENERGY,
    stepOptions=LAST_STEP
)

# Eigenfrequency
task.SingleTermDesignResponse(
    name='frequency',
    region=MODEL,
    identifier=EIGENFREQUENCY,
    modes=(1,)  # First mode
)

# Displacement
task.SingleTermDesignResponse(
    name='displacement',
    region=assembly.sets['MonitorPoint'],
    identifier=DISPLACEMENT,
    dof=2  # U2
)

# Maximum stress
task.SingleTermDesignResponse(
    name='max_stress',
    region=MODEL,
    identifier=STRESS,
    stressComponent=MISES,
    operation=MAXIMUM
)
```

### Objective Functions

```python
# Minimize compliance (maximize stiffness)
task.ObjectiveFunction(
    name='MinCompliance',
    objectives=((task.designResponses['strain_energy'], MINIMIZE_MAXIMUM, 1.0, 0.0),)
)

# Maximize frequency
task.ObjectiveFunction(
    name='MaxFreq',
    objectives=((task.designResponses['frequency'], MAXIMIZE_MINIMUM, 1.0, 0.0),)
)
```

### Constraints

```python
# Volume constraint (30% of original)
task.OptimizationConstraint(
    name='VolConstraint',
    designResponse='volume',
    restrictionMethod=RELATIVE_LESS_THAN_EQUAL,
    restrictionValue=0.30
)

# Displacement constraint
task.OptimizationConstraint(
    name='DispConstraint',
    designResponse='displacement',
    restrictionMethod=ABSOLUTE_LESS_THAN_EQUAL,
    restrictionValue=1.0  # Max 1mm
)

# Stress constraint
task.OptimizationConstraint(
    name='StressConstraint',
    designResponse='max_stress',
    restrictionMethod=ABSOLUTE_LESS_THAN_EQUAL,
    restrictionValue=200.0  # Max 200 MPa
)
```

### Frozen Regions
```python
task.FrozenArea(name='FreezeMounting', region=assembly.sets['MountingRegion'])
task.FrozenArea(name='FreezeLoad', region=assembly.sets['LoadRegion'])
```

### Manufacturing Constraints

```python
# Minimum member size
task.GeometricRestriction(
    name='MinSize',
    technique=MEMBER_SIZE,
    region=MODEL,
    minSize=3.0  # mm
)

# Symmetry
task.GeometricRestriction(
    name='SymY',
    symmetric=SYMMETRIC,
    axis=AXIS_2  # Y-axis
)

# Draw direction (casting)
task.GeometricRestriction(
    name='DrawDir',
    technique=STAMP,
    region=MODEL,
    stampDirection=((0, 0, 0), (0, 1, 0))  # Pull in +Y
)
```

### Create Optimization Process
```python
opt_process = mdb.OptimizationProcess(
    name='Optimization',
    model='MyModel',
    task='TopoTask',
    maxDesignCycle=50,
    dataSaveFrequency=OPT_DATASAVE_EVERY_CYCLE
)
```

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Checkerboard" | No filtering | Add min member size |
| "Disconnected regions" | Poor load path | Add frozen regions |
| "Not converging" | Infeasible | Relax volume fraction |
| "License error" | No Tosca | Requires full license |

## API Reference

For detailed parameters: [Optimization API](../../docs/abaqus-api/modules/optimization.md)
