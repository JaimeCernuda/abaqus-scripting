# Tosca Design Responses (DRESP) Reference

Complete catalog of all DRESP TYPE values for topology optimization, with usage rules, selection area requirements, and load case configuration.

## DRESP Block Structure

```
DRESP
  ID_NAME    = <unique_name>
  DEF_TYPE   = SYSTEM | OPER
  TYPE       = <response_type>
  EL_GROUP   = <element_group>       ! For element-based types (E)
  ND_GROUP   = <node_group>          ! For node-based types (N)
  NODE       = <node_number>         ! Alternative to ND_GROUP
  ELEM       = <element_number>      ! Alternative to EL_GROUP
  GROUP_OPER = MAX | MIN | SUM | AVERAGE
  LC_SET     = <approach>,<loadcase>,<substep>
  CS_REF     = CS_0                  ! Coordinate system (default: global)
END_
```

## Core Design Response Types for Topology Optimization

These are the types most commonly used with `STRATEGY = TOPO_SENSITIVITY`.

### VOLUME (load case independent)

Total volume of elements in the group. Used in almost every topology optimization as either the objective or a constraint.

| Property | Value |
|----------|-------|
| Selection area | Element-based (E) |
| Load case dependent | No |
| Usable as OBJ_FUNC | TOPO_S, TOPO_C |
| Usable as CONSTRAINT | TOPO_S, TOPO_C |
| GROUP_OPER | Typically `SUM` |

```
DRESP
  ID_NAME    = DRESP_VOLUME
  DEF_TYPE   = SYSTEM
  TYPE       = VOLUME
  EL_GROUP   = ALL_ELEMENTS
  GROUP_OPER = SUM
END_
```

### WEIGHT (load case independent)

Total weight of elements (accounts for material density). Use instead of VOLUME when materials have different densities.

| Property | Value |
|----------|-------|
| Selection area | Element-based (E) |
| Load case dependent | No |
| Usable as OBJ_FUNC | TOPO_S, TOPO_C |
| Usable as CONSTRAINT | TOPO_S |
| GROUP_OPER | Typically `SUM` |

```
DRESP
  ID_NAME    = DRESP_WEIGHT
  DEF_TYPE   = SYSTEM
  TYPE       = WEIGHT
  EL_GROUP   = ALL_ELEMENTS
  GROUP_OPER = SUM
END_
```

### STRAIN_ENERGY (load case dependent)

Total strain energy -- proportional to structural compliance. Minimizing strain energy = maximizing stiffness.

| Property | Value |
|----------|-------|
| Selection area | Element-based (E) |
| Load case dependent | Yes |
| Usable as OBJ_FUNC | TOPO_S, TOPO_C |
| Usable as CONSTRAINT | TOPO_S |
| GROUP_OPER | `SUM` (must include ALL relevant elements) |

```
DRESP
  ID_NAME    = DRESP_STRAIN_ENERGY
  DEF_TYPE   = SYSTEM
  TYPE       = STRAIN_ENERGY
  EL_GROUP   = ALL_ELEMENTS
  GROUP_OPER = SUM
END_
```

**Important:** The element group for STRAIN_ENERGY must include all elements that contribute to the structural response, not just the design space. Missing elements leads to incorrect sensitivity calculations.

### SIG_SENS_MISES (load case dependent) -- TOPOLOGY STRESS

Density-weighted centroidal von Mises stress, specifically designed for topology optimization. This is NOT the same as the solver's von Mises stress -- it includes density interpolation to handle intermediate-density elements.

| Property | Value |
|----------|-------|
| Selection area | Element-based (E) -- centroidal only |
| Load case dependent | Yes |
| Usable as OBJ_FUNC | TOPO_S |
| Usable as CONSTRAINT | TOPO_S |
| GROUP_OPER | Not applicable (implicit MAX) |
| Solver sensitivities | Available from Abaqus |

