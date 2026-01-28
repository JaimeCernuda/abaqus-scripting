---
name: abaqus-static-analysis
description: Complete workflow for static structural analysis - stress, displacement, and reaction force analysis under constant loads. Use when analyzing stress, displacement, or reaction forces under time-independent loads. Handles geometry creation, material assignment, meshing, BCs, loads, job submission, and results extraction. Choose this for strength evaluation, factor of safety calculations, or stiffness analysis. Does not handle time-varying loads (use abaqus-dynamic-analysis) or temperature effects (use abaqus-thermal-analysis).
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
  - Skill
---

# Abaqus Static Analysis Workflow

## When to Use This Skill

**USE for:**
- Structural strength evaluation (stress vs allowable)
- Factor of safety calculations
- Stiffness analysis (deflection under load)
- Load path verification
- Linear or nonlinear static problems
- Support reaction calculations

**Do NOT use for:**
- Time-varying loads (impact, vibration) → use `/abaqus-dynamic-analysis`
- Natural frequency extraction → use `/abaqus-modal-analysis`
- Heat transfer problems → use `/abaqus-thermal-analysis`
- Combined thermal-structural → use `/abaqus-coupled-analysis`
- Contact between parts → use `/abaqus-contact-analysis`

## Key Decisions

### 1. Linear vs Nonlinear?

| Condition | Analysis Type | When |
|-----------|--------------|------|
| Small deformation, linear material | Linear (nlgeom=OFF) | Displacements < 1% of part size |
| Large deformation | Nonlinear (nlgeom=ON) | Thin structures, rubber, large rotation |
| Yielding expected | Nonlinear + Plasticity | Stress > yield strength |
| Contact | Nonlinear | Parts touching |

**Default:** Start with linear. Switch to nonlinear if convergence issues or large deformation.

### 2. What Results Do I Need?

| Goal | Variables | Check |
|------|-----------|-------|
| Strength assessment | S (stress), MISES | MISES < σ_yield |
| Stiffness check | U (displacement) | Max deflection acceptable? |
| Support sizing | RF (reaction force) | Reactions = applied loads? |
| Buckling concern | Eigenvalues | Positive eigenvalues? |

## Required Inputs

### CRITICAL (Must Have)

| Input | What to Ask If Missing |
|-------|------------------------|
| Geometry | "What are the dimensions? (e.g., 100x50x20 mm)" |
| Material | "What material? (Steel, Aluminum, custom E/ν)" |
| Boundary Conditions | "How is it supported? (fixed face, pinned points)" |
| Loads | "What loads? (force, pressure, location, direction)" |

### WITH DEFAULTS

| Input | Default | When to Ask |
|-------|---------|-------------|
| Mesh size | Auto (10 elements across min dimension) | Stress concentrations need refinement |
| Element type | C3D8R | Complex geometry may need C3D10 |
| Nonlinear | OFF | Large deformation expected |

## Workflow Steps

### Step 1: Create Geometry
```
/abaqus-geometry → Create part, assembly, and region sets
```
- Define dimensions
- Create partitions if needed for BC/load regions
- Create instance in assembly

### Step 2: Define Material
```
/abaqus-material → Material properties and section assignment
```
- Elastic: E, ν (always required)
- Density: ρ (only if gravity or mass needed)
- Plastic: σy, εp (only for yielding analysis)

### Step 3: Create Mesh
```
/abaqus-mesh → Element type and mesh density
```
- Choose element type (C3D8R default)
- Set mesh size
- Verify node count (Learning Edition: ≤1000)

### Step 4: Apply Boundary Conditions
```
/abaqus-bc → Supports and constraints
```
- At least one fixed region
- Prevent all 6 rigid body modes

### Step 5: Apply Loads
```
/abaqus-load → Forces, pressures, gravity
```
- Apply to correct region
- Verify direction (sign matters!)

### Step 6: Configure Analysis Step
```
/abaqus-step → Static step settings
```
- Linear: default settings fine
- Nonlinear: set increment controls

### Step 7: Run and Post-Process
```
/abaqus-job → Submit and monitor
/abaqus-odb → Extract results
```

## Validation Checkpoints

### After Each Step

| Step | Validation |
|------|------------|
| Geometry | Part has cells, no errors |
| Material | Section assigned to all cells |
| Mesh | Node count OK, no warnings |
| BCs | At least one Encastre or equivalent |
| Loads | Applied to correct surface/point |
| Job | Completes without errors |

### Results Sanity Checks

| Check | Expected |
|-------|----------|
| Reaction forces | Sum ≈ applied loads |
| Displacement | Reasonable magnitude |
| Stress pattern | Logical load path |
| Max stress location | At expected stress concentration |

