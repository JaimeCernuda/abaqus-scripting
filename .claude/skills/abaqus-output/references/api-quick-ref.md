# Output API Quick Reference

## FieldOutputRequest
```python
model.FieldOutputRequest(
    name='F-Output',
    createStepName='StepName',
    variables=('S', 'U', 'RF', 'E'),  # tuple of variable names
    frequency=1,                       # every N increments
    region=MODEL                       # or specific set
)
```

## HistoryOutputRequest
```python
model.HistoryOutputRequest(
    name='H-Output',
    createStepName='StepName',
    variables=('U1', 'U2', 'RF1'),
    region=nodeSet,                    # specific node/element set
    frequency=1
)
```

## Common Field Variables
| Variable | Description |
|----------|-------------|
| S | Stress tensor |
| U | Displacement |
| RF | Reaction force |
| E | Strain tensor |
| PEEQ | Equivalent plastic strain |
| MISES | von Mises stress |
| TEMP | Temperature |
| ENER | Energy densities |
| PE | Plastic strain |
| V | Velocity (dynamic) |
| A | Acceleration (dynamic) |
| NT | Nodal temperature |
| HFL | Heat flux |
| CSTRESS | Contact stress |
| CDISP | Contact displacement |

## Common History Variables
| Variable | Description |
|----------|-------------|
| U1, U2, U3 | Displacement components |
| RF1, RF2, RF3 | Reaction force components |
| S11, S22, S12 | Stress components |
| ALLSE | Strain energy |
| ALLKE | Kinetic energy |
| ALLWK | External work |
| ETOTAL | Total energy |
| ALLPD | Plastic dissipation |

## Output Frequency Options
| Parameter | Description |
|-----------|-------------|
| frequency=1 | Every increment |
| frequency=10 | Every 10th increment |
| numIntervals=20 | Fixed 20 output frames |
| timeInterval=0.1 | Every 0.1 time units |

## Region Options
| Value | Description |
|-------|-------------|
| MODEL | Entire model (default) |
| assembly.sets['SetName'] | Specific set |
| instance.sets['SetName'] | Instance-level set |
