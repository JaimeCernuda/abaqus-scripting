# Boundary Condition API Quick Reference

## EncastreBC (Fixed - All DOFs)
```python
model.EncastreBC(
    name='BCName',
    createStepName='Initial',  # Usually in Initial step
    region=region              # Set of faces, edges, or vertices
)
```

## DisplacementBC (Selective DOFs)
```python
model.DisplacementBC(
    name='BCName',
    createStepName='Initial',
    region=region,
    u1=0.0, u2=0.0, u3=0.0,      # Translations (SET or UNSET)
    ur1=UNSET, ur2=UNSET, ur3=UNSET  # Rotations
)
```
- SET value = constrained to that value
- UNSET = free

## Symmetry BCs
```python
model.XsymmBC(name='SymX', createStepName='Initial', region=region)  # YZ plane
model.YsymmBC(name='SymY', createStepName='Initial', region=region)  # XZ plane
model.ZsymmBC(name='SymZ', createStepName='Initial', region=region)  # XY plane
```

## Prescribed Displacement (non-zero)
```python
model.DisplacementBC(name='Move', createStepName='LoadStep', region=region,
                     u1=10.0)  # Move 10mm in X
```

## VelocityBC (Dynamic Analysis)
```python
model.VelocityBC(
    name='Impact',
    createStepName='Step-1',
    region=region,
    v1=0.0, v2=-1000.0, v3=0.0,  # mm/s
    vr1=UNSET, vr2=UNSET, vr3=UNSET
)
```

## TemperatureBC (Thermal Analysis)
```python
model.TemperatureBC(
    name='HotEnd',
    createStepName='HeatStep',
    region=region,
    magnitude=100.0  # Fixed temperature
)
```

## Modifying BCs in Steps
```python
# Release a DOF
model.boundaryConditions['Support'].setValuesInStep(
    stepName='LoadStep',
    u1=FREED  # Now free to move
)

# Deactivate entirely
model.boundaryConditions['Support'].deactivate(stepName='ReleaseStep')
```
