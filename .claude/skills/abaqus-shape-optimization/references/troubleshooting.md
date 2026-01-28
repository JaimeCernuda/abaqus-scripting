# Shape Optimization Troubleshooting

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| "Mesh distortion" | Too large movement | Reduce distance limit |
| "Not converging" | Conflicting constraints | Relax constraints |
| "Invalid mesh" | Extreme shape change | Use smaller increments |
| "Tosca license" | Learning Edition | Requires full license |
| "No design response" | Missing identifier | Check response setup |
| "Negative jacobian" | Element inversion | Reduce movement limits |

## Shape vs Topology Comparison

| Shape Opt | Topology Opt |
|-----------|--------------|
| Moves existing surfaces | Adds/removes material |
| Good for fillets, notches | Good for load paths |
| Preserves topology | Changes topology |
| Smaller changes | Larger redesign |
| Traditional manufacturing | May need AM/casting |
| Refine existing design | Conceptual design |

## Best Practices

1. **Start with working static analysis**
   - Verify stress results before optimization
   - Confirm load paths and boundary conditions

2. **Define clear design surface**
   - Only include surfaces that can change
   - Exclude functional interfaces
   - Exclude features like holes and threads

3. **Set reasonable movement limits**
   - Start with 5-10mm maximum
   - Increase only if no improvement
   - Consider manufacturing constraints

4. **Use MEDIUM mesh quality**
   - LOW may cause mesh issues
   - HIGH is slow with minimal benefit

5. **Run 20-30 design cycles**
   - Check convergence history
   - Stop early if converged

## Mesh Distortion Issues

### Symptoms
- Error: "Negative jacobian detected"
- Error: "Distorted elements"
- Optimization terminates early

### Solutions

```python
# 1. Reduce movement limits
task.designVariables = (
    ('DesignSurfaces', 2.0, -2.0),  # Reduced from 5.0
)

# 2. Use mesh smoothing
task.GeometricRestriction(
    name='MeshQuality',
    meshQualityTechnique=LAPLACIAN_SMOOTHING
)

# 3. Refine initial mesh in design region
part.seedEdgeBySize(edges=corner_edges, size=1.0)  # Finer mesh
```

## Convergence Problems

### Symptoms
- Objective oscillates
- No steady improvement
- "Failed to converge" error

### Solutions

1. **Relax constraints**
```python
# Allow more volume change
task.OptimizationConstraint(
    name='VolumeLimit',
    designResponse='volume',
    restrictionMethod=RELATIVE_LESS_THAN_EQUAL,
    restrictionValue=1.1  # Allow 10% increase
)
```

2. **Simplify objective**
   - Use single objective first
   - Add constraints gradually

3. **Check design region**
   - Ensure surfaces can actually move
   - Remove fixed surfaces from design region

## No Improvement

### Symptoms
- Stress unchanged after optimization
- Design variables not changing

### Causes and Solutions

| Cause | Solution |
|-------|----------|
| Wrong design surfaces | Select surfaces at stress concentration |
| Movement too small | Increase distance limits |
| Conflicting constraints | Remove or relax constraints |
| Stress not in design region | Expand design region |

## License Requirements

Shape optimization requires:
- Abaqus/CAE full license
- Tosca Structure module

**Not available in:**
- Abaqus Learning Edition
- Basic Abaqus/Standard license

### Check License

```bash
abaqus licensing lmstat -a
```

Look for:
- `tosca_structure` feature

## Debugging Workflow

1. **Verify static analysis**
```bash
abaqus job=BaseAnalysis interactive
abaqus cae database=BaseAnalysis.odb
```

2. **Check design region selection**
```python
# Highlight design surfaces
for face in inner_faces:
    print("Face area:", face.getSize())
```

3. **Monitor optimization progress**
```python
# Check convergence history
for cycle in range(opt.numDesignCycles):
    print("Cycle %d: Objective = %f" % (cycle, opt.objectiveHistory[cycle]))
```

4. **Compare before/after**
```bash
abaqus cae database=ShapeOptimization_CYCLE_1.odb   # Initial
abaqus cae database=ShapeOptimization_CYCLE_30.odb  # Final
```
