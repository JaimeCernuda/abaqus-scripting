# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository contains Abaqus Python scripts for finite element analysis (FEA) and topology optimization. Scripts use the Abaqus Scripting Interface (Python 2.7 embedded in Abaqus) and must be executed through the Abaqus interpreter.

## Running Scripts

Scripts cannot be run with standard Python. Use the Abaqus interpreter:

```bash
# With GUI (opens Abaqus CAE)
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

When Claude Code is running commands use the form
```
Bash("C:/SIMULIA/Commands/abaqus.bat" information=release 2>&1) timeout: 30s  
```

## Project Structure

- **cantilever/**: Step-by-step FEA workflow (geometry → model → analysis → post-process)
- **cube/**: Simple compression example
- **TO/**: Topology optimization examples (requires full Abaqus license with Tosca)

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
- Length: mm
- Force: N
- Stress/Modulus: MPa
- Density: tonne/mm³ (e.g., steel = 7.85e-9)

## Limitations

- **Learning Edition**: Limited to 1000 nodes. Increase `MESH_SIZE` if exceeded.
- **Topology Optimization**: Requires full license with Tosca module (not available in Learning Edition).
- **noGUI mode**: Some GUI-only features (viewport operations) don't work headless.

## IDE Support

Install `abqpy` in a separate environment for type hints in VS Code:
```bash
pip install abqpy
```
This provides autocompletion only—scripts must still run through Abaqus.

## PATH Setup

Ensure Abaqus commands are accessible:
```bash
# Add to PATH
C:\SIMULIA\Commands

# Verify installation
abaqus information=release
```