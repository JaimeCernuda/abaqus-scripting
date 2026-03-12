# Topology Optimization Workflow Specification

## Document Purpose

This document defines the complete workflow for performing topology optimization using Abaqus/Tosca. Each step specifies:
- **What** needs to be done
- **Inputs** required to complete the step
- **Outputs** produced by the step
- **Dependencies** on previous steps

**Conclusion**: If you have all the required inputs for each step, that step can be completed. If you complete all steps in sequence, you get an optimized structural design. If you automate each step, you have a fully automated topology optimization system.

---

## Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TOPOLOGY OPTIMIZATION WORKFLOW                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  A. Define Geometry                                                  │
│       ↓                                                              │
│  B. Define Material Properties                                       │
│       ↓                                                              │
│  C. Create Mesh                                                      │
│       ↓                                                              │
│  D. Define Boundary Conditions                                       │
│       ↓                                                              │
│  E. Define Loads                                                     │
│       ↓                                                              │
│  F. Define Analysis Step                                             │
│       ↓                                                              │
│  G. Define Design Space and Frozen Regions                           │
│       ↓                                                              │
│  H. Define Optimization Objective                                    │
│       ↓                                                              │
│  I. Define Optimization Constraints                                  │
│       ↓                                                              │
│  J. Define Manufacturing Constraints (Optional)                      │
│       ↓                                                              │
│  K. Configure Optimization Solver Settings                           │
│       ↓                                                              │
│  L. Run Optimization                                                 │
│       ↓                                                              │
│  M. Post-Process and Extract Results                                 │
│       ↓                                                              │
│  N. Export Optimized Geometry                                        │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Step A: Define Geometry

### Purpose
Create the design space - the volume of material within which the optimizer will work to find the optimal structure.

### Required Inputs

| Input | Description | Example |
|-------|-------------|---------|
| **Geometry Type** | How the geometry is defined | Primitive, CAD import, parametric |
| **Dimensions** | Size of the design space | Length=100mm, Width=50mm, Height=30mm |
| **Coordinate System** | Reference frame | Cartesian (X, Y, Z) |
| **Units** | Measurement system | mm, N, MPa, tonne (consistent set) |

#### If Primitive Shape:
| Input | Description | Example |
|-------|-------------|---------|
| Shape Type | Box, Cylinder, Sphere, etc. | Box |
| Origin Point | Reference point location | (0, 0, 0) |
| Dimensions | Shape-specific sizes | Length, Width, Height |

#### If CAD Import:
| Input | Description | Example |
|-------|-------------|---------|
| File Path | Location of CAD file | /path/to/design_space.step |
| File Format | CAD format | STEP, IGES, Parasolid |
| Import Options | Healing, simplification | Heal geometry = Yes |

#### If Parametric:
| Input | Description | Example |
|-------|-------------|---------|
| Sketch Definition | 2D profile | Rectangle with corners at (0,0) and (100,50) |
| Extrusion/Revolution | 3D operation | Extrude 30mm in Z direction |
| Features | Holes, fillets, etc. | Hole at (20,25) radius 5mm |

### Outputs
- 3D solid body representing the design space
- Part definition in model database

### Validation Criteria
- Geometry is watertight (no gaps or overlaps)
- Volume is calculable
- Geometry can be meshed

---

## Step B: Define Material Properties

### Purpose
Specify the material behavior for finite element analysis.

### Required Inputs

| Input | Description | Example |
|-------|-------------|---------|
| **Material Name** | Identifier for the material | Steel_AISI_1020 |
| **Young's Modulus (E)** | Elastic stiffness | 210,000 MPa |
| **Poisson's Ratio (ν)** | Lateral contraction ratio | 0.3 |
| **Density (ρ)** | Mass per unit volume | 7.85e-9 tonne/mm³ |

