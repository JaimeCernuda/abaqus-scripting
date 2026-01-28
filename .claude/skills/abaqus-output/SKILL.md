---
name: abaqus-output
description: Configure output requests in Abaqus - field outputs, history outputs, and output database settings.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
---

# Abaqus Output Skill

## When to Use This Skill

**USE when you need to:**
- Request specific field outputs (S, U, RF, etc.)
- Set up history outputs at specific locations
- Control output frequency to manage file size
- Request energy outputs for validation
- Configure restart output
- Request contact-specific outputs

**Do NOT use for:**
- Extracting results from ODB → use `/abaqus-odb`
- Running the analysis → use `/abaqus-job`
- Post-processing or visualization → use `/abaqus-odb`

## Key Decisions

### 1. Field vs History Output

| Type | What | When |
|------|------|------|
| Field Output | All nodes/elements | Contour plots, full-field results |
| History Output | Specific locations | Time series, monitoring points |

### 2. What Variables to Request

| Analysis | Essential Variables |
|----------|---------------------|
| Static | S, U, RF |
| Dynamic | S, U, V, A, RF, ENER |
| Thermal | NT, HFL, RFL |
| Contact | CSTRESS, CDISP, COPEN |
| Plastic | S, PE, PEEQ |
| Modal | U (mode shapes) |

### 3. Output Frequency

| Concern | frequency | Guidance |
|---------|-----------|----------|
| Full detail | 1 | Every increment |
| Balanced | 5-10 | Every N increments |
| Space-saving | 20+ or numIntervals | Fixed number of frames |

## Required Inputs

| Input | Required | Default |
|-------|----------|---------|
| Step name | YES | - |
| Variables | YES | (S, U, RF) |
| Frequency | NO | 1 |

## Common Patterns

### Basic Field Output
```python
model.FieldOutputRequest(
    name='F-Output-1',
    createStepName='LoadStep',
    variables=('S', 'U', 'RF')
)
```

### Comprehensive Field Output
```python
model.FieldOutputRequest(
    name='AllFields',
    createStepName='LoadStep',
    variables=(
        'S', 'E', 'U', 'RF',  # Basic
        'PEEQ', 'PE',          # Plastic
        'ENER',                # Energy
    ),
    frequency=1
)
```

### History Output at Point
```python
# Create set for monitoring
monitor_vertex = instance.vertices.findAt(((x, y, z),))
assembly.Set(vertices=monitor_vertex, name='MonitorPoint')

model.HistoryOutputRequest(
    name='H-Output-1',
    createStepName='LoadStep',
    variables=('U1', 'U2', 'U3', 'RF1', 'RF2', 'RF3'),
    region=assembly.sets['MonitorPoint'],
    frequency=1
)
```

### Energy History (Global)
```python
model.HistoryOutputRequest(
    name='Energies',
    createStepName='LoadStep',
    variables=(
        'ALLSE',   # Strain energy
        'ALLKE',   # Kinetic energy
        'ALLWK',   # External work
        'ETOTAL',  # Total energy (should be ~constant)
    ),
    frequency=1
)
```

### Contact Output
```python
model.FieldOutputRequest(
    name='ContactOutput',
    createStepName='LoadStep',
    variables=('CSTRESS', 'CDISP', 'COPEN', 'CSLIP')
)
```

### Reduced Frequency
```python
# Every 10th increment
model.FieldOutputRequest(
    name='Sparse',
    createStepName='LoadStep',
    variables=('S', 'U'),
    frequency=10
)

# Fixed number of output frames
model.FieldOutputRequest(
    name='Fixed20',
    createStepName='LoadStep',
    variables=('S', 'U'),
    numIntervals=20
)
```

### Output for Specific Region
```python
model.FieldOutputRequest(
    name='CriticalRegion',
    createStepName='LoadStep',
    variables=('S', 'PE', 'PEEQ'),
    region=assembly.sets['StressConcentration'],
    frequency=1
)
```

### Delete Default Output
```python
if 'F-Output-1' in model.fieldOutputRequests:
    del model.fieldOutputRequests['F-Output-1']
```

### Restart Request
```python
model.RestartRequest(
    name='Restart',
    createStepName='LoadStep',
    frequency=10  # Every 10 increments
)
```

## Common Output Variables

| Variable | Description |
|----------|-------------|
| S | Stress tensor (S11, S22, S33, S12, S13, S23, Mises) |
| E | Total strain |
| U | Displacement (U1, U2, U3, magnitude) |
| RF | Reaction force (RF1, RF2, RF3) |
| V | Velocity (dynamic) |
| A | Acceleration (dynamic) |
| PEEQ | Equivalent plastic strain |
| NT | Nodal temperature |
| ENER | Energy densities |

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Variable not available" | Wrong element type or analysis | Check compatibility |
| "ODB file too large" | Too much output | Reduce frequency or variables |
| "No history output" | Bad region specification | Verify set exists |

## API Reference

For detailed parameters: [Output API](../../docs/abaqus-api/modules/output.md)
