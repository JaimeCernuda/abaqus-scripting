---
name: abaqus-dynamic-analysis
description: Complete workflow for dynamic analysis - explicit and implicit time integration for impact, crash, and transient problems.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
  - Skill
---

# Abaqus Dynamic Analysis Workflow

## When to Use This Skill

**USE for:**
- Impact and crash simulation (drop tests, collisions)
- Blast and explosion loading
- High-speed events (milliseconds)
- Wave propagation problems
- Transient vibration response
- Problems with severe nonlinearity (contact, plasticity)

**Do NOT use for:**
- Natural frequency extraction → use `/abaqus-modal-analysis`
- Static loads (constant) → use `/abaqus-static-analysis`
- Harmonic/sinusoidal response → use modal + steady-state dynamics
- Very long transients (minutes+) → consider implicit or quasi-static

## Key Decisions

### 1. Explicit vs Implicit?

| Factor | Explicit | Implicit |
|--------|----------|----------|
| Time scale | Short (µs to ms) | Longer (ms to s) |
| Step size | Very small (automatic) | User-controlled |
| Nonlinearity | Handles well | May need iterations |
| Memory | Lower | Higher |
| Contact | Natural handling | Needs care |
| Best for | Impact, crash | Vibration, long transient |

**Decision rule:**
- Event < 10ms with impact/contact → **Explicit**
- Event > 100ms without severe nonlinearity → **Implicit**
- In between → Either can work, explicit often easier

### 2. Time Period Selection

| Event Type | Typical Duration |
|------------|------------------|
| High-speed impact | 0.1-10 ms |
| Drop test | 1-100 ms |
| Blast loading | 1-50 ms |
| Seismic/vibration | 1-100 s |

### 3. Mass Scaling (Explicit Only)

| Option | Effect | When |
|--------|--------|------|
| None | True inertia | Very short events |
| At beginning | Scale once | Quasi-static explicit |
| Throughout | Continuous scaling | When inertia less important |

**Warning:** Mass scaling speeds up analysis but affects inertial response.

## Required Inputs

| Input | Required | Guidance |
|-------|----------|----------|
| Geometry | YES | Part(s) to analyze |
| Material + Density | YES | Density required for mass matrix |
| Time period | YES | Duration of event |
| Initial conditions | Often | Initial velocity, position |
| Loads/BCs | YES | Applied forces, constraints |

## Workflow Steps

1. **Geometry** (`/abaqus-geometry`) - Create parts
2. **Material with Density** (`/abaqus-material`) - E, ν, ρ required
3. **Mesh** (`/abaqus-mesh`) - Finer mesh = smaller explicit time step
4. **BCs** (`/abaqus-bc`) - Fixed supports
5. **Initial Conditions** (`/abaqus-field`) - Initial velocity
6. **Step** - ExplicitDynamicsStep or ImplicitDynamicsStep
7. **Run** (`/abaqus-job`) - Submit job
8. **Post-process** (`/abaqus-odb`) - Extract results

## Complete Explicit Impact Example