```
DRESP
  ID_NAME  = DRESP_STRESS
  DEF_TYPE = SYSTEM
  TYPE     = SIG_SENS_MISES
  EL_GROUP = ALL_ELEMENTS
END_
```

**Critical rules for SIG_SENS_MISES:**

1. **Each SIG_SENS_MISES DRESP can only be used ONCE** -- either in the objective OR in a constraint, not both. If you need stress in both, define separate DRESP blocks.

2. **Exclude stress singularities.** Elements at loaded nodes and boundary conditions have non-physical stress concentrations. Create a group that excludes these elements:
   ```
   GROUP_DEF
     ID_NAME = STRESS_EVAL_ELEMENTS
     TYPE    = ELEM
     FORMAT  = LIST_SUBTRACT_GROUP
     LIST_BEGIN
     ALL_ELEMENTS, LoadedElements, BCElements
   END_
   ```

3. **Only von Mises stress is supported** for topology optimization. No other stress measure works.

4. **Supported elements:** 3D solid continuum only (hex8, hex20, tet10, pent6, pent15). Tet4 is NOT recommended (locking). Shell elements and pyramids are NOT supported.

5. **Only linear materials** in the stress evaluation group. Anisotropic and nonlinear materials are only allowed if their elements are excluded from the SIG_SENS_MISES group.

6. **Stress interpretation:** For solid elements (density = 1.0) with an active stress constraint, SIG_SENS_MISES equals the FE solver's von Mises stress. For intermediate densities, the values differ due to density interpolation.

7. **When SIG_SENS_MISES is present in the optimization, Tosca automatically:**
   - Sets DENSITY_MOVE = 0.10 (from default 0.25)
   - Sets ITER_MAX = 80 (from default 50)
   - Uses conservative update strategy
   - Override with `STRESS_DRESP_OPT = OFF` in OPT_PARAM

8. **Recommended interpolation:** Use `MAT_INTERPOLATION = MIMP` for stress-constrained problems, especially with body loads.

### Displacement Types (load case dependent)

All displacement types follow the same pattern:

| TYPE | Description | Selection |
|------|-------------|-----------|
| `DISP_ABS` | Absolute displacement magnitude | Node (N) |
| `DISP_X` | Displacement in X (signed) | Node (N) |
| `DISP_X_ABS` | Absolute displacement in X | Node (N) |
| `DISP_Y` | Displacement in Y (signed) | Node (N) |
| `DISP_Y_ABS` | Absolute displacement in Y | Node (N) |
| `DISP_Z` | Displacement in Z (signed) | Node (N) |
| `DISP_Z_ABS` | Absolute displacement in Z | Node (N) |

All are usable as OBJ_FUNC and CONSTRAINT for TOPO_S.

```
DRESP
  ID_NAME  = DRESP_DISP_MAX
  DEF_TYPE = SYSTEM
  TYPE     = DISP_Y_ABS
  NODE     = 110            ! Single node
END_
```

```
DRESP
  ID_NAME    = DRESP_DISP_GROUP
  DEF_TYPE   = SYSTEM
  TYPE       = DISP_Z_ABS
  ND_GROUP   = tip_nodes
  GROUP_OPER = MAX
END_
```

### DYN_FREQ (load case dependent -- modal)

Eigenfrequency from modal analysis.

| Property | Value |
|----------|-------|
| Selection area | Scalar (S) -- no group needed |
| Load case dependent | Yes (modal load case) |
| Usable as OBJ_FUNC | TOPO_S |
| Usable as CONSTRAINT | TOPO_S |

```
DRESP
  ID_NAME  = DRESP_FREQ_1
  DEF_TYPE = SYSTEM
  TYPE     = DYN_FREQ
  LC_SET   = MODAL, 1, ALL
END_
```

For multiple eigenfrequencies, define separate DRESPs:
```
DRESP
  ID_NAME  = DRESP_FREQ_2
  DEF_TYPE = SYSTEM
  TYPE     = DYN_FREQ
  LC_SET   = MODAL, 2, ALL
END_
```

