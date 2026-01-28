# Common Load Patterns

## Total Force as Distributed Traction

When you have a total force but need to apply it as surface traction:

```python
# Convert 1000N total force to traction on 50x20mm face
total_force = 1000.0  # N
area = 50.0 * 20.0    # mm²
traction = total_force / area  # = 1.0 MPa

face = instance.faces.findAt(((LENGTH, HEIGHT/2, WIDTH/2),))
surface = assembly.Surface(side1Faces=face, name='LoadSurface')

model.SurfaceTraction(
    name='DistributedLoad',
    createStepName='LoadStep',
    region=surface,
    magnitude=traction,
    directionVector=((0, 0, 0), (0, -1, 0)),  # -Y direction
    distributionType=UNIFORM,
    traction=GENERAL
)
```

## Gravity with Density

Gravity requires material density to have any effect:

```python
# MUST define density in material
material = model.Material(name='Steel')
material.Elastic(table=((210000.0, 0.3),))
material.Density(table=((7.85e-9,),))  # tonne/mm³

# Then gravity works
model.Gravity(
    name='Gravity',
    createStepName='LoadStep',
    comp2=-9810.0  # mm/s² in -Y direction
)
```

## Moment via Force Couple

Apply a moment using two equal and opposite forces:

```python
# Moment = Force × Distance
# For 1000 N·mm moment with 10mm separation: F = 100N

# Find two vertices separated by distance
v1 = instance.vertices.findAt(((x, y+5, z),))
v2 = instance.vertices.findAt(((x, y-5, z),))

region1 = assembly.Set(vertices=v1, name='MomentPoint1')
region2 = assembly.Set(vertices=v2, name='MomentPoint2')

model.ConcentratedForce(
    name='Couple_F1',
    createStepName='LoadStep',
    region=region1,
    cf3=100.0   # +Z force
)

model.ConcentratedForce(
    name='Couple_F2',
    createStepName='LoadStep',
    region=region2,
    cf3=-100.0  # -Z force (opposite)
)
```

## Varying Load with Amplitude

Create time-varying loads using amplitudes:

```python
# Define amplitude (time, scale factor)
model.TabularAmplitude(
    name='Ramp',
    data=(
        (0.0, 0.0),   # Start at zero
        (0.5, 1.0),   # Full load at t=0.5
        (1.0, 1.0),   # Maintain full load
    )
)

# Apply load with amplitude
model.Pressure(
    name='RampingPressure',
    createStepName='LoadStep',
    region=surface,
    magnitude=10.0,       # Peak value
    amplitude='Ramp'      # Scale by amplitude
)
```

## Multi-Step Loading

Increase or modify loads across analysis steps:

```python
# Step 1: Initial load
model.ConcentratedForce(
    name='Load',
    createStepName='Step-1',
    region=region,
    cf2=-500.0  # 500N downward
)

# Step 2: Increase load
model.loads['Load'].setValuesInStep(
    stepName='Step-2',
    cf2=-1000.0  # Increase to 1000N
)

# Step 3: Remove load
model.loads['Load'].deactivate(stepName='Step-3')
```

## Hydrostatic Pressure (Varying with Depth)

For fluid pressure that varies with depth:

```python
# Define analytical field for depth-varying pressure
# p = rho * g * depth
# For water: rho = 1e-9 tonne/mm³, g = 9810 mm/s²

model.ExpressionField(
    name='HydrostaticField',
    expression='9.81e-6 * (100 - Y)'  # Pressure at depth (100-Y) mm
)

model.Pressure(
    name='Hydrostatic',
    createStepName='LoadStep',
    region=surface,
    distributionType=FIELD,
    field='HydrostaticField'
)
```

## Cyclic Loading

Apply sinusoidal or cyclic loads:

```python
# Sinusoidal amplitude
model.PeriodicAmplitude(
    name='Sine',
    frequency=10.0,  # Hz
    start=0.0,
    a_0=0.0,         # DC offset
    data=((1.0, 0.0),)  # (amplitude, phase)
)

model.ConcentratedForce(
    name='CyclicLoad',
    createStepName='DynamicStep',
    region=region,
    cf2=-1000.0,
    amplitude='Sine'
)
```
