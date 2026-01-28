# Simple Version: Manual TO Geometry Recreation
## Fatigue-Topology Optimized IN718 Specimen (Student License)

**Paper:** "Fatigue Response of a Topology Optimized Feature-based Component"
**Authors:** Carr, Quach, Hochhalter, Sangid
**Material:** IN718 (Inconel 718) via LPBF
**License:** Abaqus Student Edition (no Tosca optimization)

---

## Goal

Recreate the topology optimized (TO) specimen from the paper using manually constructed geometry that approximates the final optimized shape shown in Figure 2(f). This allows fatigue-relevant FEA analysis without requiring the full Abaqus license with TOSCA optimization module.

---

## Extracted Parameters from Paper

### Material Properties (IN718)
| Property | Value | Source |
|----------|-------|--------|
| Young's Modulus (E) | 198.4 GPa | Table 2 |
| Poisson's Ratio (ν) | 0.30 | Section 3 |
| Yield Strength (σ_0.2%) | 1191 MPa | Table 2 |
| Proportional Limit | 980 MPa | Table 2 |
| Density | 8.19e-9 tonne/mm³ | IN718 standard |
| Ramberg-Osgood α | 0.002041 | Table 2 |
| Ramberg-Osgood n | 11.5 | Table 2 |

### Specimen Geometry (from Figures 1 & 2)
| Dimension | Value | Source |
|-----------|-------|--------|
| Total Height | 146.17 mm | Figure 1 |
| Overall Width | 64.60 mm | Figure 1 |
| Upper Tab | ~25×25 mm | Estimated |
| Lower Pin Blocks | ~25×25×20 mm each | Estimated |
| Pin Hole Diameter | ~10 mm | Standard clevis |
| Part Thickness | ~12 mm | Estimated |

### Loading Conditions
| Load Case | F₁ (Vertical) | F₂ (Horizontal) | Purpose |
|-----------|---------------|-----------------|---------|
| Fatigue Test | 20 kN at upper pin | None | Actual test condition |
| TO Design | 20 kN at upper pin | ±5 kN at lower pins | Original optimization loads |

### Boundary Conditions
- **Lower pins:** Fixed in Y and Z directions; free translation and rotation about X
- **Upper pin:** Load application point via coupling constraint

### Mesh Parameters
| Parameter | Value | Notes |
|-----------|-------|-------|
| Element Type | C3D10 | 10-node quadratic tetrahedral |
| Mesh Size | 2-3 mm | Coarsened for student license limit |
| Target Nodes | < 1000 | Student license constraint |

---

## Workflow Phases

```
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 1: Geometry Creation                                     │
│  Skill: abaqus-geometry                                         │
│  Create simplified TO-like bracket geometry manually            │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 2: Material Definition                                   │
│  Skill: abaqus-material                                         │
│  Define IN718 with elastic-plastic properties                   │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 3: Assembly & Analysis Steps                             │
│  Skills: abaqus-step                                            │
│  Create instance, define static steps with NLGEOM              │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 4: Boundary Conditions                                   │
│  Skill: abaqus-bc                                               │
│  Pin constraints with partial DOF freedom                       │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 5: Loads                                                 │
│  Skill: abaqus-load                                             │
│  Two load cases: fatigue test + TO design loads                 │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 6: Mesh                                                  │
│  Skill: abaqus-mesh                                             │
│  C3D10 elements at 2-3mm size                                   │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 7: Job Submission                                        │
│  Skill: abaqus-job                                              │
│  Run static analysis for both load cases                        │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 8: Results Extraction                                    │
│  Skill: abaqus-odb                                              │
│  Extract von Mises, max principal stress, displacements         │
└─────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Geometry Creation

**Skill:** `abaqus-geometry`

### Geometry Strategy

Approximate the final TO shape from Figure 2(f):

```
    ┌───────────────────────┐  ← Upper tab (25×25×12mm)
    │         ○             │  ← Pin hole Ø10mm centered
    └─────────┬─────────────┘
              │
         ╱────┴────╲            ← Curved transition region
        ╱           ╲
       │             │          ← Two diverging legs
       │     ○       │          ← Internal elliptical cutout
       │             │
     ┌─┴─┐         ┌─┴─┐
     │ ○ │         │ ○ │        ← Lower pin blocks (25×25×20mm)
     └───┘         └───┘

     |←── 64.60mm ───→|
```

### Implementation Steps
1. Create 2D sketch in Z-X plane (front profile)
2. Sketch upper tab rectangle
3. Sketch two leg outlines with curved transitions
4. Sketch lower block rectangles
5. Add internal elliptical cutout
6. Extrude to 12mm thickness (Y direction)
7. Cut cylindrical pin holes (Ø10mm)
8. Add fillets at sharp corners to reduce stress concentrations

### Key Dimensions
```python
# Geometry parameters
TOTAL_HEIGHT = 146.17      # mm
TOTAL_WIDTH = 64.60        # mm
THICKNESS = 12.0           # mm

