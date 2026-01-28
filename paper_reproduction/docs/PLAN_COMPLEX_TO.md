# Complex Version: Full Topology Optimization Recreation
## Fatigue-Topology Optimized IN718 Specimen (Full Abaqus License with TOSCA)

**Paper:** "Fatigue Response of a Topology Optimized Feature-based Component"
**Authors:** Carr, Quach, Hochhalter, Sangid
**Material:** IN718 (Inconel 718) via LPBF
**License:** Full Abaqus with TOSCA Optimization Module

---

## Goal

Fully recreate the topology optimization workflow from the paper using Abaqus TOSCA, including:
1. Design space definition with frozen pin regions
2. Volume minimization with stress constraints
3. Optimized geometry extraction and export
4. Validation FEA on the final design

This version replicates the exact methodology described in Section 3 of the paper.

---

## Paper Methodology Summary (Section 3)

The TO specimens were designed via **Abaqus CAE 2021 with TOSCA software**:

1. Solution space governed by clevis grip geometry and MTS load frame capacity
2. Objective: **Minimize volume** (weight) with uniform material density
3. Constraint: **Maximum von Mises stress ≤ 800 MPa**
4. TOSCA uses **non-parametric approach** allowing material to evolve freely
5. Iterative process: FEA → sensitivity analysis → material removal → repeat
6. Convergence when change in objective and constraint violation below threshold
7. Post-processing: extract geometry at density > 0.51, smooth, enforce symmetry

---

## Extracted Parameters from Paper

### Topology Optimization Parameters (Table 1)
| Parameter | Value | Description |
|-----------|-------|-------------|
| Element Type | C3D10 | 10-node quadratic tetrahedral |
| Mesh Seed Size | 1 mm | Global seed for design space |
| F₁ (Vertical Load) | 20 kN | Applied at upper pin |
| F₂ (Horizontal Loads) | ±5 kN | Applied at lower pins |
| Boundary Conditions | Y,Z fixed; X free | At lower pins |
| Stress Constraint | 800 MPa | Maximum von Mises |
| Iterations | 75 | Total optimization cycles |
| Extracted Density | >0.51 | Iso-surface threshold |

### Material Properties (Elastic for TO)
| Property | Value | Notes |
|----------|-------|-------|
| Young's Modulus (E) | 200 GPa | Simplified for linear TO |
| Poisson's Ratio (ν) | 0.30 | |

*Note: Linear elastic is justified as HCF nominally elastic loading*

### Design Space Geometry
| Dimension | Value | Source |
|-----------|-------|--------|
| Total Height | ~150 mm | Figure 2(a) estimated |
| Total Width | ~65 mm | Figure 2(a) estimated |
| Thickness | ~15 mm | Figure 2(a) estimated |
| Upper pin region | ~25×25 mm | Frozen (non-designable) |
| Lower pin blocks | ~25×25×20 mm each | Frozen (non-designable) |

---

## Workflow Phases

```
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 1: Design Space Creation                                 │
│  Skill: abaqus-geometry                                         │
│  Create rectangular envelope with pin connection regions        │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 2: Frozen Region Definition                              │
│  Skill: abaqus-geometry                                         │
│  Mark upper and lower pin areas as non-designable               │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 3: Material & Analysis Setup                             │
│  Skills: abaqus-material, abaqus-step                           │
│  Linear elastic IN718, static step                              │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 4: Boundary Conditions                                   │
│  Skill: abaqus-bc                                               │
│  Pin constraints as per paper specification                     │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 5: TO Load Case Definition                               │
│  Skill: abaqus-load                                             │
│  20 kN vertical + ±5 kN horizontal (for asymmetric solution)    │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 6: Mesh                                                  │
│  Skill: abaqus-mesh                                             │
│  C3D10 elements at 1mm seed size                                │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 7: TOSCA Optimization Setup                              │
│  Skill: abaqus-topology-optimization                            │
│  Define objective, constraints, design responses                │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 8: Run Optimization                                      │
│  Skill: abaqus-job                                              │
│  Submit and monitor TOSCA job                                   │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 9: Geometry Extraction                                   │
│  Skill: abaqus-export                                           │
│  Extract iso-surface at density >0.51, export STL/STEP          │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 10: Post-Processing & Symmetry                           │
│  External CAD (NX, Fusion, etc.)                                │
│  Smooth surfaces, enforce symmetry, cleanup                     │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 11: Validation FEA                                       │
│  Skills: abaqus-static-analysis, abaqus-odb                     │
│  Re-mesh final geometry, analyze with test loads                │
└─────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Design Space Creation

**Skill:** `abaqus-geometry`

### Design Space Envelope

Create the initial solution space as shown in Figure 2(a):

```
      ┌─────────────────────────────┐
      │                             │
      │      ┌───────────────┐      │  ← Upper pin connection
      │      │       ○       │      │     (will be frozen)
      │      └───────────────┘      │
      │                             │
      │                             │  ← Designable region
      │                             │     (material can be removed)
      │                             │
      │                             │
   ┌──┴──┐                     ┌──┴──┐
   │  ○  │                     │  ○  │  ← Lower pin blocks
   │     │                     │     │     (will be frozen)
   └─────┘                     └─────┘
