---
name: tosca
description: Tosca .par file authoring for topology, shape, bead, and sizing optimization. Covers block syntax, design responses, constraints, objectives, optimization parameters, and STL export. This is the definitive reference for hand-written .par files.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
  - Skill
---

# Tosca .par File Authoring

Complete reference for writing Tosca Structure parameter files (.par) that define optimization problems. Every .par file in this project is hand-written -- no API generates valid ones.

## When to Use This Skill

**Triggers:** .par file, parameter file, design response, DRESP, objective function, OBJ_FUNC, optimization constraint, CONSTRAINT, Tosca parameters, OPT_PARAM, SIMP penalty, filter radius, sensitivity strategy, TOPO_SENSITIVITY, DV_TOPO, DVCON_TOPO, FEM_INPUT, SMOOTH block, SIG_SENS_MISES, volume fraction, material interpolation, MIMP, RAMP

**USE for:**
- Creating new .par files from scratch
- Adding/modifying blocks in existing .par files
- Debugging Tosca optimization failures caused by .par syntax
- Understanding block dependencies and required fields
- Configuring stress constraints, manufacturing constraints, or multi-load-case setups

**Do NOT use for:**
- Abaqus .inp file creation -> use `/abaqus-*` skills
- Running Tosca from Python API -> Tosca uses CLI only
- Post-processing ODB results -> use `/abaqus-odb`
- Abaqus CAE topology optimization setup -> use `/abaqus-topology-optimization`

## Prerequisites

1. A valid Abaqus .inp file (the FEA model to optimize)
2. Element sets and node sets defined in the .inp file (referenced by GROUP_DEF or directly)
3. Full Abaqus license with Tosca module (not Learning Edition)
4. Understanding of the physical optimization goal

## What to Ask the User

**Critical -- must know before writing any .par file:**
1. What is the optimization type? (topology, shape, bead, sizing)
2. What is the objective? (minimize volume, minimize compliance/strain energy, maximize frequency)
3. What constraints apply? (stress limit, displacement limit, volume fraction)
4. **What is the volume fraction target/limit?** Volume constraints are ALWAYS required — even when minimizing volume. Without a volume upper bound, the optimizer removes all material in one cycle.
5. What element groups define the design space vs. frozen regions?

**With sensible defaults:**
- Material interpolation: SIMP (default, good for compliance; use MIMP for stress)
- Penalty factor: 3.0 (range 2-4; higher = sharper solid/void boundary)
- Filter radius: 1.3 * avg element edge length (controls min member size)
- Max iterations: 50 for compliance, 80 for stress-constrained
- Move limit (DENSITY_MOVE): 0.25 for compliance, 0.10 for stress
- Strategy: TOPO_SENSITIVITY (always for topology with constraints)
- ISO_VALUE for SMOOTH: 0.3 (range 0.2-0.5)

## Block Dependency Order

A valid .par file must define blocks in dependency order:

```
FEM_INPUT       -> references the .inp file
GROUP_DEF       -> defines element/node groups (optional if sets exist in .inp)
DV_TOPO         -> references EL_GROUP (design space)
DVCON_TOPO      -> references EL_GROUP (frozen regions, manufacturing constraints)
DRESP           -> references EL_GROUP or ND_GROUP (what to measure)
OBJ_FUNC        -> references DRESP (what to optimize)
CONSTRAINT      -> references DRESP (limits on responses)
OPTIMIZE        -> ties DV, OBJ_FUNC, DVCON, CONSTRAINT together
OPT_PARAM       -> references OPTIMIZE (tuning knobs)
STOP            -> iteration limit and convergence criteria
SMOOTH          -> post-processing: isosurface extraction and STL export
```

## Quick Reference

See detailed documentation in `references/`:
- `par-file-syntax.md` -- Complete block-by-block syntax reference
- `design-responses.md` -- All DRESP types with usage rules
- `common-patterns.md` -- Ready-to-use .par templates for 5 common setups
- `troubleshooting.md` -- Error diagnosis, convergence fixes, common pitfalls

## Validation Checklist

Before running Tosca with a .par file:

| Check | How |
|-------|-----|
| Every block ends with `END_` | Search for missing terminators |
| No line exceeds 160 characters | Tosca silently truncates long lines |
| EL_GROUP names match .inp set names exactly | Case-sensitive match |
| DRESP referenced in OBJ_FUNC/CONSTRAINT exists | Cross-reference ID_NAMEs |
| OPTIMIZE references all DV, OBJ_FUNC, DVCON, CONSTRAINT | Nothing orphaned |
| OPT_PARAM references the correct OPTIMIZE | Name must match |
| .inp file path in FEM_INPUT is correct | Relative to Tosca working directory |
| SIG_SENS_MISES DRESP excludes loaded/BC nodes | Prevents stress singularities |
| For stress problems: ITER_MAX >= 75, DENSITY_MOVE <= 0.15 | Stress needs more iterations |

## Running Tosca

```bash
# From the directory containing both .par and .inp files:
"C:/SIMULIA/Commands/abaqus.bat" tosca --job <par_file_without_extension> 2>&1

# Example:
"C:/SIMULIA/Commands/abaqus.bat" tosca --job Exp10_TO 2>&1
```

## Related Skills

- `/abaqus-topology-optimization` -- Abaqus CAE side of topology optimization
- `/abaqus-optimization` -- Abaqus Python API for optimization setup
- `/abaqus-geometry` -- Creating the design space geometry
- `/abaqus-mesh` -- Meshing for optimization (fine mesh, C3D8R or C3D10)