# Upper tab
UPPER_TAB_WIDTH = 25.0     # mm
UPPER_TAB_HEIGHT = 25.0    # mm

# Lower blocks
LOWER_BLOCK_WIDTH = 25.0   # mm
LOWER_BLOCK_HEIGHT = 25.0  # mm
LOWER_BLOCK_DEPTH = 20.0   # mm

# Pin holes
PIN_DIAMETER = 10.0        # mm

# Leg geometry
LEG_WIDTH_NARROW = 8.0     # mm (at thinnest point)
LEG_SPACING_TOP = 15.0     # mm (where legs meet upper tab)
```

### File: `01_create_to_geometry.py`

---

## Phase 2: Material Definition

**Skill:** `abaqus-material`

### IN718 Elastic-Plastic Properties

```python
# Elastic properties
E = 198400.0      # MPa (198.4 GPa)
nu = 0.30
rho = 8.19e-9     # tonne/mm³

# Ramberg-Osgood to true stress-plastic strain
# ε = σ/E + α(σ/E)^n where α=0.002041, n=11.5
# Converted to tabular plastic data:
plastic_data = (
    (980.0, 0.0),       # Proportional limit (onset of plasticity)
    (1000.0, 0.00005),
    (1050.0, 0.0005),
    (1100.0, 0.0015),
    (1150.0, 0.0035),
    (1191.0, 0.006),    # 0.2% offset yield strength
    (1250.0, 0.012),
    (1300.0, 0.020),
    (1350.0, 0.030),
    (1400.0, 0.045),
)
```

### File: `02_define_in718_material.py`

---

## Phase 3: Assembly & Steps

**Skill:** `abaqus-step`

### Analysis Steps Configuration

```python
# Step 1: Fatigue Test Load Case
# Uniaxial 20 kN vertical load only
step_fatigue = model.StaticStep(
    name='FatigueTest',
    previous='Initial',
    nlgeom=ON,          # Nonlinear geometry for large deformations
    initialInc=0.1,
    maxNumInc=100,
    minInc=1e-6,
)

# Step 2: TO Design Load Case
# 20 kN vertical + ±5 kN horizontal
step_to_design = model.StaticStep(
    name='TODesign',
    previous='FatigueTest',
    nlgeom=ON,
    initialInc=0.1,
    maxNumInc=100,
)
```

### File: `03_setup_analysis.py`

---

## Phase 4: Boundary Conditions

**Skill:** `abaqus-bc`

### Pin Constraint Strategy

From paper (Table 1): "Fixed in Y and Z at lower pins; translation along and rotation about X permitted"

```python
# Lower left pin region
model.DisplacementBC(
    name='LowerLeftPin',
    createStepName='Initial',
    region=lower_left_pin_region,
    u1=UNSET,    # X translation FREE
    u2=0.0,      # Y translation FIXED
    u3=0.0,      # Z translation FIXED
    ur1=UNSET,   # X rotation FREE
    ur2=0.0,     # Y rotation FIXED
    ur3=0.0,     # Z rotation FIXED
)

# Lower right pin region (same constraints)
model.DisplacementBC(
    name='LowerRightPin',
    createStepName='Initial',
    region=lower_right_pin_region,
    u1=UNSET, u2=0.0, u3=0.0,
    ur1=UNSET, ur2=0.0, ur3=0.0,
)
```

### File: `03_setup_analysis.py` (continued)

---

## Phase 5: Loads

**Skill:** `abaqus-load`

### Load Application via Coupling Constraints

```python
# Create reference point at upper pin center
upper_rp = assembly.ReferencePoint(point=(0, THICKNESS/2, TOTAL_HEIGHT - UPPER_TAB_HEIGHT/2))

# Couple pin hole surface to reference point
model.Coupling(
    name='UpperPinCoupling',
    controlPoint=upper_rp_region,
    surface=upper_pin_surface,
    influenceRadius=WHOLE_SURFACE,
    couplingType=KINEMATIC,
)

# Load Case 1: Fatigue Test (20 kN vertical)
model.ConcentratedForce(
    name='VerticalLoad',
    createStepName='FatigueTest',
    region=upper_rp_region,
    cf3=20000.0,  # 20 kN in Z direction
)

# Load Case 2: TO Design (add horizontal loads)
model.ConcentratedForce(
    name='HorizontalLeft',
    createStepName='TODesign',
    region=lower_left_rp_region,
    cf1=-5000.0,  # -5 kN in X direction
)

