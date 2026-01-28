---
name: abaqus-topology-optimization
description: Complete workflow for topology optimization using Tosca - from design space definition through optimized geometry export. Use to minimize weight while maintaining stiffness. Handles design responses, objectives, constraints, frozen regions, and manufacturing restrictions. Requires full Abaqus license with Tosca module (not available in Learning Edition).
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
  - Skill
---

# Abaqus Topology Optimization Workflow

## When to Use This Skill

**USE for:**
- Minimize weight while maintaining stiffness
- Maximize stiffness for given weight budget
- Generate organic, efficient load-carrying structures
- Conceptual design exploration
- Lightweighting existing designs

**Do NOT use for:**
- Shape optimization (surface changes only) → use `/abaqus-shape-optimization`
- Size optimization (thickness, dimensions) → manual or scripted parametric
- Frequency-constrained optimization → combine with modal (advanced)
- Learning Edition users → Tosca requires full license

**Prerequisites:**
- Full Abaqus license with Tosca module
- Clear definition of design space (where material can exist)
- Known load cases and boundary conditions

## Key Decisions

### 1. Volume Fraction Target

| Volume Fraction | Result | When to Use |
|-----------------|--------|-------------|
| 20-30% | Aggressive lightweighting | Weight-critical (aerospace) |
| 30-40% | Balanced | General structural |
| 40-50% | Conservative | Safety-critical, fatigue |

**Rule of thumb:** Start at 30%, adjust based on stress/displacement results.

### 2. Objective Function

| Objective | Description | When |
|-----------|-------------|------|
| Min compliance (max stiffness) | Minimize strain energy | Most common |
| Min weight with stress constraint | Minimize volume | Stress-limited designs |
| Max frequency | Raise natural frequency | Vibration avoidance |

**Default:** Minimize compliance (maximize stiffness) with volume constraint.

### 3. Manufacturing Constraints

| Constraint | Effect | When to Use |
|------------|--------|-------------|
| Minimum member size | Prevents thin features | Always (3-5mm typical) |
| Maximum member size | Prevents thick blobs | Casting, heat treatment |
| Draw direction | Enables mold extraction | Casting, molding |
| Symmetry plane | Mirror geometry | Balanced loads, aesthetics |
| Overhang angle | Supports for AM | Additive manufacturing |

### 4. Mesh Size for TO

| Element Size | Design Freedom | Compute Time |
|--------------|----------------|--------------|
| 1-2mm | Maximum | Very long |
| 2-4mm | High | Moderate |
| 4-6mm | Medium | Fast |

**Guideline:** At least 3 elements across expected minimum member thickness.

## Required Inputs

### CRITICAL (Must Ask)

| Input | What to Ask |
|-------|-------------|
| Design space | "What is the bounding volume where material can exist?" |
| Frozen regions | "Which areas must remain solid? (BC/load attachment)" |
| Volume fraction | "What percentage of material should remain? (20-50%)" |
| Loads | "What loads act on the structure?" |
| BCs | "Where is the structure supported/mounted?" |

### WITH DEFAULTS

| Input | Default | When to Change |
|-------|---------|----------------|
| Objective | Min compliance | If stress/frequency is primary concern |
| Min member size | 3mm | Adjust for manufacturing process |
| Material | Steel | If different material specified |
| Max iterations | 50 | Increase if not converging |

## Workflow Steps

### Phase 1: Setup Base Model
```
/abaqus-geometry → Design space with partitions for frozen regions
/abaqus-material → Elastic properties + density (required!)
/abaqus-mesh → Fine mesh (2-5mm typical)
/abaqus-bc → Fixed supports (these regions become frozen)
/abaqus-load → Applied forces (these regions become frozen)
/abaqus-step → Static step for stiffness optimization
```

### Phase 2: Configure Optimization
```
/abaqus-optimization → Task, responses, objectives, constraints
```

1. Create TopologyTask
2. Define design responses (volume, strain energy)
3. Set objective function (minimize compliance)
4. Add constraints (volume ≤ target)
5. Define frozen regions (BC and load areas)
6. Add manufacturing constraints (min member size)

