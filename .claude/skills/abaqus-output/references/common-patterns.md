# Common Output Patterns

## Minimal Output (small ODB)
```python
model.FieldOutputRequest(name='F-Out', createStepName='Load',
                         variables=('S', 'U'), frequency=10)
```

## Full Structural Output
```python
model.FieldOutputRequest(name='F-Out', createStepName='Load',
                         variables=('S', 'U', 'RF', 'E', 'PEEQ', 'MISES'))
```

## Track Single Point Over Time
```python
# Create node set first
nodeSet = assembly.Set(nodes=instance.nodes.findAt(((x,y,z),)), name='TrackPt')
model.HistoryOutputRequest(name='H-Out', createStepName='Load',
                           variables=('U1', 'U2', 'U3'), region=nodeSet)
```

## Track Vertex Point
```python
# Using geometry (vertex) instead of mesh (node)
vertex = instance.vertices.findAt(((x, y, z),))
assembly.Set(vertices=vertex, name='MonitorPoint')
model.HistoryOutputRequest(name='H-Out', createStepName='Load',
                           variables=('U1', 'U2', 'U3', 'RF1', 'RF2', 'RF3'),
                           region=assembly.sets['MonitorPoint'])
```

## Energy Output (for validation)
```python
model.HistoryOutputRequest(name='Energy', createStepName='Load',
                           variables=('ALLSE', 'ALLKE', 'ALLWK', 'ETOTAL'))
```

## Contact Analysis Output
```python
model.FieldOutputRequest(name='Contact', createStepName='Load',
                         variables=('CSTRESS', 'CDISP', 'COPEN', 'CSLIP'))
```

## Dynamic Analysis Output
```python
model.FieldOutputRequest(name='Dynamic', createStepName='Load',
                         variables=('S', 'U', 'V', 'A', 'RF', 'ENER'))
```

## Thermal Analysis Output
```python
model.FieldOutputRequest(name='Thermal', createStepName='Load',
                         variables=('NT', 'HFL', 'RFL'))
```

## Plastic Analysis Output
```python
model.FieldOutputRequest(name='Plastic', createStepName='Load',
                         variables=('S', 'E', 'PE', 'PEEQ', 'MISES'))
```

## Fixed Number of Output Frames
```python
# Exactly 20 output frames regardless of increments
model.FieldOutputRequest(name='Fixed', createStepName='Load',
                         variables=('S', 'U'), numIntervals=20)
```

## Output for Specific Region Only
```python
# First create a set for the region of interest
model.FieldOutputRequest(name='Critical', createStepName='Load',
                         variables=('S', 'PE', 'PEEQ'),
                         region=assembly.sets['StressConcentration'])
```

## Delete Default Output Request
```python
# Remove Abaqus default output before adding custom
if 'F-Output-1' in model.fieldOutputRequests:
    del model.fieldOutputRequests['F-Output-1']
if 'H-Output-1' in model.historyOutputRequests:
    del model.historyOutputRequests['H-Output-1']
```

## Restart Output
```python
model.RestartRequest(name='Restart', createStepName='Load',
                     frequency=10)  # Every 10 increments
```