### ENERGY_STIFF_MEASURE (load case dependent)

Energy stiffness measure -- an alternative to STRAIN_ENERGY that can be more robust.

| Property | Value |
|----------|-------|
| Selection area | Element-based (E) |
| Usable as OBJ_FUNC | TOPO_S |
| Usable as CONSTRAINT | TOPO_S |
| Solver sensitivities | Available from Abaqus |

### Reaction Force Types (load case dependent)

| TYPE | Description |
|------|-------------|
| `REACTION_FORCE_ABS` | Absolute reaction force magnitude |
| `REACTION_FORCE_X` | Reaction force in X (signed) |
| `REACTION_FORCE_X_ABS` | Absolute reaction force in X |
| `REACTION_FORCE_Y` / `_Y_ABS` | Y-direction |
| `REACTION_FORCE_Z` / `_Z_ABS` | Z-direction |

All node-based (N), usable as OBJ_FUNC and CONSTRAINT for TOPO_S.

### Internal Force Types (load case dependent)

| TYPE | Description |
|------|-------------|
| `INTERNAL_FORCE_ABS` | Absolute internal force magnitude |
| `INTERNAL_FORCE_X` / `_X_ABS` | X-direction |
| `INTERNAL_FORCE_Y` / `_Y_ABS` | Y-direction |
| `INTERNAL_FORCE_Z` / `_Z_ABS` | Z-direction |

Node with element info (NE), usable as OBJ_FUNC and CONSTRAINT for TOPO_S.

### Rotation Types (load case dependent)

| TYPE | Description |
|------|-------------|
| `ROT_ABS` | Absolute rotation magnitude |
| `ROT_X` / `_X_ABS` | Rotation about X |
| `ROT_Y` / `_Y_ABS` | Rotation about Y |
| `ROT_Z` / `_Z_ABS` | Rotation about Z |

Node-based (N), usable as OBJ_FUNC and CONSTRAINT for TOPO_S.

### Geometric Properties (load case independent)

| TYPE | Description |
|------|-------------|
| `CENTER_GRAVITY_X` | Center of gravity, X coordinate |
| `CENTER_GRAVITY_Y` | Center of gravity, Y coordinate |
| `CENTER_GRAVITY_Z` | Center of gravity, Z coordinate |
| `INERTIA_XX` through `INERTIA_ZZ` | Moments of inertia |

All element-based (E), usable as OBJ_FUNC and CONSTRAINT for TOPO_S.

### Other Stress Types (for reference -- not topology-specific)

These are available for shape/bead/sizing optimization but NOT for topology optimization constraints:

| TYPE | Description | Topology support |
|------|-------------|-----------------|
| `SIG_MISES` | Standard von Mises stress | Shape/Bead only |
| `SIG_1` | Max principal stress | TOPO_S (OBJ_FUNC/CONSTRAINT with Abaqus sens) |
| `SIG_3` | Min principal stress | TOPO_S (OBJ_FUNC/CONSTRAINT with Abaqus sens) |
| `SIG_SIGNED_MISES` | Signed von Mises | TOPO_S |
| `PEMAG` | Plastic strain magnitude | TOPO_S (Abaqus sens) |

### Density Measure (load case independent)

`DENSITY_MEASURE` -- quantifies how many elements have intermediate densities. Can be used to enforce solid/void convergence.

| Property | Value |
|----------|-------|
| Selection area | Element-based (E) |
| Usable as OBJ_FUNC | TOPO_S |
| Usable as CONSTRAINT | TOPO_S |

---

## GROUP_OPER Options

| Operator | Meaning | Common Use |
|----------|---------|------------|
| `MAX` | Maximum value in the group | Displacement limits, stress peaks |
| `MIN` | Minimum value in the group | Minimum frequency |
| `SUM` | Sum of all values | Volume, weight, total strain energy |
| `AVERAGE` | Average value | Mean displacement |

