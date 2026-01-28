---
name: abaqus-contact-analysis
description: Complete workflow for contact analysis - surface-to-surface contact, friction, and multi-body problems.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
  - Skill
---

# Abaqus Contact Analysis Workflow

## When to Use This Skill

**USE for:**
- Bolted/clamped joint analysis
- Press fits and interference fits
- Bearing and gear contact
- Impact between bodies
- Assembly simulation
- Any problem where surfaces touch

**Do NOT use for:**
- Single-body analysis with no contact → use `/abaqus-static-analysis`
- Permanent connections → use tie constraint via `/abaqus-interaction`
- Just defining contact properties → use `/abaqus-interaction`

## Key Decisions

### 1. Contact Formulation

| Formulation | When to Use |
|-------------|-------------|
| Surface-to-surface | General contact (recommended) |
| Node-to-surface | Legacy, special cases |
| General contact | Many bodies, automatic detection |
| Self-contact | Folding, buckling |

### 2. Master vs Slave Selection

| Role | Should Be |
|------|-----------|
| Master | Stiffer, coarser mesh |
| Slave | Softer, finer mesh |

**Rule:** Slave surface nodes cannot penetrate master surface.

### 3. Contact Behavior

| Type | Description | When |
|------|-------------|------|
| Hard contact | No penetration | Most cases |
| Soft contact | Pressure-overclosure | Rubber, foam |
| Frictionless | No tangential resistance | Lubricated |
| Friction | Coulomb friction | Dry contact |
| Tied | No separation or slip | Bonded joint |

### 4. Friction Coefficients

| Interface | μ |
|-----------|---|
| Frictionless | 0.0 |
| Lubricated steel | 0.1-0.2 |
| Dry steel | 0.3-0.5 |
| Rubber on metal | 0.5-0.8 |

## Required Inputs

| Input | Required | Guidance |
|-------|----------|----------|
| Parts/geometry | YES | Separate parts that contact |
| Contact surfaces | YES | Which surfaces touch |
| Contact property | YES | Normal + tangential behavior |
| Friction (if any) | Depends | Coefficient value |
| Initial gap | Check | May need adjustment |

## Workflow Steps

1. **Geometry** - Create separate parts
2. **Assembly** - Position with appropriate gap/interference
3. **Contact surfaces** - Define master and slave
4. **Contact property** - Normal and tangential behavior
5. **Contact interaction** - Link surfaces with property
6. **Step** - Nonlinear static (nlgeom=ON usually needed)
7. **Run and check** - Verify contact established

## Complete Contact Example

