# Dynamic Analysis API Quick Reference

## Explicit Dynamics Step

```python
model.ExplicitDynamicsStep(
    name='StepName',
    previous='Initial',
    timePeriod=0.001,           # Real time in seconds
    massScaling=((SEMI_AUTOMATIC, MODEL, THROUGHOUT_STEP, 0.0, 1e-6, ...),)
)
```

### Full ExplicitDynamicsStep Parameters

```python
model.ExplicitDynamicsStep(
    name='Impact',
    previous='Initial',
    description='',
    timePeriod=0.001,
    nlgeom=ON,                   # Nonlinear geometry (default ON for explicit)
    adiabatic=OFF,               # Adiabatic heating
    timeIncrementationMethod=AUTOMATIC_GLOBAL,
    scaleFactor=1.0,
    linearBulkViscosity=0.06,    # Bulk viscosity for shock waves
    quadBulkViscosity=1.2,
    massScaling=((SEMI_AUTOMATIC, MODEL, AT_BEGINNING, 0.0, 1e-06, BELOW_MIN, 0, 0, 0.0, 0.0, 0, None),)
)
```

## Implicit Dynamics Step

```python
model.ImplicitDynamicsStep(
    name='StepName',
    previous='Initial',
    timePeriod=1.0,
    initialInc=0.01,
    minInc=1e-8,
    maxInc=0.1,
    application=TRANSIENT_FIDELITY  # or MODERATE_DISSIPATION
)
```

### Full ImplicitDynamicsStep Parameters

```python
model.ImplicitDynamicsStep(
    name='Transient',
    previous='Initial',
    description='',
    timePeriod=1.0,
    nlgeom=ON,
    application=TRANSIENT_FIDELITY,  # TRANSIENT_FIDELITY, MODERATE_DISSIPATION, QUASI_STATIC
    initialInc=0.01,
    minInc=1e-8,
    maxInc=0.1,
    maxNumInc=1000,
    nohaf=OFF,                   # Automatic time stepping
    amplitude=RAMP,              # RAMP or STEP
    alpha=DEFAULT,               # Hilber-Hughes-Taylor parameter
    initialConditions=DEFAULT,
    reformKernel=8,              # Kernel update frequency
    convertSDI=PROPAGATED
)
```

### Application Options

| Application | Description | Use For |
|-------------|-------------|---------|
| `TRANSIENT_FIDELITY` | Accurate transient response | Vibration, wave propagation |
| `MODERATE_DISSIPATION` | Numerical damping to reduce high-freq oscillations | Most dynamic problems |
| `QUASI_STATIC` | Large time steps, high dissipation | Slow dynamics |

## Initial Velocity

```python
model.Velocity(
    name='InitVel',
    createStepName='Initial',
    region=region,
    velocity1=0.0, velocity2=-1000.0, velocity3=0.0  # mm/s
)
```

### Full Velocity Parameters

```python
model.Velocity(
    name='InitialVelocity',
    createStepName='Initial',
    region=assembly.sets['AllNodes'],
    velocity1=0.0,               # X velocity (mm/s)
    velocity2=-5000.0,           # Y velocity (mm/s)
    velocity3=0.0,               # Z velocity (mm/s)
    omega=0.0,                   # Angular velocity (rad/s)
    axisBegin=(0.0, 0.0, 0.0),   # Rotation axis start
    axisEnd=(0.0, 1.0, 0.0),     # Rotation axis end
    distributionType=UNIFORM
)
```

## Mass Scaling (for explicit)

```python
# Increase stable time increment
model.ExplicitDynamicsStep(...,
    massScaling=((SEMI_AUTOMATIC, MODEL, THROUGHOUT_STEP, 0.0, 1e-6,
                  BELOW_MIN, 1, 0.0, 0.0, 0.0, 0.0),))
```

### Mass Scaling Tuple Format

```python
massScaling = ((
    SEMI_AUTOMATIC,       # Type: SEMI_AUTOMATIC or FIXED_MASS_SCALING
    MODEL,                # Region: MODEL, PICK_REGION
    AT_BEGINNING,         # When: AT_BEGINNING, THROUGHOUT_STEP
    0.0,                  # Frequency (for THROUGHOUT)
    1e-06,                # dt scaling target
    BELOW_MIN,            # BELOW_MIN, SET_EQUAL_DT
    0,                    # Number of instances
    0,                    # minStep
    0.0, 0.0, 0.0, 0.0,   # Other parameters
    None                  # Region (if PICK_REGION)
),)
```

## Field Output Request

```python
model.FieldOutputRequest(
    name='F-Output',
    createStepName='Impact',
    variables=('S', 'U', 'V', 'A', 'PEEQ', 'STATUS', 'ENER'),
    numIntervals=100
)
```

### Common Output Variables for Dynamics

| Variable | Description |
|----------|-------------|
| `S` | Stress |
| `U` | Displacement |
| `V` | Velocity |
| `A` | Acceleration |
| `PEEQ` | Equivalent plastic strain |
| `STATUS` | Element status (failed = 0) |
| `ENER` | Energy densities |
| `COORD` | Current coordinates |

## History Output Request (Energies)

```python
model.HistoryOutputRequest(
    name='Energies',
    createStepName='Impact',
    variables=('ALLKE', 'ALLIE', 'ALLWK', 'ALLPD', 'ALLAE', 'ETOTAL'),
    frequency=1
)
```

### Energy Variables

| Variable | Description |
|----------|-------------|
| `ALLKE` | Kinetic energy |
| `ALLIE` | Internal energy |
| `ALLWK` | External work |
| `ALLPD` | Plastic dissipation |
| `ALLAE` | Artificial strain energy (hourglass) |
| `ETOTAL` | Total energy (should be ~constant) |

## Element Types for Explicit

```python
from mesh import ElemType

# 3D solid - reduced integration (recommended)
elemType = ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT,
                    hourglassControl=ENHANCED)

# 3D solid - tetrahedral
elemType = ElemType(elemCode=C3D10M, elemLibrary=EXPLICIT)

# Shell
elemType = ElemType(elemCode=S4R, elemLibrary=EXPLICIT)
```

### Element Library

| elemLibrary | Use For |
|-------------|---------|
| `EXPLICIT` | Explicit dynamics |
| `STANDARD` | Implicit (static, implicit dynamic) |

## Damping

```python
# Material damping (Rayleigh)
material.Damping(alpha=0.1, beta=0.001)

# Structural damping on step
model.ImplicitDynamicsStep(...,
    structuralDampingControl=COMBINED,
    structuralDamping=0.02)
```