```

### Implementation

```python
# Design space dimensions (approximate from figures)
DESIGN_HEIGHT = 150.0       # mm
DESIGN_WIDTH = 65.0         # mm
DESIGN_THICKNESS = 15.0     # mm

# Upper connection region
UPPER_WIDTH = 25.0          # mm
UPPER_HEIGHT = 25.0         # mm

# Lower block dimensions
LOWER_WIDTH = 25.0          # mm
LOWER_HEIGHT = 25.0         # mm
LOWER_DEPTH = 20.0          # mm
LOWER_SPACING = 40.0        # mm (center to center)

# Pin holes
PIN_DIAMETER = 10.0         # mm

# Create design space via multiple extrusions
# 1. Main body (rectangular envelope)
# 2. Upper tab region
# 3. Lower block regions
# 4. Cut pin holes
```

### File: `TO/01_create_design_space.py`

---

## Phase 2: Frozen Region Definition

**Skill:** `abaqus-geometry`

### Non-Designable Regions

The paper states pin regions must remain solid for clevis grip connection:

```python
# Create sets for frozen (non-designable) regions

# Upper pin region - cylinder around pin hole
upper_frozen_cells = part.cells.getByBoundingBox(
    xMin=-UPPER_WIDTH/2, xMax=UPPER_WIDTH/2,
    yMin=0, yMax=DESIGN_THICKNESS,
    zMin=DESIGN_HEIGHT-UPPER_HEIGHT, zMax=DESIGN_HEIGHT
)

# Lower left pin block
lower_left_frozen = part.cells.getByBoundingBox(
    xMin=-DESIGN_WIDTH/2-1, xMax=-DESIGN_WIDTH/2+LOWER_WIDTH+1,
    yMin=0, yMax=LOWER_DEPTH,
    zMin=0, zMax=LOWER_HEIGHT
)

# Lower right pin block
lower_right_frozen = part.cells.getByBoundingBox(
    xMin=DESIGN_WIDTH/2-LOWER_WIDTH-1, xMax=DESIGN_WIDTH/2+1,
    yMin=0, yMax=LOWER_DEPTH,
    zMin=0, zMax=LOWER_HEIGHT
)

# Create frozen region set
part.Set(
    name='FrozenRegions',
    cells=upper_frozen_cells + lower_left_frozen + lower_right_frozen
)
```

### File: `TO/01_create_design_space.py` (continued)

---

## Phase 3: Material & Analysis Setup

**Skills:** `abaqus-material`, `abaqus-step`

### Linear Elastic Material for TO

```python
# Linear elastic for TO (paper states HCF is nominally elastic)
E = 200000.0      # MPa (200 GPa - simplified)
nu = 0.30

material = model.Material(name='IN718_Elastic')
material.Elastic(table=((E, nu),))
material.Density(table=((8.19e-9,),))  # tonne/mm³

# Section assignment
section = model.HomogeneousSolidSection(
    name='IN718_Section',
    material='IN718_Elastic',
)
part.SectionAssignment(
    region=(part.cells,),
    sectionName='IN718_Section',
)
```

### Static Step for TO Analysis

```python
# Single static step for TO
model.StaticStep(
    name='TOLoad',
    previous='Initial',
    nlgeom=OFF,  # Linear for efficiency in TO iterations
)

# Field output requests
model.FieldOutputRequest(
    name='F-Output-1',
    createStepName='TOLoad',
    variables=('S', 'U', 'RF', 'DENSITY'),  # Include DENSITY for TO
)
```

### File: `TO/02_setup_optimization.py`

---

## Phase 4: Boundary Conditions

**Skill:** `abaqus-bc`

### Pin Constraints (from Table 1)

```python
# Paper specification:
# "Fixed in Y and Z at lower pins; translation along and rotation about X permitted"

