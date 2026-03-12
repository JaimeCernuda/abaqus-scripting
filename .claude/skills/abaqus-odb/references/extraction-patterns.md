# ODB Extraction Patterns

Practical code patterns for extracting data from Abaqus ODB files. All examples use
`abaqus python script.py` (no CAE required) unless noted otherwise.

## Opening and Closing an ODB

```python
from odbAccess import *
from abaqusConstants import *

# Always use readOnly=True for extraction (prevents locking issues)
odb = openOdb(path='MyJob.odb', readOnly=True)

# ... extract data ...

# Always close when done
odb.close()
```

### Safe Open Pattern (handles lock files)

```python
import os
from odbAccess import openOdb

def safe_open_odb(odb_path):
    """Open an ODB with automatic lock-file cleanup."""
    try:
        return openOdb(odb_path, readOnly=True)
    except Exception as e:
        lock_file = odb_path + '.lck'
        if os.path.exists(lock_file):
            os.remove(lock_file)
            return openOdb(odb_path, readOnly=True)
        raise e
```

## Navigating Steps and Frames

```python
odb = openOdb('MyJob.odb', readOnly=True)

# List all steps
print('Steps:', list(odb.steps.keys()))

# Access a step by name
step = odb.steps['LoadStep']

# Access frames within a step
print('Number of frames:', len(step.frames))

# Last frame (final results)
frame = step.frames[-1]

# First frame (initial state, usually zero)
frame0 = step.frames[0]

# Specific frame by index
frame3 = step.frames[3]

# Frame metadata
print('Frame time:', frame.frameValue)
print('Frame increment:', frame.incrementNumber)
print('Frame description:', frame.description)

# List available field outputs in a frame
print('Fields:', list(frame.fieldOutputs.keys()))
```

### Iterating All Steps and Frames

```python
for step_name, step in odb.steps.items():
    print('Step: {}'.format(step_name))
    for i, frame in enumerate(step.frames):
        print('  Frame {}: time={}'.format(i, frame.frameValue))
        print('    Fields: {}'.format(list(frame.fieldOutputs.keys())))
```

## Extracting Stress (S) -- Von Mises

The most common extraction: find maximum von Mises stress.

```python
# Based on paper_reproduction/experiment4 extract scripts
step = odb.steps['LoadStep']
frame = step.frames[-1]

stress = frame.fieldOutputs['S']
max_mises = 0.0
max_elem = 0
for value in stress.values:
    if value.mises > max_mises:
        max_mises = value.mises
        max_elem = value.elementLabel

print('Max von Mises: {:.2f} MPa at element {}'.format(max_mises, max_elem))
```

### Stress Components

```python
for value in stress.values:
    # Invariants
    mises = value.mises           # Von Mises equivalent stress
    tresca = value.tresca         # Tresca (max shear)
    press = value.press           # Hydrostatic pressure (negative = tension)
    max_p = value.maxPrincipal    # Maximum principal stress
    mid_p = value.midPrincipal    # Middle principal stress
    min_p = value.minPrincipal    # Minimum principal stress

    # Raw tensor components (order: S11, S22, S33, S12, S13, S23 for 3D)
    components = value.data
```

## Extracting Displacement (U)

```python
disp = frame.fieldOutputs['U']

# Maximum displacement magnitude
max_mag = 0.0
max_node = 0
for value in disp.values:
    if value.magnitude > max_mag:
        max_mag = value.magnitude
        max_node = value.nodeLabel

print('Max displacement: {:.4f} mm at node {}'.format(max_mag, max_node))
```

### Displacement Components

```python
for value in disp.values:
    u1 = value.data[0]       # X displacement
    u2 = value.data[1]       # Y displacement
    u3 = value.data[2]       # Z displacement (3D only)
    mag = value.magnitude     # Total magnitude
    node = value.nodeLabel    # Node label
```

### Maximum in a Specific Direction

```python
# From experiment4: max Y-displacement
max_u2 = 0.0
for value in disp.values:
    if abs(value.data[1]) > abs(max_u2):
        max_u2 = value.data[1]
print('Max Y displacement: {:.4f} mm'.format(max_u2))
```

## Extracting Reaction Forces (RF)

```python
rf = frame.fieldOutputs['RF']

# Sum reaction forces at a boundary (total applied load check)
total_rf1 = 0.0
total_rf2 = 0.0
total_rf3 = 0.0
for value in rf.values:
    total_rf1 += value.data[0]
    total_rf2 += value.data[1]
    if len(value.data) > 2:
        total_rf3 += value.data[2]

print('Total RF: ({:.1f}, {:.1f}, {:.1f}) N'.format(
    total_rf1, total_rf2, total_rf3))
```

