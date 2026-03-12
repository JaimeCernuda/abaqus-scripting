# Common ODB Queries

Recipes for frequently needed ODB extraction tasks. Each query is self-contained
and can be dropped directly into a script.

## Query 1: Max/Min Values with Location

### Maximum Von Mises Stress (All Steps)

Based on the official `odbMaxMises.py` pattern from the Abaqus documentation.

```python
from odbAccess import *

def find_max_mises(odb, elset_name=None):
    """Find maximum von Mises stress across all steps and frames.

    Args:
        odb: An open OdbObject.
        elset_name: Optional assembly-level element set name to restrict search.

    Returns:
        dict with keys: mises, elementLabel, stepName, frameIndex
    """
    assembly = odb.rootAssembly
    elemset = None
    if elset_name:
        elemset = assembly.elementSets[elset_name]

    result = {'mises': -1.0, 'elementLabel': 0, 'stepName': '', 'frameIndex': -1}

    for step in odb.steps.values():
        for frame in step.frames:
            if 'S' not in frame.fieldOutputs:
                continue
            stress_field = frame.fieldOutputs['S']
            if elemset:
                stress_field = stress_field.getSubset(region=elemset)
            for v in stress_field.values:
                if v.mises > result['mises']:
                    result['mises'] = v.mises
                    result['elementLabel'] = v.elementLabel
                    result['stepName'] = step.name
                    result['frameIndex'] = frame.incrementNumber

    return result
```

### Maximum Displacement Magnitude

```python
def find_max_displacement(odb, step_name=None):
    """Find maximum displacement magnitude.

    Args:
        odb: An open OdbObject.
        step_name: Step to search (None = last step).

    Returns:
        dict with keys: magnitude, components, nodeLabel, frameIndex
    """
    if step_name:
        step = odb.steps[step_name]
    else:
        step = odb.steps.values()[-1]

    frame = step.frames[-1]
    disp = frame.fieldOutputs['U']

    result = {'magnitude': 0.0, 'components': None, 'nodeLabel': 0, 'frameIndex': -1}
    for v in disp.values:
        if v.magnitude > result['magnitude']:
            result['magnitude'] = v.magnitude
            result['components'] = list(v.data)
            result['nodeLabel'] = v.nodeLabel
            result['frameIndex'] = frame.incrementNumber

    return result
```

## Query 2: Subset Filtering by Region

### Filter by Node Set

```python
# Get displacement at a specific node set
node_set = odb.rootAssembly.nodeSets['MY_NSET']
disp = frame.fieldOutputs['U']
disp_subset = disp.getSubset(region=node_set)

for v in disp_subset.values:
    print('Node {}: U = ({:.4f}, {:.4f}, {:.4f}), mag = {:.4f}'.format(
        v.nodeLabel, v.data[0], v.data[1], v.data[2], v.magnitude))
```

### Filter by Element Set

```python
# Get stress in a specific element set
elem_set = odb.rootAssembly.elementSets['DESIGN_SPACE']
stress = frame.fieldOutputs['S']
stress_subset = stress.getSubset(region=elem_set)

for v in stress_subset.values:
    print('Element {}: Mises = {:.2f} MPa'.format(v.elementLabel, v.mises))
```

### Filter by Instance

```python
# Get results for a specific part instance
instance = odb.rootAssembly.instances['PART-1']
stress = frame.fieldOutputs['S']
inst_stress = stress.getSubset(region=instance)
```

### Filter by Position

```python
# Get stress at integration points only
stress_ip = stress.getSubset(position=INTEGRATION_POINT)

# Get stress extrapolated to nodes
stress_nodal = stress.getSubset(position=ELEMENT_NODAL)

# Get stress at element centroids
stress_centroid = stress.getSubset(position=CENTROID)
```

### Filter by Element Type

```python
# Get stress for specific element type
stress_c3d8r = stress.getSubset(elementType='C3D8R')
stress_c3d10 = stress.getSubset(elementType='C3D10')
```

### Combined Filters

