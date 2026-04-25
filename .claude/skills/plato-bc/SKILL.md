---
name: plato-bc
description: Define boundary conditions (essential BCs) for Plato models. Fixed supports, rollers, prescribed displacements.
allowed-tools:
  - Read
  - Write
  - Edit
---

# Plato Boundary Conditions

Define essential (Dirichlet) boundary conditions for Plato Analyze.

## When to Use

- User mentions fixed, clamped, pinned, supported, constrained, roller
- User specifies displacement constraints on faces/edges

## When NOT to Use

- Loads or forces → use `plato-load`

## What to Ask User

### Required
1. **Location**: Which face/surface (must match a sideset name in the Exodus mesh)
2. **Type**: Fixed (all DOFs), roller (1-2 DOFs free), prescribed displacement

### Optional
3. **DOFs**: Which directions to constrain (default: all three for fixed)
4. **Value**: Displacement value (default: 0)

## XML Output

Each constrained DOF requires a **separate** ParameterList entry. Index: 0=dispx, 1=dispy, 2=dispz.

### Fixed support (all 3 DOFs = 0)

```xml
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
```

### Roller (free in X, fixed in Y and Z)

```xml
<ParameterList name="Essential Boundary Conditions">
  <ParameterList name="Y Fixed">
    <Parameter name="Type" type="string" value="Zero Value"/>
    <Parameter name="Index" type="int" value="1"/>
    <Parameter name="Sides" type="string" value="roller_support"/>
  </ParameterList>
  <ParameterList name="Z Fixed">
    <Parameter name="Type" type="string" value="Zero Value"/>
    <Parameter name="Index" type="int" value="2"/>
    <Parameter name="Sides" type="string" value="roller_support"/>
  </ParameterList>
</ParameterList>
```

### Prescribed displacement

```xml
<ParameterList name="Prescribed Y Displacement">
  <Parameter name="Type" type="string" value="Fixed Value"/>
  <Parameter name="Index" type="int" value="1"/>
  <Parameter name="Sides" type="string" value="top_surface"/>
  <Parameter name="Value" type="double" value="-0.001"/>
</ParameterList>
```

## Input Deck (.i) Block

```
begin boundary_condition 1
  type fixed_value
  location_type sideset
  location_name fixed_support
  degree_of_freedom dispx dispy dispz
  value 0 0 0
end boundary_condition
```

## Key Rule

The `Sides` value (XML) and `location_name` (.i) **must exactly match** a named sideset in the Exodus mesh. Check with `ncdump -h mesh.exo`.

## Validation

- [ ] All 6 rigid body DOFs are constrained (3 translations + 3 rotations)
- [ ] Sideset names match between mesh and BC definition
- [ ] Sufficient constraints to prevent rigid body motion