#### Optional Inputs (for advanced analysis):
| Input                | Description            | When Needed             |
| -------------------- | ---------------------- | ----------------------- |
| Yield Strength       | Plastic onset stress   | Nonlinear analysis      |
| Thermal Conductivity | Heat transfer property | Thermal analysis        |
| Thermal Expansion    | Temperature response   | Thermomechanical        |
| Fatigue Properties   | S-N curve data         | Durability optimization |

### Outputs
- Material definition in model database
- Material card ready for section assignment

### Validation Criteria
- E > 0 (positive stiffness)
- -1 < ν < 0.5 (physical bounds)
- ρ > 0 (positive density)
- Units are consistent with geometry

---

## Step C: Create Mesh

### Purpose
Discretize the geometry into finite elements for numerical analysis.

### Required Inputs

| Input | Description | Example |
|-------|-------------|---------|
| **Element Size** | Target edge length | 3.0 mm |
| **Element Type** | Element formulation | C3D8R (8-node hex, reduced integration) |
| **Element Order** | Linear or quadratic | Linear (first order) |

#### Mesh Control Options:
| Input | Description | Example |
|-------|-------------|---------|
| Mesh Technique | Algorithm type | Structured, Sweep, Free |
| Element Shape | Hex, Tet, Wedge | Hex-dominated |
| Size Variation | Refinement ratio | Min size factor = 0.1 |
| Curvature Control | Deviation factor | 0.1 (10% deviation allowed) |

#### Local Refinement (if needed):
| Input | Description | Example |
|-------|-------------|---------|
| Refinement Region | Where to refine | Near holes, sharp corners |
| Local Element Size | Size in refined region | 1.0 mm |

### Outputs
- Finite element mesh
- Node count
- Element count
- Element quality metrics

### Validation Criteria
- No severely distorted elements (aspect ratio < 10:1)
- No collapsed elements (zero volume)
- Mesh is connected (no floating nodes)
- Sufficient resolution for expected gradients

### Guidance for Topology Optimization
- Finer mesh = more design freedom, but slower computation
- Rule of thumb: at least 3-5 elements across minimum expected member
- Typical: 10,000 - 500,000 elements for practical problems

---

## Step D: Define Boundary Conditions

### Purpose
Specify how the structure is constrained/supported.

### Required Inputs

| Input | Description | Example |
|-------|-------------|---------|
| **BC Name** | Identifier | FixedSupport_Left |
| **BC Type** | Constraint type | Encastre, Displacement, Symmetry |
| **Region** | Where applied | Face, Edge, Vertex, Node set |
| **Step** | When applied | Initial (throughout analysis) |

#### For Displacement BC:
| Input | Description | Example |
|-------|-------------|---------|
| U1 (X displacement) | Constrained value or free | 0 (fixed) or UNSET (free) |
| U2 (Y displacement) | Constrained value or free | 0 (fixed) |
| U3 (Z displacement) | Constrained value or free | 0 (fixed) |
| UR1 (X rotation) | Constrained value or free | 0 (fixed) |
| UR2 (Y rotation) | Constrained value or free | 0 (fixed) |
| UR3 (Z rotation) | Constrained value or free | 0 (fixed) |

#### Common BC Types:
| Type | Constraints | Use Case |
|------|-------------|----------|
| Encastre | All DOFs = 0 | Welded/bolted connection |
| Pinned | U1=U2=U3=0, rotations free | Hinge joint |
| Roller | One displacement = 0 | Sliding support |
| Symmetry | Normal displacement = 0 | Half-model |

#### Region Specification:
| Method | Description | Example |
|--------|-------------|---------|
| By Coordinates | Point location | Face containing point (0, 25, 15) |
| By Name | Named selection | Set "MountingFace" |
| By Geometry | Geometric query | All faces with normal = (-1, 0, 0) |

### Outputs
- Boundary condition definitions
- Constrained degrees of freedom
- Regions identified for "frozen" status in optimization

### Validation Criteria
- Structure is not under-constrained (rigid body modes removed)
- Structure is not over-constrained (no conflicting BCs)
- At least 6 DOFs constrained (for 3D static)

