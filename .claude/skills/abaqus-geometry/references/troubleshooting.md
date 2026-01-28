# Geometry Troubleshooting

## Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "Sketch is invalid" | Self-intersecting lines | Check sketch geometry, remove overlaps |
| "Cannot extrude" | Open sketch profile | Close all sketch loops |
| "Part has no cells" | Failed feature operation | Check feature parameters, verify sketch |
| "Import failed" | Corrupted or unsupported CAD file | Repair in CAD software, try different format |
| "Cannot find face at coordinates" | Point not exactly on face | Use bounding box method or verify coords |
| "Instance already exists" | Duplicate instance name | Use unique name or delete existing |
| "Sketch is not closed" | Gap in sketch entities | Ensure all lines connect to form closed loop |
| "Cannot mesh this geometry" | Complex shape or thin features | Add partitions, use virtual topology |

## Sketch Tips

- Always close profiles for solid extrusion
- Use exact coordinates to avoid gaps
- Avoid overlapping lines
- Construction lines are for reference only (revolution axis)
- Sketch plane determines extrusion direction

## Coordinate Debugging

```python
# Print all face centroids to find correct coordinates
for i, face in enumerate(part.faces):
    centroid = face.pointOn[0]
    print(f"Face {i}: {centroid}")

# Or for instance faces
for i, face in enumerate(instance.faces):
    centroid = face.pointOn[0]
    print(f"Face {i}: {centroid}")
```

## Part vs Instance Coordinates

**Common mistake:** Using `part.faces.findAt()` after assembly creation.

```python
# WRONG - part coordinates may not match instance
face = part.faces.findAt(((50, 0, 25),))  # Fails after translate/rotate

# CORRECT - use instance coordinates
face = instance.faces.findAt(((50, 0, 25),))
```

## Bounding Box Alternative

When `findAt()` fails due to coordinate precision:

```python
# Instead of exact coordinates
face = instance.faces.findAt(((0, 0, 50),))  # May fail

# Use bounding box (more tolerant)
faces = instance.faces.getByBoundingBox(
    xMin=-0.1, yMin=-0.1, zMin=49.9,
    xMax=0.1, yMax=100.1, zMax=50.1
)
```

## STEP Import Issues

| Problem | Solution |
|---------|----------|
| Missing faces | Repair in CAD, check for gaps |
| Wrong scale | Use `scaleFromFile=OFF`, apply manual scale |
| Invalid geometry | Simplify in CAD, remove small features |
| Multiple parts | Import creates multiple Part objects |

```python
# Check imported parts
for name, part in model.parts.items():
    print(f"Part: {name}, Cells: {len(part.cells)}")
```

## Geometry Validation Checklist

Before proceeding to mesh:
- [ ] Part has cells (solid geometry created)
- [ ] No error messages during feature creation
- [ ] Instance created in assembly
- [ ] Coordinates verified for BC/load regions
- [ ] Sets created using instance (not part) coordinates
- [ ] Partitions added if needed for local mesh control

## Regeneration Issues

If geometry fails after parameter changes:

```python
# Delete and recreate feature
part.features['MyFeature'].setValuesInStep(...)

# Or regenerate entire part
part.regenerate()
```

## Memory and Performance

- Large CAD imports may be slow
- Simplify geometry when possible
- Remove unnecessary features before import
- Use `dependent=ON` for instances (shares mesh)
