# Abaqus Element Library

Quick reference for element selection.

## 3D Continuum (Solid) Elements

### Hexahedral (Brick)

| Code | Nodes | Integration | Best For |
|------|-------|-------------|----------|
| **C3D8R** | 8 | Reduced (1 pt) | **General purpose (recommended)** |
| C3D8 | 8 | Full (8 pts) | Avoid shear locking |
| C3D8I | 8 | Incompatible modes | Bending-dominated |
| C3D8H | 8 | Hybrid | Nearly incompressible |
| **C3D20R** | 20 | Reduced (8 pts) | **High accuracy, stress concentration** |
| C3D20 | 20 | Full (27 pts) | Very high accuracy |

### Tetrahedral

| Code | Nodes | Integration | Best For |
|------|-------|-------------|----------|
| C3D4 | 4 | Full (1 pt) | Complex geometry (less accurate) |
| C3D4H | 4 | Hybrid | Nearly incompressible |
| **C3D10** | 10 | Full (4 pts) | **Complex geometry (recommended)** |
| C3D10M | 10 | Modified | Contact problems |
| C3D10H | 10 | Hybrid | Nearly incompressible |

### Wedge (Triangular Prism)

| Code | Nodes | Best For |
|------|-------|----------|
| C3D6 | 6 | Transition elements |
| C3D15 | 15 | Higher accuracy transition |

## Shell Elements

### Conventional Shell

| Code | Nodes | Integration | Best For |
|------|-------|-------------|----------|
| **S4R** | 4 | Reduced | **General purpose (recommended)** |
| S4 | 4 | Full | Thick shells, bending |
| S4R5 | 4 | Reduced, 5 DOF | Thin shells |
| S3 | 3 | Full | Complex surfaces, transition |
| S3R | 3 | Reduced | Complex surfaces |
| **S8R** | 8 | Reduced | **High accuracy** |
| S8R5 | 8 | Reduced, 5 DOF | Thin shells |

### Continuum Shell

| Code | Nodes | Best For |
|------|-------|----------|
| SC8R | 8 | 3D shell behavior |
| SC6R | 6 | Transition |

## Beam Elements

| Code | Nodes | Best For |
|------|-------|----------|
| **B31** | 2 | **General purpose (recommended)** |
| B32 | 3 | Curved beams |
| B31OS | 2 | Open sections |
| B32OS | 3 | Curved open sections |
| PIPE31 | 2 | Pipe elements |

## Truss/Rod Elements

| Code | Nodes | Best For |
|------|-------|----------|
| T3D2 | 2 | 3D truss |
| T2D2 | 2 | 2D truss |

## 2D Continuum Elements

### Plane Stress

| Code | Nodes | Best For |
|------|-------|----------|
| CPS4R | 4 | General purpose |
| CPS8R | 8 | High accuracy |
| CPS3 | 3 | Complex geometry |
| CPS6 | 6 | Complex, high accuracy |

### Plane Strain

| Code | Nodes | Best For |
|------|-------|----------|
| CPE4R | 4 | General purpose |
| CPE8R | 8 | High accuracy |
| CPE3 | 3 | Complex geometry |
| CPE6 | 6 | Complex, high accuracy |

### Axisymmetric

| Code | Nodes | Best For |
|------|-------|----------|
| CAX4R | 4 | General purpose |
| CAX8R | 8 | High accuracy |
| CAX3 | 3 | Complex geometry |
| CAX6 | 6 | Complex, high accuracy |

## Explicit Dynamics Elements

Standard/Explicit elements are generally interchangeable:
- C3D8R works for both
- Explicit prefers reduced integration
- Explicit adds hourglass control automatically

## Special Elements

### Cohesive

| Code | Nodes | Best For |
|------|-------|----------|
| COH3D8 | 8 | 3D cohesive layer |
| COH3D6 | 6 | 3D cohesive transition |
| COH2D4 | 4 | 2D cohesive |

### Connector

| Code | Best For |
|------|----------|
| CONN3D2 | Point-to-point connection |
| CONN2D2 | 2D connection |

### Rigid

| Code | Nodes | Best For |
|------|-------|----------|
| R3D4 | 4 | Rigid surface |
| R3D3 | 3 | Rigid surface |

## Element Selection Guidelines

### By Problem Type

| Problem | Recommended |
|---------|-------------|
| General 3D | C3D8R |
| Stress concentration | C3D20R or C3D10 |
| Complex CAD geometry | C3D10 |
| Thin structures | S4R |
| Frames/trusses | B31 |
| Nearly incompressible | C3D8H |
| Large deformation | C3D8R with nlgeom=ON |
| Contact | C3D10M or C3D8R |
| Crash/impact | C3D8R (explicit) |

### By Mesh Quality

| Geometry | If Hex Possible | If Tet Required |
|----------|-----------------|-----------------|
| Simple | C3D8R | - |
| Moderate | C3D8R | C3D10 |
| Complex | C3D20R | C3D10 |
| Very complex | - | C3D10 |

## Integration Point Notes

### Reduced Integration Benefits
- Faster computation
- Less susceptible to shear locking
- May exhibit hourglassing (use hourglass control)

### Full Integration Benefits
- No hourglassing
- Better for bending-dominated problems
- More computationally expensive

### Hourglassing Control
```python
elemType = mesh.ElemType(
    elemCode=C3D8R,
    elemLibrary=STANDARD,
    hourglassControl=ENHANCED  # or STIFFNESS, VISCOUS
)
```