# Lower left pin
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

# Lower right pin
model.DisplacementBC(
    name='LowerRightPin',
    createStepName='Initial',
    region=lower_right_pin_region,
    u1=UNSET, u2=0.0, u3=0.0,
    ur1=UNSET, ur2=0.0, ur3=0.0,
)
```

### File: `TO/02_setup_optimization.py` (continued)

---

## Phase 5: TO Load Case Definition

**Skill:** `abaqus-load`

### Multi-Directional Loading for Complex TO Solution

From paper (Section 3):
> "To generate more complex and TO representative features, two 5 kN loads, F₂, were applied in the positive and negative X direction to the right and left lower pin locations, respectively"

```python
# Reference points at pin centers
upper_rp = assembly.ReferencePoint(
    point=(0, DESIGN_THICKNESS/2, DESIGN_HEIGHT-UPPER_HEIGHT/2)
)
lower_left_rp = assembly.ReferencePoint(
    point=(-LOWER_SPACING/2, LOWER_DEPTH/2, LOWER_HEIGHT/2)
)
lower_right_rp = assembly.ReferencePoint(
    point=(LOWER_SPACING/2, LOWER_DEPTH/2, LOWER_HEIGHT/2)
)

# Coupling constraints
model.Coupling(name='UpperCoupling', ...)
model.Coupling(name='LowerLeftCoupling', ...)
model.Coupling(name='LowerRightCoupling', ...)

# F₁: 20 kN vertical at upper pin
model.ConcentratedForce(
    name='F1_Vertical',
    createStepName='TOLoad',
    region=upper_rp_region,
    cf3=20000.0,  # 20 kN in +Z
)

# F₂: +5 kN horizontal at right lower pin
model.ConcentratedForce(
    name='F2_Right',
    createStepName='TOLoad',
    region=lower_right_rp_region,
    cf1=5000.0,   # +5 kN in +X
)

# F₂: -5 kN horizontal at left lower pin
model.ConcentratedForce(
    name='F2_Left',
    createStepName='TOLoad',
    region=lower_left_rp_region,
    cf1=-5000.0,  # -5 kN in -X
)
```

### File: `TO/02_setup_optimization.py` (continued)

---

## Phase 6: Mesh

**Skill:** `abaqus-mesh`

### Fine Mesh for TO (1mm as per Table 1)

```python
MESH_SIZE = 1.0  # mm (per Table 1)

# Seed the part
part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)

# C3D10: 10-node quadratic tetrahedral (per Table 1)
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

print(f"Mesh generated: {len(part.nodes)} nodes, {len(part.elements)} elements")
```

### File: `TO/02_setup_optimization.py` (continued)

---

## Phase 7: TOSCA Optimization Setup

**Skill:** `abaqus-topology-optimization`

### Optimization Task Definition

```python
# Create optimization task
opt_task = model.TopologyTask(
    name='VolumeMinimization',
    region=MODEL,
    materialInterpolationTechnique=SIMP,  # Solid Isotropic Material with Penalization
    materialInterpolationPenalty=3.0,
    densityMoveLimit=0.25,
    initialDensity=1.0,
)

# Define design responses
# 1. Volume response (objective)
volume_response = opt_task.SingleTermDesignResponse(
    name='Volume',
    identifier='VOLUME',
    region=MODEL,
)

# 2. Stress response (constraint)
stress_response = opt_task.SingleTermDesignResponse(
    name='MaxStress',
    identifier='STRESS',
    stressValueType=MAX_MISES,
    region=MODEL,
    stepName='TOLoad',
)
```

### Objective Function: Minimize Volume

```python
# Objective: Minimize volume (equivalent to minimizing weight)
objective = opt_task.ObjectiveFunction(
    name='MinVolume',
    objectives=((volume_response, 1.0),),  # Minimize
)
```

### Constraint: Maximum von Mises Stress ≤ 800 MPa

```python
# Constraint: Max von Mises ≤ 800 MPa
stress_constraint = opt_task.OptimizationConstraint(
    name='StressLimit',
    designResponse=stress_response,
    restrictionMethod=UPPER_BOUND,
    restrictionValue=800.0,  # MPa
)
```

### Frozen Region Specification

```python
# Specify frozen (non-designable) regions
opt_task.FrozenArea(
    name='PinRegions',
    region=frozen_region_set,
)
```

### Optimization Control Parameters

```python
# From Table 1: 75 iterations, density threshold >0.51
opt_task.OptimizationProcess(
    name='MainProcess',
    maxIterations=75,
    convergenceTolerance=0.001,
    minDensity=0.001,
)
```

### File: `TO/02_setup_optimization.py` (continued)

---

## Phase 8: Run Optimization

**Skill:** `abaqus-job`

### Submit TOSCA Job

```python
# Create optimization job
opt_job = mdb.OptimizationProcess(
    name='TO_IN718_Bracket',
    model='DesignSpace',
    task='VolumeMinimization',
    maxIterations=75,
)

