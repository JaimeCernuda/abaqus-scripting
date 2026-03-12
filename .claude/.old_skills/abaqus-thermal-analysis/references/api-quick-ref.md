# Thermal Analysis API Quick Reference

## HeatTransferStep

```python
model.HeatTransferStep(
    name='StepName',
    previous='Initial',
    response=STEADY_STATE,   # or TRANSIENT
    timePeriod=100.0,        # For transient
    initialInc=1.0,
    minInc=0.01,
    maxInc=10.0
)
```

### Steady-State Parameters
```python
model.HeatTransferStep(
    name='SteadyState',
    previous='Initial',
    response=STEADY_STATE,
    timePeriod=1.0,          # Pseudo-time (can be 1.0)
    initialInc=1.0,
    maxNumInc=100
)
```

### Transient Parameters
```python
model.HeatTransferStep(
    name='Transient',
    previous='Initial',
    response=TRANSIENT,
    timePeriod=100.0,        # Real time in seconds
    initialInc=0.1,
    minInc=1e-6,
    maxInc=10.0,
    deltmx=5.0,              # Max temperature change per increment
    maxNumInc=10000
)
```

## Thermal Material Properties

```python
# Required for all thermal analyses
material.Conductivity(table=((k,),))      # mW/(mm·K)

# Required for transient only
material.SpecificHeat(table=((cp,),))     # mJ/(tonne·K)
material.Density(table=((rho,),))         # tonne/mm³

# For coupled thermomechanical
material.InelasticHeatFraction(fraction=0.9)
```

### Temperature-Dependent Properties
```python
# Conductivity varying with temperature
material.Conductivity(table=(
    (50.0, 20.0),    # k=50 at T=20°C
    (45.0, 100.0),   # k=45 at T=100°C
    (40.0, 200.0),   # k=40 at T=200°C
), temperatureDependency=ON)
```

## Thermal Boundary Conditions

### Fixed Temperature
```python
model.TemperatureBC(
    name='TempBC',
    createStepName='Step',
    region=region,
    magnitude=100.0,
    distributionType=UNIFORM
)
```

### Convection (Film Condition)
```python
model.FilmCondition(
    name='Conv',
    createStepName='Step',
    region=surface,
    definition=EMBEDDED_COEFF,
    filmCoeff=10.0,           # mW/(mm²·K)
    sinkTemperature=25.0      # Ambient temperature °C
)
```

### Surface Heat Flux
```python
model.SurfaceHeatFlux(
    name='Flux',
    createStepName='Step',
    region=surface,
    magnitude=100.0           # mW/mm²
)
```

### Radiation to Ambient
```python
model.RadiationToAmbient(
    name='Rad',
    createStepName='Step',
    region=surface,
    emissivity=0.8,
    ambientTemperature=25.0   # °C
)
```

### Body Heat Flux (Internal Heat Generation)
```python
model.BodyHeatFlux(
    name='BodyHeat',
    createStepName='Step',
    region=region,
    magnitude=10.0            # mW/mm³
)
```

## Initial Conditions

### Initial Temperature
```python
model.Temperature(
    name='InitTemp',
    createStepName='Initial',
    region=region,
    distributionType=UNIFORM,
    magnitudes=(100.0,)
)
```

### Initial Temperature from Field
```python
model.Temperature(
    name='InitTemp',
    createStepName='Initial',
    region=region,
    distributionType=FROM_FILE,
    fileName='previous_analysis.odb',
    step=1,
    increment=10
)
```

## Output Requests

### Field Output
```python
model.FieldOutputRequest(
    name='ThermalOutput',
    createStepName='Step',
    variables=('NT', 'HFL', 'RFL', 'HFLM')
)
```

### History Output at a Point
```python
model.HistoryOutputRequest(
    name='TempHistory',
    createStepName='Step',
    region=assembly.sets['MonitorPoint'],
    variables=('NT11',)
)
```

## Heat Transfer Elements

### 3D Solid Elements
```python
from mesh import ElemType

# Linear hexahedral
elemType = ElemType(elemCode=DC3D8, elemLibrary=STANDARD)

# Quadratic hexahedral (more accurate)
elemType = ElemType(elemCode=DC3D20, elemLibrary=STANDARD)

# Linear tetrahedral
elemType = ElemType(elemCode=DC3D4, elemLibrary=STANDARD)

# Quadratic tetrahedral
elemType = ElemType(elemCode=DC3D10, elemLibrary=STANDARD)

part.setElementType(regions=(part.cells,), elemTypes=(elemType,))
```

### 2D Elements (Shell/Plane)
```python
# Shell heat transfer
elemType = ElemType(elemCode=DS4, elemLibrary=STANDARD)

# Plane heat transfer
elemType = ElemType(elemCode=DC2D4, elemLibrary=STANDARD)
```

## Reading Results from ODB

```python
from odbAccess import openOdb

odb = openOdb('ThermalAnalysis.odb')
step = odb.steps['SteadyHeat']
frame = step.frames[-1]  # Last frame

# Temperature field
temp_field = frame.fieldOutputs['NT']
for value in temp_field.values:
    print(f"Node {value.nodeLabel}: T = {value.data}")

# Maximum temperature
max_temp = max(v.data for v in temp_field.values)
print(f"Max temperature: {max_temp}")

odb.close()
```
