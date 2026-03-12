# Interaction API Quick Reference

## Tie Constraint (bonded/welded)
```python
model.Tie(
    name='TieName',
    master=masterSurface,   # Surface object
    slave=slaveSurface,
    positionToleranceMethod=COMPUTED,
    adjust=ON               # Adjust slave nodes to master
)
```

## Contact Property
```python
model.ContactProperty('PropName')
# Friction
model.interactionProperties['PropName'].TangentialBehavior(
    formulation=PENALTY,
    fraction=0.005,         # Elastic slip tolerance
    shearStressLimit=None,
    directionality=ISOTROPIC,
    table=((friction_coeff,),)  # Friction coefficient
)
# Normal behavior
model.interactionProperties['PropName'].NormalBehavior(
    pressureOverclosure=HARD,  # or EXPONENTIAL, LINEAR, TABULAR
    allowSeparation=ON
)
```

## Surface-to-Surface Contact
```python
model.SurfaceToSurfaceContactStd(
    name='ContactName',
    createStepName='StepName',
    master=masterSurface,
    slave=slaveSurface,
    sliding=FINITE,           # or SMALL
    interactionProperty='PropName'
)
```

## General Contact (all surfaces)
```python
model.ContactExp(name='GC', createStepName='Step')
model.interactions['GC'].includedPairs.setValuesInStep(
    stepName='Step', useAllstar=ON)
model.interactions['GC'].contactPropertyAssignments.appendInStep(
    stepName='Step', assignments=((GLOBAL, SELF, 'PropName'),))
```

## Coupling Constraint
```python
model.Coupling(
    name='CouplingName',
    controlPoint=refPointRegion,
    surface=targetSurface,
    influenceRadius=WHOLE_SURFACE,
    couplingType=KINEMATIC,   # or DISTRIBUTING
    weightingMethod=UNIFORM
)
```

## Connector Section
```python
model.ConnectorSection(
    name='ConnectorName',
    assembledType=AXIAL      # CARTESIAN, ROTATION, etc.
)
model.sections['ConnectorName'].setValues(
    behaviorOptions=(
        ConnectorElasticity(components=(1,), table=((stiffness,),)),
        ConnectorDamping(components=(1,), table=((damping,),))
    )
)
```

## Rigid Body
```python
model.RigidBody(
    name='RigidBodyName',
    refPointRegion=refPointRegion,
    bodyRegion=cellRegion
)
```

## Cohesive Behavior
```python
model.interactionProperties['PropName'].CohesiveBehavior(
    defaultPenalties=OFF,
    table=((Knn, Kss, Ktt),)  # Stiffness in normal, shear directions
)
model.interactionProperties['PropName'].Damage(
    initTable=((traction_n, traction_s, traction_t),),
    criterion=MAXS
)
```
