# Load API Quick Reference

## ConcentratedForce

```python
model.ConcentratedForce(
    name='LoadName',
    createStepName='StepName',
    region=nodeSet,           # Set of vertices or nodes
    cf1=0.0, cf2=-1000.0, cf3=0.0,  # Force components (N)
    amplitude='AmpName'       # Optional time variation
)
```

**Parameters:**
- `name`: Unique load identifier
- `createStepName`: Step in which load becomes active
- `region`: A Set containing vertices or nodes
- `cf1`, `cf2`, `cf3`: Force components in X, Y, Z directions (Newtons)
- `amplitude`: Optional reference to TabularAmplitude for time-varying loads

## Pressure

```python
model.Pressure(
    name='LoadName',
    createStepName='StepName',
    region=surface,           # Surface object
    magnitude=10.0            # MPa (positive = compression)
)
```

**Parameters:**
- `name`: Unique load identifier
- `createStepName`: Step in which load becomes active
- `region`: A Surface object (not a Set)
- `magnitude`: Pressure value in MPa (positive = into surface)

## SurfaceTraction

```python
model.SurfaceTraction(
    name='LoadName',
    createStepName='StepName',
    region=surface,
    magnitude=10.0,           # MPa
    directionVector=((0,0,0), (0,-1,0)),  # Direction
    distributionType=UNIFORM,
    traction=GENERAL
)
```

**Parameters:**
- `name`: Unique load identifier
- `createStepName`: Step in which load becomes active
- `region`: A Surface object
- `magnitude`: Traction value in MPa (force per unit area)
- `directionVector`: Tuple of two points defining direction ((origin), (point))
- `distributionType`: UNIFORM or FIELD
- `traction`: GENERAL or SHEAR

## Gravity

```python
model.Gravity(
    name='Gravity',
    createStepName='StepName',
    comp1=0.0, comp2=-9810.0, comp3=0.0  # mm/s² (requires density!)
)
```

**Parameters:**
- `name`: Unique load identifier
- `createStepName`: Step in which gravity becomes active
- `comp1`, `comp2`, `comp3`: Acceleration components in mm/s²

**Important:** Requires `material.Density(table=...)` to have any effect!

## LineLoad

```python
model.LineLoad(
    name='EdgeLoad',
    createStepName='StepName',
    region=edgeSet,
    comp1=0.0, comp2=-10.0, comp3=0.0  # N/mm
)
```

**Parameters:**
- `name`: Unique load identifier
- `createStepName`: Step in which load becomes active
- `region`: A Set containing edges
- `comp1`, `comp2`, `comp3`: Force per unit length in N/mm

## SurfaceHeatFlux

```python
model.SurfaceHeatFlux(
    name='HeatIn',
    createStepName='HeatStep',
    region=surface,
    magnitude=100.0  # mW/mm²
)
```

**Parameters:**
- `name`: Unique load identifier
- `createStepName`: Heat transfer step name
- `region`: A Surface object
- `magnitude`: Heat flux in mW/mm²

## FilmCondition (Convection)

```python
model.FilmCondition(
    name='Convection',
    createStepName='HeatStep',
    region=surface,
    definition=EMBEDDED_COEFF,
    filmCoeff=10.0,        # mW/(mm²·K)
    sinkTemperature=25.0   # Ambient temperature
)
```

**Parameters:**
- `name`: Unique load identifier
- `createStepName`: Heat transfer step name
- `region`: A Surface object
- `definition`: EMBEDDED_COEFF for constant coefficient
- `filmCoeff`: Convection coefficient in mW/(mm²·K)
- `sinkTemperature`: Ambient/sink temperature
