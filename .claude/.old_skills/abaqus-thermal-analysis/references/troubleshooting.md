# Thermal Analysis Troubleshooting

## Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "No temperature output" | Wrong output variable | Use NT11 for temperature, not TEMP |
| "Conductivity not defined" | Missing material property | Add `material.Conductivity()` |
| "Transient requires specific heat" | Missing property for transient | Add `material.SpecificHeat()` and `material.Density()` |
| "Negative temperature" | Check units or model | Verify thermal loads and BCs |
| "Temperature oscillation" | Time increments too large | Reduce `maxInc` or `deltmx` |
| "No convergence" | Severe nonlinearity | Add temperature-dependent relaxation or reduce increments |
| "Heat flux is zero" | Region not properly defined | Verify surface/face selection |

## Unit Consistency

### SI-mm-tonne-s-mW-K System

This is the recommended unit system for Abaqus thermal analysis when using mm for length.

| Property | SI Units | mm-tonne-s-mW-K | Conversion |
|----------|----------|-----------------|------------|
| Length | m | mm | × 1000 |
| Mass | kg | tonne | × 1e-3 |
| Time | s | s | same |
| Temperature | K or °C | K or °C | same |
| Conductivity | W/(m·K) | mW/(mm·K) | same numerical value |
| Specific Heat | J/(kg·K) | mJ/(tonne·K) | × 1e9 |
| Heat Flux | W/m² | mW/mm² | × 1e-3 |
| Heat Generation | W/m³ | mW/mm³ | × 1e-6 |
| Film Coefficient | W/(m²·K) | mW/(mm²·K) | × 1e-3 |

### Unit Conversion Examples

**Conductivity:**
- Steel: 50 W/(m·K) → 50 mW/(mm·K)
- Aluminum: 167 W/(m·K) → 167 mW/(mm·K)

**Specific Heat:**
- Steel: 500 J/(kg·K) → 500 × 1e9 = 5.0e11 mJ/(tonne·K)
- Aluminum: 900 J/(kg·K) → 900 × 1e9 = 9.0e11 mJ/(tonne·K)

**Density:**
- Steel: 7850 kg/m³ → 7.85e-9 tonne/mm³
- Aluminum: 2700 kg/m³ → 2.70e-9 tonne/mm³

**Film Coefficient:**
- Natural convection: 10 W/(m²·K) → 0.01 mW/(mm²·K)
- Forced convection: 100 W/(m²·K) → 0.1 mW/(mm²·K)

## Common Thermal Conductivities

| Material | k (W/(m·K)) | k (mW/(mm·K)) |
|----------|-------------|---------------|
| Copper | 385-400 | 385-400 |
| Aluminum | 167-237 | 167-237 |
| Steel (mild) | 50-60 | 50-60 |
| Stainless steel | 15-25 | 15-25 |
| Titanium | 20 | 20 |
| Glass | 0.8-1.0 | 0.8-1.0 |
| Plastic (ABS) | 0.2 | 0.2 |
| Air | 0.025 | 0.025 |
| Water | 0.6 | 0.6 |

## Typical Film Coefficients

| Condition | h (W/(m²·K)) | h (mW/(mm²·K)) |
|-----------|--------------|----------------|
| Still air (natural) | 5-25 | 0.005-0.025 |
| Moving air (forced) | 25-250 | 0.025-0.25 |
| Still water | 100-900 | 0.1-0.9 |
| Flowing water | 1000-15000 | 1.0-15.0 |
| Boiling water | 2500-25000 | 2.5-25.0 |
| Condensing steam | 5000-100000 | 5.0-100.0 |

## Emissivity Values for Radiation

| Surface | Emissivity |
|---------|------------|
| Polished metals | 0.02-0.1 |
| Oxidized metals | 0.2-0.8 |
| Black paint | 0.95-0.98 |
| White paint | 0.85-0.95 |
| Concrete | 0.85-0.95 |
| Brick | 0.90-0.95 |
| Glass | 0.85-0.95 |

## Transient Analysis Tips

### Choosing Time Increments

For transient analysis, the time increment should be small enough to capture the thermal response:

```
Characteristic time = (density × specific_heat × L²) / conductivity
```

where L is the characteristic length (typically the smallest dimension or mesh size).

**Rule of thumb:**
- Initial increment: 1-10% of characteristic time
- Maximum increment: 10-50% of characteristic time
- Use `deltmx` to limit temperature change per increment (typically 5-20°C)

### Example Calculation (Steel, L=10mm)
```
t_char = (7.85e-9 × 5.0e11 × 10²) / 50 = 7.85 seconds
Initial inc: 0.1-0.8 s
Max inc: 0.8-4 s
```

## Debugging Checklist

1. **Model Setup**
   - [ ] Correct element type (DC3D8, not C3D8R)
   - [ ] Material conductivity defined
   - [ ] For transient: specific heat and density defined
   - [ ] Section assigned to all cells

2. **Boundary Conditions**
   - [ ] At least one thermal BC applied
   - [ ] BCs applied to correct step (not 'Initial' for loads)
   - [ ] Regions correctly selected (faces for surface BCs)

3. **Analysis**
   - [ ] Correct step type (STEADY_STATE vs TRANSIENT)
   - [ ] For transient: initial temperature defined
   - [ ] Time period appropriate for problem
   - [ ] Output variables include NT (temperature)

4. **Units**
   - [ ] All properties in consistent unit system
   - [ ] Temperature in °C or K (consistent)
   - [ ] Conductivity, specific heat, density all consistent

## Output Variable Reference

| Variable | Description | Notes |
|----------|-------------|-------|
| NT | Nodal temperature | Primary thermal output |
| NT11 | Temperature component | Same as NT for single temp |
| HFL | Heat flux vector | [HFL1, HFL2, HFL3] |
| HFLM | Heat flux magnitude | Scalar |
| RFL | Reaction heat flux | At constrained nodes |
| TEMP | Temperature (elements) | Use NT instead |
