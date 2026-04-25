---
name: plato-physics
description: Assemble complete Plato Analyze XML files from material, BC, and load blocks. Configures physics, criteria, and penalty functions.
allowed-tools:
  - Read
  - Write
  - Edit
---

# Plato Physics — XML Assembly

Assembles material, BC, and load XML fragments into a complete Plato Analyze XML ParameterList file.

## When to Use

- Internal: called by `plato-topology-optimization` or `plato-static-analysis` orchestrators
- After material, BC, and load blocks have been defined

## Complete XML Template — Mechanical Compliance

```xml
<?xml version="1.0"?>
<ParameterList name="Problem">
  <Parameter name="Physics" type="string" value="Plato Driver"/>
  <Parameter name="Spatial Dimension" type="int" value="3"/>
  <Parameter name="Input Mesh" type="string" value="mesh.exo"/>

  <ParameterList name="Plato Problem">
    <Parameter name="Physics" type="string" value="Mechanical"/>
    <Parameter name="PDE Constraint" type="string" value="Elliptic"/>
    <Parameter name="Self-Adjoint" type="bool" value="true"/>

    <ParameterList name="Criteria">
      <ParameterList name="my_objective">
        <Parameter name="Type" type="string" value="Internal Elastic Energy"/>
        <ParameterList name="Penalty Function">
          <Parameter name="Type" type="string" value="SIMP"/>
          <Parameter name="Exponent" type="double" value="3.0"/>
          <Parameter name="Minimum Value" type="double" value="1e-9"/>
        </ParameterList>
      </ParameterList>
    </ParameterList>

    <ParameterList name="Elliptic">
      <ParameterList name="Penalty Function">
        <Parameter name="Type" type="string" value="SIMP"/>
        <Parameter name="Exponent" type="double" value="3.0"/>
        <Parameter name="Minimum Value" type="double" value="1e-9"/>
      </ParameterList>
    </ParameterList>

    <ParameterList name="Spatial Model">
      <ParameterList name="Domains">
        <ParameterList name="Design Volume">
          <Parameter name="Element Block" type="string" value="design_domain"/>
          <Parameter name="Material Model" type="string" value="steel"/>
        </ParameterList>
      </ParameterList>
    </ParameterList>

    <!-- FROM plato-material -->
    <ParameterList name="Material Models">
      <ParameterList name="steel">
        <ParameterList name="Isotropic Linear Elastic">
          <Parameter name="Youngs Modulus" type="double" value="210e9"/>
          <Parameter name="Poissons Ratio" type="double" value="0.3"/>
        </ParameterList>
      </ParameterList>
    </ParameterList>

    <!-- FROM plato-bc -->
    <ParameterList name="Essential Boundary Conditions">
      <ParameterList name="X Fixed">
        <Parameter name="Type" type="string" value="Zero Value"/>
        <Parameter name="Index" type="int" value="0"/>
        <Parameter name="Sides" type="string" value="fixed_support"/>
      </ParameterList>
      <ParameterList name="Y Fixed">
        <Parameter name="Type" type="string" value="Zero Value"/>
        <Parameter name="Index" type="int" value="1"/>
        <Parameter name="Sides" type="string" value="fixed_support"/>
      </ParameterList>
      <ParameterList name="Z Fixed">
        <Parameter name="Type" type="string" value="Zero Value"/>
        <Parameter name="Index" type="int" value="2"/>
        <Parameter name="Sides" type="string" value="fixed_support"/>
      </ParameterList>
    </ParameterList>

    <!-- FROM plato-load -->
    <ParameterList name="Natural Boundary Conditions">
      <ParameterList name="Applied Traction">
        <Parameter name="Type" type="string" value="Uniform"/>
        <Parameter name="Values" type="Array(double)" value="{0.0, -1e6, 0.0}"/>
        <Parameter name="Sides" type="string" value="load_surface"/>
      </ParameterList>
    </ParameterList>

  </ParameterList>
</ParameterList>
```

## Criteria Types

| Type | XML Value | Self-Adjoint | Use Case |
|---|---|---|---|
| Compliance | `Internal Elastic Energy` | true | Stiffness maximization |
| Volume | `Volume` | N/A | Volume constraint |
| Stress P-Norm | `Stress P-Norm` | false | Stress-constrained TO |
| Thermal compliance | `Internal Thermal Energy` | true | Heat conduction |

## Physics Types

| Physics | PDE Constraint | Description |
|---|---|---|
| `Mechanical` | `Elliptic` | Linear elasticity (static) |
| `Thermal` | `Elliptic` | Steady-state heat conduction |
| `Thermomechanics` | `Elliptic` | Coupled thermo-mechanical |

## Key Rules

1. `Element Block` in Spatial Model must match the physical group name in the Exodus mesh
2. `Material Model` in Spatial Model must match the material name in Material Models
3. For TO: both Criteria and Elliptic blocks need their own Penalty Function
4. `Self-Adjoint` = true for compliance (saves one adjoint solve), false for stress
5. `Input Mesh` path must be relative to the working directory

## Validation

- [ ] Element block name matches Exodus mesh block name
- [ ] Material name is consistent between Spatial Model and Material Models
- [ ] All sidesets referenced in BCs and loads exist in the mesh
- [ ] Criteria type matches the optimization objective
- [ ] SIMP exponent is 3.0 (standard) unless user specifies otherwise
