# Materials Database

Ready-to-use material property sets for common engineering materials.
All values in SI (mm-tonne-s-N-MPa) units.

## Quick Copy Patterns

**Need steel fast?**
```python
mat = model.Material(name='Steel'); mat.Elastic(table=((210000.0, 0.3),)); mat.Density(table=((7.85e-9,),))
```

**Need aluminum fast?**
```python
mat = model.Material(name='Aluminum'); mat.Elastic(table=((68900.0, 0.33),)); mat.Density(table=((2.70e-9,),))
```

**Need titanium fast?**
```python
mat = model.Material(name='Titanium'); mat.Elastic(table=((113800.0, 0.34),)); mat.Density(table=((4.43e-9,),))
```

## Metals

### Steel - Mild/Structural (ASTM A36)
```python
material = model.Material(name='Steel_Mild')
material.Elastic(table=((210000.0, 0.30),))
material.Plastic(table=(
    (250.0, 0.000),
    (400.0, 0.200),
))
material.Density(table=((7.85e-9,),))
```

### Steel - High Strength (AISI 4340)
```python
material = model.Material(name='Steel_HighStrength')
material.Elastic(table=((205000.0, 0.29),))
material.Plastic(table=(
    (860.0, 0.000),
    (1100.0, 0.100),
    (1200.0, 0.200),
))
material.Density(table=((7.85e-9,),))
```

### Stainless Steel 304
```python
material = model.Material(name='SS304')
material.Elastic(table=((193000.0, 0.29),))
material.Plastic(table=(
    (215.0, 0.000),
    (505.0, 0.400),
))
material.Density(table=((8.00e-9,),))
```

### Stainless Steel 316
```python
material = model.Material(name='SS316')
material.Elastic(table=((193000.0, 0.30),))
material.Plastic(table=(
    (290.0, 0.000),
    (580.0, 0.400),
))
material.Density(table=((8.00e-9,),))
```

### Aluminum 6061-T6
```python
material = model.Material(name='Al6061T6')
material.Elastic(table=((68900.0, 0.33),))
material.Plastic(table=(
    (276.0, 0.000),
    (310.0, 0.040),
    (330.0, 0.080),
))
material.Density(table=((2.70e-9,),))
```

### Aluminum 7075-T6
```python
material = model.Material(name='Al7075T6')
material.Elastic(table=((71700.0, 0.33),))
material.Plastic(table=(
    (503.0, 0.000),
    (572.0, 0.070),
))
material.Density(table=((2.81e-9,),))
```

### Titanium Ti-6Al-4V
```python
material = model.Material(name='Ti6Al4V')
material.Elastic(table=((113800.0, 0.34),))
material.Plastic(table=(
    (880.0, 0.000),
    (950.0, 0.040),
    (1000.0, 0.100),
))
material.Density(table=((4.43e-9,),))
```

### Copper (Pure)
```python
material = model.Material(name='Copper')
material.Elastic(table=((117000.0, 0.34),))
material.Plastic(table=(
    (70.0, 0.000),
    (220.0, 0.300),
))
material.Density(table=((8.96e-9,),))
```

### Brass (70Cu-30Zn)
```python
material = model.Material(name='Brass')
material.Elastic(table=((100000.0, 0.34),))
material.Plastic(table=(
    (200.0, 0.000),
    (400.0, 0.300),
))
material.Density(table=((8.50e-9,),))
```

## Plastics/Polymers

### ABS
```python
material = model.Material(name='ABS')
material.Elastic(table=((2300.0, 0.35),))
material.Plastic(table=(
    (40.0, 0.000),
    (50.0, 0.020),
))
material.Density(table=((1.05e-9,),))
```

### Nylon 6/6
```python
material = model.Material(name='Nylon66')
material.Elastic(table=((2800.0, 0.40),))
material.Plastic(table=(
    (70.0, 0.000),
    (85.0, 0.050),
))
material.Density(table=((1.14e-9,),))
```

### PEEK
```python
material = model.Material(name='PEEK')
material.Elastic(table=((3600.0, 0.40),))
material.Plastic(table=(
    (100.0, 0.000),
    (110.0, 0.030),
))
material.Density(table=((1.30e-9,),))
```

### Polycarbonate
```python
material = model.Material(name='PC')
material.Elastic(table=((2400.0, 0.37),))
material.Plastic(table=(
    (60.0, 0.000),
    (70.0, 0.050),
))
material.Density(table=((1.20e-9,),))
```

## Composites

