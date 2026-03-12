---
name: abaqus-topology-optimization
description: Complete workflow for topology optimization. Two paths available — (a) CAE API path using TopologyTask + ObjectiveFunction + OptimizationProcess for Abaqus built-in optimization, or (b) Tosca CLI hybrid path where CAE builds the FE model, writeInput() generates the .inp, a .par file defines the optimization, and `tosca optimize` runs it. Tosca requires full Abaqus license with Tosca module (not Learning Edition).
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

Two workflow paths for topology optimization:

1. **CAE API path** — Use `TopologyTask`, `DesignResponse`, `ObjectiveFunction`, and `OptimizationProcess` entirely within Abaqus CAE. Works for Abaqus built-in optimization.
2. **Tosca CLI hybrid path** — CAE API builds the FE model, then Tosca CLI runs the optimization via a hand-written `.par` file. Required when using Tosca-specific features.

## When to Use This Skill

**Triggers:** topology optimization, minimize weight, lightweight design, organic structure, generative design, where to remove material, material efficiency, design for additive, stress-constrained optimization

**USE for:** Minimize weight subject to stress constraint, maximize stiffness at target volume fraction, generate organic load-carrying structures

**Do NOT use for:** Shape optimization (surface only) -> `/abaqus-shape-optimization`, Learning Edition users -> Tosca requires full license

## CAE API Path (Abaqus Built-In Optimization)

The CAE optimization API works correctly when used with the right tuple format:

```python
# TopologyTask defines design space
model.TopologyTask(name='Task', region=model.rootAssembly.sets['DesignSpace'])

# DesignResponse — 4 members: name, region, type, stepName
model.optimizationTasks['Task'].DesignResponse(
    name='DR_Volume', region=MODEL, response=VOLUME)
model.optimizationTasks['Task'].DesignResponse(
    name='DR_StrainEnergy', region=MODEL, response=STRAIN_ENERGY)

# ObjectiveFunction — objectives is a tuple of 4-tuples:
#   (suppress, designResponse, weight, referenceValue)
model.optimizationTasks['Task'].ObjectiveFunction(
    name='ObjFunc',
    objectives=((OFF, 'DR_StrainEnergy', 1.0, 0.0),))  # 4-tuple!

# OptimizationProcess
mdb.OptimizationProcess(name='OptProcess', model='Model-1',
                         task='Task', prototypeJob='Job-1')
mdb.optimizationProcesses['OptProcess'].submit()
```

**CRITICAL PITFALL:** The `objectives` parameter must use **4-tuples** `(suppress, designResponse, weight, referenceValue)`. Passing a 5-tuple (e.g., with a trailing empty string) corrupts internal C++ state and causes segfaults or KeyErrors.

**Note:** The CAE API generates .par files for Abaqus's own optimization system, not for standalone Tosca. For Tosca CLI usage, .par files must be hand-written (see Tosca CLI path below).

## Tosca CLI Hybrid Path

For Tosca-specific features or when running Tosca standalone, use the hybrid pipeline (proven in experiments 7-10): CAE builds the model, `writeInput()` or `noPartsInputFile=ON` generates a flat `.inp`, a hand-written `.par` defines the optimization, and `tosca optimize` runs it.

## Important: License Required

Topology optimization requires a **full Abaqus license with Tosca module**. NOT available in Learning Edition.

## Prerequisites

1. Working static analysis model (geometry, material, mesh, BCs, loads)
2. Design space defined with frozen regions partitioned via datum planes
3. Clear objective (min volume with stress constraint, or min compliance with volume constraint)
4. Known load cases and boundary conditions
5. Element type selection: **C3D10** for stress-constrained, **C3D8R** for compliance

## Workflow Paths Overview

### Path A: CAE API (Abaqus built-in optimization)
```
CAE API (noGUI)
----------------
1. Build FE model
2. TopologyTask + DesignResponse + ObjectiveFunction (4-tuple!)
3. OptimizationProcess.submit()
4. Post-process ODB
```

