# Field API Quick Reference

## Temperature (Initial/Predefined)
```python
# Uniform temperature
model.Temperature(
    name='FieldName',
    createStepName='Initial',
    region=region,
    distributionType=UNIFORM,
    magnitudes=(temperature,)
)

# From ODB (transfer from previous analysis)
model.Temperature(
    name='FieldName',
    createStepName='Initial',
    region=region,
    distributionType=FROM_FILE,
    fileName='thermal.odb',
    step='HeatStep',
    frame=-1  # Last frame
)
```

## Velocity (for explicit dynamics)
```python
model.Velocity(
    name='InitVelocity',
    createStepName='Initial',
    region=region,
    velocity1=0.0,      # X component (mm/s)
    velocity2=-1000.0,  # Y component
    velocity3=0.0       # Z component
)
```

## Stress (initial/residual)
```python
model.Stress(
    name='ResidualStress',
    createStepName='Initial',
    region=region,
    distributionType=UNIFORM,
    sigma11=100.0, sigma22=50.0, sigma33=0.0,  # Normal components
    sigma12=0.0, sigma13=0.0, sigma23=0.0      # Shear components
)
```
