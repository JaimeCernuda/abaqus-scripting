# Modal Analysis Troubleshooting

## Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "Zero frequency modes" | Rigid body motion | Add BCs or expect 6 RBMs for free-free |
| "No modes found" | Frequency range too narrow | Widen minEigen/maxEigen range |
| "Negative eigenvalue" | Instability or bad geometry | Check material props, geometry, BCs |
| "Missing mass" | No density defined | Add `material.Density(table=...)` |
| "Memory error" | Too many modes/elements | Reduce numEigen or coarsen mesh |
| "Solver failure" | Singular stiffness matrix | Check for unconnected parts, bad elements |

## Detailed Troubleshooting

### Zero Frequency Modes

**Symptom:** First several modes have frequency = 0 Hz (or very small, ~1e-10 Hz)

**Cause:** Rigid body motion is not constrained.

**Solutions:**
1. **Expected for free-free:** First 6 modes are rigid body modes (3 translation + 3 rotation)
2. **Unexpected zeros:** Add boundary conditions to constrain rigid body motion
3. **Soft spring workaround:** Add very soft springs to ground (affects low modes slightly)

```python
# Check if zeros are expected
if num_zero_modes == 6:
    print("Free-free analysis: 6 RBMs expected")
elif num_zero_modes > 0:
    print("WARNING: Unexpected rigid body modes - check BCs")
```

### No Density Error

**Symptom:** "The material 'MaterialName' has no mass defined"

**Cause:** Density property not assigned to material.

**Solution:**
```python
material = model.Material(name='Steel')
material.Elastic(table=((210000.0, 0.3),))
material.Density(table=((7.85e-9,),))  # REQUIRED for modal!
```

### Negative Eigenvalues

**Symptom:** "Negative eigenvalue encountered"

**Causes:**
- Buckling/instability (structure under compression)
- Incorrect material properties (negative stiffness)
- Bad element geometry (distorted elements)

**Solutions:**
1. Check for compressive preload causing buckling
2. Verify material properties are positive
3. Check mesh quality (element warnings)
4. For prestressed analysis, reduce preload

### Frequencies Too High or Low

**Symptom:** Computed frequencies don't match expectations.

**Cause:** Usually unit inconsistency.

**Verification:**
```python
# Unit check for mm-tonne-s system
# Frequency f = (1/2pi) * sqrt(k/m)
# k in N/mm, m in tonne

# Steel cantilever first mode
# f1 = 0.56 * sqrt(E*I / (rho*A*L^4))

import math
L = 200.0  # mm
b = 20.0   # mm
h = 5.0    # mm
E = 210000.0  # MPa = N/mm^2
rho = 7.85e-9  # tonne/mm^3

I = b * h**3 / 12
A = b * h
beta1 = 1.875

f1 = (beta1**2 / (2 * math.pi * L**2)) * math.sqrt(E * I / (rho * A))
print(f"Expected f1: {f1:.2f} Hz")
```

## Frequency Validation Formulas

### Cantilever Beam
```
f_n = (beta_n^2 / (2*pi*L^2)) * sqrt(E*I / (rho*A))

beta_1 = 1.875
beta_2 = 4.694
beta_3 = 7.855
```

### Simply Supported Beam
```
f_n = (n*pi)^2 / (2*pi*L^2) * sqrt(E*I / (rho*A))

f_1 = pi^2 / (2*L^2) * sqrt(E*I / (rho*A))
```

### Fixed-Fixed Beam
```
f_1 = 3.56 * sqrt(E*I / (rho*A*L^4))
```

### Circular Plate (Fixed Edge)
```
f_1 = 10.21 / (2*pi*R^2) * sqrt(D / (rho*h))

where D = E*h^3 / (12*(1-nu^2))
```

## Mass Participation Check

**Good modal basis:** Total mass participation > 90% in each direction.

```python
# Check mass participation in .msg or .dat file
# Look for "PARTICIPATION FACTORS" table

# If participation is low:
# 1. Extract more modes
# 2. Check if modes are localized
# 3. Verify boundary conditions
```

### Reading Mass Participation

```python
# Mass participation from .dat file
import re

with open('Modal.dat', 'r') as f:
    content = f.read()

# Look for participation factor table
# Format varies by Abaqus version
```

## Mesh Quality Effects

| Issue | Effect on Modes | Solution |
|-------|-----------------|----------|
| Coarse mesh | Overly stiff, high frequencies | Refine mesh |
| Distorted elements | Inaccurate mode shapes | Improve mesh quality |
| Linear elements | Shear locking (beams/plates) | Use quadratic or reduced integration |
| Too fine mesh | Excessive computation | Balance accuracy vs cost |

### Mesh Convergence Study

```python
# Run modal analysis with increasing mesh density
# Plot frequency vs mesh size
# Converged when frequency change < 1-2%

mesh_sizes = [20, 10, 5, 2.5]
frequencies = []

for size in mesh_sizes:
    # Run analysis with mesh size
    # Record first N frequencies
    pass

# Check convergence
for i in range(1, len(frequencies)):
    change = abs(frequencies[i] - frequencies[i-1]) / frequencies[i-1] * 100
    print(f"Mesh {mesh_sizes[i]}mm: {change:.2f}% change")
```

## Performance Tips

1. **Start coarse:** Begin with coarse mesh to verify setup
2. **Use LANCZOS:** Default solver is efficient for most problems
3. **Limit modes:** Only request modes you need
4. **Use frequency range:** More efficient than requesting many modes
5. **Symmetry:** Use symmetry BCs to reduce model size
6. **Shell vs solid:** Use shells for thin structures (much faster)

## Debugging Workflow

1. **Check input:**
   - Material has density?
   - BCs appropriate for intended analysis?
   - Mesh quality acceptable?

2. **Run with few modes first:**
   ```python
   model.FrequencyStep(name='Test', previous='Initial', numEigen=3)
   ```

3. **Check .msg file for warnings:**
   ```bash
   findstr /i "warning error" Modal.msg
   ```

4. **Verify against analytical:**
   - Use simple geometry first
   - Compare to handbook formulas

5. **Visualize mode shapes:**
   - Do shapes look physical?
   - Any unexpected localized modes?
