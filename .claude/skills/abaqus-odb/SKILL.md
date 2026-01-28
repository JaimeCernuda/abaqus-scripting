---
name: abaqus-odb
description: Extract and analyze results from Abaqus ODB files - field outputs, history outputs, and post-processing operations.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
  - Bash(python:*)
---

# Abaqus ODB Skill

## When to Use This Skill

**USE when you need to:**
- Extract maximum stress/displacement values
- Read reaction forces
- Get nodal/element results at specific locations
- Export results to CSV or text
- Extract eigenfrequencies from modal analysis
- Generate analysis reports
- Process time history data

**Do NOT use for:**
- Running the analysis → use `/abaqus-job`
- Configuring output requests → use `/abaqus-output`
- Exporting geometry (STL, STEP) → use `/abaqus-export`

## Key Decisions

### 1. What to Extract?

| Goal | Field/Method |
|------|--------------|
| Maximum stress | S → find max mises |
| Maximum displacement | U → find max magnitude |
| Reaction forces | RF → sum all values |
| Eigenfrequencies | Frame descriptions |
| Time history | historyOutputs |

### 2. Read-Only vs Modify

| Purpose | Mode |
|---------|------|
| Extract data | readOnly=True |
| Add custom fields | readOnly=False |

## Required Inputs

| Input | Required |
|-------|----------|
| ODB path | YES |
| Step name | YES (for specific step) |
| Variable names | YES (S, U, RF, etc.) |

## Common Patterns

### Open ODB
```python
from odbAccess import openOdb

odb = openOdb('MyJob.odb', readOnly=True)
# ... work with ODB
odb.close()
```

### Find Maximum Displacement
```python
step = odb.steps['LoadStep']
frame = step.frames[-1]  # Last frame

disp_field = frame.fieldOutputs['U']
max_disp = max(v.magnitude for v in disp_field.values)
print(f"Max displacement: {max_disp:.6f} mm")
```

### Find Maximum Von Mises Stress
```python
stress_field = frame.fieldOutputs['S']
max_mises = max(v.mises for v in stress_field.values if hasattr(v, 'mises'))
print(f"Max von Mises: {max_mises:.2f} MPa")
```

### Sum Reaction Forces
```python
rf_field = frame.fieldOutputs['RF']
total_rf = [0.0, 0.0, 0.0]
for value in rf_field.values:
    total_rf[0] += value.data[0]
    total_rf[1] += value.data[1]
    total_rf[2] += value.data[2]
print(f"Total reaction: {total_rf}")
```

### Extract at Specific Node
```python
node_label = 100
for value in frame.fieldOutputs['U'].values:
    if value.nodeLabel == node_label:
        print(f"Node {node_label}: U = {value.data}")
        break
```

### Extract from Set
```python
instance = odb.rootAssembly.instances['PART-1']
node_set = instance.nodeSets['MYREGION']
subset = frame.fieldOutputs['U'].getSubset(region=node_set)
for value in subset.values:
    print(f"Node {value.nodeLabel}: {value.data}")
```

### Get Eigenfrequencies (Modal)
```python
step = odb.steps['Frequency']
frequencies = []
for frame in step.frames:
    if frame.description:
        freq = float(frame.description.split('=')[-1].strip())
        frequencies.append(freq)
print(f"Natural frequencies: {frequencies}")
```

### History Output
```python
history_region = odb.steps['LoadStep'].historyRegions['Node ASSEMBLY.1']
u2_data = history_region.historyOutputs['U2'].data
for time, value in u2_data:
    print(f"Time {time}: U2 = {value}")
```

### Export to CSV
```python
import csv

with open('results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['NodeID', 'U1', 'U2', 'U3', 'Magnitude'])

    for value in frame.fieldOutputs['U'].values:
        writer.writerow([
            value.nodeLabel,
            value.data[0], value.data[1], value.data[2],
            value.magnitude
        ])
```

### Generate Summary Report
```python
def generate_report(odb_path):
    odb = openOdb(odb_path, readOnly=True)

    for step_name, step in odb.steps.items():
        frame = step.frames[-1]
        print(f"\nStep: {step_name}")

        if 'U' in frame.fieldOutputs:
            max_u = max(v.magnitude for v in frame.fieldOutputs['U'].values)
            print(f"  Max displacement: {max_u:.6f} mm")

        if 'S' in frame.fieldOutputs:
            max_s = max(v.mises for v in frame.fieldOutputs['S'].values
                       if hasattr(v, 'mises'))
            print(f"  Max von Mises: {max_s:.2f} MPa")

    odb.close()
```

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "ODB locked" | Another process has it | Delete .lck file or close other sessions |
| "Key not found" | Wrong variable name | List available keys first |
| "No values" | Output not requested | Check FieldOutputRequest |
| "AttributeError: mises" | Element type doesn't have mises | Check element formulation |

## API Reference

For detailed parameters: [ODB API](../../docs/abaqus-api/modules/odb.md)
