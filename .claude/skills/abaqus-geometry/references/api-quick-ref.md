# Geometry API Quick Reference

## Part Creation

```python
part = model.Part(
    name='PartName',
    dimensionality=THREE_D,  # or TWO_D_PLANAR, AXISYMMETRIC
    type=DEFORMABLE_BODY     # or DISCRETE_RIGID_SURFACE, ANALYTICAL_RIGID_SURFACE
)
```

## Sketch Operations

```python
sketch = model.ConstrainedSketch(name='Sketch', sheetSize=200.0)
sketch.rectangle(point1=(x1, y1), point2=(x2, y2))
sketch.CircleByCenterPerimeter(center=(x, y), point1=(x+r, y))
sketch.Line(point1=(x1, y1), point2=(x2, y2))
sketch.ArcByCenterEnds(center=(x, y), point1=(x1, y1), point2=(x2, y2))
```

## Feature Operations

```python
part.BaseSolidExtrude(sketch=sketch, depth=d)
part.BaseSolidRevolve(sketch=sketch, angle=360.0)
part.CutExtrude(sketchPlane=face, sketch=cutSketch, depth=d)
part.Round(radius=r, edgeList=edges)
part.Chamfer(d=chamferDist, edgeList=edges)
```

## Assembly

```python
assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
instance = assembly.Instance(name='Name', part=part, dependent=ON)
assembly.translate(instanceList=('Name',), vector=(dx, dy, dz))
assembly.rotate(instanceList=('Name',), axisPoint=(0,0,0), axisDirection=(0,1,0), angle=90)
```

## CAD Import

```python
step = mdb.openStep('file.step', scaleFromFile=OFF)
iges = mdb.openIges('file.iges', scaleFromFile=OFF)
part = model.PartFromGeometryFile(name='Name', geometryFile=step,
                                   dimensionality=THREE_D, type=DEFORMABLE_BODY)
```

## Entity Selection

```python
# By exact coordinates (point must be ON the entity)
face = instance.faces.findAt(((x, y, z),))
edge = instance.edges.findAt(((x, y, z),))
vertex = instance.vertices.findAt(((x, y, z),))

# By bounding box (more tolerant)
faces = instance.faces.getByBoundingBox(xMin=0, yMin=0, zMin=0, xMax=100, yMax=100, zMax=100)

# Combine multiple entities
combined = face1 + face2
```

## Sets and Surfaces

```python
# Create set from faces (use instance, not part!)
assembly.Set(faces=face, name='MySet')

# Create surface for loads/contact
assembly.Surface(side1Faces=face, name='MySurface')

# Set from cells
cells = instance.cells.getByBoundingBox(...)
assembly.Set(cells=cells, name='CellSet')
```

## Partitioning

```python
# Partition by datum plane
datum = part.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=50.0)
part.PartitionCellByDatumPlane(datumPlane=part.datums[datum.id], cells=part.cells)

# Partition by sketch
part.PartitionCellBySketch(sketchPlane=face, sketch=sketch, cells=cells)
```
