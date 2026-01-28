# Step API Quick Reference

## StaticStep (most common)

```python
model.StaticStep(
    name='StepName',
    previous='Initial',  # or previous step name
    timePeriod=1.0,      # pseudo-time
    initialInc=1.0,      # initial increment
    minInc=1e-6,         # minimum increment
    maxInc=1.0,          # maximum increment
    maxNumInc=100,       # max iterations
    nlgeom=OFF           # ON for large deformation
)
```

## FrequencyStep

```python
model.FrequencyStep(
    name='Modes',
    previous='Initial',
    numEigen=10,         # number of modes
    eigensolver=LANCZOS, # or SUBSPACE
    normalization=DISPLACEMENT
)
```

## BuckleStep

```python
model.BuckleStep(
    name='Buckling',
    previous='LoadStep',  # after preload
    numEigen=5,           # number of buckling modes
    eigensolver=SUBSPACE
)
```

## ImplicitDynamicsStep

```python
model.ImplicitDynamicsStep(
    name='Transient',
    previous='Initial',
    timePeriod=0.1,      # real time in seconds
    initialInc=0.001,
    maxNumInc=10000,
    nlgeom=ON
)
```

## ExplicitDynamicsStep

```python
model.ExplicitDynamicsStep(
    name='Impact',
    previous='Initial',
    timePeriod=0.01      # real time in seconds
)
```

## HeatTransferStep

```python
# Steady-state
model.HeatTransferStep(
    name='SteadyHeat',
    previous='Initial',
    response=STEADY_STATE
)

# Transient
model.HeatTransferStep(
    name='TransientHeat',
    previous='Initial',
    response=TRANSIENT,
    timePeriod=100.0,    # real time
    initialInc=1.0,
    deltmx=5.0           # max temperature change per increment
)
```

## CoupledTempDisplacementStep

```python
model.CoupledTempDisplacementStep(
    name='ThermoMech',
    previous='Initial',
    response=TRANSIENT,
    timePeriod=10.0,
    deltmx=10.0,         # max temperature change per increment
    nlgeom=ON
)
```

## SteadyStateDynamicsStep

```python
model.SteadyStateDynamicsStep(
    name='Harmonic',
    previous='Initial',
    frequencyRange=(0.0, 1000.0)  # frequency sweep range in Hz
)
```

## Key Constants

```python
# Geometry
from abaqusConstants import ON, OFF

# Heat transfer response
from abaqusConstants import STEADY_STATE, TRANSIENT

# Eigensolvers
from abaqusConstants import LANCZOS, SUBSPACE

# Normalization
from abaqusConstants import DISPLACEMENT, MASS
```
