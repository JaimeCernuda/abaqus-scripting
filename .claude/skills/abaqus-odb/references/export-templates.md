# ODB Export Templates

Ready-to-use scripts for exporting Abaqus ODB data to external formats (CSV,
text reports, Python-readable). All scripts run with `abaqus python script.py`.

## Template 1: Export Field Output to CSV

### All Nodes -- Displacement

```python
"""Export displacement data to CSV.
Run with: abaqus python export_displacement.py
"""
import os
from odbAccess import *
from abaqusConstants import *

ODB_PATH = 'MyJob.odb'
STEP_NAME = 'LoadStep'
OUTPUT_FILE = 'displacement.csv'

odb = openOdb(ODB_PATH, readOnly=True)
frame = odb.steps[STEP_NAME].frames[-1]
disp = frame.fieldOutputs['U']

with open(OUTPUT_FILE, 'w') as f:
    f.write('NodeLabel,U1,U2,U3,Magnitude\n')
    for v in disp.values:
        if len(v.data) >= 3:
            f.write('{},{:.6e},{:.6e},{:.6e},{:.6e}\n'.format(
                v.nodeLabel, v.data[0], v.data[1], v.data[2], v.magnitude))
        else:
            # 2D model
            f.write('{},{:.6e},{:.6e},0.0,{:.6e}\n'.format(
                v.nodeLabel, v.data[0], v.data[1], v.magnitude))

odb.close()
print('Exported {} displacement values to {}'.format(len(disp.values), OUTPUT_FILE))
```

### All Elements -- Von Mises Stress

```python
"""Export von Mises stress to CSV (one row per integration point).
Run with: abaqus python export_stress.py
"""
from odbAccess import *
from abaqusConstants import *

ODB_PATH = 'MyJob.odb'
STEP_NAME = 'LoadStep'
OUTPUT_FILE = 'stress.csv'

odb = openOdb(ODB_PATH, readOnly=True)
frame = odb.steps[STEP_NAME].frames[-1]
stress = frame.fieldOutputs['S']

with open(OUTPUT_FILE, 'w') as f:
    f.write('ElementLabel,IntPoint,S11,S22,S33,S12,S13,S23,Mises,MaxPrincipal,MinPrincipal\n')
    for v in stress.values:
        components = list(v.data)
        # Pad to 6 components if fewer (2D elements have fewer)
        while len(components) < 6:
            components.append(0.0)
        f.write('{},{},{:.4f},{:.4f},{:.4f},{:.4f},{:.4f},{:.4f},{:.4f},{:.4f},{:.4f}\n'.format(
            v.elementLabel,
            v.integrationPoint if v.integrationPoint else 0,
            components[0], components[1], components[2],
            components[3], components[4], components[5],
            v.mises, v.maxPrincipal, v.minPrincipal))

odb.close()
print('Exported stress data to {}'.format(OUTPUT_FILE))
```

## Template 2: Export Subset to CSV

### Stress in a Specific Element Set

```python
"""Export stress for elements in a named set.
Run with: abaqus python export_subset_stress.py
"""
from odbAccess import *
from abaqusConstants import *

ODB_PATH = 'MyJob.odb'
STEP_NAME = 'LoadStep'
ELSET_NAME = 'DESIGN_SPACE'
OUTPUT_FILE = 'stress_subset.csv'

odb = openOdb(ODB_PATH, readOnly=True)
frame = odb.steps[STEP_NAME].frames[-1]

# Get subset
elem_set = odb.rootAssembly.elementSets[ELSET_NAME]
stress = frame.fieldOutputs['S'].getSubset(region=elem_set)

with open(OUTPUT_FILE, 'w') as f:
    f.write('ElementLabel,Mises,MaxPrincipal,MinPrincipal\n')
    for v in stress.values:
        f.write('{},{:.4f},{:.4f},{:.4f}\n'.format(
            v.elementLabel, v.mises, v.maxPrincipal, v.minPrincipal))

odb.close()
print('Exported {} stress values from set {} to {}'.format(
    len(stress.values), ELSET_NAME, OUTPUT_FILE))
```

