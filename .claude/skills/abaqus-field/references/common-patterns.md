# Common Field Patterns

## Uniform Initial Temperature
```python
allCells = assembly.Set(cells=instance.cells, name='AllCells')
model.Temperature(name='InitTemp', createStepName='Initial',
                  region=allCells, distributionType=UNIFORM,
                  magnitudes=(25.0,))
```

## Temperature Gradient (analytical field)
```python
model.ExpressionField(name='TempGrad',
                      expression='20 + 100*Y/HEIGHT')
model.Temperature(name='InitTemp', createStepName='Initial',
                  region=region, distributionType=FIELD,
                  field='TempGrad')
```

## Import from Thermal Analysis
```python
model.Temperature(name='Imported', createStepName='Initial',
                  region=region, distributionType=FROM_FILE,
                  fileName='thermal_result.odb',
                  step='Heating', frame=-1)
```

## Initial Velocity for Drop Test
```python
model.Velocity(name='DropVel', createStepName='Initial',
               region=allNodes,
               velocity1=0.0, velocity2=-4429.0, velocity3=0.0)  # 1m drop
```
