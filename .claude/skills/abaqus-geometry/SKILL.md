---
name: abaqus-geometry
description: Create and manipulate Abaqus geometry - parts, sketches, extrusions, revolutions, CAD import, and assembly operations. Use for any geometry creation task. Handles primitives (box, cylinder), parametric shapes (sketch + extrude), and CAD file import (STEP, IGES). Does not handle meshing or analysis setup.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
---

# Abaqus Geometry Skill

## When to Use This Skill

**USE when you need to:**
- Create primitive shapes (box, cylinder, sphere)
- Build parametric geometry (sketch + extrude/revolve)
- Import CAD files (STEP, IGES, Parasolid)
- Add features (holes, fillets, chamfers)
- Create partitions for BC/load application
- Set up assembly with instances
- Create sets and surfaces for analysis

**Do NOT use for:**
- Meshing the geometry → use `/abaqus-mesh`
- Defining materials/sections → use `/abaqus-material`
- Applying loads or BCs → use `/abaqus-load`, `/abaqus-bc`

## Key Decisions

### 1. How to Create Geometry?

| Method | Best For | Complexity |
|--------|----------|------------|
| Primitive (box, cylinder) | Simple shapes, quick setup | Low |
| Sketch + Extrude | Prismatic shapes with cross-section | Medium |
| Sketch + Revolve | Axisymmetric parts (pipes, discs) | Medium |
| CAD Import (STEP) | Complex/existing designs | High |

**Decision guidance:**
- **Simple box/bracket?** Use sketch + extrude
- **Round/axisymmetric?** Use sketch + revolve
- **Existing CAD model?** Import STEP file
- **Quick prototype?** Use primitives

### 2. Coordinate System and Origin

| Origin Location | When to Use |
|-----------------|-------------|
| Corner (0,0,0) | Asymmetric parts, easier coordinate math |
| Center (0,0,0) | Symmetric parts, rotation about center |
| Custom | Match existing assembly or constraints |

### 3. Part vs Instance Coordinates

| Coordinate System | Use |
|-------------------|-----|
| Part coordinates | Geometry creation, section assignment |
| Assembly/Instance coordinates | BCs, loads, sets, finding faces |

**Important:** After creating an instance, use `instance.faces.findAt()` not `part.faces.findAt()`.

## Required Inputs

| Input | Required | Guidance |
|-------|----------|----------|
| Shape type | YES | Primitive, sketch+extrude, or CAD import |
| Dimensions | YES | In mm (using mm-tonne-s-N-MPa system) |
| Part name | NO | Default: 'Part-1' |

## Common Patterns

### Box (Sketch + Extrude)
```python
from abaqus import *
from abaqusConstants import *
from caeModules import *

# Create model and part
model = mdb.Model(name='MyModel')
part = model.Part(name='Box', dimensionality=THREE_D, type=DEFORMABLE_BODY)

# Sketch rectangle in XY plane
sketch = model.ConstrainedSketch(name='BoxSketch', sheetSize=200.0)
sketch.rectangle(point1=(0.0, 0.0), point2=(LENGTH, HEIGHT))

# Extrude in Z direction
part.BaseSolidExtrude(sketch=sketch, depth=WIDTH)
```

### Cylinder
```python
part = model.Part(name='Cylinder', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='CylSketch', sheetSize=200.0)
sketch.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(RADIUS, 0.0))
part.BaseSolidExtrude(sketch=sketch, depth=HEIGHT)
```

### Revolved Solid (Pipe, Disc)
```python
part = model.Part(name='Pipe', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='RevSketch', sheetSize=200.0)

# Construction line = rotation axis (Y-axis here)
sketch.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))

# Cross-section (must be on one side of axis)
sketch.rectangle(point1=(INNER_RADIUS, 0.0), point2=(OUTER_RADIUS, HEIGHT))

# Revolve 360° around axis
part.BaseSolidRevolve(sketch=sketch, angle=360.0, flipRevolveDirection=OFF)
```

