# Fatigue Analysis Troubleshooting

## Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Life too short | Stress concentration | Refine mesh at notch, use Kt/Kf correction |
| Life too long | Missing mean stress | Apply Goodman/Gerber correction |
| Inconsistent results | Mesh dependence | Check mesh convergence at critical location |
| No fatigue data | Missing material curve | Obtain S-N data for material |
| Negative R-ratio | Compression cycles | Use appropriate S-N curve for R < 0 |
| Infinite life prediction | Below endurance limit | Check if material has endurance limit |
| Wrong units | MPa vs Pa mismatch | Verify stress units match S-N data |
| Unrealistic damage | Stress singularity | Avoid sharp corners, use submodeling |

## Material Data Requirements

### High-Cycle Fatigue (Stress-Life)

- **S-N curve**: Stress amplitude vs. cycles to failure
- **Fatigue strength coefficient (Sf')**: Typically 1.5-2x ultimate strength
- **Fatigue strength exponent (b)**: Typically -0.05 to -0.12
- **Endurance limit (Se)**: ~0.5*Su for steel, none for aluminum
- **Mean stress sensitivity**: Goodman/Gerber parameters

### Low-Cycle Fatigue (Strain-Life)

- **Fatigue strength coefficient (Sf')**: MPa
- **Fatigue strength exponent (b)**: Typically -0.05 to -0.12
- **Fatigue ductility coefficient (ef')**: Dimensionless
- **Fatigue ductility exponent (c)**: Typically -0.5 to -0.7
- **Cyclic stress-strain curve**: K' and n'

### Typical Values for Common Materials

| Material | Sf' (MPa) | b | ef' | c | Se/Su |
|----------|-----------|------|------|------|-------|
| Steel (mild) | 800-1200 | -0.08 | 0.2-0.5 | -0.5 | 0.5 |
| Steel (high strength) | 1500-2500 | -0.07 | 0.1-0.3 | -0.6 | 0.4 |
| Aluminum | 400-800 | -0.1 | 0.1-0.3 | -0.7 | None |
| Titanium | 900-1500 | -0.06 | 0.2-0.4 | -0.5 | 0.5 |

## Stress Extraction Tips

### Use MISES for Ductile Materials
```python
# Von Mises (equivalent) stress for ductile metals
for v in stress.values:
    if hasattr(v, 'mises'):
        S_eq = v.mises
```

### Use Max Principal for Brittle Materials
```python
# Maximum principal stress for brittle/cast materials
for v in stress.values:
    if hasattr(v, 'maxPrincipal'):
        S_max_principal = v.maxPrincipal
```

### Extract at Surface (Highest Stress)
```python
# Surface nodes typically have highest stress
# Create node set on critical surface
region = odb.rootAssembly.surfaces['CRITICAL_SURFACE']
stress_subset = stress.getSubset(region=region)
```

### Include Stress Concentration Factor (Kt)
```python
# Get Kt from FEA
nominal_stress = applied_load / cross_section_area
peak_stress = max_mises_from_fea

Kt = peak_stress / nominal_stress

# Convert to fatigue notch factor
q = 0.9  # Notch sensitivity (material dependent)
Kf = 1 + q * (Kt - 1)

# Use in fatigue calculation
effective_stress = nominal_stress * Kf
```

## Convergence Checks

### Mesh Sensitivity
```python
# Run analysis with different mesh sizes
mesh_sizes = [5.0, 2.5, 1.0, 0.5]  # mm
max_stresses = []

for size in mesh_sizes:
    # ... run analysis with mesh size
    max_stresses.append(result)

# Check convergence (< 5% change)
for i in range(1, len(max_stresses)):
    change = abs(max_stresses[i] - max_stresses[i-1]) / max_stresses[i-1]
    print(f"Mesh {mesh_sizes[i]}: {change*100:.1f}% change")
```

### Singularity Detection
```python
# Check if stress increases with mesh refinement (singularity)
if max_stresses[-1] > max_stresses[0] * 1.5:
    print("Warning: Possible stress singularity")
    print("Consider using Kt/Kf approach instead")
```

## Debug Checklist

1. **Units consistency**
   - [ ] Stress in same units as S-N curve (usually MPa)
   - [ ] Force in N if stress in MPa
   - [ ] Length in mm if force in N and stress in MPa

2. **Loading definition**
   - [ ] Correct R-ratio (min/max stress ratio)
   - [ ] Mean stress accounted for
   - [ ] Load sequence captured (if variable amplitude)

3. **Material data**
   - [ ] S-N curve appropriate for R-ratio
   - [ ] Endurance limit considered
   - [ ] Temperature effects included (if elevated temp)

4. **Stress extraction**
   - [ ] Correct stress component (Mises vs principal)
   - [ ] Surface stress (not internal)
   - [ ] Mesh converged at critical location

5. **Fatigue method**
   - [ ] Appropriate for cycle count (HCF vs LCF)
   - [ ] Mean stress correction applied
   - [ ] Notch effects considered

## When Results Don't Match Expectations

### Life Too Short
1. Check for stress singularities at sharp corners
2. Verify mesh is converged (not artificially high stress)
3. Check if mean stress correction is too conservative
4. Verify S-N data is for correct material condition

### Life Too Long
1. Check if mean stress effects are included
2. Verify stress extraction location is at surface
3. Check if notch effects (Kf) are included
4. Verify loading definition captures worst case

### Variable Results Between Analyses
1. Check mesh consistency
2. Verify element types are same
3. Check boundary condition application
4. Verify solver precision settings