---

## Step E: Define Loads

### Purpose
Specify the external forces acting on the structure.

### Required Inputs

| Input | Description | Example |
|-------|-------------|---------|
| **Load Name** | Identifier | TopPressure |
| **Load Type** | Force type | Concentrated, Pressure, Traction |
| **Region** | Where applied | Face, Edge, Vertex, Node set |
| **Magnitude** | Force value | 1000 N or 10 MPa |
| **Direction** | Force vector | (0, -1, 0) for downward |
| **Step** | When applied | LoadStep |

#### For Concentrated Force:
| Input | Description | Example |
|-------|-------------|---------|
| CF1 | Force in X direction | 0 N |
| CF2 | Force in Y direction | -1000 N |
| CF3 | Force in Z direction | 0 N |

#### For Pressure:
| Input | Description | Example |
|-------|-------------|---------|
| Magnitude | Pressure value | 10 MPa |
| Distribution | Uniform or varying | Uniform |

#### For Surface Traction:
| Input | Description | Example |
|-------|-------------|---------|
| Magnitude | Traction value | 25 N/mm² |
| Direction Vector | Traction direction | (0, -1, 0) |

#### Multiple Load Cases (if applicable):
| Input | Description | Example |
|-------|-------------|---------|
| Load Case Name | Identifier | LoadCase_1 |
| Load Combination | Which loads active | {TopPressure, SideForce} |
| Weight Factor | Relative importance | 1.0 |

### Outputs
- Load definitions
- Regions identified for "frozen" status in optimization
- Total applied force magnitude

### Validation Criteria
- Loads are in equilibrium with reactions (for static analysis)
- Load magnitudes are physically reasonable
- Load regions are properly defined

---

## Step F: Define Analysis Step

### Purpose
Configure the finite element analysis that will be run during each optimization iteration.

### Required Inputs

| Input | Description | Example |
|-------|-------------|---------|
| **Step Name** | Identifier | LoadStep |
| **Step Type** | Analysis type | Static, Frequency, Heat Transfer |
| **Previous Step** | Sequence | Initial |

#### For Static Analysis:
| Input | Description | Example |
|-------|-------------|---------|
| Time Period | Step duration | 1.0 |
| Initial Increment | Starting increment | 1.0 |
| Minimum Increment | Smallest allowed | 1e-6 |
| Maximum Increment | Largest allowed | 1.0 |
| Nonlinear | Geometric nonlinearity | OFF (for linear) |

#### For Frequency Analysis:
| Input | Description | Example |
|-------|-------------|---------|
| Number of Eigenvalues | Modes to extract | 10 |
| Frequency Range | Min/max frequency | 0 - 1000 Hz |
| Normalization | Mode scaling | Mass normalization |

#### Output Requests:
| Output | Description | Needed For |
|--------|-------------|------------|
| Stress (S) | Stress tensor | Stress constraints |
| Displacement (U) | Nodal displacements | Displacement constraints |
| Strain Energy (ENER) | Element energy | Stiffness optimization |
| Reaction Force (RF) | Support reactions | Verification |
| Element Volume (IVOL) | Element sizes | Volume calculation |

### Outputs
- Analysis step definition
- Output request configuration

### Validation Criteria
- Step type matches optimization objectives
- Outputs include variables needed for optimization
- Increment settings allow convergence

---

## Step G: Define Design Space and Frozen Regions

### Purpose
Specify which parts of the model the optimizer can modify and which must remain unchanged.

### Required Inputs

| Input | Description | Example |
|-------|-------------|---------|
| **Design Region** | Where optimization occurs | Entire model or subset |
| **Frozen Regions** | Where material must stay | BC regions, load regions |

#### Design Region Options:
| Option | Description | Example |
|--------|-------------|---------|
| Whole Model | Optimize everywhere | MODEL |
| Element Set | Specific elements | Set "DesignElements" |
| Geometric Region | Defined by bounds | X: 10-90, Y: 0-50, Z: 0-30 |

