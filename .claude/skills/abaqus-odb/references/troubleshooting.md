# ODB Troubleshooting

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| "ODB not found" | Wrong path | Check file exists and path is correct |
| "Key not found" | Wrong step/field name | List available: `odb.steps.keys()` |
| "No mises attribute" | Not stress data | Only stress field has mises |
| "Permission denied" | ODB locked | Close CAE or use readOnly=True |
| "ODB locked" | Another process has it | Delete .lck file or close other sessions |
| "No values" | Output not requested | Check FieldOutputRequest in model |
| "AttributeError: mises" | Element type issue | Check element formulation supports mises |

## List Available Data

```python
# List all steps
print("Steps:", list(odb.steps.keys()))

# List all field outputs in a frame
print("Fields:", list(frame.fieldOutputs.keys()))

# List all history regions
print("History regions:", list(step.historyRegions.keys()))

# List history outputs for a region
region = step.historyRegions.values()[0]
print("History outputs:", list(region.historyOutputs.keys()))

# List node/element sets
print("Node sets:", list(odb.rootAssembly.nodeSets.keys()))
print("Element sets:", list(odb.rootAssembly.elementSets.keys()))
```

## Debugging ODB Structure

```python
# Print ODB info
def debug_odb(odb):
    print(f"ODB: {odb.name}")
    print(f"Steps: {list(odb.steps.keys())}")

    for step_name, step in odb.steps.items():
        print(f"\nStep '{step_name}':")
        print(f"  Frames: {len(step.frames)}")
        print(f"  History regions: {len(step.historyRegions)}")

        if step.frames:
            frame = step.frames[-1]
            print(f"  Field outputs: {list(frame.fieldOutputs.keys())}")
```

## Memory Issues

Large ODBs can cause memory problems. Mitigations:

```python
# Process in chunks
field = frame.fieldOutputs['U']
chunk_size = 10000
values = field.values

for i in range(0, len(values), chunk_size):
    chunk = values[i:i+chunk_size]
    # Process chunk
    for v in chunk:
        pass  # Your processing here

# Use getSubset to limit data
nodeSet = odb.rootAssembly.nodeSets['SMALL_REGION']
subset = field.getSubset(region=nodeSet)

# Always close ODB when done
odb.close()
```

## Lock File Issues

If ODB is locked:

1. Check if Abaqus CAE has it open
2. Delete the `.lck` file: `MyJob.odb.lck`
3. Use `readOnly=True` when opening

```python
# Safe opening pattern
try:
    odb = openOdb('MyJob.odb', readOnly=True)
except Exception as e:
    print(f"Failed to open ODB: {e}")
    # Try deleting lock file
    import os
    lock_file = 'MyJob.odb.lck'
    if os.path.exists(lock_file):
        os.remove(lock_file)
        odb = openOdb('MyJob.odb', readOnly=True)
```

## Missing Field Outputs

If expected fields are missing:

1. Check the FieldOutputRequest in the model
2. Verify the step completed successfully
3. Check if output was requested for that step

```python
# Check what's available
for step_name, step in odb.steps.items():
    print(f"\nStep: {step_name}")
    for i, frame in enumerate(step.frames):
        print(f"  Frame {i}: {list(frame.fieldOutputs.keys())}")
```
