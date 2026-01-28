# Material API Quick Reference

Quick lookup for Abaqus material API signatures and parameters.

## Create Material

```python
material = model.Material(name='MaterialName')
```

**Parameters:**
- `name` (str): Unique material name (required)
- `description` (str): Optional description

## Elastic Properties

```python
material.Elastic(table=((E, nu),))
```

**Parameters:**
- `E`: Young's modulus (MPa) - must be > 0
- `nu`: Poisson's ratio - must be -1 < nu < 0.5

**Orthotropic/Anisotropic:**
```python
material.Elastic(
    type=ENGINEERING_CONSTANTS,
    table=((E1, E2, E3, nu12, nu13, nu23, G12, G13, G23),)
)
```

**Temperature-dependent:**
```python
material.Elastic(
    temperatureDependency=ON,
    table=(
        (E1, nu1, T1),
        (E2, nu2, T2),
    )
)
```

## Density

```python
material.Density(table=((rho,),))
```

**Parameters:**
- `rho`: Mass density (tonne/mm³ for mm-N-MPa system)

**Common values:**
| Material | Density (tonne/mm³) |
|----------|---------------------|
| Steel | 7.85e-9 |
| Aluminum | 2.70e-9 |
| Titanium | 4.43e-9 |
| Copper | 8.96e-9 |

## Plasticity

```python
material.Plastic(table=(
    (yield_stress_1, plastic_strain_1),
    (yield_stress_2, plastic_strain_2),
    ...
))
```

**Important:** First point MUST have plastic_strain = 0.0

**Example - Bilinear hardening:**
```python
material.Plastic(table=(
    (250.0, 0.0),    # Yield point (plastic strain = 0)
    (400.0, 0.20),   # Hardening point
))
```

## Thermal Properties

### Conductivity
```python
material.Conductivity(table=((k,),))
```
- `k`: Thermal conductivity (mW/mm·K)

### Specific Heat
```python
material.SpecificHeat(table=((cp,),))
```
- `cp`: Specific heat capacity (mJ/tonne·K)

### Thermal Expansion
```python
material.Expansion(table=((alpha,),))
```
- `alpha`: Coefficient of thermal expansion (1/K)

## Hyperelastic (Rubber)

### Neo-Hookean
```python
material.Hyperelastic(
    type=NEO_HOOKE,
    table=((C10, D1),)
)
```

### Mooney-Rivlin
```python
material.Hyperelastic(
    type=MOONEY_RIVLIN,
    table=((C10, C01, D1),)
)
```

## Section Creation

### Solid Section
```python
model.HomogeneousSolidSection(
    name='SectionName',
    material='MaterialName',
    thickness=None  # Only for plane stress
)
```

### Shell Section
```python
model.HomogeneousShellSection(
    name='SectionName',
    material='MaterialName',
    thickness=2.0,      # Shell thickness in mm
    numIntPts=5         # Integration points through thickness
)
```

### Beam Section
```python
model.BeamSection(
    name='SectionName',
    material='MaterialName',
    profile='ProfileName',
    integration=DURING_ANALYSIS
)
```

## Section Assignment

```python
# Create region from all cells
region = part.Set(cells=part.cells, name='AllCells')

# Assign section to region
part.SectionAssignment(
    region=region,
    sectionName='SectionName'
)
```

**Alternative - using SetFromElementLabels:**
```python
region = part.Set(elements=part.elements, name='AllElements')
part.SectionAssignment(region=region, sectionName='SectionName')
```

## Unit System Reference

All examples use consistent SI units (mm-tonne-s-N-MPa):

| Quantity | Unit | Example |
|----------|------|---------|
| Length | mm | 100.0 |
| Force | N | 1000.0 |
| Stress/Modulus | MPa | 210000.0 |
| Density | tonne/mm³ | 7.85e-9 |
| Conductivity | mW/(mm·K) | 50.0 |
| Specific Heat | mJ/(tonne·K) | 5.0e11 |
| Expansion | 1/K | 12e-6 |
