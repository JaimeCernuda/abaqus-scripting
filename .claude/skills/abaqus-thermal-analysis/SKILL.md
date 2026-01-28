---
name: abaqus-thermal-analysis
description: Complete workflow for heat transfer analysis - steady-state and transient thermal problems.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
  - Skill
---

# Abaqus Thermal Analysis Workflow

## When to Use This Skill

**USE for:**
- Steady-state temperature distribution
- Transient heat-up/cool-down analysis
- Convection and radiation problems
- Heat source/sink problems
- Determining temperature for subsequent thermal stress

**Do NOT use for:**
- Thermal stress (need both T and stress) → use `/abaqus-coupled-analysis`
- Just stress analysis → use `/abaqus-static-analysis`
- Temperature as initial condition only → use `/abaqus-field`

## Key Decisions

### 1. Steady-State vs Transient?

| Type | When | Key Parameter |
|------|------|---------------|
| Steady-state | Equilibrium temperature | response=STEADY_STATE |
| Transient | Temperature vs time | response=TRANSIENT |

**Decision rule:** Use steady-state unless you need temperature history or time-dependent behavior.

### 2. Boundary Condition Type

| Condition | Use Case | Abaqus Feature |
|-----------|----------|----------------|
| Fixed temperature | Known surface T | TemperatureBC |
| Heat flux | Known input power | SurfaceHeatFlux |
| Convection | Cooling/heating in air/fluid | FilmCondition |
| Radiation | High-temperature surfaces | RadiationToAmbient |
| Body heat | Internal heat generation | BodyHeatFlux |

### 3. Element Selection

| Element | Use |
|---------|-----|
| DC3D8 | Standard heat transfer hex |
| DC3D4 | Heat transfer tet |
| DC3D20 | High-accuracy hex |

**Note:** Heat transfer elements (DC*) are different from structural elements (C3D*).

## Required Inputs

| Input | Required | Guidance |
|-------|----------|----------|
| Geometry | YES | Part to analyze |
| Thermal conductivity (k) | YES | mW/(mm·K) in SI-mm |
| Density (ρ) | For transient | tonne/mm³ |
| Specific heat (cp) | For transient | mJ/(tonne·K) |
| Thermal BCs | YES | At least one T or q boundary |

## Material Properties (SI-mm Units)

| Material | k [mW/(mm·K)] | cp [mJ/(tonne·K)] | ρ [tonne/mm³] |
|----------|---------------|-------------------|---------------|
| Steel | 50 | 5.0e11 | 7.85e-9 |
| Aluminum | 167 | 9.0e11 | 2.70e-9 |
| Copper | 385 | 3.85e11 | 8.96e-9 |

## Steady-State Example

```python
from abaqus import *
from abaqusConstants import *
from caeModules import *

# ============= PARAMETERS =============
LENGTH = 100.0  # mm
WIDTH = 20.0
HEIGHT = 10.0

K = 50.0           # mW/(mm·K)
T_HOT = 100.0      # °C
T_COLD = 25.0      # °C
MESH_SIZE = 5.0

# ============= MODEL =============
model = mdb.Model(name='ThermalSteady')

# ============= GEOMETRY =============
part = model.Part(name='Bar', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='Sketch', sheetSize=200.0)
sketch.rectangle(point1=(0, 0), point2=(LENGTH, HEIGHT))
part.BaseSolidExtrude(sketch=sketch, depth=WIDTH)

# ============= MATERIAL =============
material = model.Material(name='Steel')
material.Conductivity(table=((K,),))
# Density/specific heat not needed for steady-state

model.HomogeneousSolidSection(name='Section', material='Steel')
part.SectionAssignment(region=part.Set(cells=part.cells, name='All'), sectionName='Section')

# ============= ASSEMBLY =============
assembly = model.rootAssembly
instance = assembly.Instance(name='Bar-1', part=part, dependent=ON)

# ============= HEAT TRANSFER STEP =============
model.HeatTransferStep(
    name='SteadyHeat',
    previous='Initial',
    response=STEADY_STATE
)

model.FieldOutputRequest(name='F-Output', createStepName='SteadyHeat',
                         variables=('NT', 'HFL', 'RFL'))

# ============= THERMAL BCs =============
hot_face = instance.faces.findAt(((0, HEIGHT/2, WIDTH/2),))
assembly.Set(faces=hot_face, name='HotEnd')
model.TemperatureBC(name='Hot', createStepName='SteadyHeat',
                    region=assembly.sets['HotEnd'], magnitude=T_HOT)

cold_face = instance.faces.findAt(((LENGTH, HEIGHT/2, WIDTH/2),))
assembly.Set(faces=cold_face, name='ColdEnd')
model.TemperatureBC(name='Cold', createStepName='SteadyHeat',
                    region=assembly.sets['ColdEnd'], magnitude=T_COLD)

# ============= MESH (Heat transfer elements) =============
part.seedPart(size=MESH_SIZE)
elemType = mesh.ElemType(elemCode=DC3D8, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType,))
part.generateMesh()

# ============= RUN =============
mdb.saveAs('ThermalSteady.cae')
job = mdb.Job(name='ThermalSteady', model='ThermalSteady')
job.submit()
job.waitForCompletion()
```

## Transient Example

```python
# Additional material properties needed
material.Conductivity(table=((K,),))
material.SpecificHeat(table=((CP,),))
material.Density(table=((DENSITY,),))

model.HeatTransferStep(
    name='TransientHeat',
    previous='Initial',
    response=TRANSIENT,
    timePeriod=100.0,     # seconds
    initialInc=0.1,
    minInc=1e-6,
    maxInc=10.0,
    deltmx=5.0            # Max temperature change per increment
)
```

## Thermal Loads

### Convection
```python
model.FilmCondition(
    name='Convection',
    createStepName='SteadyHeat',
    region=assembly.surfaces['ExposedSurf'],
    filmCoeff=10.0,        # mW/(mm²·K)
    sinkTemperature=25.0   # Ambient
)
```

### Radiation
```python
model.RadiationToAmbient(
    name='Radiation',
    createStepName='SteadyHeat',
    region=assembly.surfaces['HotSurf'],
    emissivity=0.8,
    ambientTemperature=25.0
)
```

### Heat Flux
```python
model.SurfaceHeatFlux(
    name='HeatIn',
    createStepName='SteadyHeat',
    region=assembly.surfaces['HeatedSurf'],
    magnitude=100.0  # mW/mm²
)
```

## Output Variables

| Variable | Description |
|----------|-------------|
| NT | Nodal temperature |
| HFL | Heat flux vector |
| RFL | Reaction heat flux |
| HFLM | Heat flux magnitude |

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Temperature oscillation" | Large increments in transient | Reduce maxInc or deltmx |
| "Non-physical temperature" | Unit mismatch | Verify k, cp, ρ units |
| "No heat flow" | Missing BC or bad region | Check boundary conditions |
| "Negative temperature" | Bad setup or initial condition | Review model setup |

## Next Steps

After thermal analysis:
- For thermal stress: Use `/abaqus-coupled-analysis` or
- Import temperature to structural: Use `/abaqus-field` to read from ODB

## API Reference

For material properties: `/abaqus-material`
For step settings: `/abaqus-step`