### Carbon Fiber/Epoxy (UD)
```python
material = model.Material(name='CFRP_UD')
material.Elastic(
    type=ENGINEERING_CONSTANTS,
    table=((
        135000.0,  # E1
        10000.0,   # E2
        10000.0,   # E3
        0.30,      # nu12
        0.30,      # nu13
        0.40,      # nu23
        5000.0,    # G12
        5000.0,    # G13
        3500.0,    # G23
    ),)
)
material.Density(table=((1.60e-9,),))
```

### Glass Fiber/Epoxy (UD)
```python
material = model.Material(name='GFRP_UD')
material.Elastic(
    type=ENGINEERING_CONSTANTS,
    table=((
        40000.0,   # E1
        8000.0,    # E2
        8000.0,    # E3
        0.26,      # nu12
        0.26,      # nu13
        0.40,      # nu23
        4000.0,    # G12
        4000.0,    # G13
        3000.0,    # G23
    ),)
)
material.Density(table=((2.00e-9,),))
```

## Rubber/Elastomers

### Natural Rubber (Neo-Hookean)
```python
material = model.Material(name='NaturalRubber')
material.Hyperelastic(
    type=NEO_HOOKE,
    table=((0.4, 0.001),)  # C10, D1
)
material.Density(table=((1.10e-9,),))
```

### Silicone (Mooney-Rivlin)
```python
material = model.Material(name='Silicone')
material.Hyperelastic(
    type=MOONEY_RIVLIN,
    table=((0.25, 0.06, 0.002),)  # C10, C01, D1
)
material.Density(table=((1.15e-9,),))
```

## Thermal Properties Table

| Material | k (mW/mm·K) | cp (mJ/t·K) | α (1/K) |
|----------|-------------|-------------|---------|
| Steel (Mild) | 50 | 5.0e11 | 12.0e-6 |
| SS 304 | 16 | 5.0e11 | 17.3e-6 |
| Al 6061 | 167 | 8.96e11 | 23.6e-6 |
| Ti-6Al-4V | 6.7 | 5.26e11 | 8.6e-6 |
| Copper | 385 | 3.85e11 | 17.0e-6 |
| ABS | 0.17 | 1.4e12 | 90.0e-6 |
| PEEK | 0.25 | 3.2e11 | 47.0e-6 |

### Adding Thermal Properties
```python
# Add to existing material
material.Conductivity(table=((50.0,),))        # mW/(mm·K)
material.SpecificHeat(table=((5.0e11,),))      # mJ/(tonne·K)
material.Expansion(table=((12.0e-6,),))        # 1/K
```

## Material Selection Guide

| Application | Recommended Material | Key Properties |
|-------------|---------------------|----------------|
| General structural | Steel (Mild) | High E, good yield |
| Lightweight | Aluminum 6061-T6 | Low density, decent strength |
| High strength-to-weight | Ti-6Al-4V | Best strength/density ratio |
| Corrosion resistance | SS 304/316 | Chemical stability |
| High performance | Steel 4340 | Very high yield |
| Cost-effective | Steel (Mild) | Cheapest option |

## Common Material Pairs for Comparison

### Steel vs Aluminum (Weight Saving Study)
```python
# Steel reference
steel = model.Material(name='Steel')
steel.Elastic(table=((210000.0, 0.30),))
steel.Density(table=((7.85e-9,),))

# Aluminum alternative (65% lighter, 67% less stiff)
aluminum = model.Material(name='Aluminum')
aluminum.Elastic(table=((68900.0, 0.33),))
aluminum.Density(table=((2.70e-9,),))
```

### Elastic vs Elastic-Plastic (Nonlinearity Study)
```python
# Linear elastic
steel_elastic = model.Material(name='Steel_Elastic')
steel_elastic.Elastic(table=((210000.0, 0.30),))
steel_elastic.Density(table=((7.85e-9,),))

# Elastic-plastic with hardening
steel_plastic = model.Material(name='Steel_Plastic')
steel_plastic.Elastic(table=((210000.0, 0.30),))
steel_plastic.Plastic(table=((250.0, 0.0), (400.0, 0.20),))
steel_plastic.Density(table=((7.85e-9,),))
```

## Unit Conversion Reference

If you have properties in other units:

| From | To | Multiply by |
|------|-----|-------------|
| GPa | MPa | 1000 |
| kg/m³ | tonne/mm³ | 1e-12 |
| W/(m·K) | mW/(mm·K) | 1 |
| J/(kg·K) | mJ/(tonne·K) | 1e9 |
| 1/°C | 1/K | 1 (same) |
