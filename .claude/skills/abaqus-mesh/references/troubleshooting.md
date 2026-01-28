# Mesh Troubleshooting

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| "Too many nodes" | Exceeds Learning Edition limit (1000) | Increase mesh size |
| "Unable to mesh" | Complex geometry | Try tet elements (C3D10) |
| "Badly distorted elements" | Poor geometry or sizing | Add partitions, adjust seeds |
| "Mesh verification failed" | Elements too distorted | Refine mesh, check geometry |
| "Cannot mesh region" | Geometry too complex for hex | Switch to TET with FREE technique |
| "No mesh controls assigned" | Missing setMeshControls call | Call setMeshControls() before generating |
| "Mesh connectivity error" | Gaps between instances | Use tied constraint or merge |
| "Invalid topology" | Geometry has issues | Check for small edges, sliver faces |

## Learning Edition Limits

**Maximum: 1000 nodes**

If exceeded, you must increase MESH_SIZE parameter.

### Quick Estimation

```
nodes ~ (L/size + 1) x (W/size + 1) x (H/size + 1)
```

### Size Guidelines by Model Dimensions

| Model Size (mm) | Recommended Min Mesh Size |
|-----------------|---------------------------|
| 100 x 100 x 100 | 20mm |
| 100 x 50 x 30 | 10mm |
| 50 x 50 x 50 | 12mm |
| 200 x 100 x 50 | 25mm |

**Rule of thumb:** `MESH_SIZE = max_dimension / 5`

### Checking Node Count

```python
part.generateMesh()
n_nodes = len(part.nodes)

if n_nodes > 1000:
    part.deleteMesh()
    new_size = current_size * 1.5  # Increase by 50%
    part.seedPart(size=new_size)
    part.generateMesh()
    print(f"Adjusted mesh: {len(part.nodes)} nodes")
```

## Hex Mesh Failures

### Symptoms
- "Cannot mesh region with hex elements"
- "No valid mesh algorithm for this shape"

### Solutions

1. **Switch to tet mesh:**
```python
part.setMeshControls(regions=part.cells, elemShape=TET, technique=FREE)
elemType = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType,))
```

2. **Use hex-dominated mesh:**
```python
part.setMeshControls(regions=part.cells, elemShape=HEX_DOMINATED, technique=FREE)
```

3. **Add partitions for sweep meshing:**
   - Use `/abaqus-geometry` to add partitions
   - Then use SWEEP technique

## Element Distortion

### Symptoms
- "Element Jacobian ratio exceeds threshold"
- "Badly shaped elements"
- Warning icons on mesh

### Solutions

1. **Refine locally:**
```python
problem_edges = part.edges.findAt(((x, y, z),))
part.seedEdgeBySize(edges=problem_edges, size=1.0)
part.generateMesh()
```

2. **Improve geometry:**
   - Add fillets to sharp corners
   - Remove small features
   - Use `/abaqus-geometry` skill

3. **Use quadratic elements:**
```python
# C3D10 instead of C3D4, C3D20R instead of C3D8R
elemType = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
```

## Hourglass Mode Warnings

### Symptoms
- "Hourglass mode detected"
- Spurious deformation patterns
- Results show checkerboard stress

### Solutions

1. **Enable enhanced hourglass control:**
```python
elemType = mesh.ElemType(
    elemCode=C3D8R,
    elemLibrary=STANDARD,
    hourglassControl=ENHANCED
)
```

2. **Switch to full integration:**
```python
# Use C3D8 instead of C3D8R
elemType = mesh.ElemType(elemCode=C3D8, elemLibrary=STANDARD)
```

3. **Refine mesh:** More elements reduce hourglass tendency

## Mesh Connectivity Issues

### Symptoms
- "Mesh connectivity error"
- "Nodes not connected"
- Analysis fails at assembly

### Solutions

1. **For multi-part assemblies, use tie constraints:**
```python
model.Tie(
    name='Tie-1',
    main=region1,
    secondary=region2,
    positionToleranceMethod=COMPUTED,
    adjust=ON
)
```

2. **Merge instances (if appropriate):**
```python
assembly.InstanceFromBooleanMerge(
    name='Merged',
    instances=(instance1, instance2),
    keepIntersections=ON
)
```

## Quality Check Failed

### Running Quality Verification

```python
# Check mesh quality
result = part.verifyMeshQuality(criterion=ANALYSIS_CHECKS)

# View failed elements (if any)
# Result contains element labels that failed
```

### Quality Metrics

| Metric | Target | Warning | Action |
|--------|--------|---------|--------|
| Aspect ratio | < 5:1 | 5-10:1 | Refine long edges |
| Jacobian | > 0.5 | 0.1-0.5 | Fix geometry |
| Min angle | > 45 deg | 30-45 deg | Add seeds |
| Max angle | < 135 deg | 135-160 deg | Add partitions |

## Mesh Won't Generate

### Checklist

1. **Is geometry valid?**
   - No zero-thickness regions
   - No overlapping faces
   - Closed solid (for 3D)

2. **Are seeds assigned?**
   ```python
   part.seedPart(size=5.0)  # Must be called
   ```

3. **Are controls compatible with geometry?**
   - STRUCTURED requires simple topology
   - Complex shapes need FREE + TET

4. **Is element type set?**
   ```python
   part.setElementType(regions=(part.cells,), elemTypes=(elemType,))
   ```

## Performance Issues

### Mesh Takes Too Long

- Reduce complexity: Use larger mesh size initially
- Use FREE instead of MEDIAL_AXIS algorithm
- For very complex parts, mesh in sections

### Analysis Is Slow

- Check node count is appropriate
- Consider reduced integration (C3D8R vs C3D8)
- Use shell elements for thin structures
- Use beam elements for slender members