## Template 3: Export History Output to CSV

### Time History of Displacement at a Point

```python
"""Export displacement history at a node (for plotting).
Run with: abaqus python export_history.py
"""
from odbAccess import *

ODB_PATH = 'MyJob.odb'
STEP_NAME = 'LoadStep'
OUTPUT_FILE = 'history_u2.csv'

odb = openOdb(ODB_PATH, readOnly=True)
step = odb.steps[STEP_NAME]

# List available history regions to find the right one
print('Available history regions:')
for key in step.historyRegions.keys():
    print('  {}'.format(key))

# Pick a region (adjust the key to match your model)
region_key = step.historyRegions.keys()[0]
region = step.historyRegions[region_key]

print('Available outputs:', list(region.historyOutputs.keys()))

# Export U2 history
if 'U2' in region.historyOutputs:
    data = region.historyOutputs['U2'].data
    with open(OUTPUT_FILE, 'w') as f:
        f.write('Time,U2\n')
        for time_val, u2_val in data:
            f.write('{:.6e},{:.6e}\n'.format(time_val, u2_val))
    print('Exported {} data points to {}'.format(len(data), OUTPUT_FILE))

odb.close()
```

### Energy History

```python
"""Export whole-model energy history.
Run with: abaqus python export_energy.py
"""
from odbAccess import *

ODB_PATH = 'MyJob.odb'
STEP_NAME = 'LoadStep'
OUTPUT_FILE = 'energy_history.csv'

odb = openOdb(ODB_PATH, readOnly=True)
step = odb.steps[STEP_NAME]

# Energy is in the Assembly region
assembly_region = None
for key, region in step.historyRegions.items():
    if 'Assembly' in key or 'ASSEMBLY' in key:
        assembly_region = region
        break

if assembly_region:
    energy_vars = [k for k in assembly_region.historyOutputs.keys()
                   if k.startswith('ALL')]
    print('Energy variables:', energy_vars)

    with open(OUTPUT_FILE, 'w') as f:
        f.write('Time,' + ','.join(energy_vars) + '\n')
        # Use first variable to get time values
        first_data = assembly_region.historyOutputs[energy_vars[0]].data
        for i, (time_val, _) in enumerate(first_data):
            row = ['{:.6e}'.format(time_val)]
            for var in energy_vars:
                data = assembly_region.historyOutputs[var].data
                row.append('{:.6e}'.format(data[i][1]))
            f.write(','.join(row) + '\n')

    print('Exported energy history to {}'.format(OUTPUT_FILE))

odb.close()
```

## Template 4: Summary Text Report

Based on the experiment4 pattern -- produces a human-readable results file.

