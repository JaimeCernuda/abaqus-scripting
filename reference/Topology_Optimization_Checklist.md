# Topology Optimization - Quick Reference Checklist

## The Core Principle

```
IF you have all required inputs for each step → That step can be completed
IF you complete all steps A through N      → You get an optimized design  
IF you automate each step                  → You have a fully automated system
```

---

## Step-by-Step Checklist

### ☐ Step A: Define Geometry (Design Space)

**Required:**
- [ ] Overall dimensions (Length × Width × Height)
- [ ] Geometry source (primitive shape OR CAD file path)
- [ ] Coordinate system and units

**You have enough when:** A 3D solid volume exists representing where material CAN be placed.

---

### ☐ Step B: Define Material Properties

**Required:**
- [ ] Young's Modulus (E) — stiffness
- [ ] Poisson's Ratio (ν) — lateral contraction
- [ ] Density (ρ) — mass per volume

**You have enough when:** Material behavior is fully defined for linear elastic analysis.

---

### ☐ Step C: Create Mesh

**Required:**
- [ ] Element size (how fine)
- [ ] Element type (hex, tet, etc.)

**You have enough when:** Geometry is discretized into finite elements with no quality errors.

---

### ☐ Step D: Define Boundary Conditions

**Required:**
- [ ] At least ONE fixed/constrained region
- [ ] Which degrees of freedom are constrained (translations, rotations)
- [ ] Location of constraint (coordinates or named region)

**You have enough when:** Structure cannot move as a rigid body (is properly supported).

---

### ☐ Step E: Define Loads

**Required:**
- [ ] At least ONE load
- [ ] Load type (force, pressure, etc.)
- [ ] Load magnitude
- [ ] Load direction
- [ ] Load location

**You have enough when:** External forces acting on the structure are fully defined.

---

### ☐ Step F: Define Analysis Step

**Required:**
- [ ] Analysis type (Static, Frequency, etc.)
- [ ] Step sequence (which step follows which)

**You have enough when:** The FEA solver knows what type of analysis to perform.

---

### ☐ Step G: Define Design Space and Frozen Regions

**Required:**
- [ ] Design region (where optimizer can add/remove material)
- [ ] Frozen regions (where material must remain solid)

**You have enough when:** Optimizer knows which elements it can modify.

---

### ☐ Step H: Define Optimization Objective

**Required:**
- [ ] What to optimize (strain energy, volume, frequency, etc.)
- [ ] Direction (minimize or maximize)

**You have enough when:** Optimizer has a clear goal.

---

### ☐ Step I: Define Optimization Constraints

**Required:**
- [ ] At least ONE constraint (typically volume fraction)
- [ ] Constraint type (≤, ≥, =)
- [ ] Constraint value

**You have enough when:** Optimizer has limits to satisfy (otherwise trivial solution).

---

### ☐ Step J: Define Manufacturing Constraints (Optional)

**Optional but recommended:**
- [ ] Minimum member size
- [ ] Symmetry planes
- [ ] Draw direction (for casting)
- [ ] Build direction (for 3D printing)

**You have enough when:** Optimized design will be manufacturable.

---

### ☐ Step K: Configure Solver Settings

**Required:**
- [ ] Maximum iterations
- [ ] Convergence tolerance

**You have enough when:** Optimizer knows when to stop.

---

### ☐ Step L: Run Optimization

**Required:**
- [ ] All previous steps completed
- [ ] Computational resources available

**You have enough when:** Process completes with "converged" status.

---

### ☐ Step M: Post-Process Results

**Required:**
- [ ] Access to result files
- [ ] Density threshold for interpretation

**You have enough when:** You can visualize and validate the optimized design.

---

### ☐ Step N: Export Geometry

**Required:**
- [ ] Density threshold (isosurface level)
- [ ] Output format (STL, STEP, etc.)
- [ ] Output file path

**You have enough when:** Usable geometry file exists for CAD or manufacturing.

---

## Minimum Viable Input Set

For the simplest topology optimization, you need:

| Category | Minimum Information |
|----------|---------------------|
| **Geometry** | Bounding box dimensions |
| **Material** | E, ν |
| **Mesh** | Element size |
| **Boundary Conditions** | One fixed face/edge/point |
| **Loads** | One force with magnitude and direction |
| **Objective** | "Maximize stiffness" (minimize strain energy) |
| **Constraint** | Target volume fraction (e.g., 30%) |
| **Solver** | Max iterations (e.g., 50) |

**Everything else has reasonable defaults.**

---

## Input-Output Summary Table

| Step | Key Input | Key Output |
|------|-----------|------------|
| A | Dimensions | 3D solid geometry |
| B | E, ν, ρ | Material definition |
| C | Element size | Finite element mesh |
| D | Fixed locations | Boundary condition set |
| E | Force vectors | Load definition |
| F | "Static" | Analysis step |
| G | Design vs frozen | Region assignments |
| H | "Min strain energy" | Objective function |
| I | "Volume ≤ 30%" | Constraint definition |
| J | "Min size = 3mm" | Manufacturing constraint |
| K | "Max 50 iterations" | Solver configuration |
| L | (all above) | Optimization results |
| M | Threshold = 0.3 | Validated design |
| N | "Export STL" | Geometry file |

---

## Decision Tree for Automation

```
START
  │
  ├─ Do you have geometry dimensions? 
  │    NO → Ask user for dimensions
  │    YES ↓
  │
  ├─ Do you have material properties?
  │    NO → Use default (Steel: E=210GPa, ν=0.3)
  │    YES ↓
  │
  ├─ Do you have boundary conditions?
  │    NO → Ask: "Where is this part mounted/fixed?"
  │    YES ↓
  │
  ├─ Do you have loads?
  │    NO → Ask: "What forces act on this part?"
  │    YES ↓
  │
  ├─ Do you have optimization goals?
  │    NO → Use default: "Maximize stiffness, 30% volume"
  │    YES ↓
  │
  └─ ALL INPUTS AVAILABLE → Run optimization
```

---

## MCP Tool Mapping

| Workflow Step | MCP Tool Name | Required Parameters |
|---------------|---------------|---------------------|
| A | `create_geometry` | dimensions, shape_type |
| B | `set_material` | E, nu, density |
| C | `generate_mesh` | element_size |
| D | `add_boundary_condition` | region, type, values |
| E | `add_load` | region, type, magnitude, direction |
| F | `create_step` | step_type |
| G | `define_design_space` | design_region, frozen_regions |
| H | `set_objective` | response_type, sense |
| I | `add_constraint` | response_type, operator, value |
| J | `add_manufacturing_constraint` | constraint_type, parameters |
| K | `configure_solver` | max_iter, tolerance |
| L | `run_optimization` | — |
| M | `get_results` | — |
| N | `export_geometry` | format, threshold |
