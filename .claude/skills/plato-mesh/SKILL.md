---
name: plato-mesh
description: Generate Exodus II meshes using Gmsh (open-source). Creates tet4 meshes with named sidesets/nodesets for Plato Analyze.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
---

# Plato Mesh — Gmsh to Exodus

Generate finite element meshes for Plato using Gmsh (open-source) and convert to Exodus II format.

## When to Use

- User needs a mesh for Plato analysis or optimization
- User describes a geometry (box, L-bracket, cylinder, STEP import)
- User mentions mesh, elements, nodes, mesh size, refine

## When NOT to Use

- Modifying an existing mesh → manual Exodus editing
- Abaqus meshes → use `abaqus-mesh`

## What to Ask User

### Required
1. **Geometry**: Shape type and dimensions
2. **Support regions**: Which faces are fixed (become sidesets)
3. **Load regions**: Which faces have loads (become sidesets)

### Optional (with defaults)
4. **Mesh size**: Default = max_dimension / 30
5. **Element type**: Default tet4 (only type Plato Analyze supports)
6. **Refinement zones**: Local mesh refinement near features

## Workflow

1. Generate Gmsh Python script based on user geometry
2. Submit script via SLURM (`srun` on cpu-interactive, NEVER on login node)
3. Convert .msh to .exo using meshio
4. Verify: check sideset/nodeset names, element count, quality

## CRITICAL: Never Run on Login Node

```bash
# Interactive mesh generation
srun --account=bekn-delta-cpu --partition=cpu-interactive \
  --time=00:15:00 --mem=4g --pty bash -c '
  cd /path/to/working/dir
  python3 generate_mesh.py
'
```

## Key Decisions

| Geometry | Gmsh Function | Notes |
|---|---|---|
| Box/brick | `occ.addBox()` | Simplest, good for cantilevers |
| L-bracket | `occ.cut()` (box minus box) | Boolean subtraction |
| Cylinder | `occ.addCylinder()` | For shafts, pressure vessels |
| STEP import | `occ.importShapes()` | Any CAD geometry |
| 2D extruded | `occ.extrude()` | Sketch + extrude |

| Mesh Size | Use Case |
|---|---|
| dim/20 | Coarse (fast, initial exploration) |
| dim/30 | Standard (default) |
| dim/50 | Fine (production quality) |
| dim/80+ | Very fine (stress-constrained TO) |

## Gmsh Python Pattern — Cantilever Box

```python
import gmsh
gmsh.initialize()
gmsh.model.add("cantilever")

# Geometry: 100 x 20 x 10 box
L, H, D = 100.0, 20.0, 10.0
box = gmsh.model.occ.addBox(0, 0, 0, L, H, D)
gmsh.model.occ.synchronize()

# Identify surfaces by center-of-mass
def find_surface(target_com, tol=1.0):
    for dim, tag in gmsh.model.getEntities(2):
        com = gmsh.model.occ.getCenterOfMass(dim, tag)
        if all(abs(a - b) < tol for a, b in zip(com, target_com)):
            return tag
    return None

# Fixed face at x=0, center = (0, H/2, D/2)
fixed_face = find_surface((0, H/2, D/2))
# Load face at x=L, center = (L, H/2, D/2)
load_face = find_surface((L, H/2, D/2))

# Create physical groups (become sidesets in Exodus)
gmsh.model.addPhysicalGroup(2, [fixed_face], name="fixed_support")
gmsh.model.addPhysicalGroup(2, [load_face], name="load_surface")
gmsh.model.addPhysicalGroup(3, [box], name="design_domain")

# Mesh settings
mesh_size = max(L, H, D) / 30.0
gmsh.option.setNumber("Mesh.MeshSizeMax", mesh_size)
gmsh.option.setNumber("Mesh.MeshSizeMin", mesh_size * 0.5)
gmsh.option.setNumber("Mesh.ElementOrder", 1)  # tet4
gmsh.option.setNumber("Mesh.Algorithm3D", 1)   # Delaunay

# Generate
gmsh.model.mesh.generate(3)
gmsh.write("mesh.msh")
gmsh.finalize()

# Convert to Exodus
import meshio
mesh = meshio.read("mesh.msh")
meshio.exodus.write("mesh.exo", mesh)
print(f"Mesh: {len(mesh.points)} nodes")
```

## Exodus Requirements

- **Sidesets** (physical groups dim=2): Named surfaces for BCs and loads
- **Element blocks** (physical groups dim=3): Named volume regions for material assignment
- **Element type**: tet4 only for Plato Analyze
- **Names must match**: Sideset names in .exo must match `location_name` in .i and `Sides` in XML

## Validation Checklist

- [ ] .exo file created successfully
- [ ] Named sidesets exist: `ncdump -h mesh.exo | grep side_set`
- [ ] Element block is named (not just numbered)
- [ ] Element type is tetra (tet4)
- [ ] Node count is reasonable for problem size
- [ ] No degenerate or inverted elements

## Troubleshooting

| Issue | Cause | Fix |
|---|---|---|
| meshio import error | meshio not installed | `pip install meshio[exodus]` |
| No sidesets in .exo | Physical groups not defined in Gmsh | Add `addPhysicalGroup(2, ...)` |
| Wrong element type | Element order > 1 | Set `Mesh.ElementOrder` to 1 |
| Mesh too coarse/fine | Bad mesh size | Adjust MeshSizeMax |
| Can't find surface | Wrong center-of-mass coordinates | Print all surfaces and COMs to debug |
| gmsh not found | Not installed | `pip install gmsh` |
