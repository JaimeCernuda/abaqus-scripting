# Abaqus FEA Scripting - AI-Assisted Workflow

This repository demonstrates an AI-assisted workflow for Abaqus finite element analysis using Python scripting. All scripts were developed collaboratively with Claude AI.

## Examples

### Cantilever Beam
A cantilever beam under end load - demonstrates basic FEA workflow.

- **Geometry**: 200mm × 20mm × 10mm beam
- **Load**: 1000 N point load at free end
- **Material**: Steel (E=210 GPa, ν=0.3)

![Cantilever Results](examples/cantilever/results.png)

**Results**: Max stress 150.2 MPa, Max displacement 0.476 mm

### Cube Compression
Simple cube under uniform compression - validates basic setup.

- **Geometry**: 10mm × 10mm × 10mm cube
- **Load**: 1 MPa uniform pressure
- **Material**: Steel

![Cube Results](examples/cube/results.png)

**Results**: Uniform stress distribution as expected

---

## Paper Reproduction: Topology-Optimized Fatigue Specimen

Reproduction of the fatigue specimen from the paper, featuring a topology-optimized geometry with three pin holes for testing machine mounting.

### Experiment 4 - Final Working Model

**Specimen Geometry**:
- Total height: 146 mm
- Pin holes: 12.7 mm diameter, X-direction (horizontal)
- Material: IN718 (Inconel 718), E=200 GPa, σy=980 MPa

![Geometry Verification](paper_reproduction/experiment4/screenshots/geometry/holes_right_view_wireframe.png)

*Wireframe view confirming X-direction pin holes (appear as circles from right side)*

### Analysis Results

Three load cases exploring elastic-plastic behavior:

| Load | Max Stress | Plastic Strain (PEEQ) | Response |
|------|------------|----------------------|----------|
| 20 kN | 380 MPa | 0% | Elastic |
| 60 kN | 982 MPa | 0.1% | Yield onset |
| 100 kN | 1148 MPa | 6.7% | Plastic |

#### 20 kN - Elastic Response
![20kN Results](paper_reproduction/experiment4/screenshots/results/results_20kN_elastic_iso.png)

#### 60 kN - Yield Onset
![60kN Results](paper_reproduction/experiment4/screenshots/results/results_60kN_yield_iso.png)

#### 100 kN - Plastic Deformation
![100kN Results](paper_reproduction/experiment4/screenshots/results/results_100kN_plastic_iso.png)

---

## Topology Optimization (Pending)

The `examples/topology_optimization/` folder contains scripts for:
- 2D bridge optimization
- 3D bracket optimization

**Note**: These require a full Abaqus license with the Tosca module. The Learning Edition does not support topology optimization. Scripts are ready to run once the full license is available.

---

## Running Scripts

```bash
# With GUI
abaqus cae script=script_name.py

# Headless (faster)
abaqus cae noGUI=script_name.py

# Post-processing only
abaqus python script_name.py
```

## Units

All models use consistent SI units: **mm-tonne-s-N-MPa**
