---
name: abaqus-mesh
description: Generate finite element meshes for Abaqus analysis. Use when part geometry is complete and needs discretization. Helps choose between hex (C3D8R), tet (C3D10), or shell (S4R) elements based on geometry complexity and accuracy needs. Handles seed sizing, mesh controls, and quality verification. Does not modify part geometry.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
---

# Abaqus Mesh Skill

## When to Use This Skill

**USE when you need to:**
- Discretize completed geometry into finite elements
- Choose appropriate element types for your analysis
- Control mesh density (global or local refinement)
- Verify mesh quality before analysis
- Estimate node count for Learning Edition limits

**Do NOT use for:**
- Modifying part geometry (add features, fillets) → use `/abaqus-geometry`
- Creating partitions for load/BC application → use `/abaqus-geometry`
- Mesh-based results extraction → use `/abaqus-odb`

**Prerequisites:** Geometry must be complete. Sections should be assigned before meshing (material assignment).

## Key Decisions

### 1. Element Type Selection

| Geometry | Element | Code | Best For |
|----------|---------|------|----------|
| Simple box/prism | Hex, reduced integration | C3D8R | General purpose, fast |
| Complex freeform | Tet, quadratic | C3D10 | Meshes anything, accurate |
| Thin-walled (t/L < 0.1) | Shell | S4R | Efficient for plates/shells |
| Slender beams (L/d > 10) | Beam | B31 | Frames, trusses |

**Decision guidance:**
- **Can it be hex-meshed?** Try C3D8R first - best accuracy-to-cost ratio
- **Complex shape?** Use C3D10 (tet) - meshes any geometry
- **Thin structure?** Use S4R shell - captures bending without through-thickness elements
- **Explicit dynamics?** C3D8R works well; avoid C3D20R (expensive)

### 2. Mesh Size Selection

| Use Case | Element Size | Guideline |
|----------|--------------|-----------|
| Quick feasibility | 10-20mm | 5+ elements across model |
| General analysis | 3-5mm | 10+ elements across smallest dimension |
| Stress concentrations | 1-2mm | 5+ elements in high-gradient regions |
| Topology optimization | 2-5mm | 3-5 elements across expected members |

**Rule of thumb:** At least 3 elements across any feature you care about.

### 3. Learning Edition Limits (1000 nodes max)

| Box Dimensions (mm) | Max Element Size |
|--------------------|------------------|
| 100 × 100 × 100 | 20mm |
| 100 × 50 × 30 | 10mm |
| 50 × 50 × 50 | 12mm |
| 200 × 100 × 50 | 25mm |

**Estimation formula:** `nodes ≈ (L/size + 1) × (W/size + 1) × (H/size + 1)`

## Required Inputs

| Input | Required | Default | Guidance |
|-------|----------|---------|----------|
| Element size | YES | Auto | Start coarse, refine as needed |
| Element type | NO | C3D8R | Change for complex geometry or specific needs |
| Mesh technique | NO | Free | Structured for simple shapes, Free for complex |

## Common Patterns

### Basic Meshing
```python
# 1. Seed the part (controls element size)
part.seedPart(size=5.0, deviationFactor=0.1, minSizeFactor=0.1)

# 2. Set element type
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)  # Wedge fallback
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)  # Tet fallback
part.setElementType(regions=(part.cells,), elemTypes=(elemType1, elemType2, elemType3))

# 3. Generate mesh
part.generateMesh()

# 4. Check counts (IMPORTANT for Learning Edition)
print(f"Nodes: {len(part.nodes)}, Elements: {len(part.elements)}")
```

### Tetrahedral Mesh (Complex Geometry)
```python
# Use when hex meshing fails or geometry is complex
part.setMeshControls(
    regions=part.cells,
    elemShape=TET,
    technique=FREE
)

# C3D10 is more accurate than C3D4 for tets
elemType = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType,))

part.seedPart(size=5.0)
part.generateMesh()
```

### Local Refinement
```python
# Refine specific edges (e.g., around stress concentration)
edges = part.edges.findAt(((x, y, z),))
part.seedEdgeBySize(edges=edges, size=1.0, constraint=FINER)

# Or specify number of elements along edge
part.seedEdgeByNumber(edges=edges, number=10)

# Graded mesh (bias) - dense at one end, coarse at other
part.seedEdgeByBias(
    biasMethod=SINGLE,
    end1Edges=edges,
    ratio=5.0,  # Size ratio from end1 to end2
    number=20
)
```

### Structured Mesh (Simple Shapes)
```python
# For regular shapes that can be structured-meshed
part.setMeshControls(
    regions=part.cells,
    elemShape=HEX,
    technique=STRUCTURED
)
part.seedPart(size=5.0)
part.generateMesh()
```

### Verify Mesh Quality
```python
# Check for warnings
part.verifyMeshQuality(criterion=ANALYSIS_CHECKS)

# Get element/node counts
n_nodes = len(part.nodes)
n_elements = len(part.elements)

# For Learning Edition: abort if over limit
if n_nodes > 1000:
    raise ValueError(f"Node count {n_nodes} exceeds Learning Edition limit. Increase mesh size.")
```

### Delete and Regenerate
```python
part.deleteMesh()
part.seedPart(size=NEW_SIZE)
part.generateMesh()
```

## Mesh Quality Guidelines

| Metric | Target | Warning | Failure |
|--------|--------|---------|---------|
| Aspect ratio | < 5:1 | 5-10:1 | > 10:1 |
| Jacobian | > 0.5 | 0.1-0.5 | < 0.1 |
| Min angle (quad) | > 45° | 30-45° | < 30° |

**If quality is poor:** Refine locally, improve geometry, or use higher-order elements.

## Element Type Reference

### 3D Solid Elements
| Code | Type | Nodes | Use Case |
|------|------|-------|----------|
| C3D8R | Hex, reduced integration | 8 | General purpose (recommended) |
| C3D8 | Hex, full integration | 8 | Bending-dominated, no hourglass |
| C3D20R | Hex, quadratic reduced | 20 | High accuracy, stress concentration |
| C3D4 | Tet, linear | 4 | Complex geometry (less accurate) |
| C3D10 | Tet, quadratic | 10 | Complex geometry (better accuracy) |

### Shell Elements
| Code | Type | Nodes | Use Case |
|------|------|-------|----------|
| S4R | Quad, reduced | 4 | General purpose (recommended) |
| S4 | Quad, full | 4 | No hourglass |
| S3 | Triangle | 3 | Complex surfaces |

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Cannot mesh region" | Geometry too complex for hex mesh | Switch to TET with FREE technique |
| "Element distortion warning" | Poor element shapes | Refine locally or improve geometry |
| "Exceeded node limit" | Mesh too fine for Learning Edition | Increase element size |
| "No mesh controls assigned" | Cells don't have mesh technique set | Call `setMeshControls()` before generating |
| "Mesh connectivity error" | Gaps between instances | Use tied constraint or merge instances |

## API Reference

For detailed parameters: [Mesh API](../../docs/abaqus-api/modules/mesh.md)
