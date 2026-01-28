# Coupled Analysis API Quick Reference

## CoupledTempDisplacementStep

```python
model.CoupledTempDisplacementStep(
    name='StepName',
    previous='Initial',
    response=STEADY_STATE,     # or TRANSIENT
    timePeriod=1.0,
    deltmx=10.0,               # Max temperature change per increment
    initialInc=0.1,
    minInc=1e-6,
    maxInc=1.0
)
```

### Response Types

| Response | Description | Use When |
|----------|-------------|----------|
| STEADY_STATE | Time-independent thermal equilibrium | Long-term operation |
| TRANSIENT | Time-dependent heat transfer | Heating/cooling processes |

### Key Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `timePeriod` | Total step time | 1.0 |
| `deltmx` | Max temperature change per increment | None |
| `initialInc` | Initial time increment | timePeriod |
| `minInc` | Minimum time increment | 1e-5 |
| `maxInc` | Maximum time increment | timePeriod |
| `nlgeom` | Geometric nonlinearity | OFF |

## Required Material Properties

```python
# Mechanical properties
material.Elastic(table=((E, nu),))
material.Density(table=((rho,),))

# Thermal properties
material.Conductivity(table=((k,),))
material.Expansion(table=((alpha,),))     # CRITICAL for thermal stress!
material.SpecificHeat(table=((cp,),))     # For transient analysis
```

### Material Property Units (SI-mm system)

| Property | API Call | Units | Typical Steel |
|----------|----------|-------|---------------|
| Young's modulus | `Elastic` | MPa | 210000 |
| Poisson's ratio | `Elastic` | - | 0.3 |
| Density | `Density` | tonne/mm^3 | 7.85e-9 |
| Conductivity | `Conductivity` | mW/(mm*K) | 50 |
| Specific heat | `SpecificHeat` | mJ/(tonne*K) | 5.0e11 |
| Expansion | `Expansion` | 1/K | 12e-6 |

### Temperature-Dependent Properties

```python
# Temperature-dependent elastic modulus
material.Elastic(table=(
    (210000.0, 0.3, 20.0),   # E, nu at 20C
    (200000.0, 0.3, 200.0),  # E, nu at 200C
    (180000.0, 0.3, 400.0),  # E, nu at 400C
), temperatureDependency=ON)

# Temperature-dependent expansion
material.Expansion(table=(
    (11e-6, 20.0),   # alpha at 20C
    (12e-6, 200.0),  # alpha at 200C
    (13e-6, 400.0),  # alpha at 400C
), temperatureDependency=ON, zero=20.0)
```

## Thermal Expansion Setup

```python
# Reference temperature (zero thermal strain)
material.Expansion(table=((ALPHA,),), zero=T_REF)

# Initial temperature field
model.Temperature(
    name='InitialTemp',
    createStepName='Initial',
    region=region,
    magnitude=T_REF  # Should match zero= for no initial stress
)
```

## Sequential Coupling (separate analyses)

### Step 1: Run Thermal Analysis

```python
# In thermal model
model.HeatTransferStep(
    name='Heating',
    previous='Initial',
    response=TRANSIENT,
    timePeriod=10.0
)
# ... apply thermal BCs, mesh with DC3D8, run job
```

### Step 2: Import Temperature to Structural

```python
# In structural model
model.Temperature(
    name='ImportedTemp',
    createStepName='Initial',
    region=region,
    distributionType=FROM_FILE,
    fileName='thermal_result.odb',
    step='HeatStep',
    frame=-1  # Last frame
)
```

### Import Parameters

| Parameter | Description |
|-----------|-------------|
| `distributionType` | FROM_FILE for ODB import |
| `fileName` | Path to thermal ODB |
| `step` | Step name in thermal ODB |
| `frame` | Frame number (-1 = last) |
| `beginStep` | Starting step (alternative to step) |
| `endIncrement` | LAST_INCREMENT for final state |

## Coupled Elements

```python
from mesh import ElemType

# 3D coupled elements
elemType = ElemType(elemCode=C3D8T, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType,))
```

### Available Coupled Element Types

| Code | Description |
|------|-------------|
| C3D8T | 8-node brick, full integration |
| C3D8RT | 8-node brick, reduced integration |
| C3D4T | 4-node tet |
| C3D10MT | 10-node modified tet |
| C3D20T | 20-node brick |
| C3D20RT | 20-node brick, reduced integration |

## Boundary Conditions

### Temperature BC

```python
model.TemperatureBC(
    name='HotSurface',
    createStepName='Heating',
    region=region,
    magnitude=200.0  # degrees
)
```

### Convection (Surface Film)

```python
model.FilmCondition(
    name='Convection',
    createStepName='Heating',
    surface=surface,
    filmCoeff=10.0,          # mW/(mm^2*K)
    sinkTemperature=25.0     # Ambient temp
)
```

### Heat Flux

```python
model.SurfaceHeatFlux(
    name='HeatInput',
    createStepName='Heating',
    region=surface,
    magnitude=1000.0  # mW/mm^2
)
```

## Field Output Requests

```python
model.FieldOutputRequest(
    name='ThermoMech-Output',
    createStepName='Heating',
    variables=('S', 'U', 'NT', 'THE', 'E', 'EE', 'HFL', 'RFL')
)
```

### Relevant Output Variables

| Variable | Description |
|----------|-------------|
| S | Stress |
| U | Displacement |
| NT | Temperature |
| THE | Thermal strain |
| E | Total strain |
| EE | Elastic strain |
| HFL | Heat flux |
| RFL | Reaction flux |
