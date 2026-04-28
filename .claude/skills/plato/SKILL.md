---
name: plato
description: Master skill for Plato Engine — open-source topology optimization and FEA. Routes user intent to specialized Plato skills.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Agent
---

# Plato — Master Router

Open-source topology optimization and FEA platform from Sandia National Labs.
Routes user requests to the appropriate specialized Plato skill.

## When to Use

Any request involving:
- Topology optimization with open-source tools
- Plato Engine, Plato Analyze, or Plato 3D
- Open-source FEA or structural optimization
- Gmsh + Exodus mesh workflows
- Running optimization on Delta/HPC

## Routing Table

| User Intent | Route To |
|---|---|
| "topology optimization", "optimize weight", "minimize compliance", "generative design" | `plato-topology-optimization` |
| "static analysis", "stress analysis", "check stresses", "FEA only" | `plato-static-analysis` |
| "create mesh", "mesh this", "generate elements" | `plato-mesh` |
| "define material", "steel", "aluminum", "Young's modulus" | `plato-material` |
| "fix this face", "clamp", "support", "boundary condition" | `plato-bc` |
| "apply force", "add load", "pressure", "traction" | `plato-load` |
| "set up physics", "configure analysis" | `plato-physics` |
| "run it", "submit job", "execute on cluster" | `plato-job` |
| "show results", "max stress", "displacement", "convergence" | `plato-results` |
| "export STL", "3D print", "save geometry" | `plato-export` |

## Disambiguation

| Phrase | Clarify |
|---|---|
| "optimize" alone | Ask: topology (remove material) or shape (change dimensions)? |
| "run analysis" | Ask: FEA only or with optimization? |
| "mesh" | Ask: new mesh or modify existing? |

## System Information

### Plato Installation on Delta
- **Location**: `/projects/bekn/jcernuda/plato`
- **Activate**: `source /projects/bekn/jcernuda/plato/spack/share/spack/setup-env.sh && spack env activate /projects/bekn/jcernuda/plato`
- **Binaries**: `plato` (optimizer), `analyze` (FE solver), `extract_iso`, `prune_and_refine`
- **Account**: `bekn-delta-cpu` (CPU), `bekn-delta-gpu` (GPU — limited hours)

### CRITICAL: Login Node Rules
- **NEVER** run Plato, Gmsh, Python scripts, or any computation on login nodes
- **ALWAYS** use SLURM: `srun` (interactive) or `sbatch` (batch)
- Even quick mesh generation or result extraction must go through SLURM

### Units
Plato uses SI units throughout:
- Length: m (or mm — be consistent)
- Force: N
- Stress/Modulus: Pa (or MPa if using mm)
- Density: kg/m³ (or tonne/mm³ if using mm)

**If using mm**: E in MPa, force in N, density in tonne/mm³ (steel = 7.85e-9)
**If using m**: E in Pa, force in N, density in kg/m³ (steel = 7850)

### Open-Source Stack
| Function | Tool |
|---|---|
| Mesh generation | Gmsh (Python API) |
| Mesh format | Exodus II (.exo) |
| Physics solver | Plato Analyze |
| Optimizer | ROL (Trilinos) |
| Post-processing | exodus.py / ParaView |
| Job scheduler | SLURM on Delta |

### File Types
| Extension | Purpose |
|---|---|
| `.i` | Plato input deck (optimization problem) |
| `.xml` | Plato Analyze physics definition |
| `.exo` | Exodus mesh / results |
| `.msh` | Gmsh mesh (intermediate) |
| `.stl` | Exported geometry |

## Workflow Overview

```
User describes problem
    │
    ├─ Topology optimization?
    │   └─ plato-topology-optimization (orchestrates full pipeline)
    │       ├─ plato-mesh        → Gmsh → .exo
    │       ├─ plato-material    → XML material block
    │       ├─ plato-bc          → XML essential BCs
    │       ├─ plato-load        → XML natural BCs
    │       ├─ plato-physics     → Assemble XML file
    │       ├─ Generate .i file
    │       ├─ plato-job         → sbatch on Delta
    │       ├─ plato-results     → Read Exodus output
    │       └─ plato-export      → STL extraction
    │
    └─ Static analysis only?
        └─ plato-static-analysis (FEA without optimization)
```
