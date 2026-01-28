# Common BC Patterns

## Cantilever (one end fixed)
```python
fixed_face = instance.faces.findAt(((0, HEIGHT/2, WIDTH/2),))
assembly.Set(faces=fixed_face, name='Fixed')
model.EncastreBC(name='Fixed', createStepName='Initial', region=assembly.sets['Fixed'])
```

## Simply Supported Beam (pinned at both ends)
```python
# End 1: pinned (no translation)
model.DisplacementBC(name='Pin1', createStepName='Initial', region=end1Set,
                     u1=0.0, u2=0.0, u3=0.0)
# End 2: roller (vertical + lateral fixed, axial free)
model.DisplacementBC(name='Roller', createStepName='Initial', region=end2Set,
                     u2=0.0, u3=0.0)
```

## Half-Symmetry Model
```python
# Symmetry about YZ plane (X=0)
symFace = instance.faces.findAt(((0, HEIGHT/2, WIDTH/2),))
symRegion = assembly.Set(faces=symFace, name='SymmetryPlane')
model.XsymmBC(name='Symmetry', createStepName='Initial', region=symRegion)
```

## Quarter-Symmetry Model
```python
# Two symmetry planes
model.XsymmBC(name='SymX', createStepName='Initial', region=xSymPlane)
model.YsymmBC(name='SymY', createStepName='Initial', region=ySymPlane)
```

## Prevent Rigid Body Motion (minimum BCs)
```python
# For a free-floating structure, fix one point in all directions
cornerVert = instance.vertices.findAt(((0, 0, 0),))
cornerSet = assembly.Set(vertices=cornerVert, name='CornerFix')
model.DisplacementBC(name='Fix', createStepName='Initial', region=cornerSet,
                     u1=0.0, u2=0.0, u3=0.0)
```

## Axisymmetric Model
```python
# For 2D axisymmetric, constrain radial displacement at axis
model.DisplacementBC(name='Axis', createStepName='Initial', region=axisEdge,
                     u1=0.0)  # u1 = radial direction
```

## Prescribed Displacement Loading
```python
# Apply displacement instead of force (displacement control)
topFace = instance.faces.findAt(((LENGTH/2, HEIGHT, WIDTH/2),))
topSet = assembly.Set(faces=topFace, name='TopFace')

# Fix in Initial, then apply displacement in LoadStep
model.DisplacementBC(name='TopBC', createStepName='Initial', region=topSet,
                     u1=0.0, u2=0.0, u3=0.0)
model.boundaryConditions['TopBC'].setValuesInStep(
    stepName='LoadStep',
    u2=-5.0  # Move 5mm downward
)
```

## Sliding Contact Surface
```python
# Allow tangential motion, fix normal direction
model.DisplacementBC(name='Slider', createStepName='Initial', region=slideFace,
                     u2=0.0)  # Only Y (normal) fixed
```

## Thermal-Mechanical (Fixed Temperature Edge)
```python
model.TemperatureBC(name='ColdEnd', createStepName='Initial', region=coldFace,
                    magnitude=20.0)  # Room temperature
model.TemperatureBC(name='HotEnd', createStepName='HeatStep', region=hotFace,
                    magnitude=500.0)  # Applied heat
```
