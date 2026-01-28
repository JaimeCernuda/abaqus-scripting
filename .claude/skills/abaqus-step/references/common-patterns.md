# Common Step Patterns

## Linear Static (Simple)

Most basic analysis - small deformation, linear material.

```python
model.StaticStep(name='Load', previous='Initial')
```

## Nonlinear Static (Large Deformation)

For thin structures, cables, or any large rotation/displacement.

```python
model.StaticStep(
    name='Load',
    previous='Initial',
    nlgeom=ON,
    initialInc=0.1,
    maxNumInc=100,
    minInc=1e-8,
    maxInc=0.1
)
```

## Nonlinear Static (Contact/Plasticity)

For difficult convergence - contact or material nonlinearity.

```python
model.StaticStep(
    name='Load',
    previous='Initial',
    nlgeom=ON,
    initialInc=0.01,
    maxNumInc=1000,
    minInc=1e-12,
    maxInc=0.05
)
```

## Multi-step Sequential Analysis

Apply loads in stages or ramp loads gradually.

```python
model.StaticStep(name='Preload', previous='Initial')
model.StaticStep(name='MainLoad', previous='Preload')
model.StaticStep(name='Overload', previous='MainLoad')
```

## Modal Analysis (Natural Frequencies)

Extract vibration modes and frequencies.

```python
model.FrequencyStep(
    name='Modes',
    previous='Initial',
    numEigen=10,
    eigensolver=LANCZOS,
    normalization=DISPLACEMENT
)
```

## Prestressed Modal Analysis

First apply preload, then extract modes.

```python
model.StaticStep(name='Preload', previous='Initial', nlgeom=ON)
model.FrequencyStep(name='Modes', previous='Preload', numEigen=10)
```

## Linear Buckling Analysis

Predict elastic buckling load factors.

```python
model.StaticStep(name='Load', previous='Initial')
model.BuckleStep(name='Buckling', previous='Load', numEigen=5)
```

## Impact/Crash Simulation

High-speed, short-duration events.

```python
model.ExplicitDynamicsStep(
    name='Impact',
    previous='Initial',
    timePeriod=0.001  # 1 ms
)
```

## Drop Test

Object falling and impacting surface.

```python
model.ExplicitDynamicsStep(
    name='Drop',
    previous='Initial',
    timePeriod=0.01  # 10 ms
)
```

## Transient Dynamics (Smooth Loading)

Gradual dynamic loading with implicit solver.

```python
model.ImplicitDynamicsStep(
    name='Dynamic',
    previous='Initial',
    timePeriod=0.1,
    initialInc=0.001,
    maxNumInc=10000,
    nlgeom=ON
)
```

## Steady-State Heat Transfer

Find equilibrium temperature distribution.

```python
model.HeatTransferStep(
    name='SteadyHeat',
    previous='Initial',
    response=STEADY_STATE
)
```

## Transient Heat Transfer

Temperature evolution over time.

```python
model.HeatTransferStep(
    name='Heating',
    previous='Initial',
    response=TRANSIENT,
    timePeriod=100.0,
    initialInc=1.0,
    deltmx=5.0  # limit temperature change per increment
)
```

## Coupled Thermomechanical

Simultaneous thermal and structural effects.

```python
model.CoupledTempDisplacementStep(
    name='ThermoMech',
    previous='Initial',
    response=TRANSIENT,
    timePeriod=10.0,
    deltmx=10.0,
    nlgeom=ON
)
```

## Harmonic Response

Frequency sweep for vibration response.

```python
model.SteadyStateDynamicsStep(
    name='Harmonic',
    previous='Modes',  # requires prior frequency step
    frequencyRange=(10.0, 500.0)
)
```