```python
"""Generate a summary text report from ODB results.
Run with: abaqus python generate_report.py
"""
import os
from odbAccess import *
from abaqusConstants import *

ODB_PATH = 'MyJob.odb'
STEP_NAME = 'LoadStep'
REPORT_FILE = 'analysis_report.txt'
YIELD_STRESS = 250.0  # MPa -- set to your material's yield

odb = openOdb(ODB_PATH, readOnly=True)
step = odb.steps[STEP_NAME]
frame = step.frames[-1]

# Stress
stress = frame.fieldOutputs['S']
max_mises = 0.0
max_mises_elem = 0
for v in stress.values:
    if v.mises > max_mises:
        max_mises = v.mises
        max_mises_elem = v.elementLabel

# Displacement
disp = frame.fieldOutputs['U']
max_disp = 0.0
max_disp_node = 0
for v in disp.values:
    if v.magnitude > max_disp:
        max_disp = v.magnitude
        max_disp_node = v.nodeLabel

# Reaction forces (if available)
total_rf = [0.0, 0.0, 0.0]
if 'RF' in frame.fieldOutputs:
    rf = frame.fieldOutputs['RF']
    for v in rf.values:
        for i in range(min(len(v.data), 3)):
            total_rf[i] += v.data[i]

# Write report
with open(REPORT_FILE, 'w') as f:
    f.write('Analysis Report: {}\n'.format(os.path.basename(ODB_PATH)))
    f.write('=' * 60 + '\n')
    f.write('Step: {}\n'.format(STEP_NAME))
    f.write('Frame: {} (time = {})\n'.format(
        frame.incrementNumber, frame.frameValue))
    f.write('\n')
    f.write('STRESS\n')
    f.write('-' * 40 + '\n')
    f.write('  Max von Mises: {:.2f} MPa (element {})\n'.format(
        max_mises, max_mises_elem))
    f.write('  Factor of Safety: {:.2f}\n'.format(YIELD_STRESS / max_mises))
    if max_mises > YIELD_STRESS:
        f.write('  WARNING: Exceeds yield strength!\n')
    f.write('\n')
    f.write('DISPLACEMENT\n')
    f.write('-' * 40 + '\n')
    f.write('  Max magnitude: {:.4f} mm (node {})\n'.format(
        max_disp, max_disp_node))
    f.write('\n')
    f.write('REACTION FORCES\n')
    f.write('-' * 40 + '\n')
    f.write('  Total RF1: {:.2f} N\n'.format(total_rf[0]))
    f.write('  Total RF2: {:.2f} N\n'.format(total_rf[1]))
    f.write('  Total RF3: {:.2f} N\n'.format(total_rf[2]))

odb.close()
print('Report written to {}'.format(REPORT_FILE))
```

## Template 5: Export Reaction Forces at Multiple Boundaries

```python
"""Export reaction forces at each boundary condition node set.
Run with: abaqus python export_reactions.py
"""
from odbAccess import *
from abaqusConstants import *

ODB_PATH = 'MyJob.odb'
STEP_NAME = 'LoadStep'
BC_NSETS = ['FixedEnd', 'PinnedEnd', 'RollerEnd']  # adjust to your model
OUTPUT_FILE = 'reactions.csv'

odb = openOdb(ODB_PATH, readOnly=True)
frame = odb.steps[STEP_NAME].frames[-1]
rf = frame.fieldOutputs['RF']

with open(OUTPUT_FILE, 'w') as f:
    f.write('NodeSet,RF1,RF2,RF3\n')
    for nset_name in BC_NSETS:
        try:
            nset = odb.rootAssembly.nodeSets[nset_name]
        except KeyError:
            print('Warning: node set {} not found'.format(nset_name))
            continue
        rf_sub = rf.getSubset(region=nset)
        total = [0.0, 0.0, 0.0]
        for v in rf_sub.values:
            for i in range(min(len(v.data), 3)):
                total[i] += v.data[i]
        f.write('{},{:.4f},{:.4f},{:.4f}\n'.format(nset_name, *total))

odb.close()
print('Exported reactions to {}'.format(OUTPUT_FILE))
```

## Template 6: Export Topology Optimization Results

### Export Optimized-Design Stress to CSV

After running FEA on the Tosca last-cycle `.inp`, extract results from
the optimized topology.

```python
"""Export stress/displacement from optimized-design ODB.
Run with: abaqus python export_optimized_results.py
"""
import os
import glob
from odbAccess import *
from abaqusConstants import *

TOSCA_DIR = 'my_tosca'
OUTPUT_FILE = 'optimized_results.csv'

# Find last-cycle ODB
save_inp = os.path.join(TOSCA_DIR, 'SAVE.inp')
cycle_dirs = [d for d in os.listdir(save_inp)
              if d.isdigit() and os.path.isdir(os.path.join(save_inp, d))]
last_cycle = max(cycle_dirs, key=int)
cycle_dir = os.path.join(save_inp, last_cycle)
odb_files = glob.glob(os.path.join(cycle_dir, '*.odb'))

if not odb_files:
    print('ERROR: No ODB found in {}'.format(cycle_dir))
    exit(1)

odb = openOdb(odb_files[0], readOnly=True)
step_name = odb.steps.keys()[-1]
frame = odb.steps[step_name].frames[-1]

# Extract stress
stress = frame.fieldOutputs['S']
with open(OUTPUT_FILE, 'w') as f:
    f.write('ElementLabel,Mises,MaxPrincipal,MinPrincipal\n')
    for v in stress.values:
        f.write('{},{:.4f},{:.4f},{:.4f}\n'.format(
            v.elementLabel, v.mises, v.maxPrincipal, v.minPrincipal))

print('Exported {} element stress values from optimized design'.format(
    len(stress.values)))
print('Max Mises: {:.2f} MPa'.format(max(v.mises for v in stress.values)))
odb.close()
```

