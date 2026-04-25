# Plato Workflow Matrix

## Skill Dependencies

```
plato (master router)
├── plato-topology-optimization (orchestrator)
│   ├── plato-mesh          [1] Generate Exodus mesh
│   ├── plato-material      [2] Material XML block
│   ├── plato-bc            [3] Essential BC XML block
│   ├── plato-load          [4] Natural BC XML block
│   ├── plato-physics       [5] Assemble complete XML
│   ├── (generate .i file)  [6] Orchestrator writes input deck
│   ├── plato-job           [7] Submit to SLURM
│   ├── plato-results       [8] Read Exodus output
│   └── plato-export        [9] Extract STL
│
└── plato-static-analysis (orchestrator)
    ├── plato-mesh          [1]
    ├── plato-material      [2]
    ├── plato-bc            [3]
    ├── plato-load          [4]
    ├── plato-physics       [5]
    ├── (generate .i file)  [6]
    ├── plato-job           [7]
    └── plato-results       [8]
```

## File Flow

```
Gmsh Python script
    │
    ▼
mesh.msh ──meshio──▶ mesh.exo
                        │
                        ▼
              ┌─────────┴─────────┐
              │                   │
        analyze.xml          input.i
    (physics/material/     (optimization
     BC/load definition)    problem def)
              │                   │
              └─────────┬─────────┘
                        │
                        ▼
                  plato input.i
                   (via SLURM)
                        │
                        ▼
              Iteration*.exo / platomain.exo
                   (Exodus results)
                        │
                        ▼
                  optimized.stl
```

## Skill ↔ File Mapping

| Skill | Reads | Writes |
|---|---|---|
| plato-mesh | (user geometry description) | mesh.msh, mesh.exo |
| plato-material | (user material spec) | XML block (fragment) |
| plato-bc | mesh.exo (sideset names) | XML block (fragment) |
| plato-load | mesh.exo (sideset names) | XML block (fragment) |
| plato-physics | XML fragments from above | analyze.xml (complete) |
| plato-topology-optimization | all above | input.i |
| plato-job | input.i, mesh.exo, analyze.xml | SLURM script, submit |
| plato-results | Iteration*.exo, platomain.exo | (console output, CSV) |
| plato-export | Exodus results | optimized.stl, optimized.vtu |

## Parallel vs Sequential

Steps 2-4 (material, BC, load) can run in parallel — they're independent XML fragments.
All other steps are sequential.
