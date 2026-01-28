---
name: abaqus-bc
description: Define boundary conditions in Abaqus - fixed supports, displacements, symmetry, and other constraints. Use when constraining structural degrees of freedom to prevent rigid body motion or apply kinematic conditions. Does not handle loads (forces, pressures) or contact constraints.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
---

# Abaqus Boundary Conditions Skill

## When to Use This Skill

**USE when you need to:**
- Fix a face/edge/vertex (Encastre - all DOFs constrained)
- Apply displacement constraints (prescribed motion)
- Define symmetry planes (half/quarter models)
- Constrain specific degrees of freedom (roller, pinned)
- Apply velocity or acceleration BCs (dynamics)
- Set temperature BCs (thermal analysis)

**Do NOT use for:**
- Applying forces or pressures → use `/abaqus-load`
- Contact between parts → use `/abaqus-interaction`
- Initial conditions (initial stress, temperature) → use `/abaqus-field`

## Key Decisions

### 1. What Type of Support?

| Support Type | DOFs Fixed | Physical Meaning | Use Case |
|--------------|------------|------------------|----------|
| Encastre | All 6 | Welded, bolted, embedded | Most common for fixed end |
| Pinned | U1, U2, U3 | Ball joint, hinge | Rotation allowed |
| Roller | 1 translation | Sliding support | Free in-plane motion |
| Symmetry | Normal disp + 2 rotations | Symmetric geometry/loading | Half/quarter models |

### 2. Rigid Body Motion Check

For 3D static analysis, you must constrain **at least 6 DOFs total** to prevent:
- 3 translations (X, Y, Z)
- 3 rotations (about X, Y, Z)

| Configuration | Stability |
|---------------|-----------|
| One face fixed (Encastre) | Fully constrained (most common) |
| One vertex fixed + symmetry | May be sufficient |
| Three pinned points | Check they prevent all rotation |

**Warning sign:** "Zero pivot" or "Rigid body motion" error = insufficient constraints.

### 3. Which Step to Apply BC?

| BC Type | Step | Reason |
|---------|------|--------|
| Fixed support | Initial | Always active, set before loads |
| Prescribed displacement | Load step | Applied with loading |
| Released BC | Later step | Use `FREED` to release in subsequent step |

## Required Inputs

| Input | Required | Guidance |
|-------|----------|----------|
| BC Type | YES | Encastre, Displacement, Symmetry, etc. |
| Region | YES | Face, edge, vertex, or node set |
| Step | NO | Default 'Initial' for supports |
| Values | For Displacement | Specific values or UNSET to leave free |

## Common Patterns

### Encastre (Fully Fixed)
```python
# Find the face (coordinates must be ON the face)
fixed_face = instance.faces.findAt(((0.0, HEIGHT/2, WIDTH/2),))
fixed_region = assembly.Set(faces=fixed_face, name='FixedSupport')

# Apply Encastre (all 6 DOFs = 0)
model.EncastreBC(
    name='Fixed',
    createStepName='Initial',
    region=fixed_region
)
```

### Displacement BC (Pinned, Roller)
```python
# Pinned: translations fixed, rotations free
model.DisplacementBC(
    name='Pinned',
    createStepName='Initial',
    region=region,
    u1=0.0, u2=0.0, u3=0.0,
    ur1=UNSET, ur2=UNSET, ur3=UNSET  # Rotations free
)

# Roller: only Z direction fixed
model.DisplacementBC(
    name='RollerZ',
    createStepName='Initial',
    region=region,
    u1=UNSET, u2=UNSET, u3=0.0,  # Only Z constrained
    ur1=UNSET, ur2=UNSET, ur3=UNSET
)

# Prescribed displacement (apply 5mm downward in load step)
model.DisplacementBC(
    name='Applied',
    createStepName='LoadStep',
    region=region,
    u1=UNSET, u2=-5.0, u3=UNSET
)
```

### Symmetry BCs
```python
# X-Symmetry: plane perpendicular to X-axis
# Constrains U1 (normal displacement) and UR2, UR3 (tangent rotations)
model.XsymmBC(name='SymX', createStepName='Initial', region=region)

# Y-Symmetry
model.YsymmBC(name='SymY', createStepName='Initial', region=region)

# Z-Symmetry
model.ZsymmBC(name='SymZ', createStepName='Initial', region=region)
```

**Symmetry guidance:**
- Use X-symmetry when the model is symmetric about a YZ plane
- Apply to the face AT the symmetry plane
- Reduces model size by 2x (or 4x with two symmetry planes)

### Temperature BC (Thermal)
```python
model.TemperatureBC(
    name='HotEnd',
    createStepName='HeatStep',
    region=region,
    magnitude=100.0  # Fixed temperature value
)
```

### Velocity BC (Dynamic)
```python
model.VelocityBC(
    name='Impact',
    createStepName='Step-1',
    region=region,
    v1=0.0, v2=-1000.0, v3=0.0,  # mm/s downward
    vr1=UNSET, vr2=UNSET, vr3=UNSET
)
```

## Finding Regions

### By Coordinates (Most Common)
```python
# Point must be EXACTLY on the face
face = instance.faces.findAt(((x, y, z),))
region = assembly.Set(faces=face, name='MySet')
```

### By Bounding Box (Approximate Location)
```python
faces = instance.faces.getByBoundingBox(
    xMin=-0.01, yMin=0, zMin=0,
    xMax=0.01, yMax=100, zMax=50  # Small tolerance around x=0
)
region = assembly.Set(faces=faces, name='XZeroFace')
```

### Multiple Faces
```python
face1 = instance.faces.findAt(((x1, y1, z1),))
face2 = instance.faces.findAt(((x2, y2, z2),))
region = assembly.Set(faces=face1 + face2, name='CombinedSet')
```

## Modifying BCs in Later Steps

### Release a DOF
```python
# Initial: fully fixed
model.DisplacementBC(name='Support', createStepName='Initial', region=region,
                     u1=0.0, u2=0.0, u3=0.0)

# LoadStep: release U1
model.boundaryConditions['Support'].setValuesInStep(
    stepName='LoadStep',
    u1=FREED  # Now free to move in X
)
```

### Deactivate Entirely
```python
model.boundaryConditions['Support'].deactivate(stepName='ReleaseStep')
```

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Zero pivot" / "Rigid body motion" | Insufficient constraints | Add more BCs to prevent all 6 rigid body modes |
| "Face not found at coordinates" | Point not exactly on face | Use bounding box method or verify coordinates |
| "Over-constraint warning" | Conflicting BCs | Review if multiple BCs act on same DOF |
| "BC has no effect" | Applied to wrong region | Verify region set contains expected entities |
| "Negative eigenvalue" | Structure unstable or buckling | Check for proper support, may need stabilization |

## BC Checklist

Before running analysis:
- [ ] At least one region has fixed support (Encastre or equivalent)
- [ ] All 6 rigid body modes are constrained
- [ ] BCs applied in correct step (Initial for supports, Load step for prescribed displacement)
- [ ] Symmetry planes match actual model symmetry
- [ ] No conflicting BCs on same DOF

## API Reference

For detailed parameters: [BC API](../../docs/abaqus-api/modules/bc.md)