### Import STEP File
```python
step_file = mdb.openStep('path/to/file.step', scaleFromFile=OFF)
part = model.PartFromGeometryFile(
    name='Imported',
    geometryFile=step_file,
    dimensionality=THREE_D,
    type=DEFORMABLE_BODY
)
```

### Add Hole (Cut Extrude)
```python
# Create sketch on top face
top_face = part.faces.findAt(((LENGTH/2, HEIGHT, WIDTH/2),))
sketch = model.ConstrainedSketch(name='HoleSketch', sheetSize=50.0,
                                  transform=part.MakeSketchTransform(sketchPlane=top_face[0]))

# Draw circle for hole
sketch.CircleByCenterPerimeter(center=(LENGTH/2, WIDTH/2), point1=(LENGTH/2 + HOLE_RADIUS, WIDTH/2))

# Cut through
part.CutExtrude(
    sketchPlane=top_face[0],
    sketch=sketch,
    depth=HEIGHT,  # Through entire height
    flipExtrudeDirection=ON
)
```

### Fillet Edges
```python
edges = part.edges.findAt(((x, y, z),))
part.Round(radius=FILLET_RADIUS, edgeList=edges)
```

### Create Partition (for BC/Load Regions)
```python
# Partition by datum plane
datum = part.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=50.0)
part.PartitionCellByDatumPlane(datumPlane=part.datums[datum.id], cells=part.cells)
```

### Assembly Setup
```python
assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
instance = assembly.Instance(name='Part-1', part=part, dependent=ON)
```

### Position Instance
```python
# Translate
assembly.translate(instanceList=('Part-1',), vector=(dx, dy, dz))

# Rotate about Z-axis
assembly.rotate(
    instanceList=('Part-1',),
    axisPoint=(0, 0, 0),
    axisDirection=(0, 0, 1),
    angle=90.0
)
```

### Create Sets and Surfaces
```python
# Set from face (use instance coordinates!)
face = instance.faces.findAt(((x, y, z),))
assembly.Set(faces=face, name='MyFaceSet')

# Surface for loads/contact
assembly.Surface(side1Faces=face, name='MySurface')

# Cells by bounding box
cells = instance.cells.getByBoundingBox(xMin=0, yMin=0, zMin=0, xMax=50, yMax=100, zMax=20)
assembly.Set(cells=cells, name='DesignRegion')
```

## Finding Entities

### By Exact Coordinates
```python
# Point must be EXACTLY on the face/edge/vertex
face = instance.faces.findAt(((x, y, z),))
```

### By Bounding Box
```python
# More tolerant - finds entities within box
faces = instance.faces.getByBoundingBox(
    xMin=-0.1, yMin=0, zMin=0,
    xMax=0.1, yMax=100, zMax=50
)
```

### Multiple Entities
```python
face1 = instance.faces.findAt(((x1, y1, z1),))
face2 = instance.faces.findAt(((x2, y2, z2),))
combined = face1 + face2
```

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Cannot find face at coordinates" | Point not exactly on face | Use bounding box or verify coordinates |
| "Sketch is not closed" | Gap in sketch entities | Ensure all lines connect to form closed loop |
| "Cannot mesh this geometry" | Complex shape or thin features | Add partitions, use virtual topology |
| "Part has no cells" | 2D sketch, not extruded | Call `BaseSolidExtrude()` or similar |
| "Instance already exists" | Duplicate instance name | Use unique name or delete existing |

## Geometry Checklist

Before proceeding to mesh/analysis:
- [ ] Part created with correct dimensions
- [ ] Geometry is watertight (no gaps)
- [ ] Instance created in assembly
- [ ] Sets created for BC/load regions (use instance, not part)
- [ ] Partitions added if needed for local mesh control or region selection

## API Reference

For detailed parameters:
- [Part API](../../docs/abaqus-api/modules/part.md)
- [Sketcher API](../../docs/abaqus-api/modules/sketcher.md)
- [Assembly API](../../docs/abaqus-api/modules/assembly.md)