### Phase 3: Run and Post-Process
```
/abaqus-job → Submit OptimizationProcess
/abaqus-odb → View density distribution
/abaqus-export → STL export at density threshold
```

## Validation Checkpoints

| Stage | Check |
|-------|-------|
| Base model | Static analysis runs, results sensible |
| Optimization setup | No errors in task definition |
| After iteration 5 | Objective decreasing, no disconnection |
| Convergence | Objective stable (< 0.1% change) |
| Final design | Load path intact, no floating regions |

## Complete Script Template

```python
# topology_optimization.py
# Run with: abaqus cae noGUI=topology_optimization.py
# NOTE: Requires full Abaqus license with Tosca

from abaqus import *
from abaqusConstants import *
from caeModules import *

# ============= PARAMETERS =============
LENGTH = 100.0      # Design space length (mm)
WIDTH = 40.0        # Design space width (mm)
HEIGHT = 20.0       # Design space height (mm)
FROZEN_SIZE = 10.0  # Frozen region at each end (mm)

E = 210000.0        # Young's modulus (MPa)
NU = 0.3
DENSITY = 7.85e-9   # tonne/mm³ (REQUIRED for TO)

VOLUME_FRACTION = 0.30   # Target: 30% material
MIN_MEMBER_SIZE = 3.0    # Minimum feature size (mm)
MAX_ITERATIONS = 50
MESH_SIZE = 2.5          # Fine mesh for TO

FORCE = 1000.0      # Applied force (N)

# ============= MODEL =============
model = mdb.Model(name='TopologyOpt')
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']

# ============= GEOMETRY =============
part = model.Part(name='DesignSpace', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='Sketch', sheetSize=200.0)
sketch.rectangle(point1=(0, 0), point2=(LENGTH, WIDTH))
part.BaseSolidExtrude(sketch=sketch, depth=HEIGHT)

# Partitions for frozen regions
datum1 = part.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=FROZEN_SIZE)
datum2 = part.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=LENGTH-FROZEN_SIZE)
part.PartitionCellByDatumPlane(datumPlane=part.datums[datum1.id], cells=part.cells)
part.PartitionCellByDatumPlane(datumPlane=part.datums[datum2.id], cells=part.cells)

# Part sets
part.Set(cells=part.cells, name='AllCells')

# ============= MATERIAL =============
material = model.Material(name='Steel')
material.Elastic(table=((E, NU),))
material.Density(table=((DENSITY,),))  # REQUIRED for volume calculation

model.HomogeneousSolidSection(name='Section', material='Steel')
part.SectionAssignment(region=part.sets['AllCells'], sectionName='Section')

# ============= ASSEMBLY =============
assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
instance = assembly.Instance(name='DesignSpace-1', part=part, dependent=ON)

# Assembly sets for BCs/loads
fixed_face = instance.faces.findAt(((0, WIDTH/2, HEIGHT/2),))
assembly.Set(faces=fixed_face, name='FixedFace')

load_face = instance.faces.findAt(((LENGTH, WIDTH/2, HEIGHT/2),))
assembly.Surface(side1Faces=load_face, name='LoadSurface')

# Frozen regions (cells at BC and load ends)
mount_cells = instance.cells.findAt(((FROZEN_SIZE/2, WIDTH/2, HEIGHT/2),))
assembly.Set(cells=mount_cells, name='FrozenMount')

load_cells = instance.cells.findAt(((LENGTH-FROZEN_SIZE/2, WIDTH/2, HEIGHT/2),))
assembly.Set(cells=load_cells, name='FrozenLoad')

# ============= STEP =============
model.StaticStep(name='Load', previous='Initial')
model.FieldOutputRequest(name='F-Output', createStepName='Load',
                         variables=('S', 'U', 'RF', 'ENER'))

# ============= BCs AND LOADS =============
model.EncastreBC(name='Fixed', createStepName='Initial', region=assembly.sets['FixedFace'])

area = WIDTH * HEIGHT
model.SurfaceTraction(
    name='Load',
    createStepName='Load',
    region=assembly.surfaces['LoadSurface'],
    magnitude=FORCE/area,
    directionVector=((0,0,0), (0,-1,0)),
    distributionType=UNIFORM,
    traction=GENERAL
)

# ============= MESH =============
part.seedPart(size=MESH_SIZE)
elemType = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, hourglassControl=ENHANCED)
part.setElementType(regions=(part.cells,), elemTypes=(elemType,))
part.generateMesh()

print(f"Mesh: {len(part.nodes)} nodes, {len(part.elements)} elements")

# ============= TOPOLOGY OPTIMIZATION =============
# Create task
model.TopologyTask(
    name='TopoTask',
    region=MODEL,
    materialInterpolationTechnique=SIMP,
    materialInterpolationPenalty=3.0,
    freezeBoundaryConditionRegions=ON,
    freezeLoadRegions=ON,
    objectiveFunctionDeltaStopCriteria=0.001
)

task = model.optimizationTasks['TopoTask']

# Design responses
task.SingleTermDesignResponse(name='volume', region=MODEL, identifier=VOLUME)
task.SingleTermDesignResponse(name='strain_energy', region=MODEL,
                              identifier=STRAIN_ENERGY, stepOptions=LAST_STEP)

# Objective: minimize strain energy (maximize stiffness)
task.ObjectiveFunction(
    name='MinCompliance',
    objectives=((task.designResponses['strain_energy'], MINIMIZE_MAXIMUM, 1.0, 0.0),)
)

# Constraint: volume <= target
task.OptimizationConstraint(
    name='VolumeConstraint',
    designResponse='volume',
    restrictionMethod=RELATIVE_LESS_THAN_EQUAL,
    restrictionValue=VOLUME_FRACTION
)

# Frozen regions
task.FrozenArea(name='FreezeMounting', region=assembly.sets['FrozenMount'])
task.FrozenArea(name='FreezeLoad', region=assembly.sets['FrozenLoad'])

# Manufacturing: minimum member size
task.GeometricRestriction(
    name='MinMember',
    technique=MEMBER_SIZE,
    region=MODEL,
    minSize=MIN_MEMBER_SIZE
)

# ============= OPTIMIZATION PROCESS =============
opt_process = mdb.OptimizationProcess(
    name='TopologyOptimization',
    model='TopologyOpt',
    task='TopoTask',
    maxDesignCycle=MAX_ITERATIONS,
    dataSaveFrequency=OPT_DATASAVE_EVERY_CYCLE
)

# ============= SAVE =============
mdb.saveAs('TopologyOptimization.cae')

print("\n" + "="*60)
print("TOPOLOGY OPTIMIZATION READY")
print("="*60)
print(f"Design space: {LENGTH} x {WIDTH} x {HEIGHT} mm")
print(f"Volume fraction: {VOLUME_FRACTION*100:.0f}%")
print(f"Min member size: {MIN_MEMBER_SIZE} mm")
print(f"\nTo run: opt_process.submit(); opt_process.waitForCompletion()")
```

## Post-Processing

### View Results
```bash
abaqus cae database=TopologyOptimization/TOSCA_POST/TopologyOptimization.odb
```

### Export STL
1. Open post ODB in Abaqus/CAE
2. Optimization module → Extract → STL
3. Set density threshold (0.3-0.5 typical)
4. Export for CAD import

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Checkerboard pattern | Numerical instability | Add min member size constraint |
| Not converging | Infeasible constraints | Relax volume fraction, check frozen regions |
| Disconnected regions | Insufficient frozen areas | Add more frozen regions along load path |
| Thin features | No min member size | Add GeometricRestriction |
| Takes forever | Mesh too fine | Coarsen mesh, reduce iterations |

## Feedback Loops

- **If base analysis fails:** Fix BCs/loads before optimization
- **If checkerboard pattern:** Add minimum member size
- **If disconnected:** Increase volume fraction or add frozen regions
- **If not converging:** Relax constraints, increase iterations
- **If result not manufacturable:** Add appropriate manufacturing constraints

## API Reference

For optimization-specific parameters: `/abaqus-optimization`
For base model setup: `/abaqus-static-analysis`
