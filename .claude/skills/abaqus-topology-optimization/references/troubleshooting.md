# Topology Optimization Troubleshooting

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| "Tosca license not found" | Learning Edition | Requires full Abaqus license |
| "Checkerboard pattern" | No manufacturing constraint | Add minimum member size |
| "Disconnected regions" | Geometry issue | Add connectivity constraint |
| "Not converging" | Too strict constraint | Relax volume fraction |
| "Thin features" | No min member constraint | Add GeometricRestriction |
| "Takes forever" | Mesh too fine | Coarsen mesh, reduce iterations |
| "Cannot find parameter file" | CLI `task=` expects `.par` file | Use `OptimizationProcess.submit()` from CAE instead |
| "ObjectiveFunction expected 5 got 4" | Abaqus 2025 5-tuple format | Use `(OFF, 'response_name', weight, refValue, '')` |

### Cannot Find Parameter File

The `abaqus optimization task=TopoTask` CLI command expects a Tosca `.par` parameter file, **not** a CAE task name. If you set up your optimization in CAE (via `model.TopologyTask`), the `.par` file is never generated.

**Solution:** Create an `OptimizationProcess` in your CAE script and call `submit()`:
```python
mdb.Job(name='MyModel', model='MyModel', numCpus=4, numDomains=4)
opt = mdb.OptimizationProcess(
    name='MyOpt', model='MyModel', task='TopoTask',
    prototypeJob='MyModel', maxDesignCycle=50)
opt.submit(validate=False)
opt.waitForCompletion()
```

### ObjectiveFunction Tuple Error (Abaqus 2025)

In Abaqus 2025, `ObjectiveFunction.objectives` requires a **5-element tuple**: `(suppress, designResponseName, weight, referenceValue, stepName)`. Older 4-element tuples will fail.

**Solution:**
```python
task.ObjectiveFunction(name='Obj',
    objectives=((OFF, 'strain_energy', 1.0, 0.0, ''),),
    target=MINIMIZE)
```

## Learning Edition Limitation

Topology optimization requires the Tosca module, which is **NOT available** in the Learning Edition.

**Alternatives:**
- Use static analysis with manual design iteration
- Use academic license with full Tosca access
- Use third-party topology optimization tools

## Best Practices

1. **Start with 30-40% volume fraction** - Easier to converge than aggressive targets
2. **Use SIMP with penalty = 3.0** - Standard value, increase to 4-5 for sharper boundaries
3. **Always add minimum member size** - Set to 3-5x mesh size to avoid checkerboard
4. **Run 30-50 design cycles** - Most problems converge within this range
5. **Freeze BC and load regions** - Ensures structural integrity at connection points

## Convergence Issues

### Objective Not Decreasing

```python
# Reduce move limit for stability
model.TopologyTask(
    name='TopoTask',
    region=MODEL,
    densityMoveLimit=0.15,  # Default 0.25, reduce for stability
    ...
)
```

### Checkerboard Pattern

```python
# Add minimum member size (required)
task.GeometricRestriction(
    name='MinMember',
    technique=MEMBER_SIZE,
    region=MODEL,
    minSize=3.0 * MESH_SIZE  # 3-5x mesh size
)
```

### Disconnected Regions

1. Increase volume fraction
2. Add frozen regions along expected load path
3. Check that load path is physically connected

### Very Slow Convergence

- Coarsen mesh (larger element size)
- Reduce max iterations for initial exploration
- Check if constraints are too strict

## Mesh Guidelines for TO

| Element Size | Design Freedom | Compute Time | Use Case |
|--------------|----------------|--------------|----------|
| 1-2mm | Maximum | Very long | Final optimization |
| 2-4mm | High | Moderate | General use |
| 4-6mm | Medium | Fast | Initial exploration |

**Rule:** At least 3 elements across expected minimum member thickness.

## Post-Processing Issues

### Can't Export STL

1. Open post ODB: `abaqus cae database=.../TOSCA_POST/...odb`
2. Go to Optimization module
3. Extract > STL
4. Set density threshold (0.3-0.5 typical)

### Result Not Manufacturable

Add appropriate manufacturing constraints:
- **Casting:** Draw direction constraint
- **Additive manufacturing:** Overhang angle constraint
- **Machining:** Minimum feature size

## Debugging Commands

```python
# Check task definition
print(model.optimizationTasks['TopoTask'].members)

# List all design responses
for dr in task.designResponses.values():
    print(dr.name, dr.identifier)

# Check constraints
for oc in task.optimizationConstraints.values():
    print(oc.name, oc.designResponse, oc.restrictionValue)
```
