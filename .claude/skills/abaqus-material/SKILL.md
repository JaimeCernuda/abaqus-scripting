---
name: abaqus-material
description: Define material properties and section assignments for Abaqus FEA. Use when specifying elastic modulus, Poisson's ratio, plasticity, thermal conductivity, or composite layups. Creates sections and assigns to part regions. Does not handle optimization material interpolation or contact surface properties.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
---

# Abaqus Material Skill

## When to Use This Skill

**USE when you need to:**
- Define elastic properties (Young's modulus, Poisson's ratio)
- Add density for dynamic analysis, gravity loads, or mass calculations
- Specify plastic behavior (yield stress, hardening)
- Define thermal properties (conductivity, specific heat, expansion)
- Create orthotropic/composite material definitions
- Assign sections to part regions

**Do NOT use for:**
- Contact surface properties (friction, damping) → use `/abaqus-interaction`
- Optimization material interpolation (SIMP, RAMP) → use `/abaqus-optimization`
- Temperature-dependent boundary conditions → use `/abaqus-field`

## Key Decisions

### 1. What Properties Do I Need?

| Analysis Type | Required Properties | Optional |
|--------------|---------------------|----------|
| Static stress | E, ν | - |
| Static with gravity | E, ν, ρ | - |
| Yielding/plastic | E, ν, σy, εp table | ρ |
| Modal/frequency | E, ν, ρ | - |
| Dynamic explicit | E, ν, ρ | Plasticity |
| Thermal stress | E, ν, α | k, cp |
| Heat transfer only | k | cp, ρ |

**Key insight:** Density (ρ) is required whenever inertia matters - modal analysis, dynamics, gravity loads.

### 2. Choosing Material Values

| Material | E (MPa) | ν | ρ (t/mm³) | σy (MPa) | Typical Use |
|----------|---------|---|-----------|----------|-------------|
| Steel (mild) | 210000 | 0.30 | 7.85e-9 | 250 | General structural |
| Steel (high-strength) | 210000 | 0.30 | 7.85e-9 | 550 | High-load applications |
| Stainless 304 | 193000 | 0.29 | 8.00e-9 | 215 | Corrosion resistance |
| Aluminum 6061-T6 | 68900 | 0.33 | 2.70e-9 | 276 | Lightweight structures |
| Aluminum 7075-T6 | 71700 | 0.33 | 2.81e-9 | 503 | Aerospace |
| Titanium Ti-6Al-4V | 113800 | 0.34 | 4.43e-9 | 880 | High strength-to-weight |

**Unit system:** mm-tonne-s-N-MPa (consistent SI)

### 3. Section Type Selection

| Geometry Type | Section | When to Use |
|--------------|---------|-------------|
| 3D solid (hex/tet) | HomogeneousSolidSection | Most FEA models |
| Thin walls (t/L < 0.1) | HomogeneousShellSection | Plates, sheet metal |
| Slender members (L/d > 10) | BeamSection | Frames, trusses |
| Layered composites | CompositeShellSection | Carbon fiber, laminates |

## Required Inputs

| Input | Required | Guidance |
|-------|----------|----------|
| Young's Modulus (E) | YES | Must be > 0. If unknown, use steel (210000 MPa) as baseline |
| Poisson's Ratio (ν) | YES | Must be -1 < ν < 0.5. Typical metals: 0.25-0.35, rubber: ~0.49 |
| Density (ρ) | For dynamic | Required for modal, explicit, gravity. Units: tonne/mm³ |
| Yield Stress (σy) | For plastic | First point where plastic strain = 0 |

## Common Patterns

### Basic Elastic Material
```python
material = model.Material(name='Steel')
material.Elastic(table=((210000.0, 0.3),))  # (E, nu)
material.Density(table=((7.85e-9,),))        # Required for dynamics/gravity

# Create section
model.HomogeneousSolidSection(name='SolidSection', material='Steel')

# Assign to part (do this AFTER section creation)
region = part.Set(cells=part.cells, name='AllCells')
part.SectionAssignment(region=region, sectionName='SolidSection')
```

### Elastic-Plastic (Bilinear Hardening)
```python
material = model.Material(name='Steel_Plastic')
material.Elastic(table=((210000.0, 0.3),))
material.Plastic(table=(
    (250.0, 0.0),    # (yield stress, plastic strain) - must start at 0 plastic strain
    (400.0, 0.20),   # Hardening: stress increases with plastic strain
))
material.Density(table=((7.85e-9,),))
```

### Thermal Material (Heat Transfer + Thermal Stress)
```python
material = model.Material(name='Steel_Thermal')
material.Elastic(table=((210000.0, 0.3),))
material.Density(table=((7.85e-9,),))
material.Conductivity(table=((50.0,),))        # mW/(mm·K)
material.SpecificHeat(table=((5.0e11,),))      # mJ/(tonne·K)
material.Expansion(table=((12e-6,),))          # Thermal expansion coefficient (1/K)
```

### Temperature-Dependent Properties
```python
material.Elastic(
    temperatureDependency=ON,
    table=(
        (210000.0, 0.30, 20.0),   # (E, nu, temperature)
        (200000.0, 0.30, 200.0),
        (180000.0, 0.31, 400.0),
    )
)
```

### Orthotropic (Composites)
```python
material = model.Material(name='Carbon_Epoxy')
material.Elastic(
    type=ENGINEERING_CONSTANTS,
    table=((
        135000.0,  # E1 (fiber direction)
        10000.0,   # E2 (transverse)
        10000.0,   # E3
        0.30, 0.30, 0.40,  # nu12, nu13, nu23
        5000.0, 5000.0, 3500.0,  # G12, G13, G23
    ),)
)
```

### Shell Section
```python
model.HomogeneousShellSection(
    name='ShellSection',
    material='Steel',
    thickness=2.0,  # Shell thickness in mm
    numIntPts=5     # Integration points through thickness
)
```

## Validation Checks

Before running analysis, verify:
- E > 0 (positive stiffness)
- -1 < ν < 0.5 (stable material; ν = 0.5 causes numerical issues)
- ρ > 0 if needed
- Plastic table starts at zero plastic strain
- Section is assigned to ALL cells that need it

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Material has no density" | Density required for this analysis type | Add `material.Density(table=((value,),))` |
| "Negative eigenvalue in material stiffness" | Invalid Poisson's ratio | Ensure -1 < ν < 0.5 |
| "Section not assigned to region" | Missing SectionAssignment call | Call `part.SectionAssignment(region=..., sectionName=...)` |
| "Region has no mesh" | Cells not meshed before assignment | Mesh after section assignment, or use part-level assignment |
| "Material X not found" | Typo in material name reference | Check spelling matches exactly |

## API Reference

For detailed parameter syntax: [Material API](../../docs/abaqus-api/modules/material.md)
