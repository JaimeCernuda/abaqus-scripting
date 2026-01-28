# Export API Quick Reference

## STL Export (for 3D printing, CAD)
```python
# From Part
part.writeStlFile(fileName='output.stl', precision='double')

# From Instance
instance.writeStlFile(fileName='output.stl')

# Parameters
#   fileName (str): Output file path
#   precision (str): 'single' or 'double' (double recommended for quality)
```

## STEP Export
```python
part.writeStepFile('output.step')

# Parameters
#   fileName (str): Output file path (required)
```

## IGES Export
```python
part.writeIgesFile('output.igs')

# Parameters
#   fileName (str): Output file path (required)
```

## ACIS (SAT) Export
```python
# Part level
part.writeAcisFile('output.sat')

# Assembly level
assembly.writeAcisFile(fileName='output.sat')
```

## Input File (INP)
```python
job = mdb.Job(name='Model', model='ModelName')
job.writeInput()  # Creates Model.inp

# With options
job.writeInput(consistencyChecking=OFF)

# Parameters
#   consistencyChecking: ON or OFF (skip model validation)
```

## ODB to CSV
```python
import csv
from odbAccess import openOdb

odb = openOdb('result.odb', readOnly=True)
frame = odb.steps['Load'].frames[-1]

with open('stress.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Element', 'Mises'])
    for v in frame.fieldOutputs['S'].values:
        if hasattr(v, 'mises'):
            writer.writerow([v.elementLabel, v.mises])
odb.close()
```

## Displacement Export
```python
with open('displacement.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Node', 'U1', 'U2', 'U3', 'Magnitude'])
    for v in frame.fieldOutputs['U'].values:
        writer.writerow([
            v.nodeLabel,
            v.data[0], v.data[1], v.data[2],
            v.magnitude
        ])
```

## Mesh Export (nodes and elements)
```python
with open('mesh.csv', 'w') as f:
    # Nodes
    for node in part.nodes:
        f.write(f"NODE,{node.label},{node.coordinates[0]},{node.coordinates[1]},{node.coordinates[2]}\n")
    # Elements
    for elem in part.elements:
        f.write(f"ELEM,{elem.label},{','.join(str(n) for n in elem.connectivity)}\n")
```

## Image Export (requires GUI)
```python
# Basic PNG
session.printToFile(fileName='image', format=PNG)

# High resolution PNG
session.printToFile(fileName='image_hq', format=PNG, resolution=300)

# Vector SVG
session.printToFile(fileName='image', format=SVG)

# Print options
session.printOptions.setValues(
    rendition=COLOR,           # COLOR, GREYSCALE, BLACK_AND_WHITE
    vpDecorations=OFF,         # Hide viewport decorations
    vpBackground=ON            # Include background
)
```

## Report File Export
```python
session.writeFieldReport(
    fileName='report.rpt',
    append=OFF,
    odb=odb,
    step=0,
    frame=-1,
    outputPosition=NODAL,      # or INTEGRATION_POINT, ELEMENT_NODAL
    variable=(
        ('S', INTEGRATION_POINT, ((INVARIANT, 'Mises'),)),
        ('U', NODAL, ((COMPONENT, 'U3'),)),
    )
)
```

## XY Data Export
```python
# Export XY data to file
session.writeXYReport(
    fileName='xy_data.rpt',
    appendMode=OFF,
    xyData=(xy_data,)
)
```

## Full Parameter Reference

### writeStlFile
| Parameter | Type | Description |
|-----------|------|-------------|
| fileName | str | Output file path (required) |
| precision | str | 'single' or 'double' |

### writeStepFile
| Parameter | Type | Description |
|-----------|------|-------------|
| fileName | str | Output file path (required) |

### writeIgesFile
| Parameter | Type | Description |
|-----------|------|-------------|
| fileName | str | Output file path (required) |

### writeAcisFile
| Parameter | Type | Description |
|-----------|------|-------------|
| fileName | str | Output file path (required) |
| version | float | ACIS version (e.g., 7.0) |

### printToFile
| Parameter | Type | Description |
|-----------|------|-------------|
| fileName | str | Output file path (required) |
| format | constant | PNG, SVG, EPS, TIFF, PS |
| resolution | int | DPI (for raster formats) |
| canvasObjects | tuple | Viewports to capture |

### writeFieldReport
| Parameter | Type | Description |
|-----------|------|-------------|
| fileName | str | Output file path (required) |
| append | constant | ON or OFF |
| odb | Odb | ODB object |
| step | int | Step index |
| frame | int | Frame index (-1 for last) |
| outputPosition | constant | NODAL, INTEGRATION_POINT |
| variable | tuple | Variables to export |
