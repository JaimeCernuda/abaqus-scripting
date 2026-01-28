# Experiment 4 - Loop 2 Results Summary

## Date: January 27, 2026

## VERIFIED STATUS: Geometry and Analysis COMPLETE

Multiple programmatic verifications confirm correct geometry:
- Hole direction: All 3 holes go through X-direction (18mm span)
- Upper hole location: Y=132.2 (in upper block, Y>118)
- Lower hole locations: Y=14.0 (in lower blocks, Y<28)

## Key Accomplishment: Corrected Pin Hole Orientation

### Critical Fix Applied
- **Issue**: Pin holes were oriented through Z-axis (wrong for testing machine)
- **Solution**: Recreated geometry with X-direction pin holes (horizontal through thickness)
- **Verification**: All 3 pin holes visible going through X-axis for proper specimen mounting

### Geometry Correction Details
The 3442-003M-020-ST Extensometer testing machine requires:
- Pins inserted horizontally (X direction)
- Two parallel pins at bottom, one at top
- Previous Z-direction holes were physically impossible for actual testing

Fixed by using inner faces with -X normal and proper sketchUpEdge selection:
```python
# Upper hole - Use inner face at X=-9 with norm=(-1,0,0)
upper_face = part.faces.findAt(((-9.0, 127.5, 16.7),))
# flipExtrudeDirection=OFF (cut in +X direction)
```

## Analysis Results with Correct Geometry

### Material: IN718 (Inconel 718)
- E = 200,000 MPa
- v = 0.30
- Yield strength = 980 MPa (proportional limit)
- Density = 8.19e-9 tonne/mm³

### Load Cases Analyzed

| Job | Load | Max Stress | Max Disp | PEEQ | Status |
|-----|------|------------|----------|------|--------|
| Job_v19 | 20 kN | 380.72 MPa | 0.0641 mm | 0 | **ELASTIC** |
| Job_v19_60kN | 60 kN | 982.39 MPa | 0.1908 mm | 0.001 | **YIELD ONSET** |
| Job_100kN | 100 kN | 1148.03 MPa | 0.9370 mm | 0.067 | **PLASTIC** |

### Key Observations

1. **Elastic Range (20 kN)**:
   - Max stress 380 MPa well below yield (980 MPa)
   - Safety factor = 2.57
   - No permanent deformation

2. **Yield Onset (60 kN)**:
   - Stress reaches 982 MPa (just above proportional limit)
   - Small plastic strain (0.1%) - localized yielding begins
   - Displacement tripled from 20 kN case

3. **Significant Plasticity (100 kN)**:
   - Stress exceeds yield by 17% (1148 vs 980 MPa)
   - Plastic strain 6.7% - permanent deformation
   - Displacement increased 4.9x vs 60 kN case (nonlinear response)

### Stress Concentration
Higher stresses with X-direction holes (380 MPa) vs Z-direction (236 MPa) at same 20 kN load:
- X-direction holes create more realistic but also more severe stress concentration
- Load transfer through horizontal pins induces higher local stresses
- This matches expected behavior for actual test specimen

## Files Modified/Created

### Geometry Scripts
- `scripts/create_geometry_v16.py` - Final working geometry with X-direction holes
- `scripts/fresh_model_v19.py` - Creates meshed model from scratch

### Analysis Scripts
- `scripts/setup_v19.py` - BCs, coupling, and load setup
- `scripts/setup_60kN.py` - 60 kN load variation
- `scripts/setup_100kN_v2.py` - 100 kN load setup
- `scripts/extract_*.py` - Results extraction scripts

### Output Files
- `Job_v19.odb` - 20 kN results
- `Job_v19_60kN.odb` - 60 kN results
- `Job_100kN.odb` - 100 kN results

## Mesh Details
- Element type: C3D4 (4-node tetrahedral)
- Node count: 853 (within Learning Edition 1000 limit)
- Mesh size: 7.0 mm global seed
- Free meshing with TET technique

## Verification
- All 6 circular edges found (2 per hole x 3 holes)
- Pin holes confirmed through bounding cylinder face selection
- Jobs completed successfully (COMPLETED status in .sta files)

## Conclusion
Experiment 4 successfully demonstrates elastic-plastic behavior of the topology-optimized fatigue specimen with correctly oriented X-direction pin holes. The specimen transitions from elastic to plastic response between 60-100 kN load levels.

## Screenshots
- `loop2_start.png` - Job_100kN.odb showing deformed mesh

## Next Steps (Optional)
1. Add stress contour visualization to screenshots
2. Compare stress distribution with paper reference
3. Identify exact stress concentration locations
4. Consider cyclic loading simulation for actual fatigue analysis
