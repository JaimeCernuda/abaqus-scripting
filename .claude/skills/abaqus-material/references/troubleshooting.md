# Material Troubleshooting

Common errors when defining materials in Abaqus and their solutions.

## Quick Reference Table

| Error | Cause | Solution |
|-------|-------|----------|
| "Material has no density" | Density required for dynamics/gravity | Add `material.Density(table=((value,),))` |
| "Negative eigenvalue in stiffness" | Invalid Poisson's ratio | Ensure -1 < nu < 0.5 |
| "Section not assigned" | Missing SectionAssignment | Call `part.SectionAssignment(...)` |
| "Material X not found" | Typo in name | Check spelling matches exactly |
| "Region has no mesh" | Meshed before assignment | Mesh after section assignment |
| "Zero pivot" | E = 0 or missing properties | Verify E > 0 |
| "Plastic strain not zero" | First plastic point wrong | Start plastic table at strain = 0 |

## Detailed Solutions

### Error: "Material has no density"

**When it occurs:** Running modal analysis, explicit dynamics, or applying gravity loads.

**Cause:** Density is required whenever inertia effects matter.

**Fix:**
```python
material.Density(table=((7.85e-9,),))  # Steel density in tonne/mm³
```

**Analysis types requiring density:**
- Modal/frequency analysis
- Dynamic explicit/implicit
- Gravity loads (GRAV)
- Inertia relief

---

### Error: "Negative eigenvalue in material stiffness matrix"

**When it occurs:** During element stiffness calculation.

**Cause:** Invalid Poisson's ratio (nu >= 0.5 or nu <= -1).

**Fix:** Ensure Poisson's ratio is in valid range:
```python
# WRONG - causes instability
material.Elastic(table=((210000.0, 0.5),))  # nu = 0.5 is incompressible

# CORRECT
material.Elastic(table=((210000.0, 0.3),))  # nu = 0.3
```

**Note:** For nearly incompressible materials (rubber), use nu ~ 0.49, not 0.5.

---

### Error: "Section not assigned to region"

**When it occurs:** Submitting job or generating input file.

**Cause:** Part cells have no section assignment.

**Fix:**
```python
# Step 1: Create section
model.HomogeneousSolidSection(name='Section', material='Steel')

# Step 2: Create set from cells
region = part.Set(cells=part.cells, name='AllCells')

# Step 3: Assign section
part.SectionAssignment(region=region, sectionName='Section')
```

---

### Error: "Material 'X' not found"

**When it occurs:** Creating section or during job submission.

**Cause:** Material name in section doesn't match created material name (case-sensitive).

**Fix:** Ensure exact name match:
```python
# Create material with specific name
material = model.Material(name='Steel_A36')

# Reference with EXACT same name
model.HomogeneousSolidSection(name='Section', material='Steel_A36')  # Correct
# model.HomogeneousSolidSection(name='Section', material='steel_a36')  # WRONG
```

---

### Error: "Plastic strain at first data point is not zero"

**When it occurs:** Defining plastic material properties.

**Cause:** First point in plastic table must have zero plastic strain.

**Fix:**
```python
# WRONG - first plastic strain not zero
material.Plastic(table=(
    (250.0, 0.001),  # Starting at non-zero strain
    (400.0, 0.200),
))

# CORRECT - first point at zero plastic strain
material.Plastic(table=(
    (250.0, 0.0),    # Yield point (plastic strain = 0)
    (400.0, 0.200),  # Hardening
))
```

---

### Error: "Zero pivot in element stiffness"

**When it occurs:** Solving equilibrium equations.

**Cause:** Young's modulus is zero or material has insufficient properties.

**Fix:**
```python
# Ensure E > 0
material.Elastic(table=((210000.0, 0.3),))  # E = 210 GPa
```

---

### Error: "Region has no mesh"

**When it occurs:** Assigning section to element-based region.

**Cause:** Trying to use element sets before meshing.

**Fix:** For part-level assignment, use geometry (cells), not elements:
```python
# Use cells (geometry) - works before meshing
region = part.Set(cells=part.cells, name='AllCells')
part.SectionAssignment(region=region, sectionName='Section')

# Then mesh
part.generateMesh()
```

---

### Error: "Incompatible element type for section"

**When it occurs:** Assigning shell section to 3D solid mesh.

**Cause:** Section type doesn't match element type.

**Fix:** Match section to geometry/element type:

| Geometry | Element Type | Section Type |
|----------|--------------|--------------|
| 3D solid | C3D8R, C3D10 | HomogeneousSolidSection |
| Shell/surface | S4R, S3 | HomogeneousShellSection |
| Wire/beam | B31, B32 | BeamSection |

---

## Best Practices

1. **Always define density** - Even for static analysis, it's good practice for future reuse.

2. **Use consistent units** - Stick to mm-tonne-s-N-MPa system.

3. **Validate material values:**
   ```python
   # Quick validation
   assert E > 0, "Young's modulus must be positive"
   assert -1 < nu < 0.5, "Poisson's ratio out of bounds"
   assert rho > 0, "Density must be positive"
   ```

4. **Name materials descriptively:**
   ```python
   # Good
   model.Material(name='Steel_A36_Elastic')
   model.Material(name='Al6061T6_WithPlasticity')

   # Avoid
   model.Material(name='Material-1')
   ```

5. **Assign sections immediately after creation** - Don't wait until the end of the script.