#### Frozen Region Specification:
| Input | Description | Example |
|-------|-------------|---------|
| Region Name | Identifier | FrozenMounting |
| Region Type | Element set or geometry | Element set |
| Reason | Why frozen | Contains boundary conditions |

#### Automatic Freezing Options:
| Option | Description | Recommendation |
|--------|-------------|----------------|
| Freeze BC Regions | Keep BC areas solid | ON |
| Freeze Load Regions | Keep load areas solid | ON |
| Freeze Contact Regions | Keep contact surfaces | ON (if applicable) |

### Outputs
- Design region definition
- List of frozen regions
- Element sets for optimization control

### Validation Criteria
- Design region contains meshable elements
- Frozen regions include all BC and load application areas
- Frozen regions are sufficient for structural connectivity

---

## Step H: Define Optimization Objective

### Purpose
Specify what the optimization should achieve - what quantity to minimize or maximize.

### Required Inputs

| Input | Description | Example |
|-------|-------------|---------|
| **Objective Name** | Identifier | MaximizeStiffness |
| **Design Response** | Quantity to optimize | Strain Energy |
| **Optimization Sense** | Direction | MINIMIZE (for strain energy) |
| **Weight** | Relative importance | 1.0 |

#### Common Objectives:

| Objective | Design Response | Sense | Physical Meaning |
|-----------|----------------|-------|------------------|
| Maximize Stiffness | Strain Energy | MINIMIZE | Least deformation under load |
| Minimize Weight | Volume | MINIMIZE | Lightest structure |
| Maximize Frequency | Eigenfrequency | MAXIMIZE | Avoid resonance |
| Minimize Stress | Max von Mises | MINIMIZE | Most uniform stress |

#### Design Response Definition:
| Input | Description | Example |
|-------|-------------|---------|
| Response Name | Identifier | StrainEnergy |
| Response Type | Physical quantity | STRAIN_ENERGY |
| Region | Where measured | MODEL (whole model) |
| Step | Which analysis step | LoadStep |
| Operation | How combined | SUM (total energy) |

#### Multi-Objective Optimization (if applicable):
| Input | Description | Example |
|-------|-------------|---------|
| Objective 1 | Primary objective | Minimize Strain Energy (weight=0.7) |
| Objective 2 | Secondary objective | Minimize Volume (weight=0.3) |
| Formulation | How combined | Weighted sum |

### Outputs
- Objective function definition
- Design response definitions

### Validation Criteria
- Objective is measurable from FEA results
- Objective sense is correct (minimize vs maximize)
- For multi-objective: weights sum to 1.0

---

## Step I: Define Optimization Constraints

### Purpose
Specify limits that the optimized design must satisfy.

### Required Inputs

| Input | Description | Example |
|-------|-------------|---------|
| **Constraint Name** | Identifier | VolumeLimit |
| **Design Response** | Quantity constrained | Volume |
| **Restriction Type** | How limited | RELATIVE_LESS_THAN_EQUAL |
| **Restriction Value** | Limit value | 0.30 (30% of original) |

#### Constraint Types:

| Type | Meaning | Example |
|------|---------|---------|
| RELATIVE_LESS_THAN_EQUAL | ≤ fraction of initial | Volume ≤ 30% |
| RELATIVE_GREATER_THAN_EQUAL | ≥ fraction of initial | Stiffness ≥ 80% |
| ABSOLUTE_LESS_THAN_EQUAL | ≤ absolute value | Displacement ≤ 1mm |
| ABSOLUTE_GREATER_THAN_EQUAL | ≥ absolute value | Frequency ≥ 100 Hz |
| ABSOLUTE_EQUAL | = exact value | (rarely used) |

#### Common Constraints:

