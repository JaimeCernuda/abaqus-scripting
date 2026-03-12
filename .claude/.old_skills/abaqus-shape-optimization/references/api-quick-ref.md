# Shape Optimization API Quick Reference

## ShapeTask

```python
model.ShapeTask(
    name='TaskName',
    region=designSurface,      # Surface nodes that can move
    targetMeshQuality=MEDIUM,  # LOW, MEDIUM, HIGH
    morphingRegion=DESIGN      # or MODEL
)
```

## Design Responses

```python
task.SingleTermDesignResponse(
    name='stress',
    region=MODEL,
    identifier=MAX_PRINCIPAL_STRESS  # or MISES_STRESS, STRAIN_ENERGY
)
```

### Common Identifiers

| Identifier | Description |
|------------|-------------|
| `MISES_STRESS` | Von Mises stress |
| `MAX_PRINCIPAL_STRESS` | Maximum principal stress |
| `MIN_PRINCIPAL_STRESS` | Minimum principal stress |
| `STRAIN_ENERGY` | Total strain energy |
| `VOLUME` | Part volume |
| `MASS` | Part mass |

## Objective Function

```python
task.ObjectiveFunction(
    name='MinStress',
    objectives=((task.designResponses['stress'], MINIMIZE_MAXIMUM, 1.0, 0.0),)
)
```

### Objective Types

| Type | Use Case |
|------|----------|
| `MINIMIZE_MAXIMUM` | Reduce peak stress |
| `MINIMIZE` | Reduce total value |
| `MAXIMIZE` | Increase value (e.g., stiffness) |
| `TARGET` | Match specific value |

## Shape Constraints

### Limit Maximum Surface Movement

```python
task.ShapeDemoldControl(
    name='MaxMove',
    region=surface,
    technique=MAXIMUM_MOVEMENT,
    distance=5.0  # mm
)
```

### Maintain Symmetry

```python
task.ShapeSymmetryConstraint(
    name='Symmetry',
    region=surface,
    planePoint=(0, 0, 0),
    planeNormal=(1, 0, 0)
)
```

### Fix Surfaces

```python
task.GeometricRestriction(
    name='FixedSurf',
    surfaces=fixed_surfaces,
    movement=FIXED
)
```

### Maintain Planar Surface

```python
task.GeometricRestriction(
    name='StayPlanar',
    surfaces=planar_surfaces,
    movement=PLANAR
)
```

## Design Variables

```python
# (region_name, max_growth, max_shrink)
task.designVariables = (
    ('DesignSurfaces', 5.0, -5.0),  # +/-5mm movement allowed
)
```

## Optimization Process

```python
opt = mdb.OptimizationProcess(
    name='ShapeOptProcess',
    model='ModelName',
    task='ShapeTask',
    maxDesignCycle=30,           # Number of iterations
    dataSaveFrequency=OPT_DATASAVE_EVERY_CYCLE
)

# Submit optimization
opt.submit()

# Wait for completion
opt.waitForCompletion()
```

## Volume Constraint

```python
# First create volume design response
task.SingleTermDesignResponse(
    name='volume',
    region=MODEL,
    identifier=VOLUME
)

# Then constrain it
task.OptimizationConstraint(
    name='VolumeLimit',
    designResponse='volume',
    restrictionMethod=RELATIVE_LESS_THAN_EQUAL,
    restrictionValue=1.0  # 100% of original volume
)
```
