---
name: plato-export
description: Export Plato optimization results to STL, VTK, or CSV formats for 3D printing and CAD import
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
---

# Plato Export

Export optimized topology results from Plato to STL (3D printing), VTK (visualization), or CSV (data analysis).

## When to Use

- User asks to export STL, STEP, or 3D-printable geometry
- User wants to extract the optimized shape from density results
- User needs to convert Exodus results to other formats
- User mentions ParaView, VTK, or visualization

## When NOT to Use

- Reading raw results (use plato-results)
- Running the optimization (use plato-job)
- Generating meshes (use plato-mesh)

## What to Ask User

### Required
- **Source file**: Which Exodus result file (e.g., `platomain.exo` or `Iteration050.exo`)
- **Output format**: STL (default), VTK, CSV

### Optional (with defaults)
- **Density threshold**: Isosurface value for STL extraction (default: 0.5)
- **Smoothing**: Apply Laplacian smoothing to STL (default: yes, 20 iterations)

## Workflow

1. Verify the Exodus result file exists and contains a `Topology` or density field
2. Generate a Python extraction script using VTK or meshio
3. Submit the script via SLURM (never on login node)
4. Report output file location and mesh statistics (triangle count, volume)

## Key Decisions

| Scenario | Threshold | Smoothing |
|---|---|---|
| Visualization only | 0.3 | Light (10 iter) |
| 3D printing | 0.5 | Medium (20 iter) |
| Precise boundary | 0.5 | None |
| Conservative design | 0.4 | Medium (20 iter) |

## Extraction Methods

### Method 1: meshio + scipy (simplest, no ParaView needed)

```python
import meshio
import numpy as np

mesh = meshio.read("platomain.exo")

# Get density field from last time step
density = mesh.point_data.get("Topology", mesh.point_data.get("density"))
if density is not None and density.ndim > 1:
    density = density[-1]  # last time step

# Threshold: keep elements where average nodal density > 0.5
threshold = 0.5
cells_to_keep = []
for cell_block in mesh.cells:
    if cell_block.type == "tetra":
        avg_density = np.mean(density[cell_block.data], axis=1)
        mask = avg_density > threshold
        cells_to_keep.append(meshio.CellBlock("tetra", cell_block.data[mask]))

# Write filtered mesh
filtered = meshio.Mesh(points=mesh.points, cells=cells_to_keep)
meshio.write("optimized.vtu", filtered)
# Then use meshio or trimesh to extract surface and write STL
```

### Method 2: ParaView Python (pvpython)

```python
from paraview.simple import *

reader = ExodusIIReader(FileName="platomain.exo")
reader.UpdatePipeline()

# Contour at density = 0.5
contour = Contour(Input=reader)
contour.ContourBy = ['POINTS', 'Topology']
contour.Isosurfaces = [0.5]
contour.UpdatePipeline()

# Save STL
SaveData("optimized.stl", proxy=contour, FileType="Ascii")
```

### Method 3: Plato's built-in extract_iso

```bash
# extract_iso is installed with platoengine
extract_iso --input platomain.exo --output optimized.exo --field Topology --value 0.5
```

## SLURM Submission

**CRITICAL**: Never run extraction on login nodes. Use interactive or batch:

```bash
# Interactive (quick extraction)
srun --account=bekn-delta-cpu --partition=cpu-interactive \
  --time=00:10:00 --mem=8g --pty bash -c '
  source /projects/bekn/jcernuda/plato/spack/share/spack/setup-env.sh
  spack env activate /projects/bekn/jcernuda/plato
  python3 extract_stl.py
'
```

## Validation Checklist

- [ ] STL file is watertight (no holes)
- [ ] Triangle count is reasonable (1k-100k typical)
- [ ] Volume is approximately `volume_fraction × design_domain_volume`
- [ ] No floating disconnected regions
- [ ] Dimensions match original design domain

## Troubleshooting

| Issue | Cause | Fix |
|---|---|---|
| Empty STL | Threshold too high | Lower to 0.3-0.4 |
| Noisy surface | No smoothing | Add Laplacian smoothing |
| Missing field | Wrong field name | Check with `ncdump -h file.exo` or exodus.py |
| Very large STL | Too fine mesh | Decimate mesh (reduce triangles) |