## Complete Script Template

```python
# static_analysis.py
# Run with: abaqus cae noGUI=static_analysis.py

from abaqus import *
from abaqusConstants import *
from caeModules import *

# ============= PARAMETERS =============
LENGTH = 100.0  # mm
WIDTH = 50.0    # mm
HEIGHT = 20.0   # mm

E = 210000.0     # MPa (Steel)
NU = 0.3
DENSITY = 7.85e-9  # tonne/mm³ (only if needed)

FORCE = 1000.0   # N
MESH_SIZE = 5.0  # mm

# ============= MODEL =============
model = mdb.Model(name='StaticAnalysis')
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']

# ============= GEOMETRY =============
part = model.Part(name='Part', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='Sketch', sheetSize=200.0)
sketch.rectangle(point1=(0, 0), point2=(LENGTH, HEIGHT))
part.BaseSolidExtrude(sketch=sketch, depth=WIDTH)

# ============= MATERIAL =============
material = model.Material(name='Steel')
material.Elastic(table=((E, NU),))
# material.Density(table=((DENSITY,),))  # Uncomment for gravity/dynamics

model.HomogeneousSolidSection(name='Section', material='Steel')
part.SectionAssignment(region=part.Set(cells=part.cells, name='All'), sectionName='Section')

# ============= ASSEMBLY =============
assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
instance = assembly.Instance(name='Part-1', part=part, dependent=ON)

# ============= STEP =============
model.StaticStep(name='Load', previous='Initial')
model.FieldOutputRequest(name='F-Output', createStepName='Load', variables=('S', 'U', 'RF'))

# ============= BOUNDARY CONDITIONS =============
fixed_face = instance.faces.findAt(((0, HEIGHT/2, WIDTH/2),))
assembly.Set(faces=fixed_face, name='Fixed')
model.EncastreBC(name='Fixed', createStepName='Initial', region=assembly.sets['Fixed'])

# ============= LOADS =============
load_face = instance.faces.findAt(((LENGTH, HEIGHT/2, WIDTH/2),))
assembly.Surface(side1Faces=load_face, name='LoadSurf')
area = HEIGHT * WIDTH
model.SurfaceTraction(
    name='Load',
    createStepName='Load',
    region=assembly.surfaces['LoadSurf'],
    magnitude=FORCE/area,
    directionVector=((0,0,0), (0,-1,0)),
    distributionType=UNIFORM,
    traction=GENERAL
)

# ============= MESH =============
part.seedPart(size=MESH_SIZE)
elemType = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType,))
part.generateMesh()

print(f"Nodes: {len(part.nodes)}, Elements: {len(part.elements)}")

# ============= RUN =============
mdb.saveAs('StaticAnalysis.cae')
job = mdb.Job(name='StaticAnalysis', model='StaticAnalysis')
job.submit()
job.waitForCompletion()

# ============= RESULTS =============
from odbAccess import openOdb
odb = openOdb('StaticAnalysis.odb', readOnly=True)
frame = odb.steps['Load'].frames[-1]

max_u = max(v.magnitude for v in frame.fieldOutputs['U'].values)
max_s = max(v.mises for v in frame.fieldOutputs['S'].values if hasattr(v, 'mises'))

print(f"\nMax displacement: {max_u:.6f} mm")
print(f"Max von Mises stress: {max_s:.2f} MPa")

odb.close()
```

## Nonlinear Settings

If convergence issues or large deformation:

```python
model.StaticStep(
    name='Load',
    previous='Initial',
    nlgeom=ON,          # Geometric nonlinearity
    initialInc=0.1,     # Start with 10% of load
    maxNumInc=100,      # Allow many increments
    minInc=1e-8,        # Allow small steps
    maxInc=0.1          # Limit step size
)
```

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Zero pivot" | Rigid body motion | Add more BCs |
| "Negative eigenvalue" | Instability/buckling | Check BCs, may need stabilization |
| "Too many increments" | Load too large or material softening | Reduce load, check material |
| "Equilibrium not achieved" | Convergence failure | Try smaller increments, check model |
| "Memory exceeded" | Mesh too fine | Increase element size |

## Feedback Loops

- **If mesh fails:** Go back to geometry, add partitions or simplify
- **If job fails with "zero pivot":** Go back to BCs, ensure rigid body modes constrained
- **If results unreasonable:** Verify material properties, check load direction
- **If stress too high:** Either design issue (expected) or check BCs/loads

## API Reference

For module-specific details:
- `/abaqus-geometry`, `/abaqus-material`, `/abaqus-mesh`
- `/abaqus-bc`, `/abaqus-load`, `/abaqus-step`
- `/abaqus-job`, `/abaqus-odb`