model.ConcentratedForce(
    name='HorizontalRight',
    createStepName='TODesign',
    region=lower_right_rp_region,
    cf1=5000.0,   # +5 kN in X direction
)
```

### File: `03_setup_analysis.py` (continued)

---

## Phase 6: Mesh

**Skill:** `abaqus-mesh`

### Mesh Configuration

```python
MESH_SIZE = 3.0  # mm (adjust if node count exceeds 1000)

# Seed the part
part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)

# Set element type to C3D10 (10-node quadratic tetrahedral)
elem_type = mesh.ElemType(
    elemCode=C3D10,
    elemLibrary=STANDARD,
)

part.setElementType(
    regions=(part.cells,),
    elemTypes=(elem_type,),
)

# Generate mesh
part.generateMesh()

# Check node count
num_nodes = len(part.nodes)
print(f"Total nodes: {num_nodes}")
if num_nodes > 1000:
    print("WARNING: Exceeds student license limit. Increase MESH_SIZE.")
```

### File: `04_mesh_and_run.py`

---

## Phase 7: Job Submission

**Skill:** `abaqus-job`

### Job Configuration

```python
# Create and submit job
job = mdb.Job(
    name='TO_Specimen_Simple',
    model='TO_Specimen',
    type=ANALYSIS,
    memory=90,
    memoryUnits=PERCENTAGE,
)

# Write input file and submit
job.writeInput(consistencyChecking=OFF)
job.submit(consistencyChecking=OFF)
job.waitForCompletion()
```

### File: `04_mesh_and_run.py` (continued)

---

## Phase 8: Results Extraction

**Skill:** `abaqus-odb`

### Post-Processing

```python
from odbAccess import openOdb

odb = openOdb(path='TO_Specimen_Simple.odb', readOnly=True)

# Extract results for each step
for step_name in ['FatigueTest', 'TODesign']:
    step = odb.steps[step_name]
    frame = step.frames[-1]

    # Von Mises stress
    stress_field = frame.fieldOutputs['S']
    max_mises = max(v.mises for v in stress_field.values)

    # Maximum principal stress
    max_principal = max(v.maxPrincipal for v in stress_field.values)

    # Displacement
    disp_field = frame.fieldOutputs['U']
    max_disp = max(v.magnitude for v in disp_field.values)

    print(f"\n{step_name} Results:")
    print(f"  Max von Mises stress: {max_mises:.1f} MPa")
    print(f"  Max principal stress: {max_principal:.1f} MPa")
    print(f"  Max displacement: {max_disp:.4f} mm")

odb.close()
```

### File: `05_extract_results.py`

---

## Verification Checklist

- [ ] Geometry dimensions match paper (146.17 × 64.60 mm)
- [ ] IN718 material properties match Table 2
- [ ] Elastic-plastic behavior correctly defined
- [ ] BCs allow X translation/rotation, fix Y and Z
- [ ] Both load cases created (fatigue test + TO design)
- [ ] Mesh uses C3D10 elements
- [ ] Node count within student license limit (~1000)
- [ ] Analysis completes without errors
- [ ] Maximum stress location at inner lower legs (Location 3 from paper)
- [ ] Stress pattern comparable to Figure 3

---

## Expected Results

| Metric | Paper Value (15 kN) | Expected Simulation (20 kN) |
|--------|---------------------|----------------------------|
| Max von Mises | ~800 MPa | ~1000-1200 MPa |
| Failure location | Inner lower leg face | Inner lower leg face |
| Stress concentration | Location 3 | Location 3 |

---

## Running the Scripts

```bash
# Step 1: Create geometry
abaqus cae noGUI=paper_reproduction/01_create_to_geometry.py

# Step 2: Add material (run in same session or load .cae)
abaqus cae noGUI=paper_reproduction/02_define_in718_material.py

# Step 3: Setup analysis
abaqus cae noGUI=paper_reproduction/03_setup_analysis.py

# Step 4: Mesh and run
abaqus cae noGUI=paper_reproduction/04_mesh_and_run.py

# Step 5: Extract results
abaqus python paper_reproduction/05_extract_results.py

# View results in GUI
abaqus cae database=TO_Specimen_Simple.odb
```

---

## Files to Create

| File | Purpose | Skill |
|------|---------|-------|
| `01_create_to_geometry.py` | Create simplified TO bracket geometry | abaqus-geometry |
| `02_define_in718_material.py` | Define IN718 elastic-plastic | abaqus-material |
| `03_setup_analysis.py` | Assembly, steps, BCs, loads | abaqus-bc, abaqus-load, abaqus-step |
| `04_mesh_and_run.py` | Mesh and job submission | abaqus-mesh, abaqus-job |
| `05_extract_results.py` | ODB post-processing | abaqus-odb |
