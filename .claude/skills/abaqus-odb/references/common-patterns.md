# Common ODB Patterns

## Max Stress and Displacement

```python
frame = odb.steps['Load'].frames[-1]
max_u = max(v.magnitude for v in frame.fieldOutputs['U'].values)
max_s = max(v.mises for v in frame.fieldOutputs['S'].values if hasattr(v, 'mises'))
```

## Reaction Force Sum

```python
rf = frame.fieldOutputs['RF']
total_rf = [0.0, 0.0, 0.0]
for v in rf.values:
    for i in range(3):
        total_rf[i] += v.data[i]
print(f"Total reaction: {total_rf}")
```

## Export to CSV

```python
import csv
with open('results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Node', 'U1', 'U2', 'U3', 'Magnitude'])
    for v in frame.fieldOutputs['U'].values:
        writer.writerow([v.nodeLabel, v.data[0], v.data[1], v.data[2], v.magnitude])
```

## Time History at Point

```python
region = odb.steps['Load'].historyRegions['Node ASSEMBLY.1']
u1_history = region.historyOutputs['U1'].data
times = [t for t, v in u1_history]
values = [v for t, v in u1_history]
```

## Find Node with Max Value

```python
disp = frame.fieldOutputs['U']
max_node = max(disp.values, key=lambda v: v.magnitude)
print(f"Max at node {max_node.nodeLabel}: {max_node.magnitude}")
```

## Extract Eigenfrequencies

```python
step = odb.steps['Frequency']
frequencies = []
for frame in step.frames:
    if frame.description:
        # Parse frequency from description like "Mode 1: EigenFrequency = 123.45"
        freq = float(frame.description.split('=')[-1].strip())
        frequencies.append(freq)
print(f"Natural frequencies: {frequencies}")
```

## Get Results at Specific Node

```python
target_node = 100
for value in frame.fieldOutputs['U'].values:
    if value.nodeLabel == target_node:
        print(f"Node {target_node}: U = {value.data}, Magnitude = {value.magnitude}")
        break
```

## Extract from Node Set

```python
instance = odb.rootAssembly.instances['PART-1']
node_set = instance.nodeSets['LOAD_REGION']
subset = frame.fieldOutputs['U'].getSubset(region=node_set)
for value in subset.values:
    print(f"Node {value.nodeLabel}: {value.data}")
```

## Stress Components at Element

```python
target_elem = 50
for value in frame.fieldOutputs['S'].values:
    if value.elementLabel == target_elem:
        print(f"Element {target_elem}:")
        print(f"  S11={value.data[0]:.2f}, S22={value.data[1]:.2f}, S33={value.data[2]:.2f}")
        print(f"  S12={value.data[3]:.2f}, S13={value.data[4]:.2f}, S23={value.data[5]:.2f}")
        print(f"  Mises={value.mises:.2f}")
        break
```

## Generate Summary Report

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

        if 'RF' in frame.fieldOutputs:
            rf = frame.fieldOutputs['RF']
            total = [sum(v.data[i] for v in rf.values) for i in range(3)]
            print(f"  Total reaction: [{total[0]:.2f}, {total[1]:.2f}, {total[2]:.2f}] N")

    odb.close()
```
