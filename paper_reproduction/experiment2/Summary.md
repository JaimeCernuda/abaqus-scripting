# Experiment 2 - Y-Shape Bracket with Horizontal Loads

## Overview

This experiment analyzes a Y-shape bracket under two load cases:
- **Job 1**: Vertical load only (20 kN)
- **Job 2**: Vertical + horizontal spreading loads (20 kN + 2×5 kN)

## Geometry

```
                    ┌─────────────┐
                    │             │
                    │   ○ RP-1    │  ← Upper pin hole
                    │    (Upper)  │     20 kN downward (-Y)
                    └──────┬──────┘
                          /  \
                         /    \
                        /      \
                       /        \
                      /          \
          ┌──────────┐            ┌──────────┐
          │          │            │          │
   5 kN ← │  ○ RP-2  │            │  ○ RP-3  │ → 5 kN
   (-X)   │  (Lower  │            │  (Lower  │   (+X)
          │   Left)  │            │   Right) │
          └──────────┘            └──────────┘
              ▲                        ▲
              │ Fixed Y,Z              │ Fixed Y,Z
              │ Free X                 │ Free X

          Coordinate System:
          Y ↑
            │
            └──→ X
           Z (into page)
```

## Dimensions

| Parameter | Value | Description |
|-----------|-------|-------------|
| Total Height | 146.17 mm | Overall Y dimension |
| Total Width | 64.60 mm | Distance between lower pin centers |
| Lower Block Size | 35×35×35 mm | Cube-like lower supports |
| Upper Tab | 30×30 mm | Upper section width×height |
| Pin Diameter | 12 mm | All three pin holes |
| Thickness | 35 mm | Z direction (depth) |

## Material Properties (IN718)

| Property | Value |
|----------|-------|
| Young's Modulus | 198,400 MPa |
| Poisson's Ratio | 0.30 |
| Density | 8.19×10⁻⁹ tonne/mm³ |
| Yield Strength | 980 MPa |

## Applied Loads

### Job 1: Vertical Only
| Location | Force | Direction |
|----------|-------|-----------|
| RP-1 (Upper pin) | 20 kN | -Y (downward) |

### Job 2: Vertical + Horizontal
| Location | Force | Direction |
|----------|-------|-----------|
| RP-1 (Upper pin) | 20 kN | -Y (downward) |
| RP-2 (Lower left) | 5 kN | -X (outward left) |
| RP-3 (Lower right) | 5 kN | +X (outward right) |

## Boundary Conditions

### Job 1: All Lower Pins Fixed
- RP-2 and RP-3: Fixed in X, Y, Z (fully constrained)

### Job 2: Modified for Spreading
- RP-2 and RP-3: Fixed in Y, Z only (X is free to allow spreading)

## Results Summary

| Metric | Job 1 (Vertical) | Job 2 (V+H) | Change |
|--------|------------------|-------------|--------|
| Max von Mises Stress | 35.91 MPa | 36.22 MPa | +0.9% |
| Max Displacement | 0.0082 mm | 0.0167 mm | +102.9% |

## Key Observations

1. **Stress increase is minimal (0.9%)** - The horizontal spreading forces add little to the peak stress because the stress concentration at the upper pin dominates.

2. **Displacement doubles (+103%)** - The horizontal forces cause significant spreading at the lower supports, which translates to larger overall displacement.

3. **Stress concentration** - Maximum stress occurs at the upper pin hole where the vertical load is applied through the coupling constraint.

## Output Files

| File | Description |
|------|-------------|
| `Exp2_Job1_Vertical.odb` | Job 1 results database |
| `Exp2_Job2_Horizontal.odb` | Job 2 results database |
| `screenshots/Job1_VonMises.png` | Job 1 stress contour |
| `screenshots/Job2_VonMises.png` | Job 2 stress contour |
| `screenshots/Forces_Diagram_*.png` | Geometry with reference points |
| `results_summary.txt` | Numerical results comparison |

## Scripts

| Script | Purpose |
|--------|---------|
| `01_create_geometry_rotated.py` | Create Y-shape geometry with X-axis holes |
| `02_define_material.py` | Define IN718 material |
| `03_setup_analysis.py` | Set up Job 1 (vertical load) |
| `04_mesh_and_run.py` | Mesh and run Job 1 |
| `05_job2_horizontal.py` | Modify BCs, add horizontal loads, run Job 2 |
| `06_extract_results.py` | Extract results from both ODBs |
| `visualize_job1.py` | Save Job 1 contour screenshots |
| `visualize_job2.py` | Save Job 2 contour screenshots |
