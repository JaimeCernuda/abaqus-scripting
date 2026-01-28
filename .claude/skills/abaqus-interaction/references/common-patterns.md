# Common Interaction Patterns

## Frictionless Contact
```python
model.ContactProperty('Frictionless')
model.interactionProperties['Frictionless'].TangentialBehavior(formulation=FRICTIONLESS)
model.interactionProperties['Frictionless'].NormalBehavior(pressureOverclosure=HARD)
```

## Contact with Friction (mu=0.3)
```python
model.ContactProperty('Friction')
model.interactionProperties['Friction'].TangentialBehavior(
    formulation=PENALTY, table=((0.3,),))
model.interactionProperties['Friction'].NormalBehavior(pressureOverclosure=HARD)
```

## Bonded Surfaces (Tie)
```python
master = assembly.Surface(side1Faces=masterFaces, name='Master')
slave = assembly.Surface(side1Faces=slaveFaces, name='Slave')
model.Tie(name='Bonded', master=master, slave=slave, adjust=ON)
```

## Self-Contact
```python
model.SelfContactStd(name='SelfContact', createStepName='Step',
                     surface=surface, interactionProperty='PropName')
```

## Bolt-Plate Connection Pattern
```python
# Create surfaces for bolt head and plate
bolt_face = bolt_instance.faces.findAt(((bolt_x, bolt_y, bolt_z),))
bolt_surf = assembly.Surface(side1Faces=bolt_face, name='BoltHead')

plate_face = plate_instance.faces.findAt(((plate_x, plate_y, plate_z),))
plate_surf = assembly.Surface(side1Faces=plate_face, name='PlateTop')

# Contact with friction
model.ContactProperty('BoltContact')
model.interactionProperties['BoltContact'].TangentialBehavior(
    formulation=PENALTY, table=((0.4,),))  # Steel-steel friction
model.interactionProperties['BoltContact'].NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=ON)

model.SurfaceToSurfaceContactStd(
    name='Bolt-Plate',
    createStepName='Initial',
    master=bolt_surf,
    slave=plate_surf,
    sliding=SMALL,
    interactionProperty='BoltContact'
)
```

## Press-Fit / Interference Fit
```python
# For initial overclosure, use interference fit
model.ContactProperty('PressFit')
model.interactionProperties['PressFit'].TangentialBehavior(
    formulation=PENALTY, table=((0.3,),))
model.interactionProperties['PressFit'].NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=OFF)  # No separation

model.SurfaceToSurfaceContactStd(
    name='PressFit',
    createStepName='Initial',
    master=outer_surf,
    slave=inner_surf,
    sliding=SMALL,
    interactionProperty='PressFit',
    initialClearance=OMIT,
    interferenceType=SHRINK_FIT
)
```

## General Contact (Explicit Dynamics)
```python
# Automatically detect all contacting surfaces
model.ContactExp(name='GeneralContact', createStepName='Step-1')

# Include all exterior surfaces
model.interactions['GeneralContact'].includedPairs.setValuesInStep(
    stepName='Step-1', useAllstar=ON)

# Assign contact property globally
model.interactions['GeneralContact'].contactPropertyAssignments.appendInStep(
    stepName='Step-1',
    assignments=((GLOBAL, SELF, 'ContactProp'),))
```

## Coupling for Load Distribution
```python
# Create reference point at load application location
rp = assembly.ReferencePoint(point=(load_x, load_y, load_z))
rp_region = assembly.Set(
    referencePoints=(assembly.referencePoints[rp.id],),
    name='LoadPoint')

# Get surface to distribute load
load_surf = assembly.Surface(side1Faces=load_faces, name='LoadSurface')

# Create coupling (distributing for deformable bodies)
model.Coupling(
    name='LoadCoupling',
    controlPoint=rp_region,
    surface=load_surf,
    influenceRadius=WHOLE_SURFACE,
    couplingType=DISTRIBUTING,
    weightingMethod=UNIFORM
)

# Now apply load to reference point
model.ConcentratedForce(
    name='Load',
    createStepName='Step-1',
    region=rp_region,
    cf2=-1000.0  # Force in Y direction
)
```

## Multi-Part Assembly with Ties
```python
# Tie multiple parts together at their interfaces
for i in range(len(parts) - 1):
    master_surf = assembly.Surface(
        side1Faces=instances[i].faces.findAt(((x, y, z),)),
        name='Master-%d' % i)
    slave_surf = assembly.Surface(
        side1Faces=instances[i+1].faces.findAt(((x, y, z),)),
        name='Slave-%d' % i)

    model.Tie(
        name='Tie-%d' % i,
        master=master_surf,
        slave=slave_surf,
        positionToleranceMethod=COMPUTED,
        adjust=ON,
        tieRotations=ON
    )
```
