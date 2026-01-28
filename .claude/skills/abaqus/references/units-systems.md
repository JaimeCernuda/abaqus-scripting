# Abaqus Units Systems

Abaqus has no built-in unit system. You must use consistent units throughout.

## Recommended System: SI (mm)

This project uses the SI (mm) system:

| Quantity | Unit | Symbol |
|----------|------|--------|
| Length | millimeter | mm |
| Force | newton | N |
| Mass | tonne (1000 kg) | t |
| Time | second | s |
| Stress/Pressure | megapascal | MPa |
| Energy | millijoule | mJ |
| Density | tonne/mm³ | t/mm³ |

## Common Material Properties

### Steel (General)
```python
YOUNGS_MODULUS = 210000.0   # MPa
POISSONS_RATIO = 0.3        # dimensionless
DENSITY = 7.85e-9           # tonne/mm³
YIELD_STRENGTH = 250.0      # MPa
```

### Aluminum 6061-T6
```python
YOUNGS_MODULUS = 68900.0    # MPa
POISSONS_RATIO = 0.33       # dimensionless
DENSITY = 2.70e-9           # tonne/mm³
YIELD_STRENGTH = 276.0      # MPa
```

### Titanium Ti-6Al-4V
```python
YOUNGS_MODULUS = 113800.0   # MPa
POISSONS_RATIO = 0.34       # dimensionless
DENSITY = 4.43e-9           # tonne/mm³
YIELD_STRENGTH = 880.0      # MPa
```

### Carbon Fiber (Unidirectional)
```python
E1 = 135000.0               # MPa (fiber direction)
E2 = 10000.0                # MPa (transverse)
NU12 = 0.30                 # dimensionless
G12 = 5000.0                # MPa
DENSITY = 1.60e-9           # tonne/mm³
```

### ABS Plastic
```python
YOUNGS_MODULUS = 2300.0     # MPa
POISSONS_RATIO = 0.35       # dimensionless
DENSITY = 1.05e-9           # tonne/mm³
YIELD_STRENGTH = 40.0       # MPa
```

## Unit Conversion

### Density Conversions
| From | To t/mm³ | Multiply by |
|------|----------|-------------|
| kg/m³ | t/mm³ | 1e-12 |
| g/cm³ | t/mm³ | 1e-9 |
| kg/mm³ | t/mm³ | 1e-3 |

Example: Steel 7850 kg/m³ = 7850 × 1e-12 = 7.85e-9 t/mm³

### Stress/Pressure Conversions
| From | To MPa | Multiply by |
|------|--------|-------------|
| Pa | MPa | 1e-6 |
| kPa | MPa | 1e-3 |
| GPa | MPa | 1e3 |
| psi | MPa | 0.00689476 |
| ksi | MPa | 6.89476 |

### Force Conversions
| From | To N | Multiply by |
|------|------|-------------|
| kN | N | 1e3 |
| MN | N | 1e6 |
| lbf | N | 4.44822 |
| kip | N | 4448.22 |

## Alternative Unit Systems

### SI (m) - Rarely used for FEA
| Quantity | Unit |
|----------|------|
| Length | m |
| Force | N |
| Mass | kg |
| Time | s |
| Stress | Pa |
| Density | kg/m³ |

### US Customary (inch-lbf-s)
| Quantity | Unit |
|----------|------|
| Length | inch |
| Force | lbf |
| Mass | lbf·s²/in (slug/12) |
| Time | s |
| Stress | psi |
| Density | lbf·s²/in⁴ |

## Thermal Properties

### For SI (mm) system:
| Property | Unit | Steel Example |
|----------|------|---------------|
| Conductivity | mW/(mm·K) | 50.0 |
| Specific Heat | mJ/(t·K) | 500e9 |
| Expansion | 1/K | 12e-6 |

### Conversion from SI:
- Conductivity: W/(m·K) → mW/(mm·K): multiply by 1.0 (same value!)
- Specific Heat: J/(kg·K) → mJ/(t·K): multiply by 1e6

## Verification Checks

Always verify units are correct by:

1. **Dimensional analysis**: Ensure equations balance
2. **Order of magnitude**: Check if results are reasonable
3. **Comparison**: Compare with analytical solutions or known benchmarks

### Example Check: Cantilever Beam

For a cantilever beam with:
- Length L = 100 mm
- Cross-section: 10 mm × 10 mm (I = 833.33 mm⁴)
- E = 210000 MPa
- Load P = 1000 N

Theoretical deflection at free end:
```
δ = PL³/(3EI) = 1000 × 100³/(3 × 210000 × 833.33) = 0.190 mm
```

If your FEA gives a similar value, units are correct.
