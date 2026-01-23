# Cantilever Beam - Abaqus Python Scripting Workflow

A step-by-step demonstration of finite element analysis using the Abaqus Scripting Interface.
```
    FIXED                                                    LOAD
    (Encastre)                                               ↓ 1000 N
    ▓▓▓▓▓╔════════════════════════════════════════════════════╗
    ▓▓▓▓▓║                                                    ║
    ▓▓▓▓▓║              STEEL BEAM                            ║
    ▓▓▓▓▓║              100 × 10 × 10 mm                      ║
    ▓▓▓▓▓║                                                    ║
    ▓▓▓▓▓╚════════════════════════════════════════════════════╝
    x=0                                                    x=100
```

---

## Files

| File | Description |
|------|-------------|
| `01_create_geometry.py` | Creates beam geometry only |
| `02_define_model.py` | Geometry + material + BCs + loads + mesh (no run) |
| `03_run_analysis.py` | Complete workflow: build model and run analysis |
| `04_analyze_results.py` | Post-process ODB and extract results |

---

## Quick Start

### Run the full analysis:
```cmd
abaqus cae script=03_run_analysis.py
```

### View results in GUI:
```cmd
abaqus cae database=CantileverBeam.odb
```

### Extract results to text:
```cmd
abaqus python 04_analyze_results.py
```

---

## Script Progression

Each script builds on the previous, demonstrating the FEA workflow:

### Script 01: Geometry Only
```cmd
abaqus cae noGUI=01_create_geometry.py
```

**Creates:**
- Part geometry (100×10×10 mm rectangular beam)

**Does NOT create:**
- Material, sections, BCs, loads, mesh, job

**Output:** `CantileverBeam_Geometry.cae`

---

### Script 02: Model Definition (No Run)
```cmd
abaqus cae noGUI=02_define_model.py
```

**Creates:**
- Geometry
- Material (Steel: E=210 GPa, ν=0.3)
- Section assignment
- Assembly instance
- Analysis step (Static)
- Boundary condition (Encastre at x=0)
- Load (SurfaceTraction at x=100)
- Mesh (C3D8R elements)
- Job definition
- Input file (.inp)

**Does NOT:**
- Submit the job

**Output:** `CantileverBeam_Defined.cae`, `CantileverBeam.inp`

---

### Script 03: Full Analysis
```cmd
abaqus cae script=03_run_analysis.py
```

**Creates everything from Script 02, plus:**
- Submits job to solver
- Waits for completion
- Generates results

**Output:** `CantileverBeam.cae`, `CantileverBeam.inp`, `CantileverBeam.odb`, `.dat`, `.msg`, `.sta`

---

### Script 04: Post-Processing
```cmd
abaqus python 04_analyze_results.py
```

**Reads the ODB and extracts:**
- Displacement field (max magnitude, location)
- Stress field (max von Mises, location)
- Reaction forces (totals)
- Mesh info

**Output:** `CantileverBeam_report.txt`

---

## Parameters

All scripts use consistent parameters (edit at top of each file):
```python
# Geometry (mm)
BEAM_LENGTH = 100.0
BEAM_HEIGHT = 10.0
BEAM_WIDTH = 10.0

# Material (Steel)
YOUNGS_MODULUS = 210000.0  # MPa
POISSONS_RATIO = 0.3
DENSITY = 7.85e-9          # tonne/mm³

# Loading
APPLIED_FORCE = -1000.0    # N (negative = downward Y)

# Mesh
MESH_SIZE = 5.0            # mm
```

---

## Expected Results

| Quantity | FEA Result | Analytical (Beam Theory) |
|----------|------------|--------------------------|
| Max Deflection | ~0.19 mm | 0.190 mm |
| Max Stress | ~60 MPa | 60.0 MPa |
| Reaction Force (Y) | 1000 N | 1000 N |

### Analytical Formulas
```
I = bh³/12 = 10×10³/12 = 833.33 mm⁴

Max deflection:  δ = PL³/(3EI) = 1000×100³/(3×210000×833.33) = 0.190 mm
Max stress:      σ = PLc/I = 1000×100×5/833.33 = 60 MPa
```

---

## Output Files

After running Script 03:

| File | Description |
|------|-------------|
| `CantileverBeam.cae` | Model database (open in CAE) |
| `CantileverBeam.inp` | Input file (text, editable) |
| `CantileverBeam.odb` | Results database (open in Viewer) |
| `CantileverBeam.dat` | Printed output |
| `CantileverBeam.msg` | Solver messages |
| `CantileverBeam.sta` | Status/convergence info |

---

## Viewing Results in Abaqus/CAE

1. Open results:
```cmd
   abaqus cae database=CantileverBeam.odb
```

2. Show deformed shape with stress contours:
   - Plot → Contours → On Deformed Shape
   - Or click the rainbow icon in toolbar

3. Change displayed variable:
   - Results → Field Output
   - Select `S` (stress) or `U` (displacement)

4. Show specific component:
   - Results → Field Output → S → S11 (axial stress)
   - Results → Field Output → U → U2 (vertical displacement)

---

## Troubleshooting

### "abaqus is not recognized"

Add to PATH:
```cmd
set PATH=%PATH%;C:\SIMULIA\Commands
```

### "Learning edition is restricted to 1000 nodes"

Increase mesh size:
```python
MESH_SIZE = 10.0  # was 5.0
```

### No .odb file generated

Check for errors:
```cmd
type CantileverBeam.msg
type CantileverBeam.dat
```

### GUI closes immediately

Use `noGUI=` instead of `script=`:
```cmd
abaqus cae noGUI=03_run_analysis.py
abaqus cae database=CantileverBeam.odb
```