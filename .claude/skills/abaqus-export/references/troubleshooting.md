# Export Troubleshooting

## Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "Part has no mesh" | Unmeshed part | Mesh the part before STL export |
| "Cannot write STL - no mesh" | Part not meshed | Use `/abaqus-mesh` to mesh first |
| "STEP export failed" | Complex or invalid geometry | Simplify geometry or use IGES/SAT |
| "File permission denied" | File open in another program | Close Excel/CAD and retry |
| "Invalid filename" | Special characters in path | Use simple alphanumeric names |
| "ODB is read-only" | Opened with readOnly=True | This is normal for export operations |
| "Key error: 'S'" | Field output not requested | Add stress output in step definition |
| "No such step" | Step name mismatch | Check `odb.steps.keys()` for names |
| "Large STL file" | Very fine mesh | Coarsen mesh or reduce precision |

## Format Selection Guide

| Format | Use For | File Size | Quality |
|--------|---------|-----------|---------|
| STL | 3D printing, visualization | Large | Mesh-dependent |
| STEP | CAD exchange, further design | Medium | Parametric |
| IGES | Legacy CAD systems | Medium | Good |
| SAT | ACIS-based CAD | Medium | Good |
| INP | Solver input, archival | Small | Full model |
| CSV | Data analysis, Excel | Small | Full precision |
| RPT | Formatted reports | Small | Text only |
| PNG | Presentations (raster) | Medium | Resolution-dependent |
| SVG | Publications (vector) | Small | Scalable |

## When to Use Each Format

### For 3D Printing
- **Best**: STL with `precision='double'`
- Check mesh quality before export
- Consider mesh density (finer = larger file)

### For CAD Software
- **SolidWorks/CATIA**: STEP preferred
- **Legacy systems**: IGES
- **ACIS-based**: SAT

### For Data Analysis
- **Python/Excel**: CSV
- **Abaqus post-processing**: ODB (keep original)
- **Formatted output**: RPT

### For Documentation
- **Web/PowerPoint**: PNG at 150-300 DPI
- **Publications/LaTeX**: SVG or EPS

## File Size Optimization

### Large STL Files
```python
# Use single precision (smaller but less accurate)
part.writeStlFile(fileName='output.stl', precision='single')

# Or coarsen mesh before export
part.seedPart(size=5.0)  # Increase from original
part.generateMesh()
part.writeStlFile(fileName='output_coarse.stl')
```

### Large CSV Files
```python
# Export only max values instead of all data
max_disp = max(v.magnitude for v in frame.fieldOutputs['U'].values)
max_stress = max(v.mises for v in frame.fieldOutputs['S'].values if hasattr(v, 'mises'))

with open('summary.csv', 'w') as f:
    f.write(f"Max Displacement,{max_disp}\n")
    f.write(f"Max von Mises,{max_stress}\n")
```

### Large ODB Files
- Reduce field output frequency in step definition
- Output only needed variables
- Use element sets to limit output regions

## Debugging Export Issues

### Check Available Field Outputs
```python
from odbAccess import openOdb

odb = openOdb('Model.odb', readOnly=True)
frame = odb.steps['Load'].frames[-1]

print("Available field outputs:")
for name in frame.fieldOutputs.keys():
    print(f"  {name}")

odb.close()
```

### Check Part Has Mesh
```python
part = mdb.models['Model'].parts['Part-1']
print(f"Nodes: {len(part.nodes)}")
print(f"Elements: {len(part.elements)}")

if len(part.elements) == 0:
    print("Part has no mesh - generate mesh first")
```

### Check Step Names
```python
odb = openOdb('Model.odb', readOnly=True)
print("Available steps:")
for name in odb.steps.keys():
    print(f"  {name}")
odb.close()
```

### Verify Export Success
```python
import os

export_path = 'output.stl'
part.writeStlFile(fileName=export_path, precision='double')

if os.path.exists(export_path):
    size = os.path.getsize(export_path)
    print(f"Export successful: {export_path} ({size} bytes)")
else:
    print("Export failed - file not created")
```

## Platform-Specific Issues

### Windows Path Issues
```python
# Use forward slashes or raw strings
part.writeStlFile(fileName='C:/output/part.stl')  # Good
part.writeStlFile(fileName=r'C:\output\part.stl')  # Also good
part.writeStlFile(fileName='C:\\output\\part.stl')  # Escaped backslashes
```

### Long Path Names
- Windows has 260 character path limit
- Use shorter directory names
- Or enable long paths in Windows settings

### File Permissions
```python
import os

output_dir = 'C:/export'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Check write permission
test_file = os.path.join(output_dir, 'test.txt')
try:
    with open(test_file, 'w') as f:
        f.write('test')
    os.remove(test_file)
    print("Write permission OK")
except PermissionError:
    print("No write permission to directory")
```

## Memory Issues with Large Exports

### Batch Processing
```python
# Process in chunks to avoid memory issues
chunk_size = 10000
values = list(frame.fieldOutputs['U'].values)

for i in range(0, len(values), chunk_size):
    chunk = values[i:i+chunk_size]
    with open(f'displacement_chunk_{i}.csv', 'w') as f:
        for v in chunk:
            f.write(f"{v.nodeLabel},{v.magnitude}\n")
```

### Close ODBs After Use
```python
# Always close ODB to free memory
odb = openOdb('Model.odb', readOnly=True)
try:
    # ... export operations ...
finally:
    odb.close()
```

## Recovery from Failed Exports

### Partial CSV Recovery
```python
# If export was interrupted, count existing rows
with open('partial.csv', 'r') as f:
    existing_rows = sum(1 for line in f)

print(f"Export stopped at row {existing_rows}")
# Resume from that point
```

### Clean Up Failed STL
```python
import os

stl_path = 'output.stl'
if os.path.exists(stl_path) and os.path.getsize(stl_path) < 100:
    # Likely corrupt/incomplete
    os.remove(stl_path)
    print("Removed incomplete STL file")
```
