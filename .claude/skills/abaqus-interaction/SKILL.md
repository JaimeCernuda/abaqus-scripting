---
name: abaqus-interaction
description: Define contact and interactions in Abaqus - contact pairs, tie constraints, connectors, cohesive behavior. Use for multi-body contact problems.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
---

# Abaqus Interaction Skill

## When to Use This Skill

**USE when you need to:**
- Define contact between two surfaces (with friction, separation)
- Create tie constraints (join different meshes permanently)
- Add coupling constraints (distribute load from point to surface)
- Define connector elements (springs, dampers, joints)
- Set up cohesive behavior (adhesive, delamination)
- Create rigid body constraints

**Do NOT use for:**
- Fixed supports or prescribed displacements → use `/abaqus-bc`
- Applied forces or pressures → use `/abaqus-load`
- Contact in optimization context → combine with `/abaqus-optimization`

## Key Decisions

### 1. What Type of Connection?

| Connection Type | When to Use | Key Feature |
|-----------------|-------------|-------------|
| Contact | Parts can separate and slide | Friction, gap |
| Tie | Permanent join, different meshes | No relative motion |
| Coupling | Distribute load from point to area | Reference point control |
| Connector | Springs, dampers, joints | Stiffness/damping |
| Cohesive | Adhesive bonds, delamination | Damage initiation |

### 2. Contact Formulation

| Formulation | Best For |
|-------------|----------|
| Surface-to-surface | General contact (recommended) |
| Node-to-surface | Legacy, special cases |
| General contact | Automatic detection (explicit) |
| Self-contact | Folding, buckling |

### 3. Friction Values

| Surface Pair | Friction Coefficient |
|--------------|---------------------|
| Frictionless | 0.0 |
| Lubricated metal | 0.1-0.3 |
| Dry metal | 0.3-0.5 |
| Rubber on surface | 0.5-0.8 |
| Rough (no slip) | Use ROUGH formulation |

## Required Inputs

| Input | Required | Guidance |
|-------|----------|----------|
| Master surface | YES | Usually stiffer/coarser mesh |
| Slave surface | YES | Usually finer mesh or softer |
| Contact property | YES | Normal + tangential behavior |
| Friction | If friction | Coefficient value |

## Common Patterns

### Surface-to-Surface Contact
```python
# Create surfaces
master_face = instance1.faces.findAt(((x1, y1, z1),))
master_surf = assembly.Surface(side1Faces=master_face, name='MasterSurf')

slave_face = instance2.faces.findAt(((x2, y2, z2),))
slave_surf = assembly.Surface(side1Faces=slave_face, name='SlaveSurf')

# Contact property with friction
model.ContactProperty('IntProp')
model.interactionProperties['IntProp'].TangentialBehavior(
    formulation=PENALTY,
    table=((0.3,),)  # Friction coefficient
)
model.interactionProperties['IntProp'].NormalBehavior(
    pressureOverclosure=HARD,
    allowSeparation=ON
)

# Create interaction
model.SurfaceToSurfaceContactStd(
    name='Contact-1',
    createStepName='Initial',
    master=master_surf,
    slave=slave_surf,
    sliding=FINITE,
    interactionProperty='IntProp'
)
```

### Frictionless Contact
```python
model.ContactProperty('Frictionless')
model.interactionProperties['Frictionless'].TangentialBehavior(
    formulation=FRICTIONLESS
)
model.interactionProperties['Frictionless'].NormalBehavior(
    pressureOverclosure=HARD,
    allowSeparation=ON
)
```

### Tie Constraint
```python
# Permanently join surfaces (no slip, no separation)
model.Tie(
    name='Tie-1',
    master=master_surf,
    slave=slave_surf,
    positionTolerance=0.1,
    adjust=ON,
    tieRotations=ON
)
```

### Coupling (Distribute Point Load)
```python
# Create reference point
ref_point = assembly.ReferencePoint(point=(x, y, z))
ref_region = assembly.Set(
    referencePoints=(assembly.referencePoints[ref_point.id],),
    name='RP'
)

# Couple RP to surface
model.Coupling(
    name='Coupling-1',
    controlPoint=ref_region,
    surface=surface,
    influenceRadius=WHOLE_SURFACE,
    couplingType=KINEMATIC
)
```

### Connector (Spring)
```python
# Create connector section
model.ConnectorSection(name='Spring', assembledType=AXIAL)
model.sections['Spring'].setValues(
    behaviorOptions=(
        ConnectorElasticity(components=(1,), table=((1000.0,),)),  # K=1000 N/mm
    )
)

# Create wire and assign
assembly.WirePolyLine(points=((point1, point2),), meshable=OFF)
```

### Self-Contact
```python
model.SelfContactStd(
    name='SelfContact',
    createStepName='Step-1',
    surface=surface,
    interactionProperty='IntProp'
)
```

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Contact not detected" | Surfaces too far apart | Use adjust=ON or reduce gap |
| "Severe discontinuity" | Contact chattering | Add stabilization, smaller increments |
| "Negative eigenvalue with contact" | Improper master/slave | Swap master and slave |
| "Overclosure too large" | Initial interference | Use shrink fit or adjust geometry |

## API Reference

For detailed parameters: [Interaction API](../../docs/abaqus-api/modules/interaction.md)
