# Static Analysis Troubleshooting

## Quick Reference Table

| Symptom | Cause | Solution |
|---------|-------|----------|
| "Zero pivot" | Rigid body motion | Add more BCs to constrain all 6 DOFs |
| Unrealistic displacement | Wrong E or units | Check material (E in MPa, not Pa) |
| Stress too high | Local singularity | Refine mesh or check geometry |
| Reactions ≠ loads | Model error | Check BC and load regions |
| "Negative eigenvalue" | Buckling/instability | Check BCs, may need stabilization |
| "Too many increments" | Severe nonlinearity | Reduce load, smaller increments |
| "Memory exceeded" | Mesh too fine | Increase element size |
| Node count exceeded | Learning Edition limit | Increase MESH_SIZE |

---

## Detailed Troubleshooting

### Zero Pivot / Singular Matrix

**Symptoms:**
- Error: "Zero pivot" or "Singular matrix"
- Analysis fails immediately
- Huge/infinite displacements if it runs

**Causes:**
1. Rigid body motion not constrained
2. Disconnected parts
3. Fully constrained in wrong directions

**Solutions:**
1. Check boundary conditions constrain all 6 DOFs:
   - 3 translations (U1, U2, U3)
   - 3 rotations (UR1, UR2, UR3)
2. For single part, one Encastre usually sufficient
3. If multiple parts, ensure connectivity
4. Add temporary soft springs to find the problem

**Diagnostic:**
```python
# Check if all DOFs constrained
# In CAE: Tools → Query → General → Mass properties
# Should show center of mass, not error
```

---

### Unrealistic Displacements

**Symptoms:**
- Displacement much larger/smaller than expected
- Part moves through itself
- Results don't match hand calculations

**Causes:**
1. Wrong material properties (E in wrong units)
2. Wrong load magnitude
3. Wrong geometry dimensions
4. Missing or extra decimal places

**Solutions:**
1. Verify units: E in MPa (210000 for steel, not 2.1e11)
2. Check load: Force in N, pressure in MPa
3. Verify geometry dimensions match intent
4. Compare to analytical solution

**Quick Check:**
```
δ ≈ F*L/(A*E) for axial
δ ≈ F*L³/(3*E*I) for cantilever bending
```

---

### Stress Singularities

**Symptoms:**
- Stress increases without bound with mesh refinement
- Very high stress at sharp corners
- Max stress at BC application point

**Causes:**
1. Sharp corners (90° edges without fillet)
2. Point loads on solid elements
3. Point BCs on solid elements
4. Stress extraction at singularity

**Solutions:**
1. Add fillets to sharp corners (real parts have them)
2. Use surface traction instead of concentrated force
3. Apply BCs to surfaces/edges, not points
4. Ignore stress at singularity, check nearby region
5. Use St. Venant's principle: stress correct far from BC

**Note:** Some singularities are acceptable if:
- You're checking stress away from the singularity
- The singularity is at a BC (not in the structure)
- Mesh convergence achieved in region of interest

---

### Convergence Issues (Nonlinear)

**Symptoms:**
- "Equilibrium not achieved"
- "Too many increments"
- Analysis stalls at certain load level

**Causes:**
1. Load too large for material/geometry
2. Buckling or instability
3. Material softening (plasticity)
4. Contact opening/closing

**Solutions:**
1. Reduce initial increment size:
   ```python
   model.StaticStep(name='Load', previous='Initial',
                    initialInc=0.01, maxNumInc=1000, minInc=1e-10)
   ```
2. Enable automatic stabilization:
   ```python
   model.StaticStep(..., stabilizationMethod=DAMPING_FACTOR,
                    continueDampingFactors=False,
                    adaptiveDampingRatio=0.05)
   ```
3. Check for buckling with eigenvalue analysis first
4. Use arc-length method (Riks) for post-buckling

---

### Memory / Performance Issues

**Symptoms:**
- "Memory allocation failed"
- Analysis runs extremely slowly
- Computer becomes unresponsive

**Causes:**
1. Mesh too fine
2. Too many output requests
3. Insufficient RAM
4. Learning Edition node limit

**Solutions:**
1. Increase mesh size (start coarse, refine only where needed)
2. Reduce output frequency:
   ```python
   model.FieldOutputRequest(name='F-Output', createStepName='Load',
                            variables=('S', 'U'), frequency=10)
   ```
3. Use submodeling for local refinement
4. Check node count: `print(len(part.nodes))`

---

### Results Don't Match Expectations

**Symptoms:**
- Stress pattern looks wrong
- Displacement direction unexpected
- Reactions don't sum to applied load

**Causes:**
1. Load applied in wrong direction
2. BC applied to wrong region
3. Material assigned to wrong cells
4. Coordinate system confusion

**Solutions:**
1. Visualize loads and BCs in CAE before running
2. Check `findAt()` coordinates match intended location
3. Verify section assignment covers all cells
4. Print debug info:
   ```python
   print("Load face center:", load_face.pointOn)
   print("BC face center:", fixed_face.pointOn)
   ```

---

## Convergence Tips

### Linear Analysis
- Should converge in one increment
- If it doesn't, check for rigid body motion
- No need for `nlgeom=ON` or increment controls

### Mildly Nonlinear
```python
model.StaticStep(
    name='Load',
    previous='Initial',
    nlgeom=ON,
    initialInc=0.1,
    maxNumInc=100
)
```

### Highly Nonlinear
```python
model.StaticStep(
    name='Load',
    previous='Initial',
    nlgeom=ON,
    initialInc=0.01,
    maxNumInc=1000,
    minInc=1e-10,
    maxInc=0.05
)
```

### With Contact or Buckling
```python
model.StaticStep(
    name='Load',
    previous='Initial',
    nlgeom=ON,
    initialInc=0.01,
    maxNumInc=1000,
    minInc=1e-15,
    stabilizationMethod=DAMPING_FACTOR,
    adaptiveDampingRatio=0.05
)
```

---

## Debugging Checklist

When analysis fails:

1. [ ] Check .dat file for error messages
2. [ ] Check .msg file for iteration history
3. [ ] Verify geometry in CAE (Visual check)
4. [ ] Verify BCs applied to correct regions
5. [ ] Verify loads applied to correct regions
6. [ ] Check material properties and units
7. [ ] Try coarser mesh first
8. [ ] Try linear analysis first (nlgeom=OFF)
9. [ ] Apply load in steps (ramp up)
10. [ ] Compare to simple analytical case
