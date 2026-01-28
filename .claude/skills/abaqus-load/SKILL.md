---
name: abaqus-load
description: Define loads in Abaqus - forces, pressures, tractions, thermal loads, and gravity. Use when applying external forces or thermal inputs to structures. Handles point loads, distributed loads, and body forces. Does not handle boundary conditions (constraints) or contact forces.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
---

# Abaqus Load Skill

## When to Use This Skill

**USE when you need to:**
- Apply point forces to vertices/nodes
- Apply distributed forces (traction) to surfaces
- Apply pressure (normal to surface)
- Add gravity or other body forces
- Define thermal loads (heat flux, convection)
- Create time-varying loads with amplitudes

**Do NOT use for:**
- Constraining motion (fixed, pinned) → use `/abaqus-bc`
- Prescribed displacements → use `/abaqus-bc`
- Contact forces between parts → use `/abaqus-interaction`
- Initial temperature fields → use `/abaqus-field`

## Key Decisions

### 1. Which Load Type?

| Scenario | Load Type | Units |
|----------|-----------|-------|
| Force at a point | ConcentratedForce | N |
| Force spread over surface | SurfaceTraction | MPa (force/area) |
| Normal force on surface | Pressure | MPa (+ = compression) |
| Force along edge | LineLoad | N/mm |
| Self-weight, acceleration | Gravity | mm/s² |
| Heat input | SurfaceHeatFlux | mW/mm² |

### 2. Force vs Traction Conversion

If you have a **total force** but need to apply it as **traction**:

```
Traction (MPa) = Total Force (N) / Surface Area (mm²)
```

**Example:** 1000 N on a 50×20mm face = 1000 / (50×20) = 1.0 MPa

### 3. Pressure Sign Convention

| Pressure Value | Effect |
|----------------|--------|
| Positive (+) | Compression (pushes into surface) |
| Negative (-) | Tension (pulls away from surface) |

### 4. Direction Specification

| Load Type | Direction Method |
|-----------|-----------------|
| ConcentratedForce | cf1, cf2, cf3 (X, Y, Z components) |
| SurfaceTraction | directionVector=((origin), (endpoint)) |
| Pressure | Always normal to surface (no direction needed) |
| Gravity | comp1, comp2, comp3 (acceleration components) |

## Required Inputs

| Input | Required | Guidance |
|-------|----------|----------|
| Load type | YES | Based on physical scenario |
| Region | YES | Surface, edge, or vertex |
| Magnitude | YES | Force (N), Pressure (MPa), etc. |
| Direction | Depends | Required for directional loads |
| Step | NO | Default: first analysis step |

## Common Patterns

### Concentrated Force (Point Load)
```python
# Find vertex
vertex = instance.vertices.findAt(((LENGTH, HEIGHT/2, WIDTH/2),))
region = assembly.Set(vertices=vertex, name='LoadPoint')

# Apply force (components in X, Y, Z)
model.ConcentratedForce(
    name='PointLoad',
    createStepName='LoadStep',
    region=region,
    cf1=0.0,       # X component (N)
    cf2=-1000.0,   # Y component (N) - negative = downward
    cf3=0.0        # Z component (N)
)
```

### Surface Traction (Distributed Force)
```python
# Find face and create surface
load_face = instance.faces.findAt(((LENGTH, HEIGHT/2, WIDTH/2),))
load_surface = assembly.Surface(side1Faces=load_face, name='LoadSurface')

# Direction vector: from origin point to direction point
model.SurfaceTraction(
    name='DistributedLoad',
    createStepName='LoadStep',
    region=load_surface,
    magnitude=10.0,  # MPa (force per area)
    directionVector=((0, 0, 0), (0, -1, 0)),  # Points in -Y direction
    distributionType=UNIFORM,
    traction=GENERAL
)
```

### Pressure (Normal to Surface)
```python
# Pressure always acts normal to the surface
model.Pressure(
    name='InternalPressure',
    createStepName='LoadStep',
    region=surface,
    magnitude=10.0  # MPa, positive = compression
)

# Tension (suction) - negative value
model.Pressure(
    name='Suction',
    createStepName='LoadStep',
    region=surface,
    magnitude=-5.0  # Pulls away from surface
)
```

### Gravity
```python
# Requires density in material definition!
model.Gravity(
    name='Gravity',
    createStepName='LoadStep',
    comp2=-9810.0  # mm/s² (g in -Y direction)
)
```

**Important:** Gravity requires material density. Without density, gravity has no effect.

### Line Load (Force on Edge)
```python
edge = instance.edges.findAt(((x, y, z),))
region = assembly.Set(edges=edge, name='LoadEdge')

model.LineLoad(
    name='EdgeLoad',
    createStepName='LoadStep',
    region=region,
    comp1=0.0,     # N/mm in X
    comp2=-10.0,   # N/mm in Y
    comp3=0.0      # N/mm in Z
)
```

### Heat Flux (Thermal)
```python
model.SurfaceHeatFlux(
    name='HeatIn',
    createStepName='HeatStep',
    region=surface,
    magnitude=100.0  # mW/mm²
)
```

### Convection (Thermal)
```python
model.FilmCondition(
    name='Convection',
    createStepName='HeatStep',
    region=surface,
    definition=EMBEDDED_COEFF,
    filmCoeff=10.0,        # mW/(mm²·K)
    sinkTemperature=25.0   # Ambient temperature (°C or K)
)
```

## Time-Varying Loads

### Create Amplitude First
```python
model.TabularAmplitude(
    name='LoadRamp',
    data=(
        (0.0, 0.0),   # (time, amplitude factor)
        (0.5, 1.0),   # Full load at t=0.5
        (1.0, 0.5),   # Half load at t=1.0
    )
)
```

### Apply Load with Amplitude
```python
model.ConcentratedForce(
    name='VaryingLoad',
    createStepName='LoadStep',
    region=region,
    cf2=-1000.0,
    amplitude='LoadRamp'  # References the amplitude by name
)
```

## Modifying Loads in Steps

### Change Magnitude
```python
# Original load
model.ConcentratedForce(name='Load', createStepName='Step-1',
                        region=region, cf2=-500.0)

# Increase in Step-2
model.loads['Load'].setValuesInStep(stepName='Step-2', cf2=-1000.0)
```

### Deactivate Load
```python
model.loads['Load'].deactivate(stepName='UnloadStep')
```

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Load region not found" | Typo in surface/set name | Check spelling matches exactly |
| "Zero reaction forces" | Load direction wrong or magnitude too small | Verify direction vector and units |
| "Gravity has no effect" | Material missing density | Add `material.Density(table=...)` |
| "Equilibrium not achieved" | Load too large for material/geometry | Reduce load or improve convergence settings |
| "Negative eigenvalue" | Structure unstable under load | Check BCs, may need stabilization |

## Load Checklist

Before running:
- [ ] Load applied to correct region (surface, vertex, edge)
- [ ] Direction matches physical scenario
- [ ] Magnitude in correct units (N, MPa, mW/mm²)
- [ ] Load in correct step (not Initial unless prescribed displacement)
- [ ] Density defined if using gravity
- [ ] Reactions should equal applied loads (equilibrium check)

## API Reference

For detailed parameters: [Load API](../../docs/abaqus-api/modules/load.md)