**Rule:** GROUP_OPER is required when EL_GROUP or ND_GROUP references a group with multiple entities. Not needed for single-node (`NODE = 110`) or single-element specifications.

---

## DEF_TYPE = OPER (Derived Design Responses)

Create a design response from operations on other DRESPs.

### SUB / SUB_ABS (difference of two responses)

```
DRESP
  ID_NAME  = relative_disp
  DEF_TYPE = OPER
  VAR_A    = disp_node_1
  VAR_B    = disp_node_2
  VAR_OPER = SUB_ABS          ! |A - B|
END_
```

**Allowed types for SUB/SUB_ABS:** DISP_X/Y/Z, ROT_X/Y/Z, REACTION_FORCE_X/Y/Z, INTERNAL_FORCE_X/Y/Z and their absolute variants.

### COMBINE (weighted sum of up to 2500 responses)

```
DRESP
  ID_NAME  = mean_disp
  DEF_TYPE = OPER
  VARIABLE = disp_x_node1, 0.5
  VARIABLE = disp_x_node2, 0.5
  VAR_OPER = COMBINE
END_
```

### KSO (Kreisselmeier-Steinhauser for frequency)

```
DRESP
  ID_NAME  = kso_freq
  DEF_TYPE = OPER
  VARIABLE = freq_1
  VARIABLE = freq_2
  VARIABLE = freq_3
  VAR_OPER = KSO
END_
```

**Rule:** OPER responses can only combine DRESPs that refer to the same group and same load cases.

---

## LC_SET Syntax Detail

```
LC_SET = <approach>, <loadcase>, <substep>, <shell_layer>
```

| Parameter | Options | Default |
|-----------|---------|---------|
| `approach` | ALL, STATIC, MODAL, NONLINEAR, DAMAGE | ALL |
| `loadcase` | ALL, or specific number (1, 2, ...) | ALL |
| `substep` | ALL, or specific number | ALL |
| `shell_layer` | TOP, MID, BOT, MAX, MIN | (not applicable for solids) |

**Multi-file load case numbering:**
- File 1: load cases 1, 2, 3, ...
- File 2: load cases 10001, 10002, 10003, ...
- File 3: load cases 20001, 20002, 20003, ...

**Multiple LC_SET entries** can be specified to select specific load cases:
```
DRESP
  ID_NAME    = DRESP_STRESS_LC1_LC3
  DEF_TYPE   = SYSTEM
  TYPE       = SIG_SENS_MISES
  EL_GROUP   = DESIGN_ELEMENTS
  LC_SET     = STATIC, 1, ALL
  LC_SET     = STATIC, 3, ALL
END_
```

**Abaqus note:** For Abaqus users, "substep" means increment in nonlinear analysis. Only the last increment is used; user-defined substep values are ignored for nonlinear. "Substep" does NOT mean load case number within an Abaqus step that has multiple load cases.

---

## Quick Selection Guide

| Goal | DRESP TYPE | OBJ or CONSTRAINT |
|------|-----------|-------------------|
| Maximize stiffness | STRAIN_ENERGY, SUM | OBJ_FUNC, TARGET=MIN |
| Limit volume to X% | VOLUME, SUM | CONSTRAINT, MAGNITUDE=REL, LE_VALUE=X |
| Limit stress | SIG_SENS_MISES | CONSTRAINT, MAGNITUDE=ABS, LE_VALUE=sigma |
| Minimize weight | VOLUME or WEIGHT, SUM | OBJ_FUNC, TARGET=MIN |
| Limit displacement | DISP_X_ABS (etc.) | CONSTRAINT, MAGNITUDE=ABS, LE_VALUE=delta |
| Target frequency | DYN_FREQ | CONSTRAINT, MAGNITUDE=ABS, GE_VALUE=f |
| Minimize stress | SIG_SENS_MISES | OBJ_FUNC, TARGET=MIN |
