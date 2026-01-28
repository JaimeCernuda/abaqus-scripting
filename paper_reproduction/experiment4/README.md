# Experiment 4: Topology Optimized Fatigue Specimen FEA

## Overview

This experiment simulates the stress and plastic deformation behavior of a topology-optimized fatigue specimen from the reference paper. The specimen is designed for use with the MTS 370.02 testing machine.

## Geometry

The specimen features:
- Overall height: 146 mm
- Upper block: 28 mm wide x 28 mm tall with single pin hole
- Lower blocks: Two 28 mm x 28 mm blocks with pin holes
- Narrowing middle section (topology-optimized shape)
- **Pin holes: 12.7 mm diameter, oriented in X-direction (horizontal)**

## Material: IN718 (Inconel 718)

| Property | Value | Unit |
|----------|-------|------|
| Young's Modulus | 200,000 | MPa |
| Poisson's Ratio | 0.30 | - |
| Yield Strength | 980 | MPa |
| Density | 8.19e-9 | tonne/mm³ |

Plasticity (hardening):
- 980 MPa at 0% plastic strain
- 1100 MPa at 5% plastic strain
- 1200 MPa at 10% plastic strain

## Analysis Results

| Job | Load | Max Stress | Max Displacement | PEEQ | Status |
|-----|------|------------|------------------|------|--------|
| Job_20kN | 20 kN | 380.72 MPa | 0.0641 mm | 0 | Elastic |
| Job_60kN | 60 kN | 982.39 MPa | 0.1908 mm | 0.001 | Yield onset |
| Job_100kN | 100 kN | 1148.03 MPa | 0.9370 mm | 0.067 | Plastic |

### Key Observations

1. **Elastic Response (20 kN)**: Stress well below yield (safety factor 2.57)
2. **Yield Onset (60 kN)**: Stress reaches yield point, localized plasticity begins
3. **Significant Plasticity (100 kN)**: 6.7% plastic strain, permanent deformation

## Files

### Main Files
- `TO_Specimen.cae` - Abaqus CAE model file
- `Job_20kN.odb` - 20 kN elastic analysis results
- `Job_60kN.odb` - 60 kN yield onset results
- `Job_100kN.odb` - 100 kN plastic deformation results

### Scripts
- `scripts/create_geometry.py` - Create TO specimen geometry with X-direction pin holes
- `scripts/create_model.py` - Create meshed model from geometry
- `scripts/setup_20kN.py` - Set up 20 kN load case with BCs
- `scripts/setup_60kN.py` - Set up 60 kN load case
- `scripts/setup_100kN.py` - Set up 100 kN load case
- `scripts/extract_*_results.py` - Extract results from ODB files

### Screenshots
- `screenshots/loop2_DEFINITIVE_right_view.png` - Wireframe view confirming X-direction pin holes

### Archive
Old script versions, debug files, and verification outputs are stored in the `archive/` folder.

## Running the Analysis

```bash
# Create geometry and mesh
abaqus cae noGUI=scripts/create_geometry.py
abaqus cae noGUI=scripts/create_model.py

# Run 20 kN analysis
abaqus cae noGUI=scripts/setup_20kN.py
abaqus job=Job_20kN interactive

# Run 60 kN analysis
abaqus cae noGUI=scripts/setup_60kN.py
abaqus job=Job_60kN interactive

# Run 100 kN analysis
abaqus cae noGUI=scripts/setup_100kN.py
abaqus job=Job_100kN interactive

# Extract results
abaqus python scripts/extract_60kN_results.py
abaqus python scripts/extract_100kN_results.py
```

## Verification

The geometry was verified multiple ways:
1. **Programmatic**: Circular edge analysis confirmed 18mm X-span, 0mm Z-span
2. **Visual**: Right-side wireframe view shows pin holes as circles (X-direction)
3. **Node analysis**: Upper hole at Y=132.2mm (in upper block), lower holes at Y=14.0mm

See `DEFINITIVE_VERIFICATION.md` for detailed verification.

## Mesh

- Element type: C3D4 (4-node tetrahedral)
- Node count: 853 (within Learning Edition 1000 limit)
- Global seed: 7.0 mm
