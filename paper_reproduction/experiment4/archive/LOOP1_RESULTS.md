# Experiment 4 - Loop 1 Results Summary

## Date: January 27, 2026

## Accomplishments

### 1. Geometry Fixed
- **Issue**: Lower pin holes were missing from previous attempts
- **Solution**: Created `create_geometry_v2.py` that properly cuts all 3 pin holes
  - Upper pin hole: centered in upper block
  - Left lower pin hole: centered in left lower block
  - Right lower pin hole: centered in right lower block
- **Verified**: All pin holes visible in Abaqus viewport

### 2. Material Defined
- Material: IN718 (Inconel 718)
- Properties from paper Table 2:
  - E = 198,400 MPa
  - ν = 0.30
  - ρ = 8.19e-9 tonne/mm³
  - Proportional limit = 980 MPa
  - Yield strength (0.2%) = 1191 MPa
- Elastic-plastic behavior defined with tabular data

### 3. Analysis Setup Complete
- Steps: FatigueTest, TODesign, PlasticityTest
- BCs: Lower pins fixed in Y,Z; free in X
- Load: Vertical load at upper pin via kinematic coupling
- Mesh: 570 nodes, C3D4 elements (within Learning Edition limit)

### 4. Jobs Completed Successfully

#### Job 1: FatigueTest (20 kN)
| Metric | Value |
|--------|-------|
| Max von Mises | 235.8 MPa |
| Max Principal | 208.4 MPa |
| Max Displacement | 0.0839 mm |
| Plastic Strain | 0.0 (NONE) |
| Status | **ELASTIC** |

#### Job 2: FatigueTest + TODesign (20 kN)
- Both steps completed
- Same elastic response as Job 1
- No plastic deformation

#### Job 3: PlasticityTest (100 kN)
| Metric | Value |
|--------|-------|
| Max von Mises | **1065.3 MPa** |
| Max Principal | 1029.2 MPa |
| Min Principal | -1116.5 MPa |
| Max Displacement | 0.4199 mm |
| Plastic Strain (PEEQ) | **0.000806** |
| Status | **EARLY PLASTIC** |

### Key Finding
- 100 kN load induces plasticity with stress exceeding the proportional limit (980 MPa)
- Plastic strain of 0.08% detected - permanent deformation occurring
- Material is between proportional limit and 0.2% yield strength

## Screenshots Saved
- `loop1_start.png` - Initial state showing geometry
- `loop1_end.png` - Geometry with all pin holes verified
- `loop1_job1_results.png` - Job 1 results visualization
- `loop1_end_job3_plasticity.png` - Job 3 plasticity results

## Files Created
- `scripts/create_geometry_v2.py` - Fixed geometry script
- `scripts/define_material.py` - IN718 material definition
- `scripts/setup_analysis_v2.py` - Simplified analysis setup
- `scripts/mesh_and_job_v2.py` - Mesh and job creation
- `scripts/setup_job2_todesign.py` - Job 2 setup
- `scripts/setup_job3_plasticity.py` - High-load plasticity test
- `scripts/extract_results.py` - Results extraction
- `scripts/extract_all_results.py` - Comprehensive results

## Next Steps for Loop 2
1. Visualize stress distribution with contour plots
2. Identify stress concentration locations
3. Compare with paper results (Location 3 - inner lower leg)
4. Consider adding horizontal loads for TODesign case
5. Potentially refine mesh in high-stress regions
