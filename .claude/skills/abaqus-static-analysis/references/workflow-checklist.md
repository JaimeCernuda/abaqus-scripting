# Static Analysis Workflow Checklist

## Before Analysis

### Requirements Gathering
- [ ] Geometry defined (dimensions, shape)
- [ ] Material selected (E, ν, yield strength)
- [ ] Boundary conditions identified (supports)
- [ ] Loads identified (forces, pressures)
- [ ] Success criteria defined (max stress, max deflection)

### Design Intent
- [ ] Understand what the part does
- [ ] Know where loads are applied
- [ ] Know how part is mounted/supported
- [ ] Identify expected failure modes

## Model Setup

### Geometry (Step 1)
- [ ] Part created with correct dimensions
- [ ] Units consistent (mm-tonne-s-N-MPa)
- [ ] Partitions created for BC/load regions if needed
- [ ] Instance created in assembly

### Material (Step 2)
- [ ] Material defined with correct E and ν
- [ ] Density added if gravity or mass needed
- [ ] Plasticity defined if yielding expected
- [ ] Section created and assigned to all cells

### Mesh (Step 3)
- [ ] Appropriate element type selected
- [ ] Mesh size appropriate for features
- [ ] Node count within limits (Learning Edition: ≤1000)
- [ ] Mesh quality acceptable (no warnings)
- [ ] Refined mesh at stress concentrations

### Boundary Conditions (Step 4)
- [ ] BCs prevent rigid body motion (all 6 DOFs constrained)
- [ ] BCs applied to correct regions
- [ ] BC type matches physical support (fixed, pinned, roller)
- [ ] BCs don't over-constrain the model

### Loads (Step 5)
- [ ] Loads applied in correct direction
- [ ] Load magnitude correct
- [ ] Loads applied to correct region
- [ ] Distributed loads have correct total force

### Step Configuration (Step 6)
- [ ] Correct analysis type (Static)
- [ ] nlgeom setting appropriate
- [ ] Output requests include needed variables (S, U, RF)
- [ ] Increment settings appropriate for nonlinear

## After Analysis

### Job Completion
- [ ] Job completed without errors
- [ ] No warnings about convergence
- [ ] .odb file created successfully

### Results Validation
- [ ] Displacement is physically reasonable
- [ ] Displacement pattern matches expected behavior
- [ ] Sum of reaction forces ≈ applied loads
- [ ] Stress pattern follows expected load path
- [ ] Max stress located at expected concentration

### Engineering Assessment
- [ ] Max stress vs yield strength evaluated
- [ ] Factor of safety calculated: FOS = σ_yield / σ_max
- [ ] Max displacement acceptable for application
- [ ] No unexpected stress concentrations
- [ ] Results documented

## Factor of Safety Guidelines

| Application | Minimum FOS |
|-------------|-------------|
| Static, known loads | 1.5 - 2.0 |
| Dynamic/fatigue | 2.0 - 3.0 |
| Human safety critical | 3.0 - 4.0 |
| Unknown loads/materials | 4.0+ |

## Common Material Properties

| Material | E (MPa) | ν | σ_yield (MPa) | ρ (tonne/mm³) |
|----------|---------|---|---------------|---------------|
| Steel | 210,000 | 0.30 | 250-350 | 7.85e-9 |
| Aluminum | 70,000 | 0.33 | 270 (6061-T6) | 2.70e-9 |
| Titanium | 110,000 | 0.34 | 880 (Ti-6Al-4V) | 4.43e-9 |
| Stainless | 193,000 | 0.29 | 205 (304) | 8.00e-9 |
