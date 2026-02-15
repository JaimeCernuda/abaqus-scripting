# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Repository of Abaqus Python scripts for finite element analysis (FEA) and topology optimization. Scripts use the Abaqus Scripting Interface (Python 2.7 embedded in Abaqus) and must be executed through the Abaqus interpreter—not standard Python.

## Running Scripts

```bash
# With GUI
abaqus cae script=script_name.py

# Headless (faster, no GUI)
abaqus cae noGUI=script_name.py

# Post-processing only (ODB access, no CAE needed)
abaqus python script_name.py

# Submit a job (after model creation)
abaqus job=JobName interactive

# View results
abaqus cae database=ModelName.odb
```

When Claude Code runs Abaqus commands, always use the full `.bat` path:
```
"C:/SIMULIA/Commands/abaqus.bat" cae noGUI=script_name.py 2>&1
```

## Project Structure

```
examples/
  cantilever/         # 4-step progressive FEA tutorial (geometry → model → analysis → post-process)
  cube/               # Simple compression validation example
  topology_optimization/  # TO scripts (requires full license with Tosca)

paper_reproduction/
  experiment4/        # Final working model: IN718 fatigue specimen with 3 load cases (20/60/100 kN)
    scripts/          # Production scripts (create_geometry, setup_*kN, extract_*_results)
    archive/          # Iterative development history (v2–v19+, debug scripts)
  experiment1-3/      # Earlier iterations

reference/            # Topology optimization checklists and specifications

.claude/skills/       # 22+ specialized Claude Code skills for FEA task routing
  abaqus/             # Master skill: routes user intent to specialized skills
  abaqus-static-analysis/, abaqus-modal-analysis/, ...  # Analysis workflow skills
  abaqus-geometry/, abaqus-material/, abaqus-mesh/, ...  # Module skills
  docs/abaqus-api/    # 13 API module reference documents (mdb, part, material, mesh, odb, etc.)
```

## Architecture: Skills System

The `.claude/skills/` directory implements a hierarchical routing system:

1. **Master skill** (`abaqus/SKILL.md`) — interprets user intent and routes to the right specialized skill
2. **Analysis skills** — complete end-to-end workflows (static, modal, dynamic, thermal, coupled, contact, fatigue, topology/shape optimization)
3. **Module skills** — single-purpose tasks (geometry, material, mesh, bc, load, step, interaction, amplitude, field, output, job, odb, export, docs)

Each skill contains a `SKILL.md` (activation criteria, questions to ask) and a `references/` directory (API quick-reference, patterns, troubleshooting). The master skill's `references/workflow-matrix.md` documents dependencies between skills.

## Key Abaqus API Patterns

All scripts follow this workflow:
1. Create model: `model = mdb.Model(name='...')`
2. Create part with sketch + extrude: `part.BaseSolidExtrude(sketch=sketch, depth=...)`
3. Define material and section, assign to cells
4. Create assembly instance: `assembly.Instance(name='...', part=part, dependent=ON)`
5. Create analysis step: `model.StaticStep(name='...', previous='Initial')`
6. Apply BCs and loads using `findAt()` to locate faces
7. Mesh with `seedPart()` + `generateMesh()`, element type C3D8R
8. Create and submit job: `mdb.Job(name='...').submit()`

## Units

All scripts use consistent units (mm-tonne-s-N-MPa):
- Length: mm | Force: N | Stress/Modulus: MPa | Density: tonne/mm³ (steel = 7.85e-9)

## Limitations

- **Learning Edition**: Limited to 1000 nodes. Increase `MESH_SIZE` if exceeded.
- **Topology Optimization**: Requires full license with Tosca module (not available in Learning Edition).
- **noGUI mode**: Viewport operations (screenshots, display settings) don't work headless.

## Tooling

- **Package manager**: `uv` (see `pyproject.toml`). The project has no runtime dependencies—Abaqus provides its own Python 2.7 environment.
- **Workspace member**: `.claude/skills/abaqus-docs` has its own `pyproject.toml` with web scraping deps (`crawl4ai`, `beautifulsoup4`, `httpx`, `markdownify`).
- **IDE support**: Install `abqpy` separately (`pip install abqpy`) for type hints. Scripts still run through Abaqus only.
- **PATH**: Ensure `C:\SIMULIA\Commands` is on PATH. Verify with `abaqus information=release`.