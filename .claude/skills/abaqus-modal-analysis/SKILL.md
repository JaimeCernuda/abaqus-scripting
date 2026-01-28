---
name: abaqus-modal-analysis
description: Complete workflow for modal/frequency analysis - extract natural frequencies and mode shapes. Use for vibration analysis and resonance avoidance.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
  - Skill
---

# Abaqus Modal Analysis Workflow

## When to Use This Skill

**USE for:**
- Finding natural frequencies of a structure
- Extracting mode shapes for visualization
- Resonance avoidance (comparing natural freq to excitation)
- Dynamic characterization before transient analysis
- NVH (Noise, Vibration, Harshness) studies
- Validating FE model against modal test data

**Do NOT use for:**
- Forced vibration response (use transient dynamic)
- Frequency response function (use steady-state dynamics)
- Static stress/deflection → use `/abaqus-static-analysis`
- Impact/crash → use `/abaqus-dynamic-analysis`

**Key requirement:** Density MUST be defined. Modal analysis depends on mass.

## Key Decisions

### 1. Boundary Condition Type

| Configuration | First Modes | Use Case |
|---------------|-------------|----------|
| Free-free (no BCs) | 6 rigid body modes ≈ 0 Hz | Test correlation, unconstrained |
| Cantilever (one end fixed) | Bending modes | Mounted component |
| Simply supported | Bending, plate modes | Bridge-like structures |
| Fully constrained | Localized modes | Heavily mounted parts |

**Note:** Free-free analysis gives 6 modes at ~0 Hz (rigid body). Real modes start at mode 7.

### 2. Number of Modes to Extract

| Application | Modes | Guidance |
|-------------|-------|----------|
| Quick check | 5-10 | First few modes often sufficient |
| Full characterization | 20-50 | Capture all modes in frequency range of interest |
| Modal participation | All in range | Use frequency range instead of count |

### 3. Frequency Range vs Mode Count

| Method | Parameter | When |
|--------|-----------|------|
| Fixed count | numEigen=10 | Know you need N modes |
| Frequency range | minEigen=0, maxEigen=1000 Hz | Need all modes up to frequency |
| Shift-invert | shift=500 Hz | Need modes near specific frequency |

## Required Inputs

### CRITICAL

| Input | Why | What to Ask |
|-------|-----|-------------|
| Geometry | Part to analyze | "What are the dimensions?" |
| Material | E, ν, **ρ** | "What material? (density required!)" |
| BCs | Determines mode type | "How is it supported?" |
| Number of modes | What to extract | "How many modes to find? (default: 10)" |

### IMPORTANT

| Input | Default | Note |
|-------|---------|------|
| Density | NONE | **MUST** be specified - no default |
| Eigensolver | LANCZOS | Good for most problems |
| Normalization | DISPLACEMENT | Mode shapes normalized to max=1 |

## Workflow Steps

### Step 1: Create Geometry
```
/abaqus-geometry → Part and assembly
```

### Step 2: Define Material WITH DENSITY
```
/abaqus-material → E, ν, and ρ (REQUIRED!)
```
Density is essential. Without it, Abaqus cannot compute mass matrix.

### Step 3: Create Mesh
```
/abaqus-mesh → Standard meshing
```
Mesh quality affects mode shapes. Finer mesh = more accurate high-frequency modes.

### Step 4: Apply Boundary Conditions
```
/abaqus-bc → Define support type
```
- Fixed end → Encastre
- Pinned → DisplacementBC with rotations free
- Free-free → No BCs (will get 6 rigid body modes)

### Step 5: Configure Frequency Step
```
/abaqus-step → FrequencyStep settings
```
**Note:** No loads needed for eigenvalue extraction.

### Step 6: Run and Extract
```
/abaqus-job → Submit
/abaqus-odb → Read frequencies from frames
```

## Complete Script Template

