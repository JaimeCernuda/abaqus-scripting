# Load Troubleshooting

## Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "Gravity has no effect" | Missing density | Add `material.Density(table=((7.85e-9,),))` |
| "Load region not found" | Typo in set/surface name | Check spelling matches exactly |
| "Zero reaction forces" | Load direction wrong | Check sign and direction vector |
| "Equilibrium not achieved" | Load too large | Reduce magnitude or use increments |
| "Negative eigenvalue" | Structure unstable | Check BCs allow reaction to load |
| "Cannot find face at location" | Wrong coordinates for findAt | Use face centroid, not vertex |

## Sign Conventions

### Pressure
- **Positive (+)**: Compression (pushes into surface)
- **Negative (-)**: Tension (pulls away from surface)

```python
# Compression: pushes inward
model.Pressure(name='Compress', ..., magnitude=10.0)

# Suction: pulls outward
model.Pressure(name='Suction', ..., magnitude=-10.0)
```

### ConcentratedForce
- **Positive cf1**: Force in +X direction
- **Positive cf2**: Force in +Y direction
- **Positive cf3**: Force in +Z direction

```python
# 1000N in -Y direction (downward if Y is up)
model.ConcentratedForce(..., cf1=0.0, cf2=-1000.0, cf3=0.0)
```

### Gravity
- Standard gravity in -Y direction: `comp2=-9810.0` (mm/s²)
- Standard gravity in -Z direction: `comp3=-9810.0` (mm/s²)

```python
# Gravity in -Y direction
model.Gravity(name='Gravity', ..., comp2=-9810.0)
```

## Debugging Checklist

### Load Not Applied
1. Verify step name matches an existing step
2. Verify region (Set/Surface) exists and has correct name
3. Check that the step comes after 'Initial'
4. For gravity: confirm density is defined

### Wrong Magnitude
1. Check unit consistency (N, MPa, mm)
2. For traction: did you convert force to force/area?
3. For amplitude: check scale factor at analysis time

### Wrong Direction
1. For SurfaceTraction: verify directionVector points correct way
2. For ConcentratedForce: check signs of cf1, cf2, cf3
3. For Pressure: positive = into surface

## Region Selection Tips

### Finding Faces with findAt
```python
# Use a point ON the face (typically face centroid)
face = instance.faces.findAt(((x, y, z),))

# For multiple faces
faces = instance.faces.findAt(
    ((x1, y1, z1),),
    ((x2, y2, z2),),
)
```

### Finding Vertices
```python
# Use exact vertex coordinates
vertex = instance.vertices.findAt(((x, y, z),))
```

### Finding Edges
```python
# Use a point ON the edge (typically edge midpoint)
edge = instance.edges.findAt(((x, y, z),))
```

## Performance Tips

1. **Large models**: Use element sets instead of geometric sets for loads
2. **Many load cases**: Create base load, modify with `setValuesInStep()`
3. **Convergence issues**: Apply loads gradually using amplitudes

## Verification

### Check Reactions Equal Applied Loads
After analysis, verify equilibrium:
```python
# In post-processing script
odb = session.openOdb('Job.odb')
step = odb.steps['LoadStep']
frame = step.frames[-1]
rf = frame.fieldOutputs['RF']

# Sum reaction forces
total_rf = sum([v.data for v in rf.values])
print('Total reaction:', total_rf)
# Should equal applied load (opposite sign)
```

### Visual Verification
```python
# In Abaqus CAE
session.viewports['Viewport: 1'].odbDisplay.displayBodyOptions.setValues(
    bodyLoadVectorDisplay=ON)
```
