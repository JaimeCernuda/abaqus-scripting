# Common Shape Optimization Patterns

## Minimize Stress Concentration

```python
task.SingleTermDesignResponse(name='stress', region=MODEL,
                               identifier=MISES_STRESS)
task.ObjectiveFunction(name='Obj',
    objectives=((task.designResponses['stress'], MINIMIZE_MAXIMUM, 1.0, 0.0),))
task.ShapeDemoldControl(name='Limit', region=designSurf, distance=10.0)
```

## Optimize Fillet

```python
# 1. Define design region as fillet surface
fillet_faces = instance.faces.getByBoundingBox(
    xMin=corner_x-10, yMin=corner_y-10, zMin=0,
    xMax=corner_x+10, yMax=corner_y+10, zMax=thickness
)
assembly.Set(faces=fillet_faces, name='FilletSurfaces')

# 2. Objective: minimize max stress in fillet area
task.SingleTermDesignResponse(
    name='fillet_stress',
    region=assembly.sets['FilletSurfaces'],
    identifier=MISES_STRESS
)
task.ObjectiveFunction(name='MinFilletStress',
    objectives=((task.designResponses['fillet_stress'], MINIMIZE_MAXIMUM, 1.0, 0.0),))

# 3. Constraint: limit movement to maintain overall geometry
task.ShapeDemoldControl(name='FilletLimit', region=assembly.sets['FilletSurfaces'],
                         technique=MAXIMUM_MOVEMENT, distance=5.0)
```

## Maintain Volume

```python
task.SingleTermDesignResponse(name='vol', region=MODEL, identifier=VOLUME)
task.OptimizationConstraint(name='VolCon', designResponse='vol',
    restrictionMethod=RELATIVE_EQUAL, restrictionValue=1.0)
```

## Uniform Stress Distribution

```python
# Minimize stress variation for uniform stress
task.SingleTermDesignResponse(
    name='stress_var',
    region=MODEL,
    identifier=STRESS,
    stressComponent=MISES,
    operation=STANDARD_DEVIATION
)
task.ObjectiveFunction(name='UniformStress',
    objectives=((task.designResponses['stress_var'], MINIMIZE, 1.0, 0.0),))
```

## Maximize Stiffness with Shape

```python
# Minimize compliance = maximize stiffness
task.SingleTermDesignResponse(
    name='compliance',
    region=MODEL,
    identifier=STRAIN_ENERGY
)
task.ObjectiveFunction(name='MaxStiffness',
    objectives=((task.designResponses['compliance'], MINIMIZE, 1.0, 0.0),))
```

## Multi-Region Design

```python
# Different movement limits for different regions
task.designVariables = (
    ('FilletSurfaces', 5.0, -5.0),    # Fillets: +/-5mm
    ('NotchSurfaces', 3.0, -3.0),     # Notches: +/-3mm
    ('CornerSurfaces', 2.0, -2.0),    # Corners: +/-2mm
)
```

## Preserve Functional Surfaces

```python
# Keep mating surfaces fixed
mating_faces = instance.faces.findAt(((x1, y1, z1),), ((x2, y2, z2),))
assembly.Set(faces=mating_faces, name='MatingSurfaces')

task.GeometricRestriction(
    name='PreserveMating',
    surfaces=assembly.sets['MatingSurfaces'],
    movement=FIXED
)
```

## Symmetric Shape Change

```python
# Enforce symmetric shape changes about XZ plane
task.ShapeSymmetryConstraint(
    name='YSymmetry',
    region=MODEL,
    planePoint=(0, 0, 0),
    planeNormal=(0, 1, 0)
)
```

## Fatigue Life Optimization

```python
# Reduce peak stress to improve fatigue life
# Target stress below endurance limit
task.SingleTermDesignResponse(
    name='max_stress',
    region=MODEL,
    identifier=MAX_PRINCIPAL_STRESS
)

# Set target below fatigue endurance limit
task.ObjectiveFunction(name='FatigueLife',
    objectives=((task.designResponses['max_stress'], TARGET, 1.0, 150.0),))  # Target 150 MPa
```
