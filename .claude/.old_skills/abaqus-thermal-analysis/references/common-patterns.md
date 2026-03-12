# Common Thermal Analysis Patterns

## Steady-State with Fixed Temperatures

Classic conduction problem with known boundary temperatures.

```python
from abaqus import *
from abaqusConstants import *

model = mdb.Model(name='SteadyStateConduction')

# Step
model.HeatTransferStep(name='SS', previous='Initial', response=STEADY_STATE)

# Material (only conductivity needed)
material = model.Material(name='Steel')
material.Conductivity(table=((50.0,),))

# Boundary conditions
model.TemperatureBC(name='Hot', createStepName='SS',
                    region=assembly.sets['HotFace'], magnitude=100.0)
model.TemperatureBC(name='Cold', createStepName='SS',
                    region=assembly.sets['ColdFace'], magnitude=20.0)
```

## Transient Heating with Heat Source

Part heating up from a heat source over time.

```python
# Material (need all thermal properties for transient)
material = model.Material(name='Steel')
material.Conductivity(table=((50.0,),))       # mW/(mm·K)
material.SpecificHeat(table=((5.0e11,),))     # mJ/(tonne·K)
material.Density(table=((7.85e-9,),))         # tonne/mm³

# Step
model.HeatTransferStep(
    name='Heat',
    previous='Initial',
    response=TRANSIENT,
    timePeriod=100.0,
    initialInc=0.1,
    maxInc=10.0,
    deltmx=5.0  # Max temp change per increment
)

# Initial temperature
model.Temperature(name='InitTemp', createStepName='Initial',
                   region=assembly.sets['AllNodes'],
                   distributionType=UNIFORM, magnitudes=(20.0,))

# Heat input
model.SurfaceHeatFlux(name='HeatIn', createStepName='Heat',
                       region=assembly.surfaces['HeatedSurf'],
                       magnitude=1000.0)  # mW/mm²
```

## Convection Cooling

Natural or forced convection on surfaces.

```python
# Step
model.HeatTransferStep(name='Cool', previous='Initial', response=TRANSIENT,
                        timePeriod=300.0, initialInc=1.0, maxInc=30.0)

# Initial hot temperature
model.Temperature(name='InitTemp', createStepName='Initial',
                   region=assembly.sets['AllNodes'],
                   distributionType=UNIFORM, magnitudes=(150.0,))

# Convection on all exposed surfaces
model.FilmCondition(name='AirCool', createStepName='Cool',
                     region=assembly.surfaces['Exterior'],
                     filmCoeff=25.0,        # Natural convection in air
                     sinkTemperature=25.0)
```

### Typical Convection Coefficients

| Condition | h [mW/(mm²·K)] |
|-----------|----------------|
| Natural convection (air) | 5-25 |
| Forced convection (air) | 25-250 |
| Natural convection (water) | 100-1000 |
| Forced convection (water) | 500-10000 |

## Combined Convection and Radiation

High-temperature surface with both heat transfer modes.

```python
model.HeatTransferStep(name='Cooling', previous='Initial',
                        response=TRANSIENT, timePeriod=600.0)

# Convection
model.FilmCondition(name='Conv', createStepName='Cooling',
                     region=assembly.surfaces['HotSurf'],
                     filmCoeff=50.0, sinkTemperature=25.0)

# Radiation
model.RadiationToAmbient(name='Rad', createStepName='Cooling',
                          region=assembly.surfaces['HotSurf'],
                          emissivity=0.8,
                          ambientTemperature=25.0)
```

## Heat Sink Design

Analyzing a heat sink with base heating and fin cooling.

```python
# Step
model.HeatTransferStep(name='Steady', previous='Initial',
                        response=STEADY_STATE)

# Heat input at base
model.SurfaceHeatFlux(name='ChipHeat', createStepName='Steady',
                       region=assembly.surfaces['Base'],
                       magnitude=500.0)  # Power input

# Convection on fins
model.FilmCondition(name='FinCooling', createStepName='Steady',
                     region=assembly.surfaces['Fins'],
                     filmCoeff=100.0,
                     sinkTemperature=25.0)
```

## Initial Temperature Field

Setting non-uniform initial temperature.

```python
# Uniform initial temperature
model.Temperature(name='InitTemp', createStepName='Initial',
                   region=assembly.sets['AllNodes'],
                   distributionType=UNIFORM,
                   magnitudes=(100.0,))
```

### From Previous Analysis
```python
model.Temperature(name='InitTemp', createStepName='Initial',
                   region=assembly.sets['AllNodes'],
                   distributionType=FROM_FILE,
                   fileName='previous.odb',
                   step=1, increment=-1)  # Last increment
```

## Multi-Step Analysis

Heat up, then cool down.

```python
# Heat-up phase
model.HeatTransferStep(name='HeatUp', previous='Initial',
                        response=TRANSIENT, timePeriod=60.0)

# Cool-down phase
model.HeatTransferStep(name='CoolDown', previous='HeatUp',
                        response=TRANSIENT, timePeriod=300.0)

# Heat source active only during heat-up
model.SurfaceHeatFlux(name='Heater', createStepName='HeatUp',
                       region=assembly.surfaces['HeaterSurf'],
                       magnitude=1000.0)

# Deactivate heater in cool-down
model.loads['Heater'].deactivate('CoolDown')

# Convection active in both steps
model.FilmCondition(name='Cooling', createStepName='HeatUp',
                     region=assembly.surfaces['Exterior'],
                     filmCoeff=25.0, sinkTemperature=25.0)
```

## Temperature-Dependent Properties

Material properties that vary with temperature.

```python
material = model.Material(name='Steel')

# Conductivity: (k, T) pairs
material.Conductivity(table=(
    (53.0, 0.0),
    (50.0, 100.0),
    (45.0, 200.0),
    (40.0, 300.0),
), temperatureDependency=ON)

# Specific heat: (cp, T) pairs
material.SpecificHeat(table=(
    (4.5e11, 0.0),
    (5.0e11, 100.0),
    (5.5e11, 200.0),
    (6.0e11, 300.0),
), temperatureDependency=ON)
```

## Cyclic Thermal Loading

Repeated heating/cooling cycles using amplitude.

```python
# Define cyclic amplitude
model.PeriodicAmplitude(
    name='CyclicHeat',
    frequency=0.1,     # Hz (10s period)
    start=0.0,
    a_0=0.5,           # Mean
    data=((0.5, 0.0),) # (amplitude, phase) for cosine term
)

# Apply heat flux with amplitude
model.SurfaceHeatFlux(name='CyclicFlux', createStepName='Cycling',
                       region=assembly.surfaces['HeatedSurf'],
                       magnitude=1000.0,
                       amplitude='CyclicHeat')
```
