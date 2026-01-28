# Common Export Patterns

## Full Results CSV (Displacement + Stress)
```python
import csv
from odbAccess import openOdb

odb = openOdb('Model.odb', readOnly=True)
frame = odb.steps['Load'].frames[-1]

# Export displacements
with open('displacements.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Node', 'U1', 'U2', 'U3', 'Magnitude'])
    for v in frame.fieldOutputs['U'].values:
        writer.writerow([v.nodeLabel, v.data[0], v.data[1], v.data[2], v.magnitude])

# Export stresses
with open('stresses.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Element', 'IntPt', 'S11', 'S22', 'S33', 'S12', 'Mises'])
    for v in frame.fieldOutputs['S'].values:
        if hasattr(v, 'mises'):
            writer.writerow([
                v.elementLabel, v.integrationPoint,
                v.data[0], v.data[1], v.data[2], v.data[3],
                v.mises
            ])

odb.close()
```

## Time History Export
```python
region = odb.steps['Load'].historyRegions['Node ASSEMBLY.1']
history = region.historyOutputs['U2'].data

with open('history.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Time', 'U2'])
    for time, value in history:
        writer.writerow([time, value])
```

## Export All Frames (Time Series)
```python
import csv
from odbAccess import openOdb

odb = openOdb('Model.odb', readOnly=True)
step = odb.steps['Load']

with open('time_series.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Frame', 'Time', 'MaxDisp', 'MaxMises'])

    for i, frame in enumerate(step.frames):
        max_u = max(v.magnitude for v in frame.fieldOutputs['U'].values)
        max_s = max(v.mises for v in frame.fieldOutputs['S'].values if hasattr(v, 'mises'))
        writer.writerow([i, frame.frameValue, max_u, max_s])

odb.close()
```

## STL for 3D Printing
```python
# Export each part in the model
model = mdb.models['Model']
for name, part in model.parts.items():
    if len(part.elements) > 0:  # Only meshed parts
        part.writeStlFile(fileName=f'{name}.stl', precision='double')
        print(f"Exported {name}.stl")
```

## Export Deformed Shape to STL
```python
from odbAccess import openOdb
from visualization import *

# Open ODB and set deformed view
odb = openOdb('Model.odb')
vp = session.viewports['Viewport: 1']
vp.setValues(displayedObject=odb)
vp.odbDisplay.display.setValues(plotState=(DEFORMED,))
vp.odbDisplay.commonOptions.setValues(deformationScaling=UNIFORM, uniformScaleFactor=1.0)

# Export STL from deformed shape (requires GUI)
# Note: Native writeStlFile exports undeformed; use Report tool for deformed
```

## Abaqus Report File
```python
# Use session.writeFieldReport in CAE
session.writeFieldReport(
    fileName='report.rpt',
    append=OFF,
    odb=odb,
    step=0, frame=-1,
    outputPosition=NODAL,
    variable=(
        ('S', INTEGRATION_POINT, ((INVARIANT, 'Mises'),)),
        ('U', NODAL, ((COMPONENT, 'U1'), (COMPONENT, 'U2'), (COMPONENT, 'U3'))),
    )
)
```

## Export Mesh to Separate Node/Element Files
```python
part = mdb.models['Model'].parts['Part-1']

# Export nodes
with open('nodes.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['NodeLabel', 'X', 'Y', 'Z'])
    for node in part.nodes:
        writer.writerow([node.label, node.coordinates[0], node.coordinates[1], node.coordinates[2]])

# Export elements
with open('elements.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ElementLabel', 'Type', 'Connectivity'])
    for elem in part.elements:
        conn_str = ' '.join(str(n) for n in elem.connectivity)
        writer.writerow([elem.label, elem.type.name, conn_str])
```

## Export Sets and Surfaces
```python
part = mdb.models['Model'].parts['Part-1']

with open('sets.txt', 'w') as f:
    # Node sets
    f.write("=== NODE SETS ===\n")
    for name, nset in part.sets.items():
        if hasattr(nset, 'nodes') and len(nset.nodes) > 0:
            labels = [n.label for n in nset.nodes]
            f.write(f"{name}: {labels}\n")

    # Element sets
    f.write("\n=== ELEMENT SETS ===\n")
    for name, eset in part.sets.items():
        if hasattr(eset, 'elements') and len(eset.elements) > 0:
            labels = [e.label for e in eset.elements]
            f.write(f"{name}: {labels}\n")
```

## Batch Export Multiple ODBs
```python
import os
import glob
from odbAccess import openOdb

odb_files = glob.glob('*.odb')

for odb_path in odb_files:
    job_name = os.path.splitext(odb_path)[0]
    odb = openOdb(odb_path, readOnly=True)

    # Get last frame of last step
    last_step = list(odb.steps.values())[-1]
    frame = last_step.frames[-1]

    # Export summary
    with open(f'{job_name}_summary.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Metric', 'Value'])

        if 'U' in frame.fieldOutputs:
            max_u = max(v.magnitude for v in frame.fieldOutputs['U'].values)
            writer.writerow(['Max Displacement (mm)', max_u])

        if 'S' in frame.fieldOutputs:
            max_s = max(v.mises for v in frame.fieldOutputs['S'].values if hasattr(v, 'mises'))
            writer.writerow(['Max von Mises (MPa)', max_s])

    odb.close()
    print(f"Processed {odb_path}")
```

## Export for External Solvers (INP + Data)
```python
# Generate input file
job = mdb.Job(name='ForExport', model='Model')
job.writeInput()

# Read and extract specific sections
with open('ForExport.inp', 'r') as f:
    inp_content = f.read()

# Find and save node definitions
import re
node_section = re.search(r'\*Node(.*?)\*', inp_content, re.DOTALL)
if node_section:
    with open('nodes_only.inp', 'w') as f:
        f.write('*Node\n')
        f.write(node_section.group(1))
```

## Export Reaction Forces
```python
from odbAccess import openOdb

odb = openOdb('Model.odb', readOnly=True)
frame = odb.steps['Load'].frames[-1]

with open('reactions.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Node', 'RF1', 'RF2', 'RF3', 'Magnitude'])

    if 'RF' in frame.fieldOutputs:
        for v in frame.fieldOutputs['RF'].values:
            writer.writerow([
                v.nodeLabel,
                v.data[0], v.data[1], v.data[2],
                v.magnitude
            ])

odb.close()
```

## Export Contact Results
```python
with open('contact.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Node', 'CPRESS', 'CSHEAR1', 'CSHEAR2'])

    if 'CPRESS' in frame.fieldOutputs:
        for v in frame.fieldOutputs['CPRESS'].values:
            writer.writerow([v.nodeLabel, v.data])

    # Or combined contact output
    if 'CSTRESS' in frame.fieldOutputs:
        for v in frame.fieldOutputs['CSTRESS'].values:
            writer.writerow([v.nodeLabel] + list(v.data))
```

## Export Optimization Density Field
```python
from odbAccess import openOdb

odb = openOdb('Optimization/TOSCA_POST/Optimization.odb', readOnly=True)
frame = odb.steps['Optimization'].frames[-1]

with open('density.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Element', 'Density'])

    if 'DENSITY' in frame.fieldOutputs:
        for v in frame.fieldOutputs['DENSITY'].values:
            writer.writerow([v.elementLabel, v.data])

odb.close()
```