### Path B: Tosca CLI Hybrid Pipeline
```
CAE API (noGUI)          .inp generation                Tosca CLI
----------------         ----------------------         ---------
1. Build FE model   -->  3. noPartsInputFile=ON    --> 5. tosca optimize
2. writeInput()          4. Generate .par file      --> 6. Post-process
```

**Note:** Path B previously required manual .inp flattening (removing `*Part`/`*Instance`/`*Assembly` wrappers). This is no longer necessary — set `noPartsInputFile=ON` before `writeInput()` and Abaqus produces a flat .inp directly. Alternatively, Tosca auto-flattens hierarchical .inp during its data check (but group names get prefixed with `<assembly>_<instance>_`).

## Workflow Steps

### Phase 1: Build FE Model in CAE (Steps 1-5 of script)

1. **Geometry** -- Create design space envelope
2. **Pin holes** -- Cut holes for load application points
3. **Partition frozen regions** -- Use `DatumPlaneByPrincipalPlane` to split cells at boundaries between frozen blocks and design space. This creates separate cells that can be assigned to element sets.
4. **Create part-level sets** -- `FrozenUpper`, `FrozenLowerLeft`, etc. using `getByBoundingBox()` on the partitioned cells. Sets MUST be on the part (not instance) when using `dependent=ON`.
5. **Material + Section** -- Elastic properties AND density (required for volume response)
6. **Mesh** -- TET/FREE with appropriate element type:
   - **C3D10** (quadratic tet) for stress-constrained optimization -- avoids shear locking
   - **C3D8R** (hex) for compliance optimization -- faster, no stress accuracy needed
   - Mesh size 2-5mm typical. Filter radius = 2-3x mesh size.
7. **Assembly + Step** -- `dependent=ON` instance, `StaticStep`, field outputs including `ENER`
8. **RP coupling for pin loads** -- Reference points coupled to cylindrical hole surfaces via `KINEMATIC` coupling, loads/BCs applied to RPs
9. **Generate flat `.inp`** -- Set `noPartsInputFile=ON` then call `writeInput()`

### Phase 2: Generate Flat .inp for Tosca

Tosca requires a flat `.inp` without `*Part`/`*Instance`/`*Assembly` hierarchy. The simplest approach:

```python
mdb.models['Model-1'].setValues(noPartsInputFile=ON)
mdb.jobs[job_name].writeInput()
```

This produces a flat `.inp` directly — no manual flattening needed.

**Note on group names:** When Tosca auto-flattens a hierarchical `.inp`, set names get prefixed with `<assembly>_<instance>_` (e.g., `ASSEMBLY_PART-1_FrozenUpper`). Using `noPartsInputFile=ON` avoids this prefix issue.

**Legacy approach (manual flattening):** If `noPartsInputFile=ON` is not available, the `.inp` can be flattened manually by removing wrapper keywords, stripping `instance=` qualifiers, and renumbering assembly-level RP nodes. See `references/common-patterns.md` for the legacy flattening code.

### Phase 3: Generate .par File

The `.par` file defines the Tosca optimization in its native format:

- `FEM_INPUT` -- points to the flattened `.inp`
- `DV_TOPO` -- design variables on `ALL_ELEMENTS`
- `GROUP_DEF` + `DVCON_TOPO` -- frozen region groups with `CHECK_TYPE = FROZEN`
- `DRESP` -- design responses (VOLUME, STRAIN_ENERGY, SIG_SENS_MISES)
- `OBJ_FUNC` -- objective (MIN volume or MIN strain energy)
- `CONSTRAINT` -- constraint (stress <= limit or volume <= fraction)
- `OPTIMIZE` -- ties DV, objective, constraints, strategy together
- `OPT_PARAM` -- filter radius
- `STOP` -- max iterations
- `SMOOTH` -- STL export at iso-surface threshold

See `references/common-patterns.md` for complete .par templates.

