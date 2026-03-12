# Contact Analysis API Quick Reference

## Contact Property

```python
model.ContactProperty('PropName')

# Friction
model.interactionProperties['PropName'].TangentialBehavior(
    formulation=PENALTY,       # or FRICTIONLESS, ROUGH
    table=((friction_coeff,),),
    fraction=0.005            # Elastic slip tolerance
)

# Normal behavior
model.interactionProperties['PropName'].NormalBehavior(
    pressureOverclosure=HARD,  # or EXPONENTIAL, LINEAR
    allowSeparation=ON
)
```

## Surface-to-Surface Contact

```python
model.SurfaceToSurfaceContactStd(
    name='ContactName',
    createStepName='StepName',
    master=masterSurface,      # Stiffer surface
    slave=slaveSurface,        # Softer surface
    sliding=FINITE,            # or SMALL
    interactionProperty='PropName',
    adjustment=OVERCLOSED      # Initial overclosure handling
)
```

## Tie Constraint (bonded)

```python
model.Tie(
    name='TieName',
    master=masterSurface,
    slave=slaveSurface,
    positionToleranceMethod=COMPUTED,
    adjust=ON
)
```

## General Contact (explicit)

```python
model.ContactExp(name='GC', createStepName='Step')
model.interactions['GC'].includedPairs.setValuesInStep(stepName='Step', useAllstar=ON)
```

## Surface Creation

```python
# Create surface on assembly instance
face = instance.faces.findAt(((x, y, z),))
assembly.Surface(side1Faces=face, name='SurfaceName')

# Access surface
assembly.surfaces['SurfaceName']
```

## Contact Output Requests

```python
model.FieldOutputRequest(
    name='ContactOutput',
    createStepName='StepName',
    variables=('CSTRESS', 'CDISP', 'COPEN', 'CSLIP')
)
```

## Tangential Behavior Options

| Formulation | Description |
|-------------|-------------|
| `FRICTIONLESS` | No friction (mu=0) |
| `PENALTY` | Friction with penalty method |
| `ROUGH` | Infinite friction (no slip) |
| `LAGRANGE` | Friction with Lagrange multipliers |

## Normal Behavior Options

| pressureOverclosure | Description |
|---------------------|-------------|
| `HARD` | Hard contact (default) |
| `EXPONENTIAL` | Soft contact with exponential relation |
| `LINEAR` | Soft contact with linear relation |
| `TABULAR` | User-defined pressure-overclosure |

## Sliding Formulation

| Option | Description |
|--------|-------------|
| `FINITE` | Large sliding (general) |
| `SMALL` | Small sliding (faster, limited motion) |

## Contact Stabilization

```python
model.SurfaceToSurfaceContactStd(
    name='Contact',
    createStepName='Step',
    master=masterSurf,
    slave=slaveSurf,
    interactionProperty='Prop',
    contactStabilization=ON,
    stabilizationMagnitude=0.001
)
```
