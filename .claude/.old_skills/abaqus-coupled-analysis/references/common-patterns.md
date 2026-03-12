# Common Coupled Analysis Patterns

## Fully Coupled (Simultaneous Thermal-Mechanical)

Use when deformation affects temperature (friction heating, plastic work).

```python
# Create coupled step
model.CoupledTempDisplacementStep(
    name='Coupled',
    previous='Initial',
    response=STEADY_STATE
)

# Apply both thermal and mechanical loads in same step
model.TemperatureBC(name='Hot', createStepName='Coupled',
                    region=hotRegion, magnitude=200.0)
model.ConcentratedForce(name='Force', createStepName='Coupled',
                        region=forceRegion, cf1=1000.0)

# Use coupled elements
elemType = mesh.ElemType(elemCode=C3D8T, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType,))
```

## Sequential Coupling (One-Way: Thermal to Structural)

Use when only temperature affects stress (no feedback to thermal).

### Pattern 1: Separate Models

```python
# === THERMAL MODEL ===
thermal_model = mdb.Model(name='ThermalOnly')
# ... geometry, mesh with DC3D8 elements
thermal_model.HeatTransferStep(name='Heat', previous='Initial',
                                response=TRANSIENT, timePeriod=10.0)
# ... BCs, run job

# === STRUCTURAL MODEL ===
struct_model = mdb.Model(name='StructuralOnly')
# ... same geometry, mesh with C3D8R elements
struct_model.StaticStep(name='ThermalStress', previous='Initial')

# Import temperature from thermal ODB
struct_model.Temperature(
    name='Temp',
    createStepName='Initial',
    region=allNodes,
    distributionType=FROM_FILE,
    fileName='ThermalOnly.odb',
    step='Heat',
    frame=-1
)
```

### Pattern 2: Single Model with Sequential Steps

```python
# First do thermal analysis
model.HeatTransferStep(name='ThermalStep', previous='Initial',
                        response=TRANSIENT, timePeriod=10.0)

# Then structural (predefined field carries forward)
model.StaticStep(name='StructuralStep', previous='ThermalStep')
```

## Thermal Expansion Only (No External Mechanical Loads)

Temperature change causes stress due to constraints.

```python
# Standard static step (not coupled)
model.StaticStep(name='Expand', previous='Initial')

# Material with expansion coefficient
material.Elastic(table=((210000.0, 0.3),))
material.Expansion(table=((12e-6,),), zero=25.0)  # Reference: 25C

# Initial temperature at reference
model.Temperature(name='InitialT', createStepName='Initial',
                   region=region, magnitude=25.0)

# Apply temperature change as predefined field
model.Temperature(name='DeltaT', createStepName='Expand',
                   region=region, magnitude=125.0)  # 100C above reference

# Constraints cause thermal stress (free expansion = no stress)
model.EncastreBC(name='Fixed', createStepName='Initial',
                  region=fixedRegion)
```

## Transient Heating with Temperature Gradient

```python
model.CoupledTempDisplacementStep(
    name='Heating',
    previous='Initial',
    response=TRANSIENT,
    timePeriod=100.0,
    initialInc=0.1,
    deltmx=5.0  # Max 5 degree change per increment
)

# Hot end
model.TemperatureBC(name='HotEnd', createStepName='Heating',
                    region=hotFace, magnitude=300.0)

# Cold end (or convection)
model.TemperatureBC(name='ColdEnd', createStepName='Heating',
                    region=coldFace, magnitude=25.0)
```

## Thermal Shock Analysis

Rapid temperature change causing high stress.

```python
# Short time period for rapid change
model.CoupledTempDisplacementStep(
    name='Shock',
    previous='Initial',
    response=TRANSIENT,
    timePeriod=1.0,          # 1 second
    initialInc=0.001,        # Small initial increment
    minInc=1e-8,
    maxInc=0.01,
    deltmx=2.0               # Small temp change per increment
)

# Sudden temperature application
model.TemperatureBC(name='ShockTemp', createStepName='Shock',
                    region=surface, magnitude=500.0)
```

## Steady-State Operating Condition

```python
model.CoupledTempDisplacementStep(
    name='Operate',
    previous='Initial',
    response=STEADY_STATE,   # Time-independent
    timePeriod=1.0
)

# Operating temperature
model.TemperatureBC(name='Operating', createStepName='Operate',
                    region=region, magnitude=150.0)

# Convection to ambient
model.FilmCondition(name='Cooling', createStepName='Operate',
                    surface=outerSurface, filmCoeff=25.0,
                    sinkTemperature=25.0)
```

## Temperature-Dependent Material

```python
# Young's modulus decreases with temperature
material.Elastic(table=(
    (210000.0, 0.3, 20.0),
    (195000.0, 0.3, 200.0),
    (175000.0, 0.3, 400.0),
    (150000.0, 0.3, 600.0),
), temperatureDependency=ON)

# Expansion coefficient varies with temperature
material.Expansion(table=(
    (11.0e-6, 20.0),
    (12.5e-6, 200.0),
    (14.0e-6, 400.0),
    (15.0e-6, 600.0),
), temperatureDependency=ON, zero=20.0)

# Conductivity varies with temperature
material.Conductivity(table=(
    (50.0, 20.0),
    (48.0, 200.0),
    (45.0, 400.0),
), temperatureDependency=ON)
```

## Bi-Material Assembly (Different Expansion)

Two parts with different thermal expansion bonded together.

```python
# Material 1: Steel
steel = model.Material(name='Steel')
steel.Elastic(table=((210000.0, 0.3),))
steel.Expansion(table=((12e-6,),), zero=25.0)

# Material 2: Aluminum (higher expansion)
aluminum = model.Material(name='Aluminum')
aluminum.Elastic(table=((70000.0, 0.33),))
aluminum.Expansion(table=((23e-6,),), zero=25.0)

# Tie constraint between parts
model.Tie(name='Bond', main=surface1, secondary=surface2)
```

## Cyclic Thermal Loading

```python
# Use amplitude for cyclic temperature
model.TabularAmplitude(name='Cycle', data=(
    (0.0, 0.0),
    (1.0, 1.0),
    (2.0, 0.0),
    (3.0, 1.0),
    (4.0, 0.0),
))

model.CoupledTempDisplacementStep(
    name='Cycling',
    previous='Initial',
    response=TRANSIENT,
    timePeriod=4.0
)

model.TemperatureBC(name='CyclicTemp', createStepName='Cycling',
                    region=region, magnitude=200.0,
                    amplitude='Cycle')
```