## Template 7: Multi-ODB Comparison

### Compare Results Across Multiple Jobs

```python
"""Compare results from multiple ODB files (e.g., different load levels).
Run with: abaqus python compare_jobs.py
"""
from odbAccess import *
from abaqusConstants import *

JOBS = [
    ('Job_20kN', 'LoadStep'),
    ('Job_60kN', 'LoadStep'),
    ('Job_100kN', 'LoadStep'),
]
OUTPUT_FILE = 'comparison.csv'

with open(OUTPUT_FILE, 'w') as f:
    f.write('Job,MaxMises_MPa,MaxDisp_mm,MaxPEEQ\n')

    for job_name, step_name in JOBS:
        odb = openOdb(job_name + '.odb', readOnly=True)
        frame = odb.steps[step_name].frames[-1]

        max_mises = max(v.mises for v in frame.fieldOutputs['S'].values)
        max_disp = max(v.magnitude for v in frame.fieldOutputs['U'].values)

        max_peeq = 0.0
        if 'PEEQ' in frame.fieldOutputs:
            max_peeq = max(v.data for v in frame.fieldOutputs['PEEQ'].values)

        f.write('{},{:.2f},{:.4f},{:.6f}\n'.format(
            job_name, max_mises, max_disp, max_peeq))

        odb.close()

print('Comparison written to {}'.format(OUTPUT_FILE))
```

## Utility: Generic CSV Exporter

```python
def export_field_to_csv(odb, step_name, field_name, csv_path,
                        region=None, frame_index=-1):
    """Generic field output exporter.

    Args:
        odb: Open OdbObject.
        step_name: Step name.
        field_name: Field output key ('S', 'U', 'RF', 'PEEQ', etc.).
        csv_path: Output CSV file path.
        region: Optional OdbSet to filter by (node set or element set).
        frame_index: Frame index (-1 for last).
    """
    frame = odb.steps[step_name].frames[frame_index]
    field = frame.fieldOutputs[field_name]
    if region:
        field = field.getSubset(region=region)

    values = field.values
    if not values:
        print('No values found for field {}'.format(field_name))
        return

    # Determine columns from first value
    v0 = values[0]
    is_nodal = hasattr(v0, 'nodeLabel') and v0.nodeLabel is not None
    has_mises = hasattr(v0, 'mises')

    with open(csv_path, 'w') as f:
        if is_nodal:
            header = 'NodeLabel'
        else:
            header = 'ElementLabel,IntPoint'

        # Data columns
        n_components = len(v0.data) if hasattr(v0.data, '__len__') else 1
        for i in range(n_components):
            header += ',Comp{}'.format(i + 1)
        if hasattr(v0, 'magnitude') and v0.magnitude is not None:
            header += ',Magnitude'
        if has_mises:
            header += ',Mises'
        f.write(header + '\n')

        for v in values:
            if is_nodal:
                row = str(v.nodeLabel)
            else:
                row = '{},{}'.format(v.elementLabel,
                                     v.integrationPoint if v.integrationPoint else 0)

            if hasattr(v.data, '__len__'):
                for d in v.data:
                    row += ',{:.6e}'.format(d)
            else:
                row += ',{:.6e}'.format(v.data)

            if hasattr(v, 'magnitude') and v.magnitude is not None:
                row += ',{:.6e}'.format(v.magnitude)
            if has_mises:
                row += ',{:.6e}'.format(v.mises)

            f.write(row + '\n')

    print('Exported {} values to {}'.format(len(values), csv_path))
```
