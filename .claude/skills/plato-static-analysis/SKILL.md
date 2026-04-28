---
name: plato-static-analysis
description: Complete workflow for static structural analysis using Plato Analyze. FEA only — no optimization. For stress, displacement, and reaction force evaluation.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Agent
---

# Plato Static Analysis — FEA Workflow

Run linear static FEA using Plato Analyze to evaluate stress, displacement, and stiffness.

## When to Use

- User wants stress/displacement analysis without optimization
- User wants to validate a design under specific loads
- User mentions "check stresses", "FEA", "static analysis"
- Verification run on an optimized topology

## When NOT to Use

- Topology optimization → use `plato-topology-optimization`
- Nonlinear analysis (contact, plasticity, large deformation) → Plato Analyze supports limited nonlinear; for complex cases, use Abaqus
- Modal/dynamic analysis → not yet implemented in this skill set

## What to Ask User

### Required
1. **Geometry**: Shape and dimensions, or existing mesh file
2. **Material**: Name or E/nu/rho values
3. **Supports**: Where fixed, which DOFs
4. **Loads**: Type, magnitude, direction, location

### Optional
5. **Mesh size**: Default auto
6. **Output variables**: Default vonmises + displacement

## Workflow

### Step 1: Generate Mesh
Invoke `plato-mesh` to create Exodus mesh.

### Step 2: Create Physics XML
Invoke `plato-material`, `plato-bc`, `plato-load`, `plato-physics`.

The XML for static analysis (no optimization) uses the same structure but without SIMP penalty:

```xml
<ParameterList name="Problem">
  <Parameter name="Physics" type="string" value="Plato Driver"/>
  <Parameter name="Spatial Dimension" type="int" value="3"/>
  <Parameter name="Input Mesh" type="string" value="mesh.exo"/>
  <ParameterList name="Plato Problem">
    <Parameter name="Physics" type="string" value="Mechanical"/>
    <Parameter name="PDE Constraint" type="string" value="Elliptic"/>
    <Parameter name="Self-Adjoint" type="bool" value="true"/>
    <ParameterList name="Criteria">
      <ParameterList name="stress">
        <Parameter name="Type" type="string" value="Stress P-Norm"/>
      </ParameterList>
    </ParameterList>
    <ParameterList name="Elliptic"/>
    <!-- Spatial Model, Material Models, BCs from sub-skills -->
  </ParameterList>
</ParameterList>
```

### Step 3: Create Input Deck

For analysis-only (no optimization), use a single forward solve:

```
begin service 1
  code platomain
  number_processors 1
end service

begin service 2
  code plato_analyze
  number_processors 1
end service

begin material 1
  material_model isotropic_linear_elastic
  youngs_modulus 210e9
  poissons_ratio 0.3
end material

begin block 1
  material 1
  name block_1
end block

begin load 1
  type traction
  location_type sideset
  location_name load_surface
  value 0 -1e6 0
end load

begin boundary_condition 1
  type fixed_value
  location_type sideset
  location_name fixed_support
  degree_of_freedom dispx dispy dispz
  value 0 0 0
end boundary_condition

begin scenario 1
  physics steady_state_mechanics
  dimensions 3
  loads 1
  boundary_conditions 1
  material 1
end scenario

begin criterion 1
  type mechanical_compliance
end criterion

begin objective
  type weighted_sum
  services 2
  criteria 1
  scenarios 1
  weights 1.0
end objective

begin optimization_parameters
  optimization_algorithm rol_bound_constrained
  discretization density
  initial_density_value 1.0
  max_iterations 0
end optimization_parameters

begin output
  service 2
  data vonmises dispx dispy dispz
end output

begin mesh
  name mesh.exo
end mesh
```

Note: `initial_density_value 1.0` and `max_iterations 0` means run one forward solve with full material everywhere (no optimization).

### Step 4: Submit Job
Invoke `plato-job` — submit via SLURM.

### Step 5: Extract Results
Invoke `plato-results` to read stress and displacement from Exodus output.

## Validation Checklist

- [ ] Displacement is physically reasonable (not zero, not enormous)
- [ ] Stress concentrations are at expected locations (near supports, load points)
- [ ] Reaction forces balance applied loads (sum ≈ 0)

## Troubleshooting

| Issue | Cause | Fix |
|---|---|---|
| Zero displacement everywhere | BCs overconstrained or no load | Check loads are non-zero and applied to correct sideset |
| Rigid body motion | Insufficient BCs | Constrain all 6 DOFs (3 translations + 3 rotations) |
| Very large displacement | Units mismatch | Verify consistent units (all SI or all mm-N-MPa) |
| Solver doesn't converge | Ill-conditioned mesh | Improve mesh quality, check for degenerate elements |