| Constraint | Response | Type | Typical Value |
|------------|----------|------|---------------|
| Volume Fraction | Volume | Relative ≤ | 0.20 - 0.50 |
| Max Displacement | Displacement | Absolute ≤ | Application-specific |
| Min Frequency | Eigenfrequency | Absolute ≥ | Above excitation freq |
| Max Stress | von Mises Stress | Absolute ≤ | Yield / Safety Factor |

### Outputs
- Constraint definitions
- Associated design responses

### Validation Criteria
- Constraint is achievable (not impossible)
- Constraint values are physically meaningful
- Initial design satisfies constraints (or optimization will find feasible region)

---

## Step J: Define Manufacturing Constraints (Optional)

### Purpose
Ensure the optimized design can actually be manufactured using intended process.

### Required Inputs

| Input | Description | Example |
|-------|-------------|---------|
| **Constraint Type** | Manufacturing method | Casting, Stamping, Extrusion |
| **Parameters** | Process-specific settings | See below |

#### Minimum Member Size:
| Input | Description | Example |
|-------|-------------|---------|
| Min Thickness | Smallest feature size | 3.0 mm |
| Region | Where applied | Design region |

*Purpose*: Prevents thin features that can't be manufactured or would be too weak.

#### Maximum Member Size:
| Input | Description | Example |
|-------|-------------|---------|
| Max Thickness | Largest solid section | 20.0 mm |
| Region | Where applied | Design region |

*Purpose*: Prevents thick sections with potential porosity (casting) or residual stress issues.

#### Symmetry:
| Input | Description | Example |
|-------|-------------|---------|
| Symmetry Plane | Mirror plane | XZ plane (Y=0) |
| Symmetry Type | Planar or cyclic | Planar |

*Purpose*: Ensures balanced design, simplifies manufacturing.

#### Draw Direction (Casting/Molding):
| Input | Description | Example |
|-------|-------------|---------|
| Pull Direction | Mold removal direction | (0, 1, 0) - pull in Y |
| Overhang Angle | Max unsupported angle | 45° |

*Purpose*: Ensures part can be removed from mold without undercuts.

#### Extrusion Constraint:
| Input | Description | Example |
|-------|-------------|---------|
| Extrusion Axis | Constant cross-section direction | Z-axis |

*Purpose*: Ensures design can be made by extrusion process.

#### Additive Manufacturing:
| Input | Description | Example |
|-------|-------------|---------|
| Build Direction | Print layer direction | (0, 0, 1) - build in Z |
| Overhang Angle | Max unsupported overhang | 45° |
| Min Feature Size | Printer resolution | 0.5 mm |

*Purpose*: Ensures design is printable without excessive supports.

### Outputs
- Manufacturing constraint definitions
- Geometric restriction regions

### Validation Criteria
- Constraints match intended manufacturing process
- Constraint parameters are achievable by manufacturer
- Multiple constraints don't conflict

---

## Step K: Configure Optimization Solver Settings

### Purpose
Set parameters controlling how the optimization algorithm operates.

### Required Inputs

| Input | Description | Example |
|-------|-------------|---------|
| **Algorithm** | Optimization method | SIMP, BESO, Level-Set |
| **Max Iterations** | Maximum design cycles | 50 |
| **Convergence Criteria** | When to stop | Objective change < 0.1% |

#### Algorithm Selection:

| Algorithm | Full Name | Best For |
|-----------|-----------|----------|
| SIMP | Solid Isotropic Material with Penalization | General topology, stiffness |
| RAMP | Rational Approximation of Material Properties | Stress-constrained problems |
| Condition-Based | Optimality criteria | Simple stiffness problems |

#### SIMP-Specific Settings:
| Input | Description | Example |
|-------|-------------|---------|
| Penalization Factor | Density penalty exponent | 3.0 |
| Initial Density | Starting element density | 1.0 (or volume fraction) |
| Min Density | Lower bound | 0.001 (not zero for stability) |
| Max Density | Upper bound | 1.0 |
| Filter Radius | Smoothing radius | 1.5 × element size |

