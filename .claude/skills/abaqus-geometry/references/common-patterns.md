# Common Geometry Patterns

## Box (L x W x H)

```python
part = model.Part(name='Box', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='BoxSketch', sheetSize=200.0)
sketch.rectangle(point1=(0.0, 0.0), point2=(LENGTH, WIDTH))
part.BaseSolidExtrude(sketch=sketch, depth=HEIGHT)
```

## Cylinder (R x H)

```python
part = model.Part(name='Cylinder', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='CylSketch', sheetSize=200.0)
sketch.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(RADIUS, 0.0))
part.BaseSolidExtrude(sketch=sketch, depth=HEIGHT)
```

## Tube/Hollow Cylinder

```python
part = model.Part(name='Tube', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='TubeSketch', sheetSize=200.0)
sketch.CircleByCenterPerimeter(center=(0,0), point1=(OUTER_R, 0))
sketch.CircleByCenterPerimeter(center=(0,0), point1=(INNER_R, 0))
part.BaseSolidExtrude(sketch=sketch, depth=HEIGHT)
```

## I-Beam Profile

```python
part = model.Part(name='IBeam', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='IBeamSketch', sheetSize=200.0)
sketch.rectangle(point1=(-W/2, 0), point2=(W/2, FLANGE_T))  # Bottom flange
sketch.rectangle(point1=(-WEB_T/2, FLANGE_T), point2=(WEB_T/2, H-FLANGE_T))  # Web
sketch.rectangle(point1=(-W/2, H-FLANGE_T), point2=(W/2, H))  # Top flange
part.BaseSolidExtrude(sketch=sketch, depth=LENGTH)
```

## Plate with Hole

```python
# Create plate
part = model.Part(name='PlateWithHole', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='PlateSketch', sheetSize=200.0)
sketch.rectangle(point1=(0, 0), point2=(L, W))
part.BaseSolidExtrude(sketch=sketch, depth=T)

# Cut hole
top_face = part.faces.findAt(((L/2, W/2, T),))
transform = part.MakeSketchTransform(sketchPlane=top_face[0], sketchPlaneSide=SIDE1,
                                      sketchOrientation=RIGHT, origin=(0, 0, T))
cutSketch = model.ConstrainedSketch(name='HoleSketch', sheetSize=100.0, transform=transform)
cutSketch.CircleByCenterPerimeter(center=(L/2, W/2), point1=(L/2+HOLE_R, W/2))
part.CutExtrude(sketchPlane=top_face[0], sketchUpEdge=..., sketch=cutSketch, depth=T)
```

## Revolved Solid (Shaft/Pipe)

```python
part = model.Part(name='Shaft', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='ShaftSketch', sheetSize=200.0)

# Construction line = rotation axis (must be Y-axis through origin)
sketch.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))

# Cross-section (must be on positive X side of axis)
sketch.rectangle(point1=(INNER_R, 0.0), point2=(OUTER_R, LENGTH))

# Revolve 360 degrees
part.BaseSolidRevolve(sketch=sketch, angle=360.0, flipRevolveDirection=OFF)
```

## L-Bracket

```python
part = model.Part(name='LBracket', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='LSketch', sheetSize=200.0)

# Draw L-shape profile
sketch.Line(point1=(0, 0), point2=(0, HEIGHT))
sketch.Line(point1=(0, HEIGHT), point2=(THICKNESS, HEIGHT))
sketch.Line(point1=(THICKNESS, HEIGHT), point2=(THICKNESS, THICKNESS))
sketch.Line(point1=(THICKNESS, THICKNESS), point2=(WIDTH, THICKNESS))
sketch.Line(point1=(WIDTH, THICKNESS), point2=(WIDTH, 0))
sketch.Line(point1=(WIDTH, 0), point2=(0, 0))

part.BaseSolidExtrude(sketch=sketch, depth=DEPTH)
```

## Assembly with Multiple Parts

```python
# Create assembly
assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)

# Add instances
inst1 = assembly.Instance(name='Part1-1', part=part1, dependent=ON)
inst2 = assembly.Instance(name='Part2-1', part=part2, dependent=ON)

# Position second instance
assembly.translate(instanceList=('Part2-1',), vector=(100.0, 0.0, 0.0))
assembly.rotate(instanceList=('Part2-1',), axisPoint=(100, 0, 0),
                axisDirection=(0, 0, 1), angle=90.0)
```

## Centered Origin (for Symmetric Parts)

```python
# Box centered at origin
sketch.rectangle(point1=(-L/2, -W/2), point2=(L/2, W/2))
part.BaseSolidExtrude(sketch=sketch, depth=H)

# Or translate after creation
assembly.translate(instanceList=('Part-1',), vector=(-L/2, -W/2, -H/2))
```