```python
# explicit_impact.py
from abaqus import *
from abaqusConstants import *
from caeModules import *

# ============= PARAMETERS =============
BLOCK_SIZE = 50.0  # mm
E = 210000.0       # MPa
NU = 0.3
DENSITY = 7.85e-9  # tonne/mm³ (REQUIRED!)
YIELD = 250.0      # MPa (plasticity)

INITIAL_VELOCITY = -5000.0  # mm/s downward
TIME_PERIOD = 0.001         # 1 ms

MESH_SIZE = 5.0

# ============= MODEL =============
model = mdb.Model(name='ExplicitImpact')
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']

# ============= GEOMETRY =============
part = model.Part(name='Block', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='Sketch', sheetSize=200.0)
sketch.rectangle(point1=(0, 0), point2=(BLOCK_SIZE, BLOCK_SIZE))
part.BaseSolidExtrude(sketch=sketch, depth=BLOCK_SIZE)

# ============= MATERIAL =============
material = model.Material(name='Steel')
material.Elastic(table=((E, NU),))
material.Plastic(table=((YIELD, 0.0), (YIELD*1.5, 0.2)))
material.Density(table=((DENSITY,),))  # REQUIRED for dynamics

model.HomogeneousSolidSection(name='Section', material='Steel')
part.SectionAssignment(region=part.Set(cells=part.cells, name='All'), sectionName='Section')

# ============= ASSEMBLY =============
assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
instance = assembly.Instance(name='Block-1', part=part, dependent=ON)

# ============= EXPLICIT STEP =============
model.ExplicitDynamicsStep(
    name='Impact',
    previous='Initial',
    timePeriod=TIME_PERIOD,
    massScaling=((SEMI_AUTOMATIC, MODEL, AT_BEGINNING, 0.0, 1e-06, BELOW_MIN, 0, 0, 0.0, 0.0, 0, None),)
)

model.FieldOutputRequest(
    name='F-Output',
    createStepName='Impact',
    variables=('S', 'U', 'V', 'A', 'PEEQ', 'STATUS'),
    numIntervals=100
)

# ============= BCs =============
bottom_face = instance.faces.findAt(((BLOCK_SIZE/2, BLOCK_SIZE/2, 0),))
assembly.Set(faces=bottom_face, name='Bottom')
model.EncastreBC(name='Fixed', createStepName='Initial', region=assembly.sets['Bottom'])

# ============= INITIAL VELOCITY =============
assembly.Set(cells=instance.cells, name='AllCells')
model.Velocity(
    name='InitialVelocity',
    createStepName='Initial',
    region=assembly.sets['AllCells'],
    velocity1=0.0, velocity2=0.0, velocity3=INITIAL_VELOCITY
)

# ============= MESH =============
part.seedPart(size=MESH_SIZE)
elemType = mesh.ElemType(elemCode=C3D8R, elemLibrary=EXPLICIT, hourglassControl=ENHANCED)
part.setElementType(regions=(part.cells,), elemTypes=(elemType,))
part.generateMesh()

# ============= RUN =============
mdb.saveAs('ExplicitImpact.cae')
job = mdb.Job(name='ExplicitImpact', model='ExplicitImpact')
job.submit()
job.waitForCompletion()
```

## Implicit Dynamic Example

```python
model.ImplicitDynamicsStep(
    name='Transient',
    previous='Initial',
    timePeriod=1.0,       # 1 second
    initialInc=0.001,
    maxNumInc=10000,
    minInc=1e-8,
    maxInc=0.01,
    nlgeom=ON,
    application=TRANSIENT_FIDELITY
)
```

## Energy Balance Check

For explicit analysis, verify energy conservation:
```python
model.HistoryOutputRequest(
    name='Energies',
    createStepName='Impact',
    variables=('ALLKE', 'ALLIE', 'ALLWK', 'ETOTAL'),
    frequency=1
)
```

**Energy check:** ETOTAL should remain approximately constant. Large changes indicate problems.

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Time increment too small" | Very small/distorted elements | Use mass scaling or coarsen mesh |
| "Energy balance error" | Hourglass or instability | Check hourglass energy, add control |
| "Analysis takes forever" (explicit) | Long time period | Consider implicit instead |
| "Convergence failure" (implicit) | Severe nonlinearity | Use explicit or smaller increments |

## Validation Checkpoints

- [ ] Density defined in material
- [ ] Time period appropriate for event
- [ ] Initial conditions applied
- [ ] Output frequency captures behavior (100+ frames typical)
- [ ] Energy balance acceptable (check ETOTAL)
- [ ] Results physically reasonable

## API Reference

For step settings: `/abaqus-step`
For initial conditions: `/abaqus-field`
For results: `/abaqus-odb`
