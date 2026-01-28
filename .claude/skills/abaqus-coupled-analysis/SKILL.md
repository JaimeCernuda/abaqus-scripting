---
name: abaqus-coupled-analysis
description: Complete workflow for coupled thermomechanical analysis - combined thermal and structural effects.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
  - Skill
---

# Abaqus Coupled Thermomechanical Analysis Workflow

## When to Use This Skill

**USE for:**
- Thermal stress analysis (expansion/contraction)
- High-temperature structural components
- Process simulation (welding, casting)
- Components with thermal gradients
- Problems where temperature affects mechanical response

**Do NOT use for:**
- Heat transfer only (no stress needed) → use `/abaqus-thermal-analysis`
- Structural only (no thermal) → use `/abaqus-static-analysis`
- Very weak coupling (can do sequential instead)

## Key Decisions

### 1. Fully Coupled vs Sequential?

| Approach | Description | When |
|----------|-------------|------|
| Fully Coupled | Solve thermal + mechanical simultaneously | Strong interaction |
| Sequential | Thermal first, then mechanical | One-way influence |

**Decision rule:**
- Deformation affects temperature (friction, plastic heating) → Fully coupled
- Only temperature affects stress (no feedback) → Sequential is simpler

### 2. Element Selection

| Element | Description |
|---------|-------------|
| C3D8T | 8-node coupled temp-displacement |
| C3D8RT | Reduced integration coupled |
| C3D10MT | 10-node modified tet |

**Note:** Coupled elements (C3D*T) combine thermal and structural DOFs.

### 3. Thermal Expansion Definition

| Parameter | Description |
|-----------|-------------|
| α (alpha) | Coefficient of thermal expansion |
| T_ref | Reference temperature (zero strain) |

Thermal strain: ε_th = α × (T - T_ref)

## Required Inputs

| Input | Required | Guidance |
|-------|----------|----------|
| Geometry | YES | Part to analyze |
| Elastic properties | YES | E, ν |
| Thermal properties | YES | k, (cp, ρ for transient) |
| Expansion coefficient | YES | α and T_ref |
| Thermal BCs | YES | Temperature or heat flux |
| Mechanical BCs | YES | Supports (prevent rigid body) |

## Material Properties (SI-mm)

| Property | Symbol | Typical Steel Value |
|----------|--------|---------------------|
| Young's modulus | E | 210000 MPa |
| Poisson's ratio | ν | 0.3 |
| Density | ρ | 7.85e-9 tonne/mm³ |
| Conductivity | k | 50 mW/(mm·K) |
| Specific heat | cp | 5.0e11 mJ/(tonne·K) |
| Expansion | α | 12e-6 /K |

## Fully Coupled Example

```python
from abaqus import *
from abaqusConstants import *
from caeModules import *

# ============= PARAMETERS =============
LENGTH = 100.0
WIDTH = 20.0
HEIGHT = 10.0

E = 210000.0         # MPa
NU = 0.3
DENSITY = 7.85e-9    # tonne/mm³
K = 50.0             # mW/(mm·K)
CP = 5.0e11          # mJ/(tonne·K)
ALPHA = 12e-6        # 1/K

T_REF = 25.0         # Reference temperature
T_HOT = 200.0        # Applied temperature
MESH_SIZE = 5.0

# ============= MODEL =============
model = mdb.Model(name='CoupledThermo')

# ============= GEOMETRY =============
part = model.Part(name='Bar', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='Sketch', sheetSize=200.0)
sketch.rectangle(point1=(0, 0), point2=(LENGTH, HEIGHT))
part.BaseSolidExtrude(sketch=sketch, depth=WIDTH)

# ============= MATERIAL (ALL PROPERTIES) =============
material = model.Material(name='Steel')
material.Elastic(table=((E, NU),))
material.Density(table=((DENSITY,),))
material.Conductivity(table=((K,),))
material.SpecificHeat(table=((CP,),))
material.Expansion(table=((ALPHA,),), zero=T_REF)

model.HomogeneousSolidSection(name='Section', material='Steel')
part.SectionAssignment(region=part.Set(cells=part.cells, name='All'), sectionName='Section')

# ============= ASSEMBLY =============
assembly = model.rootAssembly
instance = assembly.Instance(name='Bar-1', part=part, dependent=ON)

# ============= COUPLED STEP =============
model.CoupledTempDisplacementStep(
    name='Heating',
    previous='Initial',
    response=TRANSIENT,
    timePeriod=10.0,
    initialInc=0.1,
    minInc=1e-6,
    maxInc=1.0,
    deltmx=10.0,
    nlgeom=ON
)

model.FieldOutputRequest(name='F-Output', createStepName='Heating',
                         variables=('S', 'U', 'NT', 'THE'))

# ============= INITIAL TEMPERATURE =============
assembly.Set(cells=instance.cells, name='AllCells')
model.Temperature(
    name='InitialTemp',
    createStepName='Initial',
    region=assembly.sets['AllCells'],
    magnitude=T_REF
)

# ============= MECHANICAL BCs =============
fixed_face = instance.faces.findAt(((0, HEIGHT/2, WIDTH/2),))
assembly.Set(faces=fixed_face, name='Fixed')
model.EncastreBC(name='Fixed', createStepName='Initial', region=assembly.sets['Fixed'])

# ============= THERMAL BCs =============
hot_face = instance.faces.findAt(((LENGTH, HEIGHT/2, WIDTH/2),))
assembly.Set(faces=hot_face, name='HotEnd')
model.TemperatureBC(name='Heating', createStepName='Heating',
                    region=assembly.sets['HotEnd'], magnitude=T_HOT)

# ============= MESH (COUPLED ELEMENTS) =============
part.seedPart(size=MESH_SIZE)
elemType = mesh.ElemType(elemCode=C3D8T, elemLibrary=STANDARD)  # Note: C3D8T
part.setElementType(regions=(part.cells,), elemTypes=(elemType,))
part.generateMesh()

# ============= RUN =============
mdb.saveAs('CoupledThermo.cae')
job = mdb.Job(name='CoupledThermo', model='CoupledThermo')
job.submit()
job.waitForCompletion()
```

## Sequential Coupling Alternative

1. Run thermal analysis separately:
```python
model.HeatTransferStep(name='Thermal', response=TRANSIENT, ...)
```

2. In structural model, import temperature:
```python
model.Temperature(
    name='TempFromThermal',
    createStepName='StructuralStep',
    region=region,
    distributionType=FROM_FILE,
    fileName='thermal_analysis.odb',
    beginStep=1,
    endIncrement=LAST_INCREMENT
)
```

## Output Variables

| Variable | Description |
|----------|-------------|
| S | Mechanical stress |
| U | Displacement |
| NT | Temperature |
| THE | Thermal strain |
| E | Total strain |
| EE | Elastic strain |

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Large thermal strain" | Wrong α units | α should be ~1e-5/K for metals |
| "Zero thermal stress" | Missing expansion | Add material.Expansion() |
| "Non-convergence" | Large temp change | Reduce increments or deltmx |
| "Wrong element type" | Using C3D8 not C3D8T | Use coupled elements |

## Validation Checks

- [ ] Expansion coefficient defined with correct T_ref
- [ ] Initial temperature matches T_ref (for zero initial stress)
- [ ] Both mechanical and thermal BCs applied
- [ ] Using coupled elements (C3D*T)
- [ ] Thermal strain appears in results (THE)

## API Reference

For material setup: `/abaqus-material`
For step settings: `/abaqus-step`
