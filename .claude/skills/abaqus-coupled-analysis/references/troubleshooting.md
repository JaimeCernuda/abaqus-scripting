# Coupled Analysis Troubleshooting

## Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "No thermal expansion" | Missing Expansion property | Add `material.Expansion()` |
| "Zero thermal stress" | No temperature change | Check temperature field/BC |
| "Cannot import ODB" | Path or step name wrong | Verify ODB exists and step name |
| "Mesh mismatch" | Different meshes for import | Use same mesh or enable interpolation |
| "Large thermal strain" | Wrong alpha units | alpha should be ~1e-5/K for metals |
| "Non-convergence" | Large temperature change | Reduce increments or deltmx |
| "Wrong element type" | Using C3D8 not C3D8T | Use coupled elements for fully coupled |
| "Temperature not varying" | Missing conductivity | Add `material.Conductivity()` |
| "No heat transfer" | Using structural elements | Use C3D*T or DC3D* elements |

## Thermal Stress Equation

The fundamental relationship for thermal stress:

```
sigma_thermal = E * alpha * delta_T
```

Where:
- E = Young's modulus (MPa)
- alpha = Coefficient of thermal expansion (1/K)
- delta_T = Temperature change from reference (K or C)

**Requirements for thermal stress:**
1. Elastic modulus (E) - from `material.Elastic()`
2. Expansion coefficient (alpha) - from `material.Expansion()`
3. Temperature change (delta_T) - from BCs or predefined fields
4. Constraint preventing free expansion

**No constraint = no stress** (free thermal expansion)

## Coupling Type Selection Guide

| Analysis Type | When to Use | Element Type |
|---------------|-------------|--------------|
| Fully coupled | Heat generation from plastic work, friction | C3D8T |
| Sequential (thermal->structural) | One-way thermal influence | DC3D8 then C3D8R |
| Steady-state | Temperature distribution is stable | C3D8T |
| Transient | Temperature changes with time | C3D8T |

### Decision Tree

```
Does deformation generate significant heat?
  YES -> Fully Coupled (CoupledTempDisplacementStep)
  NO  -> Is thermal analysis complex?
           YES -> Sequential (HeatTransferStep + import)
           NO  -> Fully Coupled (simpler setup)
```

## Zero Thermal Stress Issues

### Problem: No stress despite temperature change

**Checklist:**
1. Is `material.Expansion()` defined?
2. Is `zero=T_REF` correct in Expansion definition?
3. Is initial temperature equal to T_REF?
4. Is there a constraint preventing free expansion?
5. Is temperature actually different from T_REF?

**Debug code:**
```python
# Print material properties
print("Expansion defined:", hasattr(material, 'expansion'))

# Check temperature field
odb = openOdb('result.odb')
frame = odb.steps['Heating'].frames[-1]
temps = frame.fieldOutputs['NT']
print("Min temp:", min([v.data for v in temps.values]))
print("Max temp:", max([v.data for v in temps.values]))
```

## ODB Import Failures

### Problem: "Cannot read from ODB file"

**Common causes:**
1. ODB file doesn't exist (job didn't complete)
2. Wrong path (use absolute paths)
3. ODB is open in another process
4. Step name doesn't match

**Verification:**
```python
import os
from odbAccess import openOdb

# Check file exists
odb_path = 'thermal.odb'
if not os.path.exists(odb_path):
    print("ODB not found:", odb_path)
else:
    odb = openOdb(odb_path)
    print("Steps:", odb.steps.keys())
    for step_name, step in odb.steps.items():
        print(f"  {step_name}: {len(step.frames)} frames")
    odb.close()
```

### Problem: Mesh mismatch between thermal and structural

**Solutions:**
1. Use identical mesh for both analyses
2. Enable interpolation (may lose accuracy at boundaries)
3. Use same part geometry and mesh parameters

## Convergence Issues

### Problem: Analysis fails to converge

**Temperature increment too large:**
```python
# Reduce deltmx (max temp change per increment)
model.CoupledTempDisplacementStep(
    name='Heating',
    previous='Initial',
    deltmx=5.0,      # Reduce from default
    initialInc=0.01, # Smaller initial increment
    minInc=1e-8,
    maxInc=0.1       # Limit max increment
)
```

**Material nonlinearity:**
```python
# Enable geometric nonlinearity
model.CoupledTempDisplacementStep(
    name='Heating',
    previous='Initial',
    nlgeom=ON
)
```

### Problem: Negative eigenvalue warning

Usually indicates:
- Unconstrained rigid body motion
- Insufficient boundary conditions
- Material instability

**Solution:** Check mechanical boundary conditions prevent all 6 DOFs.

## Unit Consistency

### Problem: Unrealistic results (stress in GPa or microns)

**SI-mm system reference:**

| Property | Units | Steel Value |
|----------|-------|-------------|
| Length | mm | - |
| Force | N | - |
| Stress | MPa (N/mm^2) | - |
| E | MPa | 210000 |
| Density | tonne/mm^3 | 7.85e-9 |
| Conductivity | mW/(mm*K) | 50 |
| Specific heat | mJ/(tonne*K) | 5.0e11 |
| Expansion | 1/K | 12e-6 |
| Temperature | K or C | - |

**Note:** Thermal expansion coefficient alpha is the same in 1/K and 1/C since delta_T is the same.

## Element Type Issues

### Problem: "Element type not available"

**For fully coupled analysis:**
- Use elements with temperature DOF: C3D8T, C3D8RT, C3D10MT
- NOT: C3D8, C3D8R, C3D10 (structural only)

**For thermal-only analysis:**
- Use heat transfer elements: DC3D8, DC3D10, DC3D20
- NOT: C3D8T (includes displacement DOF)

### Problem: Mixed element types in assembly

```python
# Different element types for different regions
part1.setElementType(
    regions=(part1.cells,),
    elemTypes=(mesh.ElemType(elemCode=C3D8T),)
)
part2.setElementType(
    regions=(part2.cells,),
    elemTypes=(mesh.ElemType(elemCode=C3D8T),)
)
```

## Output Not Available

### Problem: THE (thermal strain) not in results

**Cause:** Not requested or wrong element type

**Solution:**
```python
model.FieldOutputRequest(
    name='ThermalOutput',
    createStepName='Heating',
    variables=('S', 'U', 'NT', 'THE', 'E', 'EE')
)
```

### Problem: Temperature shows as 0 everywhere

**Causes:**
1. No thermal boundary conditions applied
2. Initial temperature not set
3. Wrong output variable (use NT, not TEMP)

## Performance Issues

### Problem: Analysis runs very slowly

**Optimizations:**
1. Use reduced integration elements (C3D8RT instead of C3D8T)
2. Increase deltmx if convergence allows
3. Use coarser mesh where thermal gradients are small
4. Consider sequential coupling if feedback is weak

### Problem: Excessive output file size

```python
# Reduce output frequency
model.FieldOutputRequest(
    name='Output',
    createStepName='Heating',
    variables=('S', 'U', 'NT'),
    frequency=10  # Every 10th increment
)

# Output only at specific times
model.FieldOutputRequest(
    name='Output',
    createStepName='Heating',
    variables=('S', 'U', 'NT'),
    timeInterval=0.5  # Every 0.5 time units
)
```
