# Mesh API Quick Reference

## Global Seeding

```python
part.seedPart(size=meshSize, deviationFactor=0.1, minSizeFactor=0.1)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| size | float | Target element size |
| deviationFactor | float | Allowed deviation from curved geometry (default 0.1) |
| minSizeFactor | float | Minimum element size as fraction of size (default 0.1) |

## Edge Seeding (Local Refinement)

### By Size
```python
part.seedEdgeBySize(edges=edgeSequence, size=localSize, constraint=FINER)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| edges | EdgeArray | Edges to seed |
| size | float | Target element size along edges |
| constraint | SymbolicConstant | FINER, FIXED, or FREE |

### By Number
```python
part.seedEdgeByNumber(edges=edgeSequence, number=numElements)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| edges | EdgeArray | Edges to seed |
| number | int | Number of elements along each edge |

### By Bias (Graded Mesh)
```python
part.seedEdgeByBias(
    biasMethod=SINGLE,
    end1Edges=edges,
    ratio=5.0,
    number=20
)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| biasMethod | SymbolicConstant | SINGLE or DOUBLE |
| end1Edges | EdgeArray | Edges (elements dense at end1) |
| end2Edges | EdgeArray | Edges (elements dense at end2) |
| ratio | float | Size ratio between ends |
| number | int | Number of elements |

## Mesh Controls

```python
part.setMeshControls(
    regions=part.cells,
    elemShape=HEX,
    technique=STRUCTURED
)
```

| Parameter | Type | Values |
|-----------|------|--------|
| regions | CellArray | Cells to control |
| elemShape | SymbolicConstant | HEX, HEX_DOMINATED, TET, WEDGE |
| technique | SymbolicConstant | FREE, STRUCTURED, SWEEP |
| algorithm | SymbolicConstant | MEDIAL_AXIS, ADVANCING_FRONT |

## Element Type Assignment

```python
from mesh import ElemType
from abaqusConstants import *

# Single element type
elemType = ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType,))

# Multiple fallback types (hex, wedge, tet)
elemType1 = ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
elemType2 = ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType1, elemType2, elemType3))

# With hourglass control
elemType = ElemType(
    elemCode=C3D8R,
    elemLibrary=STANDARD,
    hourglassControl=ENHANCED
)
```

## Generate Mesh

```python
part.generateMesh()
```

No parameters. Seeds and controls must be set first.

## Check Mesh

```python
# Node and element counts
len(part.nodes)     # Node count
len(part.elements)  # Element count

# Verify quality
part.verifyMeshQuality(criterion=ANALYSIS_CHECKS)
```

## Delete Mesh

```python
part.deleteMesh()
```

Removes mesh, preserving seeds and controls.

## Common Element Codes

### 3D Solids
| Code | Description |
|------|-------------|
| C3D8R | 8-node hex, reduced integration (default for solids) |
| C3D8 | 8-node hex, full integration |
| C3D20R | 20-node hex, reduced integration (high accuracy) |
| C3D4 | 4-node tet, linear (less accurate) |
| C3D10 | 10-node tet, quadratic (for complex geometry) |
| C3D6 | 6-node wedge (transition elements) |

### Shells
| Code | Description |
|------|-------------|
| S4R | 4-node shell, reduced integration (recommended) |
| S4 | 4-node shell, full integration |
| S3 | 3-node triangular shell |
| S8R | 8-node shell, reduced integration (high accuracy) |

### Beams
| Code | Description |
|------|-------------|
| B31 | 2-node beam (general purpose) |
| B32 | 3-node beam (curved) |

## Finding Edges for Local Refinement

```python
# By coordinates
edges = part.edges.findAt(((x1, y1, z1),), ((x2, y2, z2),))

# By bounding box
edges = part.edges.getByBoundingBox(xMin, yMin, zMin, xMax, yMax, zMax)

# Get all edges
edges = part.edges[:]
```

## Complete Example

```python
from abaqus import *
from abaqusConstants import *
import mesh

# Assume part already exists
part = mdb.models['Model-1'].parts['Part-1']

# Global seed
part.seedPart(size=5.0, deviationFactor=0.1, minSizeFactor=0.1)

# Local refinement on specific edges
refinement_edges = part.edges.findAt(((10, 0, 5),))
part.seedEdgeBySize(edges=refinement_edges, size=1.0, constraint=FINER)

# Set mesh controls for hex mesh
part.setMeshControls(regions=part.cells, elemShape=HEX, technique=STRUCTURED)

# Set element type
elemType = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType,))

# Generate and verify
part.generateMesh()

# Check counts
print(f"Nodes: {len(part.nodes)}, Elements: {len(part.elements)}")

# Verify quality
part.verifyMeshQuality(criterion=ANALYSIS_CHECKS)
```
