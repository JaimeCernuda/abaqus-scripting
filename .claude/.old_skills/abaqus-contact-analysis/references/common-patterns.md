# Common Contact Patterns

## Bolt-Plate Assembly

```python
# Bolt shank to plate hole - tie constraint (bonded)
model.Tie(name='BoltHole', master=plateSurf, slave=boltSurf)

# Bolt head to plate top - contact with friction
model.ContactProperty('HeadProp')
model.interactionProperties['HeadProp'].TangentialBehavior(
    formulation=PENALTY, table=((0.3,),))
model.interactionProperties['HeadProp'].NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=ON)
model.SurfaceToSurfaceContactStd(
    name='HeadContact',
    createStepName='Initial',
    master=plateTopSurf,
    slave=boltHeadSurf,
    sliding=FINITE,
    interactionProperty='HeadProp'
)
```

## Press Fit (Interference)

```python
# Allow initial overclosure to be resolved
model.SurfaceToSurfaceContactStd(
    name='PressFit',
    createStepName='Initial',
    master=holeSurf,
    slave=shaftSurf,
    sliding=FINITE,
    interactionProperty='Prop',
    adjustment=OVERCLOSED  # Critical for interference fits
)
```

## Frictionless Contact

```python
# For lubricated surfaces
model.ContactProperty('Frictionless')
model.interactionProperties['Frictionless'].TangentialBehavior(
    formulation=FRICTIONLESS)
model.interactionProperties['Frictionless'].NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=ON)
```

## Self Contact

```python
# For folding/buckling where surface contacts itself
model.SelfContactStd(
    name='SelfContact',
    createStepName='Step',
    surface=deformingSurface,
    interactionProperty='Prop'
)
```

## Bearing Contact

```python
# Inner race to rolling element contact
model.ContactProperty('BearingProp')
model.interactionProperties['BearingProp'].TangentialBehavior(
    formulation=PENALTY, table=((0.1,),))  # Low friction
model.interactionProperties['BearingProp'].NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=ON)
```

## Gear Meshing

```python
# Gear teeth contact with friction
model.ContactProperty('GearProp')
model.interactionProperties['GearProp'].TangentialBehavior(
    formulation=PENALTY, table=((0.2,),))
model.interactionProperties['GearProp'].NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=ON)

# Use FINITE sliding for rolling contact
model.SurfaceToSurfaceContactStd(
    name='GearContact',
    createStepName='Step',
    master=gear1Teeth,
    slave=gear2Teeth,
    sliding=FINITE,
    interactionProperty='GearProp'
)
```

## Clamp/Fixture Contact

```python
# Clamping force through contact
model.ContactProperty('ClampProp')
model.interactionProperties['ClampProp'].TangentialBehavior(
    formulation=PENALTY, table=((0.5,),))  # High friction
model.interactionProperties['ClampProp'].NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=OFF)  # No separation
```

## Rubber/Soft Contact

```python
# Soft contact for rubber-like materials
model.ContactProperty('RubberProp')
model.interactionProperties['RubberProp'].TangentialBehavior(
    formulation=PENALTY, table=((0.7,),))
model.interactionProperties['RubberProp'].NormalBehavior(
    pressureOverclosure=EXPONENTIAL,
    table=((p0, c0),),  # Pressure at zero clearance, clearance at zero pressure
    allowSeparation=ON
)
```

## Multi-Body General Contact

```python
# For assemblies with many contacting bodies
model.ContactExp(name='GeneralContact', createStepName='Step')
model.interactions['GeneralContact'].includedPairs.setValuesInStep(
    stepName='Step', useAllstar=ON)
model.interactions['GeneralContact'].contactPropertyAssignments.appendInStep(
    stepName='Step', assignments=((GLOBAL, SELF, 'PropName'),))
```
