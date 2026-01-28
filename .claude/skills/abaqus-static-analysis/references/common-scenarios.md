# Common Static Analysis Scenarios

## Cantilever Beam

### Description
- Fixed at one end
- Load at other end (point load or distributed)
- Classic bending problem

### Expected Results
- Max stress at fixed end (tension on outer fiber)
- Max displacement at load point
- Linear stress variation through thickness

### Analytical Check
```
Stress: σ = M*c/I = (F*L)*(h/2) / (b*h³/12) = 6*F*L / (b*h²)
Deflection: δ = F*L³ / (3*E*I) = 4*F*L³ / (E*b*h³)
```

### Model Tips
- Use Encastre BC at fixed end
- ConcentratedForce or SurfaceTraction at tip
- Refine mesh near fixed end

---

## Simply Supported Beam

### Description
- Pinned at both ends
- Load in middle (point or distributed)
- Both rotation and axial movement allowed at supports

### Expected Results
- Max stress at midspan (bottom fiber in tension)
- Max displacement at midspan
- Zero stress at supports

### Analytical Check
```
Stress: σ = M*c/I (M = F*L/4 at center for point load)
Deflection: δ = F*L³ / (48*E*I) for point load at center
```

### Model Tips
- One end: Fix U2, U3 (vertical + out-of-plane)
- Other end: Fix U1, U2, U3 (also horizontal to prevent rigid body)
- Or use symmetry: half model with symmetry BC

---

## Plate with Hole

### Description
- Flat plate with circular hole
- Uniaxial tension
- Classic stress concentration example

### Expected Results
- Stress concentration at hole edge
- SCF ≈ 3.0 for infinite plate
- Peak stress perpendicular to load direction

### Analytical Check
```
SCF = σ_max / σ_nominal ≈ 3.0 (for small hole)
σ_nominal = F / (W * t) where W = plate width, t = thickness
```

### Model Tips
- Use symmetry (1/4 model if symmetric)
- Fine mesh around hole edge
- At least 8-10 elements around hole circumference
- Mesh transition from fine (hole) to coarse (far field)

---

## Bracket Under Load

### Description
- L-shaped or gusseted bracket
- Fixed at mounting holes
- Load at hook or attachment point

### Expected Results
- High stress at fillets (stress concentration)
- Stress at bolt holes
- Deformation pattern shows load path

### Model Tips
- Partition geometry at fillet regions
- Refine mesh at fillets and holes
- Use coupling constraints for bolt loads
- Check both mounting and loading locations

---

## Pressure Vessel

### Description
- Cylindrical or spherical shell
- Internal or external pressure
- Hoop and axial stresses

### Expected Results
- Hoop stress: σ_h = p*r/t (cylinder)
- Axial stress: σ_a = p*r/(2t) (cylinder)
- Radial stress ≈ -p at inner surface

### Model Tips
- Can use axisymmetric elements (CAX4R)
- Or 3D with symmetry
- Apply pressure to inner surface
- Constrain one end axially to prevent rigid body motion

---

## Shaft Under Torsion

### Description
- Circular shaft
- Torque applied at one end
- Fixed at other end

### Expected Results
- Max shear stress at outer surface
- τ = T*r/J
- Twist angle θ = T*L/(G*J)

### Model Tips
- Fix one end completely
- Apply torque via coupling or distributed shear
- Use fine mesh to capture shear stress gradient
- Check S12 or S13 (shear components) not just MISES

---

## Assembly with Contact

### Note
For contact between multiple parts, use `/abaqus-contact-analysis` instead.

This skill handles single-part static analysis. If parts touch:
1. Use tie constraints for bonded contact (simple)
2. Use `/abaqus-contact-analysis` for sliding/separation

---

## Thermal Stress

### Note
For thermal stress analysis, use `/abaqus-thermal-analysis` or `/abaqus-coupled-analysis`.

If only applying a uniform temperature change:
```python
# Can add thermal expansion in static analysis
material.Expansion(table=((alpha,),))  # CTE
model.Temperature(name='Temp', createStepName='Load',
                  distributionType=UNIFORM, magnitude=dT)
```
