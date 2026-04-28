---
name: plato-material
description: Define material properties for Plato models. Generates XML ParameterList blocks and .i material blocks.
allowed-tools:
  - Read
  - Write
  - Edit
---

# Plato Material

Define material properties for Plato Analyze physics definitions.

## When to Use

- User mentions steel, aluminum, titanium, or any material name
- User specifies Young's modulus, Poisson's ratio, density
- User asks about material properties

## What to Ask User

### Required
- **Material**: Name (steel, aluminum, titanium) OR custom E/nu/rho values

### Optional
- **Units**: SI (Pa, m, kg/m³) or mm-system (MPa, mm, tonne/mm³). Default: SI

## Material Library

| Material | E (Pa) | nu | rho (kg/m³) |
|---|---|---|---|
| Steel | 210e9 | 0.3 | 7850 |
| Aluminum 6061-T6 | 68.9e9 | 0.33 | 2700 |
| Titanium Ti-6Al-4V | 113.8e9 | 0.342 | 4430 |
| IN718 | 205e9 | 0.284 | 8190 |
| Copper | 117e9 | 0.34 | 8960 |
| Nylon (PA12) | 1.7e9 | 0.4 | 1010 |

## Output: Two Blocks

### 1. XML ParameterList (for analyze.xml)

```xml
<ParameterList name="Material Models">
  <ParameterList name="steel">
    <ParameterList name="Isotropic Linear Elastic">
      <Parameter name="Youngs Modulus" type="double" value="210e9"/>
      <Parameter name="Poissons Ratio" type="double" value="0.3"/>
    </ParameterList>
  </ParameterList>
</ParameterList>
```

### 2. Input deck block (for input.i)

```
begin material 1
  material_model isotropic_linear_elastic
  youngs_modulus 210e9
  poissons_ratio 0.3
  mass_density 7850
end material
```

## Supported Material Models

| Model | XML name | Use case |
|---|---|---|
| Isotropic linear elastic | `Isotropic Linear Elastic` | Most common, metals/polymers |
| Cubic linear elastic | `Cubic Linear Elastic` | Single-crystal metals |
| Orthotropic linear elastic | `Orthotropic Linear Elastic` | Composites, wood |
| Thermal conduction | `Thermal Conduction` | Heat transfer problems |

## Validation

- [ ] E > 0 (Young's modulus must be positive)
- [ ] 0 < nu < 0.5 (Poisson's ratio physical range)
- [ ] rho > 0 (density must be positive)
- [ ] Units are consistent with geometry and loads