# Submit
opt_job.submit()
opt_job.waitForCompletion()

# Check status
print(f"Optimization complete. Final iteration: {opt_job.getValues()['iteration']}")
```

### Monitor Convergence

```python
# Read optimization history
history = opt_job.history
for iteration in history:
    vol = iteration['volume']
    max_stress = iteration['maxStress']
    print(f"Iter {iteration['number']}: Volume={vol:.1f} mm³, Max Stress={max_stress:.1f} MPa")
```

### File: `TO/03_run_optimization.py`

---

## Phase 9: Geometry Extraction

**Skill:** `abaqus-export`

### Extract Iso-Surface at Density > 0.51

```python
# From paper: "Extracted Density > 0.51"
DENSITY_THRESHOLD = 0.51

# Extract optimized geometry
opt_job.extractOptimizedGeometry(
    isoSurfaceValue=DENSITY_THRESHOLD,
    outputFileName='TO_Optimized_Raw.stl',
    outputFormat=STL,
)

# Also export as STEP for CAD editing
opt_job.extractOptimizedGeometry(
    isoSurfaceValue=DENSITY_THRESHOLD,
    outputFileName='TO_Optimized_Raw.stp',
    outputFormat=STEP,
)

print(f"Geometry extracted at density threshold {DENSITY_THRESHOLD}")
```

### File: `TO/04_export_geometry.py`

---

## Phase 10: Post-Processing & Symmetry

**External CAD (NX, Fusion 360, etc.)**

From paper (Section 3):
> "The final part design was generated based on a sketch which matches the outline of the optimized output while smoothing rough features. This process was carried out in NX12, using a sectioned half of the extracted geometry, later mirrored, to ensure symmetry."

### Manual Steps in CAD Software

1. **Import** extracted STL/STEP into CAD (NX, Fusion 360, SolidWorks)
2. **Section** the geometry along the symmetry plane (Y-Z plane at X=0)
3. **Trace** the profile outline to create a clean 2D sketch
4. **Smooth** rough mesh-dependent features
5. **Extrude/Revolve** to create solid body
6. **Mirror** across symmetry plane to ensure bilateral symmetry
7. **Add fillets** at sharp corners
8. **Re-cut** pin holes with precise dimensions
9. **Export** final geometry as STEP for validation FEA

### File: Manual CAD workflow (documented)

---

## Phase 11: Validation FEA

**Skills:** `abaqus-static-analysis`, `abaqus-odb`

### Load Final Geometry and Re-Analyze

```python
# Import final smoothed geometry
acis.openAcis(fileName='TO_Final_Smoothed.stp')

# Create new model for validation
val_model = mdb.Model(name='TO_Validation')

# Import geometry
val_model.PartFromGeometryFile(
    name='TO_Specimen_Final',
    geometryFile='TO_Final_Smoothed.stp',
)

# Apply same material, but now elastic-plastic
material = val_model.Material(name='IN718')
material.Elastic(table=((198400.0, 0.30),))
material.Plastic(table=plastic_data)
material.Density(table=((8.19e-9,),))

# Setup validation analysis
# Step 1: Uniaxial load only (actual fatigue test condition)
val_model.StaticStep(
    name='FatigueTest',
    previous='Initial',
    nlgeom=ON,
)

# Apply 20 kN vertical at upper pin (no horizontal loads)
# Apply same BC constraints

# Re-mesh with finer mesh
val_part.seedPart(size=1.0)  # Can use finer mesh now
val_part.generateMesh()

# Submit validation job
val_job = mdb.Job(name='TO_Validation', model='TO_Validation')
val_job.submit()
val_job.waitForCompletion()
```

### Extract and Compare Results

```python
# Open validation ODB
odb = openOdb(path='TO_Validation.odb', readOnly=True)
frame = odb.steps['FatigueTest'].frames[-1]