```python
# Stress at integration points in a specific element set
elem_set = odb.rootAssembly.elementSets['CRITICAL_REGION']
stress = frame.fieldOutputs['S']
filtered = stress.getSubset(region=elem_set).getSubset(position=INTEGRATION_POINT)
```

## Query 3: Listing Available Sets

```python
# Assembly-level sets (from dependent instances, these are the usable ones)
print('Node sets:', list(odb.rootAssembly.nodeSets.keys()))
print('Element sets:', list(odb.rootAssembly.elementSets.keys()))

# Instance-level sets
for inst_name, inst in odb.rootAssembly.instances.items():
    print('Instance: {}'.format(inst_name))
    print('  Node sets:', list(inst.nodeSets.keys()))
    print('  Element sets:', list(inst.elementSets.keys()))
```

## Query 4: Total Reaction Force at a Boundary

```python
def total_reaction_force(odb, step_name, nset_name):
    """Sum reaction forces at a node set (equilibrium check).

    Args:
        odb: An open OdbObject.
        step_name: Name of the analysis step.
        nset_name: Assembly-level node set name for the boundary.

    Returns:
        list of force components [RF1, RF2, RF3]
    """
    frame = odb.steps[step_name].frames[-1]
    rf = frame.fieldOutputs['RF']
    nset = odb.rootAssembly.nodeSets[nset_name]
    rf_sub = rf.getSubset(region=nset)

    total = [0.0, 0.0, 0.0]
    for v in rf_sub.values:
        for i in range(min(len(v.data), 3)):
            total[i] += v.data[i]

    return total
```

## Query 5: History Output (Time Series)

```python
def extract_history(odb, step_name, region_key, variable):
    """Extract history output as list of (time, value) tuples.

    Args:
        odb: An open OdbObject.
        step_name: Step name.
        region_key: History region key, e.g. 'Node PART-1-1.100'.
        variable: History output variable, e.g. 'U2', 'RF1'.

    Returns:
        list of (time, value) tuples
    """
    step = odb.steps[step_name]
    region = step.historyRegions[region_key]
    return list(region.historyOutputs[variable].data)


# List available history regions and outputs
step = odb.steps['LoadStep']
for region_name, region in step.historyRegions.items():
    print('Region: {}'.format(region_name))
    print('  Outputs: {}'.format(list(region.historyOutputs.keys())))
```

## Query 6: Displacement at a Specific Node

```python
def displacement_at_node(odb, step_name, node_label, instance_name=None):
    """Get displacement at a specific node.

    Args:
        odb: An open OdbObject.
        step_name: Step name.
        node_label: Integer node label.
        instance_name: Part instance name (required for multi-instance models).

    Returns:
        dict with components and magnitude, or None if not found.
    """
    frame = odb.steps[step_name].frames[-1]
    disp = frame.fieldOutputs['U']

    for v in disp.values:
        if v.nodeLabel == node_label:
            if instance_name and v.instance.name != instance_name:
                continue
            return {
                'components': list(v.data),
                'magnitude': v.magnitude,
                'nodeLabel': v.nodeLabel,
            }
    return None
```

## Query 7: Stress Along a Path (Line of Nodes)

```python
def stress_along_path(odb, step_name, node_labels):
    """Extract von Mises stress at specific nodes (for path plots).

    Args:
        odb: An open OdbObject.
        step_name: Step name.
        node_labels: List of node labels defining the path.

    Returns:
        list of (nodeLabel, mises) tuples in input order.
    """
    frame = odb.steps[step_name].frames[-1]
    # Use ELEMENT_NODAL position to get stress extrapolated to nodes
    stress = frame.fieldOutputs['S'].getSubset(position=ELEMENT_NODAL)

    # Build lookup: nodeLabel -> max mises (may have multiple values per node)
    node_mises = {}
    for v in stress.values:
        if v.nodeLabel in node_labels:
            current = node_mises.get(v.nodeLabel, 0.0)
            node_mises[v.nodeLabel] = max(current, v.mises)

    return [(n, node_mises.get(n, 0.0)) for n in node_labels]
```

## Query 8: Energy Summary

