# Common Dynamic Analysis Patterns

## Drop Test (1m drop)

```python
# v = sqrt(2*g*h) = sqrt(2*9810*1000) = 4429 mm/s
from abaqus import *
from abaqusConstants import *

# Calculate drop velocity
g = 9810.0  # mm/s²
h = 1000.0  # mm (1 meter drop)
v_impact = (2 * g * h) ** 0.5  # 4429 mm/s

# Set initial velocity on all nodes
assembly.Set(cells=instance.cells, name='AllCells')
model.Velocity(
    name='DropVelocity',
    createStepName='Initial',
    region=assembly.sets['AllCells'],
    velocity1=0.0,
    velocity2=-v_impact,  # Downward
    velocity3=0.0
)

# Short time period for impact event
model.ExplicitDynamicsStep(
    name='Impact',
    previous='Initial',
    timePeriod=0.01  # 10 ms typical for drop test
)
```

## Impact with Rigid Surface

```python
# Create analytical rigid surface (ground plane)
ground_part = model.Part(name='Ground', dimensionality=THREE_D,
                         type=ANALYTIC_RIGID_SURFACE)
ground_part.AnalyticRigidSurfExtrude(sketch=ground_sketch)

# Create reference point for rigid body
ground_part.ReferencePoint(point=(0.0, 0.0, 0.0))

# Instance ground
ground_instance = assembly.Instance(name='Ground-1', part=ground_part, dependent=ON)

# Fix ground
rp_region = assembly.Set(referencePoints=(ground_instance.referencePoints[2],), name='GroundRP')
model.EncastreBC(name='FixGround', createStepName='Initial', region=rp_region)

# Define contact (see /abaqus-interaction for full details)
model.ContactProperty('FrictionContact')
model.interactionProperties['FrictionContact'].TangentialBehavior(
    formulation=PENALTY,
    fraction=0.005,
    table=((0.3,),)  # Friction coefficient
)
model.interactionProperties['FrictionContact'].NormalBehavior(
    pressureOverclosure=HARD,
    allowSeparation=ON
)

# General contact for explicit
model.ContactExp(name='GeneralContact', createStepName='Impact')
model.interactions['GeneralContact'].includedPairs.setValuesInStep(
    stepName='Impact',
    useAllstar=ON
)
model.interactions['GeneralContact'].contactPropertyAssignments.appendInStep(
    stepName='Impact',
    assignments=((GLOBAL, SELF, 'FrictionContact'),)
)
```

## Transient Response (Force Pulse)

```python
# Define time-varying amplitude
model.TabularAmplitude(
    name='Pulse',
    data=(
        (0.0, 0.0),
        (0.001, 1.0),   # Ramp up in 1 ms
        (0.002, 1.0),   # Hold for 1 ms
        (0.003, 0.0)    # Ramp down in 1 ms
    ),
    timeSpan=STEP
)

# Apply force with amplitude
model.ConcentratedForce(
    name='ImpactLoad',
    createStepName='Response',
    region=assembly.sets['LoadPoint'],
    cf2=-1000.0,  # Force magnitude
    amplitude='Pulse'
)

# Implicit step for longer transient
model.ImplicitDynamicsStep(
    name='Response',
    previous='Initial',
    timePeriod=0.1,      # 100 ms to capture oscillation
    initialInc=0.0001,
    maxInc=0.001,
    application=TRANSIENT_FIDELITY
)
```

## Blast Loading (Simplified)

```python
# Simplified blast pressure (exponential decay)
# P(t) = P_peak * exp(-t/tau)
import math

P_peak = 10.0   # MPa
tau = 0.001     # Time constant (1 ms)
duration = 0.01  # 10 ms

# Create amplitude table
blast_data = []
for i in range(101):
    t = i * duration / 100
    p = P_peak * math.exp(-t / tau)
    blast_data.append((t, p / P_peak))

model.TabularAmplitude(name='BlastDecay', data=tuple(blast_data))

# Apply pressure with amplitude
model.Pressure(
    name='BlastPressure',
    createStepName='Blast',
    region=assembly.surfaces['ExposedFace'],
    magnitude=P_peak,
    amplitude='BlastDecay'
)
```

## Vibration Response (Base Excitation)

```python
# Define sinusoidal base motion
freq = 50.0  # Hz
amplitude_val = 1.0  # mm displacement amplitude

model.PeriodicAmplitude(
    name='Vibration',
    frequency=freq,
    start=0.0,
    a_0=0.0,
    data=((0.0, amplitude_val),)  # Sine wave
)

# Apply as displacement BC
model.DisplacementBC(
    name='BaseMotion',
    createStepName='Excitation',
    region=assembly.sets['Base'],
    u2=amplitude_val,
    amplitude='Vibration'
)

# Capture enough cycles
num_cycles = 20
model.ImplicitDynamicsStep(
    name='Excitation',
    previous='Initial',
    timePeriod=num_cycles / freq,
    initialInc=1.0 / (freq * 20),  # 20 points per cycle
    maxInc=1.0 / (freq * 10)
)
```

## High-Velocity Impact

```python
# Projectile impacting target
PROJECTILE_VELOCITY = 100000.0  # mm/s = 100 m/s

# Material with failure
material = model.Material(name='AluminumWithFailure')
material.Elastic(table=((70000.0, 0.33),))
material.Plastic(table=((280.0, 0.0), (350.0, 0.1)))
material.Density(table=((2.7e-9,),))
material.DuctileDamageInitiation(table=((0.3, -0.33, 0.0),))
material.ductileDamageInitiation.DamageEvolution(type=DISPLACEMENT, table=((0.1,),))

# Initial velocity on projectile only
assembly.Set(cells=projectile_instance.cells, name='ProjectileCells')
model.Velocity(
    name='ProjectileVel',
    createStepName='Initial',
    region=assembly.sets['ProjectileCells'],
    velocity1=PROJECTILE_VELOCITY,
    velocity2=0.0,
    velocity3=0.0
)

# Very short time period
model.ExplicitDynamicsStep(
    name='Impact',
    previous='Initial',
    timePeriod=0.0001  # 0.1 ms
)
```

## Multi-Body Contact Impact

```python
# Two bodies colliding

# Body A moving right
model.Velocity(
    name='VelocityA',
    createStepName='Initial',
    region=assembly.sets['BodyA'],
    velocity1=1000.0, velocity2=0.0, velocity3=0.0
)

# Body B moving left
model.Velocity(
    name='VelocityB',
    createStepName='Initial',
    region=assembly.sets['BodyB'],
    velocity1=-1000.0, velocity2=0.0, velocity3=0.0
)

# General contact captures collision automatically
model.ContactExp(name='GeneralContact', createStepName='Collision')
model.interactions['GeneralContact'].includedPairs.setValuesInStep(
    stepName='Collision',
    useAllstar=ON
)
```

## Output for Animation

```python
# High-frequency output for smooth animation
model.FieldOutputRequest(
    name='Animation',
    createStepName='Impact',
    variables=('S', 'U', 'V', 'PEEQ'),
    numIntervals=200  # 200 frames
)

# Or by time interval
model.FieldOutputRequest(
    name='Animation',
    createStepName='Impact',
    variables=('S', 'U', 'V', 'PEEQ'),
    timeInterval=0.00001  # Every 10 µs
)
```