# Von Mises stress
stress = frame.fieldOutputs['S']
max_mises = max(v.mises for v in stress.values)

# Find location of maximum stress
max_stress_element = None
max_stress_value = 0
for v in stress.values:
    if v.mises > max_stress_value:
        max_stress_value = v.mises
        max_stress_element = v.elementLabel

print(f"Maximum von Mises stress: {max_mises:.1f} MPa")
print(f"Location: Element {max_stress_element}")
print("Expected: Inner lower leg face (Location 3)")

# Compare to paper Figure 3 (~800 MPa at 15 kN)
# Scale: at 20 kN expect ~1067 MPa (linear scaling)
```

### File: `TO/05_validation_analysis.py`

---

## Verification Checklist

### Optimization Phase
- [ ] Design space created with correct dimensions
- [ ] Frozen regions properly defined (pin areas)
- [ ] All three loads applied (F₁ + 2×F₂)
- [ ] Boundary conditions match paper specification
- [ ] C3D10 elements at 1mm mesh size
- [ ] TOSCA optimization converges within 75 iterations
- [ ] Final stress satisfies ≤800 MPa constraint
- [ ] Volume significantly reduced from initial

### Geometry Extraction Phase
- [ ] Iso-surface extracted at density >0.51
- [ ] Geometry is connected (no floating regions)
- [ ] Pin regions remain solid
- [ ] STL/STEP files generated successfully

### Post-Processing Phase
- [ ] Symmetry enforced across centerline
- [ ] Rough mesh features smoothed
- [ ] Pin holes at correct dimensions
- [ ] Final geometry manufacturable (no thin features)

### Validation Phase
- [ ] Final geometry imports correctly
- [ ] Mesh generates without errors
- [ ] Analysis completes successfully
- [ ] Maximum stress location at inner lower legs
- [ ] Results comparable to paper Figure 3

---

## Expected Results Comparison

| Metric | Paper Value | Expected Simulation |
|--------|-------------|---------------------|
| Final volume | Significantly reduced | ~30-40% of original |
| Max von Mises (TO loads) | ≤800 MPa | Should satisfy constraint |
| Max von Mises (15 kN uniaxial) | ~800 MPa (Fig. 3) | ~800 MPa |
| Failure location | Location 3 (inner lower leg) | Inner lower leg |
| Geometry shape | Asymmetric → symmetric | Should match Fig. 2(f) |

---

## Running the Scripts

```bash
# Phase 1-6: Create design space and setup
abaqus cae noGUI=TO/01_create_design_space.py
abaqus cae noGUI=TO/02_setup_optimization.py

# Phase 7-8: Run optimization (may take hours)
abaqus cae noGUI=TO/03_run_optimization.py

# Phase 9: Export geometry
abaqus cae noGUI=TO/04_export_geometry.py

# Phase 10: Manual CAD post-processing (NX, Fusion, etc.)

# Phase 11: Validation analysis
abaqus cae noGUI=TO/05_validation_analysis.py

# View optimization results
abaqus cae database=TO_IN718_Bracket.odb

# View validation results
abaqus cae database=TO_Validation.odb
```

---

## Files to Create

| File | Purpose | Skill |
|------|---------|-------|
| `TO/01_create_design_space.py` | Design envelope + frozen regions | abaqus-geometry |
| `TO/02_setup_optimization.py` | Material, mesh, loads, TOSCA setup | abaqus-material, abaqus-mesh, abaqus-load, abaqus-topology-optimization |
| `TO/03_run_optimization.py` | Submit and monitor optimization | abaqus-job |
| `TO/04_export_geometry.py` | Extract optimized geometry | abaqus-export |
| `TO/05_validation_analysis.py` | Final validation FEA | abaqus-static-analysis, abaqus-odb |

---

## Notes

1. **Asymmetry in initial TO result**: The paper notes that TOSCA may produce asymmetric solutions due to mesh ordering effects. The manual post-processing step enforces symmetry.

2. **Horizontal loads purpose**: The ±5 kN horizontal loads are used during TO to promote complex load paths and prevent trivial solutions (straight legs).

3. **Density threshold**: The 0.51 threshold is a common choice balancing detail retention and smoothness.

4. **Stress constraint**: The 800 MPa constraint is set based on the stress response at connecting regions of the non-optimized solution space.