### Reaction Forces at a Specific Node Set

```python
# Get subset for a specific region
bc_set = odb.rootAssembly.nodeSets['FIXEDEND']
rf_subset = rf.getSubset(region=bc_set)

total = [0.0, 0.0, 0.0]
for value in rf_subset.values:
    for i in range(len(value.data)):
        total[i] += value.data[i]

print('Reaction at FixedEnd: ({:.1f}, {:.1f}, {:.1f}) N'.format(*total))
```

## Extracting Plastic Strain (PEEQ)

```python
# From experiment4: equivalent plastic strain
peeq = frame.fieldOutputs['PEEQ']
max_peeq = 0.0
for value in peeq.values:
    if value.data > max_peeq:
        max_peeq = value.data

print('Max PEEQ: {:.6f}'.format(max_peeq))
if max_peeq > 0.0:
    print('Plastic deformation has occurred')
```

## Extracting Eigenfrequencies (Modal Analysis)

```python
step = odb.steps['FreqStep']
print('Number of modes: {}'.format(len(step.frames) - 1))  # frame 0 is initial

for i, frame in enumerate(step.frames):
    if i == 0:
        continue  # skip initial frame
    # Parse frequency from description: "Mode X:  freq = Y"
    desc = frame.description
    print('Mode {}: {}'.format(i, desc))

    # Access mode shape (displacement pattern)
    mode_shape = frame.fieldOutputs['U']
    max_mag = max(v.magnitude for v in mode_shape.values)
    print('  Max normalized displacement: {:.6f}'.format(max_mag))
```

## Extracting Energy Outputs

```python
# Strain energy density per element
if 'ENER' in frame.fieldOutputs:
    ener = frame.fieldOutputs['ENER']
    total_se = sum(v.data[0] for v in ener.values)  # SENER component
    print('Total strain energy: {:.4f}'.format(total_se))
```

## Complete Extraction Script Template

Based on the proven pattern from experiment4:

```python
"""Extract results from an Abaqus ODB file.
Run with: abaqus python extract_results.py
"""
import os
from odbAccess import *
from abaqusConstants import *

# Configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, os.pardir))
os.chdir(PROJECT_DIR)

ODB_NAME = 'MyJob.odb'
STEP_NAME = 'LoadStep'

# Open ODB
odb = openOdb(os.path.join(PROJECT_DIR, ODB_NAME), readOnly=True)

step = odb.steps[STEP_NAME]
frame = step.frames[-1]

# Extract stress
stress = frame.fieldOutputs['S']
max_mises = 0.0
for value in stress.values:
    if value.mises > max_mises:
        max_mises = value.mises

# Extract displacement
disp = frame.fieldOutputs['U']
max_disp = 0.0
for value in disp.values:
    if value.magnitude > max_disp:
        max_disp = value.magnitude

# Write results
with open('results.txt', 'w') as f:
    f.write('Results: {}\n'.format(ODB_NAME))
    f.write('=' * 50 + '\n')
    f.write('Max von Mises stress: {:.2f} MPa\n'.format(max_mises))
    f.write('Max displacement: {:.4f} mm\n'.format(max_disp))

odb.close()
print('Results written to results.txt')
```

## FieldValue Object Members

Every `FieldValue` object (from `field.values`) has these members:

| Member | Type | Description |
|--------|------|-------------|
| `nodeLabel` | int | Node number (nodal fields) |
| `elementLabel` | int | Element number (element fields) |
| `instance` | OdbInstance | Part instance this value belongs to |
| `position` | SymbolicConstant | NODAL, INTEGRATION_POINT, CENTROID, ELEMENT_NODAL |
| `data` | array | Raw component values |
| `magnitude` | float | Vector magnitude (displacement, force) |
| `mises` | float | Von Mises equivalent (stress only) |
| `tresca` | float | Tresca equivalent (stress only) |
| `press` | float | Hydrostatic pressure (stress only) |
| `maxPrincipal` | float | Max principal value (stress/strain) |
| `midPrincipal` | float | Mid principal value |
| `minPrincipal` | float | Min principal value |
| `integrationPoint` | int | Integration point number |
| `sectionPoint` | SectionPoint | Section point (shells) |
| `face` | SymbolicConstant | Element face |
| `localCoordSystem` | tuple | Local coordinate system |