```python
from abaqus import *
from abaqusConstants import *
from caeModules import *

# ============= PARAMETERS =============
BLOCK_SIZE = 50.0
PLATE_LENGTH = 150.0
PLATE_WIDTH = 100.0
PLATE_THICK = 10.0
GAP = 0.5  # Initial gap

E = 210000.0
NU = 0.3
DENSITY = 7.85e-9
FRICTION = 0.3
MESH_SIZE = 5.0

# ============= MODEL =============
model = mdb.Model(name='ContactAnalysis')

# ============= GEOMETRY (Two Parts) =============
# Block
block = model.Part(name='Block', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch1 = model.ConstrainedSketch(name='BlockSketch', sheetSize=200.0)
sketch1.rectangle(point1=(0, 0), point2=(BLOCK_SIZE, BLOCK_SIZE))
block.BaseSolidExtrude(sketch=sketch1, depth=BLOCK_SIZE)

# Plate
plate = model.Part(name='Plate', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch2 = model.ConstrainedSketch(name='PlateSketch', sheetSize=300.0)
sketch2.rectangle(point1=(0, 0), point2=(PLATE_LENGTH, PLATE_WIDTH))
plate.BaseSolidExtrude(sketch=sketch2, depth=PLATE_THICK)

# ============= MATERIAL =============
material = model.Material(name='Steel')
material.Elastic(table=((E, NU),))
material.Density(table=((DENSITY,),))

model.HomogeneousSolidSection(name='Section', material='Steel')
block.SectionAssignment(region=block.Set(cells=block.cells, name='All'), sectionName='Section')
plate.SectionAssignment(region=plate.Set(cells=plate.cells, name='All'), sectionName='Section')

# ============= ASSEMBLY =============
assembly = model.rootAssembly

plateInst = assembly.Instance(name='Plate-1', part=plate, dependent=ON)
blockInst = assembly.Instance(name='Block-1', part=block, dependent=ON)

# Position block above plate with gap
dx = (PLATE_LENGTH - BLOCK_SIZE) / 2
dy = (PLATE_WIDTH - BLOCK_SIZE) / 2
dz = PLATE_THICK + GAP
assembly.translate(instanceList=('Block-1',), vector=(dx, dy, dz))

# ============= CONTACT SURFACES =============
# Slave: block bottom
block_bottom = blockInst.faces.findAt(((dx + BLOCK_SIZE/2, dy + BLOCK_SIZE/2, PLATE_THICK + GAP),))
assembly.Surface(side1Faces=block_bottom, name='BlockBottom')

# Master: plate top
plate_top = plateInst.faces.findAt(((PLATE_LENGTH/2, PLATE_WIDTH/2, PLATE_THICK),))
assembly.Surface(side1Faces=plate_top, name='PlateTop')

# ============= CONTACT PROPERTY =============
model.ContactProperty('ContactProp')
model.interactionProperties['ContactProp'].TangentialBehavior(
    formulation=PENALTY,
    table=((FRICTION,),)
)
model.interactionProperties['ContactProp'].NormalBehavior(
    pressureOverclosure=HARD,
    allowSeparation=ON
)

# ============= CONTACT INTERACTION =============
model.SurfaceToSurfaceContactStd(
    name='Contact-1',
    createStepName='Initial',
    master=assembly.surfaces['PlateTop'],
    slave=assembly.surfaces['BlockBottom'],
    sliding=FINITE,
    interactionProperty='ContactProp'
)

# ============= STEP (Nonlinear) =============
model.StaticStep(
    name='Load',
    previous='Initial',
    nlgeom=ON,
    initialInc=0.1,
    minInc=1e-8,
    maxNumInc=100
)

model.FieldOutputRequest(name='F-Output', createStepName='Load',
                         variables=('S', 'U', 'CSTRESS', 'CDISP'))

# ============= BCs AND LOADS =============
# Fix plate bottom
plate_bottom = plateInst.faces.findAt(((PLATE_LENGTH/2, PLATE_WIDTH/2, 0),))
assembly.Set(faces=plate_bottom, name='PlateFixed')
model.EncastreBC(name='Fixed', createStepName='Initial', region=assembly.sets['PlateFixed'])

# Pressure on block top
block_top = blockInst.faces.findAt(((dx + BLOCK_SIZE/2, dy + BLOCK_SIZE/2, PLATE_THICK + GAP + BLOCK_SIZE),))
assembly.Surface(side1Faces=block_top, name='BlockTop')
model.Pressure(name='PushDown', createStepName='Load',
               region=assembly.surfaces['BlockTop'], magnitude=10.0)

# ============= MESH =============
block.seedPart(size=MESH_SIZE)
plate.seedPart(size=MESH_SIZE)
elemType = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
block.setElementType(regions=(block.cells,), elemTypes=(elemType,))
plate.setElementType(regions=(plate.cells,), elemTypes=(elemType,))
block.generateMesh()
plate.generateMesh()

# ============= RUN =============
mdb.saveAs('ContactAnalysis.cae')
job = mdb.Job(name='ContactAnalysis', model='ContactAnalysis')
job.submit()
job.waitForCompletion()
```

## Contact Outputs

| Variable | Description |
|----------|-------------|
| CSTRESS | Contact stress (CPRESS, CSHEAR) |
| CDISP | Contact displacement |
| COPEN | Opening distance |
| CSLIP | Accumulated slip |

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Severe discontinuity" | Contact chattering | Add stabilization, smaller increments |
| "Too much penetration" | Wrong master/slave | Swap roles, refine slave mesh |
| "Contact not detected" | Surfaces too far | Use adjust=ON or reduce gap |
| "Convergence failure" | Difficult nonlinearity | Smaller increments, check setup |

## Validation

- [ ] Master/slave assigned correctly (stiffer = master)
- [ ] Contact property defined (normal + tangential)
- [ ] nlgeom=ON in step (usually needed)
- [ ] Contact outputs requested (CSTRESS, CDISP)
- [ ] Results show expected contact area

## API Reference

For contact details: `/abaqus-interaction`