#### Convergence Settings:
| Input | Description | Example |
|-------|-------------|---------|
| Objective Tolerance | Relative change threshold | 0.001 (0.1%) |
| Constraint Tolerance | Constraint satisfaction | 0.001 |
| Max Iterations | Hard stop | 50 |
| Min Iterations | Minimum to run | 15 |

#### Performance Settings:
| Input | Description | Example |
|-------|-------------|---------|
| Parallel CPUs | Processors to use | 4 |
| Memory Limit | Max RAM | 8 GB |
| Save Frequency | How often to save | Every iteration |

### Outputs
- Optimization task configuration
- Solver parameter settings

### Validation Criteria
- Settings are appropriate for problem size
- Convergence criteria are not too tight (infinite loop) or too loose (premature stop)
- Computational resources are available

---

## Step L: Run Optimization

### Purpose
Execute the optimization process.

### Required Inputs

| Input | Description | Example |
|-------|-------------|---------|
| **Process Name** | Job identifier | BracketOptimization |
| **Working Directory** | Output location | /path/to/work/ |
| **Execution Mode** | How to run | Background, Interactive |

### Process (What Happens Internally)

```
┌──────────────────────────────────────────────────────────────┐
│                    OPTIMIZATION LOOP                          │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  Iteration 0: Initialize                                      │
│       │                                                       │
│       ▼                                                       │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │  Iteration N:                                            │ │
│  │                                                          │ │
│  │  1. Update element densities based on sensitivities     │ │
│  │       ↓                                                  │ │
│  │  2. Run FEA with current density distribution           │ │
│  │       ↓                                                  │ │
│  │  3. Extract results (stress, displacement, energy)      │ │
│  │       ↓                                                  │ │
│  │  4. Compute objective function value                    │ │
│  │       ↓                                                  │ │
│  │  5. Check constraint satisfaction                       │ │
│  │       ↓                                                  │ │
│  │  6. Compute sensitivities (how objective changes        │ │
│  │     with each element's density)                        │ │
│  │       ↓                                                  │ │
│  │  7. Check convergence:                                  │ │
│  │     - Objective stable? Constraints satisfied?          │ │
│  │     - If YES → Exit loop                                │ │
│  │     - If NO  → Continue to iteration N+1               │ │
│  │                                                          │ │
│  └─────────────────────────────────────────────────────────┘ │
│       │                                                       │
│       ▼                                                       │
│  Final: Converged or max iterations reached                   │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

### Monitoring Outputs (During Run)

| Output | Description | Where Found |
|--------|-------------|-------------|
| Current Iteration | Progress counter | .sta file, console |
| Objective Value | Current objective | .sta file |
| Constraint Values | Current constraint status | .sta file |
| Convergence Status | Feasible/Infeasible | .sta file |
| Estimated Time | Time remaining | Console |

### Outputs
- Optimization history (objective vs iteration)
- Element density distribution at each iteration
- Final optimized density field
- Convergence status

### Validation Criteria
- Optimization converged (not stopped at max iterations)
- Final design is feasible (all constraints satisfied)
- Objective improved from initial design

---

## Step M: Post-Process and Extract Results

### Purpose
Analyze the optimization results and validate the optimized design.

### Required Inputs

| Input | Description | Example |
|-------|-------------|---------|
| **Result Location** | Where results stored | ProcessName/TOSCA_POST/ |
| **Density Threshold** | Solid/void cutoff | 0.3 - 0.5 |
| **Iteration to Extract** | Which design | Final (or specific iteration) |

### Analysis Tasks

#### 1. Review Convergence History
| Metric | What to Check | Good Result |
|--------|---------------|-------------|
| Objective Plot | Trend over iterations | Monotonic decrease, stable at end |
| Constraint Plot | Satisfaction history | Below limit, stable |
| Density Change | Design evolution | Large initially, small at end |

#### 2. Examine Density Distribution
| Check | Description | Action |
|-------|-------------|--------|
| Clear Boundaries | Sharp solid/void interface | Good - easy to interpret |
| Gray Regions | Intermediate densities | May need more iterations or tighter filter |
| Disconnected Islands | Floating solid regions | Check connectivity, may be artifacts |

#### 3. Validate Optimized Design
| Validation | Method | Pass Criteria |
|------------|--------|---------------|
| Run Final FEA | Analyze with threshold density | Converges, no errors |
| Check Stresses | Examine stress distribution | Below yield / safety factor |
| Check Displacements | Verify deflections | Within specification |
| Verify Connectivity | Ensure load path exists | Continuous structure from BC to load |

### Outputs
- Convergence plots
- Density contour visualization
- Validation analysis results
- Decision: Accept, Refine, or Re-run

---

## Step N: Export Optimized Geometry

### Purpose
Create usable geometry from the optimization results for CAD or manufacturing.

### Required Inputs

| Input | Description | Example |
|-------|-------------|---------|
| **Density Threshold** | Isosurface level | 0.3 (elements with ρ > 0.3 are solid) |
| **Smoothing Level** | Surface smoothing passes | 3-5 iterations |
| **Output Format** | File type | STL, STEP, IGES, Parasolid |
| **Output Path** | Where to save | /path/to/optimized_bracket.stl |

#### Export Options

| Format | Use Case | Characteristics |
|--------|----------|-----------------|
| STL | 3D printing, visualization | Triangulated surface, no CAD features |
| STEP | CAD import, further design | BREP geometry, editable |
| IGES | Legacy CAD systems | Widely compatible |
| INP | Further Abaqus analysis | Mesh-based, for verification |

#### Post-Export Processing (Typically Manual)

| Task | Description | Tools |
|------|-------------|-------|
| Surface Smoothing | Remove mesh artifacts | CAD software, MeshLab |
| Feature Addition | Add holes, mounting features | CAD software |
| Filleting | Add radii at sharp corners | CAD software |
| Thickness Adjustment | Ensure min wall thickness | CAD software |
| Validation | Check manufacturability | CAD/CAM software |

### Outputs
- Exported geometry file(s)
- Optimized design ready for manufacturing or further refinement

### Validation Criteria
- Exported file opens correctly in target software
- Geometry is watertight (for 3D printing)
- All critical features are preserved

---

## Summary: Required Information Checklist

### Minimum Required Information

| Step | Critical Inputs | Without This... |
|------|-----------------|-----------------|
| A | Geometry dimensions, shape | No design space defined |
| B | E, ν (material properties) | FEA cannot run |
| C | Element size, type | No mesh for analysis |
| D | At least one fixed region | Structure is unconstrained |
| E | At least one load | Nothing to optimize for |
| F | Analysis type (static/frequency) | No analysis possible |
| G | Design region | Optimizer doesn't know where to work |
| H | Objective (what to optimize) | No optimization goal |
| I | At least one constraint (usually volume) | Trivial solution (remove all or keep all) |
| K | Max iterations, convergence tolerance | Optimization won't terminate properly |
| N | Density threshold, output format | Can't use the results |

### Optional But Recommended

| Step | Optional Inputs | Benefit |
|------|-----------------|---------|
| J | Manufacturing constraints | Producible design |
| K | Advanced solver settings | Better convergence |
| M | Validation analysis | Confidence in results |

---

## Automation Conclusion

**If you can provide all required inputs programmatically:**
1. Each step can be executed by calling appropriate Abaqus/Tosca APIs
2. The complete workflow runs without human intervention
3. Results are automatically exported in desired format

**To build an automated system (MCP):**
1. Create input specification schema for each step
2. Implement API calls for each step
3. Add validation logic for inputs and outputs
4. Add monitoring and error handling
5. Create output parsers for results extraction

**The system becomes:**
```
User Request (natural language or structured)
    ↓
Input Parser (extract parameters for each step)
    ↓
Workflow Engine (execute steps A through N)
    ↓
Result Processor (extract and format outputs)
    ↓
Deliverable (optimized geometry + analysis report)
```