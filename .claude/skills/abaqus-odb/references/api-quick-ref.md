# ODB API Quick Reference

## Open/Close ODB

```python
from odbAccess import openOdb
odb = openOdb('file.odb', readOnly=True)
# ... work with data
odb.close()
```

## Navigate Structure

```python
odb.steps['StepName']           # Access step
step.frames[-1]                  # Last frame
step.frames[0]                   # First frame
frame.fieldOutputs['U']          # Displacement field
frame.fieldOutputs['S']          # Stress field
frame.fieldOutputs['RF']         # Reaction force
```

## Field Output Values

```python
field = frame.fieldOutputs['U']
for value in field.values:
    value.nodeLabel              # Node ID
    value.data                   # (u1, u2, u3) tuple
    value.magnitude              # sqrt(u1^2+u2^2+u3^2)

stress = frame.fieldOutputs['S']
for value in stress.values:
    value.elementLabel           # Element ID
    value.mises                  # von Mises stress
    value.data                   # (S11, S22, S33, S12, S13, S23)
```

## History Output

```python
region = odb.steps['Step'].historyRegions['Node ASSEMBLY.1']
data = region.historyOutputs['U1'].data  # List of (time, value)
```

## Subset by Region

```python
nodeSet = odb.rootAssembly.nodeSets['SET_NAME']
subset = field.getSubset(region=nodeSet)
```

## Common Field Output Keys

| Key | Description |
|-----|-------------|
| U | Displacement |
| S | Stress |
| E | Strain |
| RF | Reaction force |
| CF | Concentrated force |
| COORD | Nodal coordinates |
| NT | Nodal temperature |
| PEEQ | Equivalent plastic strain |

## Frame Attributes

```python
frame.frameId                    # Frame number
frame.frameValue                 # Time or frequency value
frame.description                # Description string (useful for modal)
frame.fieldOutputs.keys()        # List available fields
```