```python
def energy_summary(odb, step_name):
    """Extract whole-model energy values from history output.

    Common variables: ALLSE (strain energy), ALLKE (kinetic energy),
    ALLWK (external work), ALLPD (plastic dissipation).
    """
    step = odb.steps[step_name]

    # Whole-model energy is usually in the Assembly history region
    for region_name, region in step.historyRegions.items():
        if 'Assembly' in region_name or 'ASSEMBLY' in region_name:
            energies = {}
            for var_name, output in region.historyOutputs.items():
                if var_name.startswith('ALL'):
                    # Get final value
                    data = output.data
                    if data:
                        energies[var_name] = data[-1][1]
            return energies
    return {}
```

## Query 9: Comparing Results Across Load Cases

```python
def compare_load_cases(odb, step_names):
    """Compare max stress and displacement across multiple steps (load cases).

    Args:
        odb: An open OdbObject.
        step_names: List of step names to compare.

    Returns:
        list of dicts with step_name, max_mises, max_disp.
    """
    results = []
    for step_name in step_names:
        frame = odb.steps[step_name].frames[-1]

        max_mises = max(v.mises for v in frame.fieldOutputs['S'].values)
        max_disp = max(v.magnitude for v in frame.fieldOutputs['U'].values)

        results.append({
            'step_name': step_name,
            'max_mises': max_mises,
            'max_disp': max_disp,
        })
    return results
```

## Query 10: Reading Topology Optimization Results

### Reading Density Fields from Tosca Output

After Tosca optimization, the per-cycle ODBs are deleted, but the last-cycle
`.inp` files in `SAVE.inp/<N>/` contain `tosca_distribution.inp` with per-element
density values. To visualize the optimized design, run FEA on that `.inp`.

```python
import os
import glob

def find_optimized_odb(tosca_dir):
    """Find the ODB from the last optimization cycle.

    Tosca saves per-cycle .inp files in SAVE.inp/<cycle_number>/.
    After running FEA on the last cycle, the ODB appears there.

    Args:
        tosca_dir: Path to the Tosca run directory (e.g., 'my_tosca').

    Returns:
        Path to the ODB file, or None.
    """
    save_inp_dir = os.path.join(tosca_dir, 'SAVE.inp')
    if not os.path.isdir(save_inp_dir):
        return None

    cycle_dirs = [d for d in os.listdir(save_inp_dir)
                  if d.isdigit() and os.path.isdir(os.path.join(save_inp_dir, d))]
    if not cycle_dirs:
        return None

    last_cycle = max(cycle_dirs, key=int)
    cycle_dir = os.path.join(save_inp_dir, last_cycle)

    # Look for any ODB in the last cycle directory
    odbs = glob.glob(os.path.join(cycle_dir, '*.odb'))
    return odbs[0] if odbs else None
```

### Extracting Results from an Optimized-Design ODB

Based on experiment10/scripts/exp10_visualize.py:

```python
# Open the ODB produced by running FEA on the Tosca last-cycle .inp
odb = openOdb(odb_path, readOnly=True)

step_name = odb.steps.keys()[-1]
last_frame = odb.steps[step_name].frames[-1]

# Von Mises stress on the optimized topology
stress = last_frame.fieldOutputs['S']
max_mises = max(v.mises for v in stress.values)

# Displacement on the optimized topology
disp = last_frame.fieldOutputs['U']
max_disp = max(v.magnitude for v in disp.values)

print('Optimized design: max Mises = {:.2f} MPa, max U = {:.4f} mm'.format(
    max_mises, max_disp))

odb.close()
```

### Visualizing Optimized Results in CAE (requires GUI)

```python
# From exp10_visualize.py -- requires abaqus cae script= (not noGUI)
import visualization

odb = session.openOdb(name=odb_path)
vp = session.viewports['Viewport: 1']
vp.setValues(displayedObject=odb)
vp.odbDisplay.setFrame(step=0, frame=-1)

# Mises stress contour on deformed shape
vp.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))
vp.odbDisplay.setPrimaryVariable(
    variableLabel='S',
    outputPosition=INTEGRATION_POINT,
    refinement=(INVARIANT, 'Mises'))

session.printToFile(fileName='stress_mises', format=PNG, canvasObjects=(vp,))
```