### Phase 4: Run Tosca CLI

```bash
tosca optimize -j job_name -p file.par -s abaqus -scpus 4
```

Or via subprocess from within the CAE script (see exp10_optimize.py).

### Phase 5: Post-Process

- Tosca creates `job_name/` directory with per-cycle results
- `SAVE.inp/<cycle>/` contains the last-cycle `.inp` with `tosca_distribution.inp` (per-element densities)
- Run `abaqus job=Optimized input=<last_cycle>.inp` to generate ODB for stress visualization
- STL exported automatically if `SMOOTH` block is in `.par`

## Key Decisions

| Goal | Objective | Constraint | Element |
|------|-----------|------------|---------|
| Stiffest at weight | Min compliance (STRAIN_ENERGY) | Volume <= X% (REL) | C3D8R |
| Lightest under stress | Min VOLUME | Stress <= Y MPa (ABS) | C3D10 |
| Avoid resonance | Max frequency | Volume <= X% | C3D10 |

### Volume Fraction (for compliance optimization)

| Fraction | Use Case |
|----------|----------|
| 20-30% | Aggressive (aerospace) |
| 30-40% | Balanced (general) |
| 40-50% | Conservative (safety-critical) |

### Filter Radius

| Multiplier | Effect |
|------------|--------|
| 2x mesh size | Minimum (some checkerboard risk) |
| 3x mesh size | Recommended default |
| 4-5x mesh size | Thicker members, smoother topology |

## What to Ask User

**Critical:**
- Design space: "What is the bounding volume where material can exist?"
- Frozen regions: "Which areas must remain solid? (BC/load attachment)"
- Objective: "Minimize weight (stress-constrained) or maximize stiffness (volume-constrained)?"
- Loads and BCs: "What loads and supports act on the structure?"

**With Defaults:**
- Stress limit: Material yield / safety factor (if stress-constrained)
- Volume fraction: 30% (if compliance optimization)
- Mesh size: 3mm (adjust for geometry scale)
- Filter radius: 3x mesh size
- Max iterations: 20-50 (more for stress-constrained)
- Element type: C3D10 for stress, C3D8R for compliance

## Validation

| Stage | Check |
|-------|-------|
| Base model | `writeInput()` succeeds, .inp file has correct sets |
| Flat .inp | `noPartsInputFile=ON` produces flat .inp without `*Part`/`*Instance`/`*Assembly` wrappers |
| .par file | `FEM_INPUT.FILE` points to flat .inp, frozen groups reference correct set names |
| Tosca run | Exit code 0, iterations decreasing objective |
| Final design | Load path intact, no floating regions, STL exported |

## Troubleshooting

See `references/troubleshooting.md` for detailed solutions. Key issues:

| Issue | Solution |
|-------|----------|
| CAE API segfault | Check ObjectiveFunction tuple format — must be 4-tuple, not 5-tuple |
| Tosca "cannot read .inp" | Use `noPartsInputFile=ON` before `writeInput()` for flat .inp |
| RP node collision | Renumber assembly RP nodes by adding max_mesh_node_id offset |
| Stress singularity at pins | Use RP coupling (distributes load), exclude loaded nodes from stress constraint |
| Checkerboard pattern | Increase filter radius to 3-5x mesh size |
| C3D4 shear locking | Use C3D10 (quadratic tet) for stress accuracy |

## Code Patterns

For API syntax and code examples, see:
- `references/common-patterns.md` -- Real working code from experiments 7-10
- `references/workflow-checklist.md` -- Step-by-step checklist
- `references/troubleshooting.md` -- Known issues and solutions

## Related Skills

- `/abaqus-optimization` -- Base optimization concepts (objective, constraint, design response)
- `/abaqus-static-analysis` -- Required before optimization
- `/abaqus-geometry` -- Design space creation and partitioning
- `/abaqus-mesh` -- Element type selection and mesh quality
- `/abaqus-export` -- Export optimized geometry
