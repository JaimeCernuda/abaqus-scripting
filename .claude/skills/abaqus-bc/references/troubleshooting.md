# BC Troubleshooting

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| "Zero pivot" | Rigid body motion | Add more BCs or fix additional DOFs |
| "Numerical singularity" | Unconstrained DOF | Check all 6 rigid body modes are prevented |
| "Boundary condition conflicts" | Overlapping BCs | Remove duplicate constraints on same DOF |
| "Region not found" | Set doesn't exist | Create set before applying BC |
| "BC in wrong step" | Applied after Initial | Move fixed supports to Initial step |
| "Face not found at coordinates" | Point not on face | Verify coordinates or use bounding box |
| "Over-constraint warning" | Multiple BCs on same DOF | Review and consolidate BCs |
| "BC has no effect" | Applied to wrong region | Verify set contains expected entities |
| "Negative eigenvalue" | Buckling or instability | Check for proper support, may need stabilization |

## Rigid Body Modes

A 3D solid needs 6 DOFs constrained minimum to prevent:
- 3 translations (u1, u2, u3)
- 3 rotations (prevented by constraining multiple non-collinear points)

### Quick Check
| Configuration | Stability | Notes |
|---------------|-----------|-------|
| One face Encastre | Fully stable | Most common approach |
| One vertex fixed | Unstable | Still allows rotation |
| Three non-collinear points pinned | Stable | Minimal constraint |
| Line of vertices fixed | Unstable | Allows rotation about line |

## Symmetry Plane Orientation

| BC Type | Symmetry Plane | Normal Direction | Constrains |
|---------|---------------|------------------|------------|
| XsymmBC | YZ plane | X-axis | u1, ur2, ur3 |
| YsymmBC | XZ plane | Y-axis | u2, ur1, ur3 |
| ZsymmBC | XY plane | Z-axis | u3, ur1, ur2 |

**Remember:** The symmetry BC name indicates the **normal direction**, not the plane itself.

## Finding the Right Region

### Coordinate Method Issues
```python
# WRONG: Point not exactly on face
face = instance.faces.findAt(((0, 50, 25),))  # May fail if tolerance issue

# BETTER: Use bounding box for approximate location
faces = instance.faces.getByBoundingBox(
    xMin=-0.01, yMin=0, zMin=0,
    xMax=0.01, yMax=100, zMax=50
)
```

### Debugging Region Selection
```python
# Check what was selected
print("Number of faces:", len(face))
for f in face:
    print("Face index:", f.index)
```

## Step-Related Issues

### BC Not Propagating
BCs defined in Initial step automatically propagate to later steps. If BC disappears:
```python
# Explicitly set in later step
model.boundaryConditions['MyBC'].setValuesInStep(
    stepName='LoadStep',
    u1=0.0  # Maintain constraint
)
```

### Cannot Modify BC
If you cannot change a BC value in a later step, ensure:
1. BC was created with DisplacementBC (not EncastreBC)
2. The DOF was not set to UNSET in the initial definition

## Performance Tips

| Issue | Solution |
|-------|----------|
| Too many BCs slow solve | Combine into larger sets |
| Stress concentration at BC | Use larger fixed region |
| Unrealistic stress at fixed point | Consider spring/distributed support |
| Displacement control oscillating | Use smaller time increments |

## Verification Checklist

Before running analysis:
- [ ] At least one fixed support exists
- [ ] All 6 rigid body modes are constrained
- [ ] Fixed BCs applied in Initial step
- [ ] Prescribed displacements in Load step
- [ ] Symmetry planes match geometry/loading symmetry
- [ ] No conflicting BCs on same DOF
- [ ] Region sets created before BC references them
