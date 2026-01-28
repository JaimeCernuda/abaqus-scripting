# Optimization Troubleshooting

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| "License not available" | Requires Tosca module | Need full Abaqus license with Tosca |
| "Optimization not converging" | Constraint too strict | Relax volume or stress limit |
| "Checkerboard pattern" | No filtering/size constraint | Add minimum member size constraint |
| "Disconnected regions" | Poor load path | Add frozen regions, check BCs |
| "All elements frozen" | Over-constrained | Reduce frozen regions |
| "Infeasible design" | Conflicting constraints | Review constraint values |

## Learning Edition Limitation

**IMPORTANT:** Topology optimization requires the Tosca module, which is NOT available in the Abaqus Learning Edition.

If using Learning Edition:
- Use static analysis (`/abaqus-static-analysis`) instead
- Perform manual optimization by modifying geometry
- Consider commercial license for optimization features

## Checkerboard Pattern

Checkerboard patterns appear when elements alternate between full and empty densities in a grid pattern.

**Solution:**
```python
task.GeometricRestriction(
    name='MinSize',
    technique=MEMBER_SIZE,
    region=MODEL,
    minSize=3.0  # mm - adjust based on mesh size
)
```

Rule of thumb: minimum member size should be 2-3x the mesh element size.

## Disconnected Regions

Results show floating material with no connection to the structure.

**Solutions:**
1. Add frozen regions at mounting points:
```python
task.FrozenArea(name='Mount', region=assembly.sets['MountingHoles'])
```

2. Increase volume fraction to allow more load paths
3. Check that boundary conditions properly constrain the model

## Not Converging

Optimization cycles continue without improvement or oscillate.

**Solutions:**
1. Relax constraints:
```python
# Increase from 30% to 40%
task.optimizationConstraints['VolConstraint'].setValues(restrictionValue=0.4)
```

2. Increase max design cycles:
```python
opt.setValues(maxDesignCycle=100)
```

3. Adjust convergence tolerance:
```python
model.optimizationTasks['TopoTask'].setValues(
    objectiveFunctionDeltaStopCriteria=0.005  # Less strict
)
```

## Manufacturing Constraints Reference

### Minimum Member Size
Prevents thin features that are difficult to manufacture:
```python
task.GeometricRestriction(
    name='MinMember',
    technique=MEMBER_SIZE,
    region=MODEL,
    minSize=5.0  # mm
)
```

### Maximum Member Size
Limits thick sections to avoid thermal issues in casting:
```python
task.GeometricRestriction(
    name='MaxMember',
    technique=MEMBER_SIZE,
    region=MODEL,
    maxSize=15.0  # mm
)
```

### Draw Direction (Casting/Molding)
Ensures parts can be extracted from molds:
```python
task.GeometricRestriction(
    name='DrawDir',
    technique=STAMP,
    region=MODEL,
    stampDirection=((0, 0, 0), (0, 1, 0))  # Pull in +Y
)
```

### Symmetry
Enforces symmetric results:
```python
task.GeometricRestriction(
    name='SymPlane',
    symmetric=SYMMETRIC,
    axis=AXIS_2  # AXIS_1 (X), AXIS_2 (Y), AXIS_3 (Z)
)
```

## Best Practices

1. **Start with reasonable volume fraction**: Begin with 30-40% volume, adjust based on results
2. **Use SIMP with penalty 3.0**: Standard settings that work well for most problems
3. **Freeze BC and load regions**: Prevents unrealistic results near supports/loads
4. **Add minimum member size**: Eliminates checkerboard and ensures manufacturability
5. **Run 30-50 design cycles**: Usually sufficient for convergence
6. **Check mesh quality first**: Optimization cannot fix poor mesh quality
7. **Verify static analysis works**: Run a static step first before optimization

## Debugging Workflow

1. Run static analysis without optimization to verify model setup
2. Start with relaxed constraints (higher volume fraction)
3. Add manufacturing constraints one at a time
4. Check intermediate results after 10-20 cycles
5. Tighten constraints gradually once a good design emerges
