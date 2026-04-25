---
name: plato-load
description: Apply forces, tractions, and pressures to Plato models. Generates XML natural boundary condition blocks.
allowed-tools:
  - Read
  - Write
  - Edit
---

# Plato Load

Define natural (Neumann) boundary conditions — forces, tractions, pressures.

## When to Use

- User mentions force, load, pressure, traction, gravity
- User wants to apply mechanical loading to a surface

## When NOT to Use

- Fixed supports or displacement constraints → use `plato-bc`

## What to Ask User

### Required
1. **Load type**: Force (point/distributed), pressure (normal), traction (surface vector)
2. **Magnitude**: Value in N or Pa
3. **Direction**: Which direction (x, y, z) or normal
4. **Location**: Which surface (must match sideset name in mesh)

### Optional
5. **Area**: For converting point force to traction (traction = force / area)

## XML Output — Natural Boundary Conditions

### Uniform traction (surface force vector)

```xml
<ParameterList name="Natural Boundary Conditions">
  <ParameterList name="Applied Traction">
    <Parameter name="Type" type="string" value="Uniform"/>
    <Parameter name="Values" type="Array(double)" value="{0.0, -1e6, 0.0}"/>
    <Parameter name="Sides" type="string" value="load_surface"/>
  </ParameterList>
</ParameterList>
```

Values are traction components (force/area) in {x, y, z}.

### Uniform pressure (normal to surface)

```xml
<ParameterList name="Natural Boundary Conditions">
  <ParameterList name="Applied Pressure">
    <Parameter name="Type" type="string" value="Uniform Pressure"/>
    <Parameter name="Value" type="double" value="1e6"/>
    <Parameter name="Sides" type="string" value="pressure_surface"/>
  </ParameterList>
</ParameterList>
```

Positive pressure = compression (into surface).

### Multiple loads

```xml
<ParameterList name="Natural Boundary Conditions">
  <ParameterList name="Load Case 1">
    <Parameter name="Type" type="string" value="Uniform"/>
    <Parameter name="Values" type="Array(double)" value="{0.0, -5e5, 0.0}"/>
    <Parameter name="Sides" type="string" value="top_surface"/>
  </ParameterList>
  <ParameterList name="Load Case 2">
    <Parameter name="Type" type="string" value="Uniform"/>
    <Parameter name="Values" type="Array(double)" value="{1e5, 0.0, 0.0}"/>
    <Parameter name="Sides" type="string" value="side_surface"/>
  </ParameterList>
</ParameterList>
```

## Input Deck (.i) Block

```
begin load 1
  type traction
  location_type sideset
  location_name load_surface
  value 0 -1e6 0
end load
```

## Converting Point Force to Traction

Plato works with tractions (force/area), not point forces. To convert:

```
traction = force / surface_area
```

Example: 1000 N downward on a 10×5 mm face:
- Area = 50 mm² = 50e-6 m²
- Traction = 1000 / 50e-6 = 2e7 Pa
- Values: `{0.0, -2e7, 0.0}`

## Validation

- [ ] Load direction makes physical sense
- [ ] Magnitude is reasonable (not off by orders of magnitude from unit confusion)
- [ ] Sideset name matches mesh
- [ ] At least one load is applied (otherwise zero displacement everywhere)
