---
name: abaqus-shape-optimization
description: Workflow for shape optimization - optimize surface shapes to minimize stress concentrations or improve performance.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
  - Skill
---

# Abaqus Shape Optimization Workflow

## When to Use This Skill

**USE for:**
- Reducing stress concentrations at fillets/notches
- Optimizing surface contours for uniform stress
- Improving fatigue life through shape changes
- Weight reduction with smooth geometry changes
- Designs that must be traditionally manufactured

**Do NOT use for:**
- Adding/removing material (holes, organic forms) → use `/abaqus-topology-optimization`
- Complete redesign of part → topology optimization first
- Quick lightweight concepts → topology optimization

## Key Decisions

### 1. Shape vs Topology?

| Aspect | Shape Optimization | Topology Optimization |
|--------|-------------------|----------------------|
| Changes | Surface positions | Material presence |
| Result | Smooth surfaces | Holes, organic forms |
| Manufacturing | Traditional machining | Often needs AM/casting |
| Design freedom | Limited | High |
| Use case | Refine existing design | Conceptual design |

### 2. Objective Selection

| Objective | Effect |
|-----------|--------|
| Minimize max stress | Reduce stress concentrations |
| Minimize stress variation | Uniform stress distribution |
| Maximize stiffness | Minimize compliance |
| Target stress | Match specific stress value |

### 3. Design Region

Only select surfaces that:
- Can be modified in manufacturing
- Are not functional interfaces
- Don't have attached features

## Required Inputs

| Input | Required | Guidance |
|-------|----------|----------|
| Geometry | YES | Part with stress concentrations |
| Design surfaces | YES | Which surfaces can move |
| Movement limits | YES | Max growth/shrink (mm) |
| Objective | YES | What to minimize/maximize |
| Constraints | Optional | Volume, displacement limits |

## Workflow Steps

1. **Identify problem** - Run static analysis, find stress concentration
2. **Define design region** - Select surfaces to optimize
3. **Set movement limits** - How much can surfaces move
4. **Configure optimization** - Objective, constraints
5. **Run optimization** - Submit process
6. **Validate result** - Compare before/after stress

## Shape Optimization Example

