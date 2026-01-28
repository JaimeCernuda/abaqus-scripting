---
name: abaqus-export
description: Export Abaqus geometry and results to external formats - STL, STEP, INP, images, and data files.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
---

# Abaqus Export Skill

## When to Use This Skill

**USE when you need to:**
- Export part geometry to STEP/IGES for CAD
- Export mesh to STL for 3D printing
- Write input file (.inp) for external submission
- Export results to CSV for analysis
- Export topology optimization result as STL
- Generate images from CAE

**Do NOT use for:**
- Reading ODB results → use `/abaqus-odb`
- Importing CAD files → use `/abaqus-geometry`
- Running analysis → use `/abaqus-job`

## Key Decisions

### Export Format Selection

| Format | Use Case |
|--------|----------|
| STEP | CAD import, further design work |
| IGES | Legacy CAD systems |
| STL | 3D printing, visualization |
| INP | External Abaqus submission |
| CSV | Data analysis, spreadsheets |
| PNG/SVG | Reports, presentations |

## Required Inputs

| Input | Required |
|-------|----------|
| Source (part, ODB) | YES |
| Output path | YES |
| Format | YES |

## Common Patterns

### Export Part to STEP
```python
part = mdb.models['Model'].parts['Part-1']
part.writeStepFile('part_export.step')
```

### Export Part to IGES
```python
part.writeIgesFile('part_export.igs')
```

### Write Input File
```python
job = mdb.Job(name='Export', model='Model')
job.writeInput(consistencyChecking=OFF)
# Creates Export.inp
```

### Export Field Data to CSV
```python
from odbAccess import openOdb
import csv

odb = openOdb('job.odb', readOnly=True)
frame = odb.steps['LoadStep'].frames[-1]

with open('displacements.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['NodeID', 'U1', 'U2', 'U3', 'Magnitude'])

    for value in frame.fieldOutputs['U'].values:
        writer.writerow([
            value.nodeLabel,
            value.data[0], value.data[1], value.data[2],
            value.magnitude
        ])

odb.close()
```

### Export Stress to CSV
```python
with open('stress.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ElementID', 'Mises'])

    for value in frame.fieldOutputs['S'].values:
        if hasattr(value, 'mises'):
            writer.writerow([value.elementLabel, value.mises])
```

### Export TO Result to STL (GUI)

After topology optimization:
1. Open: `Optimization/TOSCA_POST/Optimization.odb`
2. Go to Optimization module
3. Select Optimization > Extract > STL
4. Set density threshold (0.3-0.5)
5. Export

### Export TO Result Script
```python
# Run in CAE with GUI
session.openOdb(name='Optimization/TOSCA_POST/Optimization.odb')

session.writeStlFiles(
    odbPath='Optimization/TOSCA_POST/Optimization.odb',
    outputPath='optimized.stl',
    threshold=0.3  # Density threshold
)
```

### Export Image from CAE
```python
# Requires GUI session
session.printOptions.setValues(rendition=COLOR, vpDecorations=OFF)
session.printToFile(fileName='result_image', format=PNG, canvasObjects=(vp,))

# High resolution
session.printToFile(
    fileName='result_hq',
    format=PNG,
    resolution=300  # DPI
)

# Vector format
session.printToFile(fileName='result_vector', format=SVG)
```

### Batch Export Results
```python
import os
from odbAccess import openOdb

def export_summary(odb_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    job_name = os.path.splitext(os.path.basename(odb_path))[0]
    odb = openOdb(odb_path, readOnly=True)

    with open(os.path.join(output_dir, f'{job_name}_summary.txt'), 'w') as f:
        for step_name, step in odb.steps.items():
            frame = step.frames[-1]
            f.write(f"Step: {step_name}\n")

            if 'U' in frame.fieldOutputs:
                max_u = max(v.magnitude for v in frame.fieldOutputs['U'].values)
                f.write(f"  Max displacement: {max_u:.6f} mm\n")

            if 'S' in frame.fieldOutputs:
                max_s = max(v.mises for v in frame.fieldOutputs['S'].values
                           if hasattr(v, 'mises'))
                f.write(f"  Max von Mises: {max_s:.2f} MPa\n")

    odb.close()
```

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Cannot write STL - no mesh" | Part not meshed | Mesh part first |
| "STEP export failed" | Invalid geometry | Try IGES instead |
| "Large file size" | Fine mesh | Coarsen for visualization |

## API Reference

For detailed parameters:
- [Part API](../../docs/abaqus-api/modules/part.md)
- [ODB API](../../docs/abaqus-api/modules/odb.md)