```python
# modal_analysis.py
# Run with: abaqus cae noGUI=modal_analysis.py

from abaqus import *
from abaqusConstants import *
from caeModules import *

# ============= PARAMETERS =============
LENGTH = 200.0  # mm
WIDTH = 20.0    # mm
HEIGHT = 5.0    # mm

E = 210000.0        # MPa
NU = 0.3
DENSITY = 7.85e-9   # tonne/mm³ - REQUIRED!

NUM_MODES = 10
MESH_SIZE = 5.0

# ============= MODEL =============
model = mdb.Model(name='ModalAnalysis')
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']

# ============= GEOMETRY =============
part = model.Part(name='Beam', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='Sketch', sheetSize=300.0)
sketch.rectangle(point1=(0, 0), point2=(LENGTH, HEIGHT))
part.BaseSolidExtrude(sketch=sketch, depth=WIDTH)

# ============= MATERIAL (DENSITY REQUIRED!) =============
material = model.Material(name='Steel')
material.Elastic(table=((E, NU),))
material.Density(table=((DENSITY,),))  # <-- ESSENTIAL for modal

model.HomogeneousSolidSection(name='Section', material='Steel')
part.SectionAssignment(region=part.Set(cells=part.cells, name='All'), sectionName='Section')

# ============= ASSEMBLY =============
assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
instance = assembly.Instance(name='Beam-1', part=part, dependent=ON)

# ============= BOUNDARY CONDITIONS =============
# Cantilever: fixed at x=0
fixed_face = instance.faces.findAt(((0, HEIGHT/2, WIDTH/2),))
assembly.Set(faces=fixed_face, name='Fixed')
model.EncastreBC(name='Fixed', createStepName='Initial', region=assembly.sets['Fixed'])

# For FREE-FREE: comment out the EncastreBC above
# First 6 modes will be ~0 Hz (rigid body)

# ============= FREQUENCY STEP =============
model.FrequencyStep(
    name='Frequency',
    previous='Initial',
    numEigen=NUM_MODES,
    eigensolver=LANCZOS,
    normalization=DISPLACEMENT
)

# Request mode shape output
model.FieldOutputRequest(
    name='F-Output',
    createStepName='Frequency',
    variables=('U',)  # Mode shapes
)

# ============= MESH =============
part.seedPart(size=MESH_SIZE)
elemType = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType,))
part.generateMesh()

print(f"Mesh: {len(part.nodes)} nodes")

# ============= RUN =============
mdb.saveAs('ModalAnalysis.cae')
job = mdb.Job(name='ModalAnalysis', model='ModalAnalysis')
job.submit()
job.waitForCompletion()

# ============= EXTRACT FREQUENCIES =============
from odbAccess import openOdb

odb = openOdb('ModalAnalysis.odb', readOnly=True)
step = odb.steps['Frequency']

print("\n" + "="*50)
print("NATURAL FREQUENCIES")
print("="*50)

frequencies = []
for i, frame in enumerate(step.frames):
    if i == 0:
        continue  # Skip initial frame
    # Extract frequency from frame description
    desc = frame.description
    freq = float(desc.split('=')[-1].strip())
    frequencies.append(freq)
    print(f"Mode {i}: {freq:.2f} Hz")

odb.close()
```

## Alternative Frequency Step Configurations

### All Modes in Frequency Range
```python
model.FrequencyStep(
    name='Frequency',
    previous='Initial',
    eigensolver=LANCZOS,
    minEigen=0.0,       # Minimum frequency (Hz)
    maxEigen=1000.0,    # Maximum frequency (Hz)
    numEigen=ALL        # Extract all in range
)
```

### Modes Near Target Frequency (Shift-Invert)
```python
model.FrequencyStep(
    name='Frequency',
    previous='Initial',
    eigensolver=LANCZOS,
    numEigen=10,
    shift=500.0  # Extract modes near 500 Hz
)
```

## Analytical Verification (Cantilever Beam)

For a cantilever beam, compare FEA results to analytical:

```python
import math

L = LENGTH / 1000  # m
b = WIDTH / 1000   # m
h = HEIGHT / 1000  # m
E_pa = E * 1e6     # Pa
rho = DENSITY * 1e12  # kg/m³

I = b * h**3 / 12  # Second moment of area
A = b * h          # Cross-sectional area

# Eigenvalue coefficients for cantilever
beta = [1.875, 4.694, 7.855, 10.996, 14.137]

for n, b_n in enumerate(beta, 1):
    fn = (b_n**2 / (2 * math.pi * L**2)) * math.sqrt(E_pa * I / (rho * A))
    print(f"Analytical Mode {n}: {fn:.2f} Hz")
```

## Mode Type Guide

### Cantilever Beam
| Mode | Shape | Frequency Pattern |
|------|-------|-------------------|
| 1 | 1st bending | f₁ |
| 2 | 2nd bending | 6.3 × f₁ |
| 3 | 3rd bending | 17.5 × f₁ |
| Higher | Torsion, axial | Depends on geometry |

### Free-Free Beam
| Mode | Type |
|------|------|
| 1-6 | Rigid body (~0 Hz) |
| 7+ | Flexible modes |

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Material has no density" | Density not defined | Add `material.Density(table=...)` |
| "Negative eigenvalue" | Unconstrained or unstable | Check BCs, add soft springs if free-free |
| "Zero frequency modes" | Free-free (expected) or insufficient BC | First 6 are rigid body for free-free |
| "Frequencies too high/low" | Unit error | Verify consistent units (mm-tonne-s) |
| "Memory error" | Too many modes or elements | Reduce numEigen or coarsen mesh |

## Validation Checklist

- [ ] Density defined in material
- [ ] BCs match intended support condition
- [ ] No loads applied (eigenvalue extraction doesn't use loads)
- [ ] Mesh adequate for highest mode of interest
- [ ] Frequencies reasonable for geometry/material
- [ ] Free-free: expect 6 modes ≈ 0 Hz

## API Reference

For step-specific parameters: `/abaqus-step`
For results extraction: `/abaqus-odb`