```python
from abaqus import *
from abaqusConstants import *
from caeModules import *

# ============= PARAMETERS =============
LENGTH = 100.0
HEIGHT = 50.0
THICKNESS = 10.0

E = 210000.0
NU = 0.3
MESH_SIZE = 3.0

MAX_SHAPE_CHANGE = 5.0  # mm

# ============= MODEL =============
model = mdb.Model(name='ShapeOpt')

# ============= GEOMETRY (L-bracket) =============
part = model.Part(name='Bracket', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='Sketch', sheetSize=200.0)

# L-shape profile with sharp corner (stress concentration)
sketch.Line(point1=(0, 0), point2=(LENGTH, 0))
sketch.Line(point1=(LENGTH, 0), point2=(LENGTH, HEIGHT/2))
sketch.Line(point1=(LENGTH, HEIGHT/2), point2=(LENGTH/3, HEIGHT/2))
sketch.Line(point1=(LENGTH/3, HEIGHT/2), point2=(LENGTH/3, HEIGHT))
sketch.Line(point1=(LENGTH/3, HEIGHT), point2=(0, HEIGHT))
sketch.Line(point1=(0, HEIGHT), point2=(0, 0))

part.BaseSolidExtrude(sketch=sketch, depth=THICKNESS)

# ============= MATERIAL =============
material = model.Material(name='Steel')
material.Elastic(table=((E, NU),))
material.Density(table=((7.85e-9,),))

model.HomogeneousSolidSection(name='Section', material='Steel')
part.SectionAssignment(region=part.Set(cells=part.cells, name='All'), sectionName='Section')

# ============= ASSEMBLY =============
assembly = model.rootAssembly
instance = assembly.Instance(name='Bracket-1', part=part, dependent=ON)

# ============= STEP =============
model.StaticStep(name='Load', previous='Initial')
model.FieldOutputRequest(name='F-Output', createStepName='Load', variables=('S', 'U'))

# ============= BCs AND LOADS =============
bottom = instance.faces.findAt(((LENGTH/2, 0, THICKNESS/2),))
assembly.Set(faces=bottom, name='Fixed')
model.EncastreBC(name='Fixed', createStepName='Initial', region=assembly.sets['Fixed'])

top = instance.faces.findAt(((LENGTH/6, HEIGHT, THICKNESS/2),))
assembly.Surface(side1Faces=top, name='LoadSurf')
model.Pressure(name='Load', createStepName='Load',
               region=assembly.surfaces['LoadSurf'], magnitude=10.0)

# ============= MESH =============
part.seedPart(size=MESH_SIZE)
elemType = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType,))
part.generateMesh()

# ============= SHAPE OPTIMIZATION =============
# Create shape task
model.ShapeTask(name='ShapeTask', region=MODEL)

# Design responses
task = model.optimizationTasks['ShapeTask']

task.SingleTermDesignResponse(
    name='max_stress',
    region=MODEL,
    identifier=STRESS,
    stressComponent=MISES,
    operation=MAXIMUM,
    stepOptions=LAST_STEP
)

task.SingleTermDesignResponse(
    name='volume',
    region=MODEL,
    identifier=VOLUME
)

# Objective: minimize maximum stress
task.ObjectiveFunction(
    name='MinStress',
    objectives=((task.designResponses['max_stress'], MINIMIZE_MAXIMUM, 1.0, 0.0),)
)

# Constraint: don't increase volume
task.OptimizationConstraint(
    name='VolumeLimit',
    designResponse='volume',
    restrictionMethod=RELATIVE_LESS_THAN_EQUAL,
    restrictionValue=1.0
)

# Define design surfaces (inner corner area)
inner_faces = instance.faces.getByBoundingBox(
    xMin=LENGTH/3-15, yMin=HEIGHT/2-15, zMin=0,
    xMax=LENGTH/3+15, yMax=HEIGHT/2+15, zMax=THICKNESS
)
assembly.Set(faces=inner_faces, name='DesignSurfaces')

# Shape design variables
task.designVariables = (
    ('DesignSurfaces', MAX_SHAPE_CHANGE, -MAX_SHAPE_CHANGE),
)

# ============= OPTIMIZATION PROCESS =============
opt = mdb.OptimizationProcess(
    name='ShapeOptimization',
    model='ShapeOpt',
    task='ShapeTask',
    maxDesignCycle=30
)

# ============= SAVE =============
mdb.saveAs('ShapeOptimization.cae')
print("Shape optimization ready. Run: opt.submit()")
```

## Design Variable Definition

```python
# (region_name, max_growth, max_shrink)
task.designVariables = (
    ('FilletSurfaces', 5.0, -5.0),  # ±5mm movement
    ('CornerSurfaces', 3.0, -3.0),  # ±3mm movement
)
```

## Geometric Restrictions

```python
# Keep certain surfaces fixed
task.GeometricRestriction(
    name='FixedSurf',
    surfaces=fixed_surfaces,
    movement=FIXED
)

# Maintain planar surface
task.GeometricRestriction(
    name='StayPlanar',
    surfaces=planar_surfaces,
    movement=PLANAR
)

# Mesh quality during shape change
task.GeometricRestriction(
    name='MeshQuality',
    meshQualityTechnique=LAPLACIAN_SMOOTHING
)
```

## Post-Processing

After optimization:
1. Compare initial vs optimized stress
2. Export modified geometry
3. Run final validation FEA
4. Check manufacturability

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Mesh distortion" | Too much shape change | Reduce movement limits |
| "No improvement" | Wrong design surfaces | Check surface selection |
| "Convergence failure" | Aggressive optimization | Smaller steps, add smoothing |

## Validation Checklist

- [ ] Initial analysis shows stress concentration
- [ ] Design surfaces selected correctly
- [ ] Movement limits are reasonable
- [ ] Constraint prevents volume increase
- [ ] Final stress is lower than initial

## API Reference

For optimization setup: `/abaqus-optimization`
For static analysis: `/abaqus-static-analysis`
