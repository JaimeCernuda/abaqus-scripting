# Abaqus Python Scripting from VS Code

This folder contains examples of how to create Abaqus models programmatically using Python.

## Prerequisites

1. **Abaqus installed** (Learning Edition or full version)
2. **Abaqus command in PATH** (see Setup below)
3. **VS Code** with Python extension

## Setup: Add Abaqus to PATH

### Option 1: Add to System PATH (Recommended)

Add the Abaqus Commands directory to your system PATH:

```
C:\SIMULIA\Commands
```

Or wherever your Abaqus is installed. To verify it works, open a new terminal and type:

```bash
abaqus information=release
```

You should see the Abaqus version info.

### Option 2: Create Environment Variable

Create a system environment variable:
- Name: `ABAQUS_BAT_PATH`  
- Value: `C:\SIMULIA\Commands\abaqus.bat`

## Running the Script

### Method 1: Command Line

Open a terminal in VS Code (`Ctrl+`` `) and run:

```bash
# With GUI (Abaqus CAE will open)
abaqus cae script=create_cube.py

# Without GUI (headless, faster)
abaqus cae noGUI=create_cube.py
```

### Method 2: VS Code Task

1. Press `Ctrl+Shift+B` to see available tasks
2. Select "Run Abaqus Script (headless/noGUI)"
3. Or use `Ctrl+Shift+P` → "Tasks: Run Task"

### Method 3: Batch File

Double-click `run_abaqus_script.bat`

## Understanding the Script

The `create_cube.py` script does the following:

1. Creates a new model called "CubeModel"
2. Creates a 10x10x10 cube using sketch + extrude
3. Defines Steel material (E=210 GPa, ν=0.3)
4. Creates a solid section and assigns it
5. Creates an assembly with one instance
6. Fixes the bottom face (encastre BC)
7. Applies 100 MPa pressure on top face
8. Meshes with ~2.5mm element size
9. Creates a job ready for submission
10. Saves everything to `CubeModel.cae`

## Running the Analysis

After creating the model:

```bash
# Submit the job
abaqus job=CubeAnalysis interactive

# Or with multiple CPUs (not available in Learning Edition)
abaqus job=CubeAnalysis cpus=4 interactive
```

## Reading Results

After the job completes, use `read_results.py`:

```bash
abaqus python read_results.py
```

## File Types

| Extension | Description |
|-----------|-------------|
| `.cae` | Abaqus CAE model database |
| `.inp` | Input file (text, can edit manually) |
| `.odb` | Output database (results) |
| `.sta` | Status file (convergence info) |
| `.msg` | Message file (detailed log) |
| `.dat` | Data file (printed output) |
| `.com` | Command file |
| `.prt` | Part file |

## Tips for VS Code

### Get Autocompletion with abqpy

Install the abqpy package in a separate Python environment:

```bash
pip install abqpy
```

This gives you type hints and autocompletion in VS Code. Note: abqpy is only for 
*writing* scripts - you still need to run them through Abaqus.

### Recommended Extensions

- Python (Microsoft)
- Pylance (for better type hints)

## Common Issues

### "abaqus is not recognized"

The Abaqus Commands directory is not in your PATH. Add it or use the full path:

```bash
"C:\SIMULIA\Commands\abaqus.bat" cae script=create_cube.py
```

### "The learning edition is restricted to 1000 nodes"

Your mesh is too fine. Increase the seed size:

```python
part.seedPart(size=5.0, ...)  # Larger = fewer elements
```

### Script works in CAE but not with noGUI

Some GUI-only features don't work in noGUI mode. Avoid viewport operations
when running headless.
