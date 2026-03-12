# Common Tosca .par File Patterns

Ready-to-use .par templates for the five most common topology optimization setups. Each pattern is a complete, valid .par file based on working examples from this project.

---

## Pattern 1: Minimize Compliance (Maximize Stiffness) at Volume Fraction

**Use case:** "Make this part as stiff as possible while removing 70% of the material."

This is the simplest and most common topology optimization setup. Minimizing strain energy (compliance) is equivalent to maximizing structural stiffness.

**Key decisions:**
- Volume fraction 0.3 = aggressive (aerospace); 0.5 = conservative
- Filter radius controls minimum member thickness

```
! Pattern 1: Minimize compliance with volume constraint
! Objective: MIN strain energy (= MAX stiffness)
! Constraint: Volume <= 30% of original

OPTIONS
  DRESP_GROUP_OPER_AGGREGATION = ON
END_

FEM_INPUT
  ID_NAME                = FEA_MODEL
  FILE                   = model.inp
END_

DV_TOPO
  ID_NAME                = design_variables
  EL_GROUP               = ALL_ELEMENTS
END_

DVCON_TOPO
  ID_NAME                = dvcon_frozen
  EL_GROUP               = FrozenElems
  CHECK_TYPE             = FROZEN
END_

DRESP
  ID_NAME                = DRESP_STRAIN_ENERGY
  LIST                   = NO_LIST
  DEF_TYPE               = SYSTEM
  TYPE                   = STRAIN_ENERGY
  EL_GROUP               = ALL_ELEMENTS
  GROUP_OPER             = SUM
  LC_SET                 = ALL, 1, ALL
END_

DRESP
  ID_NAME                = DRESP_VOLUME
  LIST                   = NO_LIST
  DEF_TYPE               = SYSTEM
  TYPE                   = VOLUME
  EL_GROUP               = ALL_ELEMENTS
  GROUP_OPER             = SUM
END_

OBJ_FUNC
  ID_NAME                = min_SE
  DRESP                  = DRESP_STRAIN_ENERGY, 1.
  TARGET                 = MIN
END_

CONSTRAINT
  ID_NAME                = vol_constraint
  DRESP                  = DRESP_VOLUME
  MAGNITUDE              = REL
  LE_VALUE               = 0.3
END_

OPTIMIZE
  ID_NAME                = TOPOLOGY_OPT
  DV                     = design_variables
  OBJ_FUNC               = min_SE
  DVCON                  = dvcon_frozen
  CONSTRAINT             = vol_constraint
  STRATEGY               = TOPO_SENSITIVITY
END_

OPT_PARAM
  ID_NAME                = OPT_PARAMS
  OPTIMIZE               = TOPOLOGY_OPT
  AUTO_FROZEN            = BOTH
  DENSITY_UPDATE         = NORMAL
  DENSITY_LOWER          = 0.001
  DENSITY_UPPER          = 1.
  DENSITY_MOVE           = 0.25
  MAT_INTERPOLATION      = SIMP
  MAT_PENALTY            = 3.
  TOPO_FILTER_RADIUS     = 10.0
  STOP_CRITERION_LEVEL   = BOTH
  STOP_CRITERION_OBJ     = 0.001
  STOP_CRITERION_DENSITY = 0.005
  STOP_CRITERION_ITER    = 4
  SUM_Q_FACTOR           = 6.
END_

STOP
  ID_NAME                = global_stop
  ITER_MAX               = 50
END_

SMOOTH
  ID_NAME                = ISO_SMOOTHING
  TASK                   = iso
  ISO_VALUE              = 0.3
  SELF_INTERSECTION_CHECK = runtime
  SMOOTH_CYCLES          = 10
  REDUCTION_RATE         = 60
  REDUCTION_ANGLE        = 5.0
  FORMAT                 = stl
END_
```

**Adapting this pattern:**
- Change `LE_VALUE` to adjust volume fraction (0.2 to 0.5 typical)
- Change `TOPO_FILTER_RADIUS` to control minimum member size (larger = thicker members)
- For faster convergence, try `STRATEGY = TOPO_CONTROLLER` (but only with this exact objective/constraint pairing)

---

## Pattern 2: Minimize Volume with Stress Constraint

**Use case:** "Make this part as light as possible while keeping stress below the yield limit."

This is the stress-constrained formulation from experiment 10. It requires more iterations and careful parameter tuning compared to compliance-based optimization.

**Key decisions:**
- Stress limit should be well below yield (safety factor)
- MIMP interpolation recommended for stress problems
- Exclude loaded/BC nodes from stress evaluation group
- More iterations needed (75-100)

```
! Pattern 2: Minimize volume with stress constraint
! Objective: MIN volume
! Constraints: Von Mises stress <= 800 MPa, Volume <= 50% (REQUIRED lower bound)
! Based on: experiment10/results/production/Exp10_TO.par
!
! WARNING: A volume constraint is ALWAYS needed even when minimizing volume.
! Without a volume upper bound, the optimizer can remove all material in a
! single cycle. The volume constraint acts as a "speed limit" on material removal.

OPTIONS
  DRESP_GROUP_OPER_AGGREGATION = ON
END_

FEM_INPUT
  ID_NAME                = FEA_MODEL
  FILE                   = model.inp
END_

DV_TOPO
  ID_NAME                = design_variables
  EL_GROUP               = ALL_ELEMENTS
END_

! Combine frozen regions into one group
GROUP_DEF
  ID_NAME                = ALL_FROZEN
  TYPE                   = ELEM
  FORMAT                 = LIST_GROUP
LIST_BEGIN
FrozenUpper, FrozenLowerLeft, FrozenLowerRight
END_

DVCON_TOPO
  ID_NAME                = dvcon_frozen
  EL_GROUP               = ALL_FROZEN
  CHECK_TYPE             = FROZEN
END_

! Volume as objective AND as constraint (both are needed)
DRESP
  ID_NAME                = DRESP_VOLUME
  LIST                   = NO_LIST
  DEF_TYPE               = SYSTEM
  TYPE                   = VOLUME
  EL_GROUP               = ALL_ELEMENTS
  GROUP_OPER             = SUM
END_

! Stress as constraint (SIG_SENS_MISES is the ONLY valid stress type for topo)
! IMPORTANT: Exclude elements at loaded nodes and BCs to avoid singularities
DRESP
  ID_NAME                = DRESP_STRESS
  LIST                   = NO_LIST
  DEF_TYPE               = SYSTEM
  TYPE                   = SIG_SENS_MISES
  EL_GROUP               = ALL_ELEMENTS
END_

OBJ_FUNC
  ID_NAME                = min_volume
  DRESP                  = DRESP_VOLUME
  TARGET                 = MIN
END_

! Volume upper bound — prevents optimizer from removing all material at once
CONSTRAINT
  ID_NAME                = vol_constraint
  DRESP                  = DRESP_VOLUME
  MAGNITUDE              = REL
  LE_VALUE               = 0.5
END_

CONSTRAINT
  ID_NAME                = stress_constraint
  DRESP                  = DRESP_STRESS
  MAGNITUDE              = ABS
  LE_VALUE               = 800.0
END_

OPTIMIZE
  ID_NAME                = TOPOLOGY_OPT
  DV                     = design_variables
  OBJ_FUNC               = min_volume
  DVCON                  = dvcon_frozen
  CONSTRAINT             = vol_constraint
  CONSTRAINT             = stress_constraint
  STRATEGY               = TOPO_SENSITIVITY
END_

OPT_PARAM
  ID_NAME                = OPT_PARAMS
  OPTIMIZE               = TOPOLOGY_OPT
  AUTO_FROZEN            = BOTH
  DENSITY_UPDATE         = NORMAL
  DENSITY_LOWER          = 0.001
  DENSITY_UPPER          = 1.
  DENSITY_MOVE           = 0.10
  MAT_INTERPOLATION      = SIMP
  MAT_PENALTY            = 3.
  TOPO_FILTER_RADIUS     = 3.0
  STOP_CRITERION_LEVEL   = BOTH
  STOP_CRITERION_OBJ     = 0.001
  STOP_CRITERION_DENSITY = 0.005
  STOP_CRITERION_ITER    = 4
  SUM_Q_FACTOR           = 6.
  ! For stress problems, also consider:
  ! MAT_INTERPOLATION    = MIMP
  ! DENSITY_UPDATE       = CONSERVATIVE
  ! STABILIZATION        = YES
END_

STOP
  ID_NAME                = global_stop
  ITER_MAX               = 75
END_

SMOOTH
  ID_NAME                = ISO_SMOOTHING
  TASK                   = iso
  ISO_VALUE              = 0.51
  SELF_INTERSECTION_CHECK = runtime
  SMOOTH_CYCLES          = 10
  REDUCTION_RATE         = 60
  REDUCTION_ANGLE        = 5.0
  FORMAT                 = stl
END_
```

**CRITICAL: Volume constraint is required even when minimizing volume.** Without `LE_VALUE`, the optimizer can collapse the entire design to void in a single cycle. The volume constraint bounds how fast material is removed.

**Adapting this pattern:**
- Change `LE_VALUE` in `vol_constraint` to the maximum allowed volume fraction (0.3-0.5 typical)
- Change `LE_VALUE` in the stress constraint to your allowable stress
- For better stress accuracy, create a STRESS_EVAL_ELEMENTS group that excludes loaded/BC elements
- If convergence is poor, try `MAT_INTERPOLATION = MIMP` and `STABILIZATION = YES`
- Lower `DENSITY_MOVE` (e.g., 0.05) if oscillating
- Higher `ISO_VALUE` (0.5-0.6) gives cleaner stress results in the smoothed geometry

---

## Pattern 3: Multi-Load-Case Compliance Minimization

**Use case:** "The part sees three different load cases. Make it stiff for all of them."

Uses weighted compliance to handle multiple loading scenarios. Each load case gets its own DRESP. The objective minimizes the weighted sum.

**Key decisions:**
- Weight factors reflect relative importance of each load case
- All load cases must use the same element group
- Can also use MINMAX target to minimize the worst-case compliance

```
! Pattern 3: Multi-load-case compliance minimization
! Objective: MIN weighted strain energy across 3 load cases
! Constraint: Volume <= 40%

FEM_INPUT
  ID_NAME                = FEA_MODEL
  FILE                   = model.inp
END_

DV_TOPO
  ID_NAME                = design_variables
  EL_GROUP               = ALL_ELEMENTS
END_

DVCON_TOPO
  ID_NAME                = dvcon_frozen
  EL_GROUP               = FrozenElems
  CHECK_TYPE             = FROZEN
END_

! Separate DRESP for each load case
DRESP
  ID_NAME                = DRESP_SE_LC1
  DEF_TYPE               = SYSTEM
  TYPE                   = STRAIN_ENERGY
  EL_GROUP               = ALL_ELEMENTS
  GROUP_OPER             = SUM
  LC_SET                 = STATIC, 1, ALL
END_

DRESP
  ID_NAME                = DRESP_SE_LC2
  DEF_TYPE               = SYSTEM
  TYPE                   = STRAIN_ENERGY
  EL_GROUP               = ALL_ELEMENTS
  GROUP_OPER             = SUM
  LC_SET                 = STATIC, 2, ALL
END_

DRESP
  ID_NAME                = DRESP_SE_LC3
  DEF_TYPE               = SYSTEM
  TYPE                   = STRAIN_ENERGY
  EL_GROUP               = ALL_ELEMENTS
  GROUP_OPER             = SUM
  LC_SET                 = STATIC, 3, ALL
END_

DRESP
  ID_NAME                = DRESP_VOLUME
  DEF_TYPE               = SYSTEM
  TYPE                   = VOLUME
  EL_GROUP               = ALL_ELEMENTS
  GROUP_OPER             = SUM
END_

! Weighted multi-objective: all load cases in one OBJ_FUNC
! Weight factors: <dresp_name>, <weight>, <ref_value>
OBJ_FUNC
  ID_NAME                = min_weighted_SE
  DRESP                  = DRESP_SE_LC1, 1.0
  DRESP                  = DRESP_SE_LC2, 1.0
  DRESP                  = DRESP_SE_LC3, 1.0
  TARGET                 = MIN
END_

! Alternative: MINMAX to minimize worst-case compliance
! OBJ_FUNC
!   ID_NAME              = min_max_SE
!   DRESP                = DRESP_SE_LC1, 1.0, 100.0
!   DRESP                = DRESP_SE_LC2, 1.0, 100.0
!   DRESP                = DRESP_SE_LC3, 1.0, 100.0
!   TARGET               = MINMAX
! END_

CONSTRAINT
  ID_NAME                = vol_constraint
  DRESP                  = DRESP_VOLUME
  MAGNITUDE              = REL
  LE_VALUE               = 0.4
END_

OPTIMIZE
  ID_NAME                = TOPOLOGY_OPT
  DV                     = design_variables
  OBJ_FUNC               = min_weighted_SE
  DVCON                  = dvcon_frozen
  CONSTRAINT             = vol_constraint
  STRATEGY               = TOPO_SENSITIVITY
END_

OPT_PARAM
  ID_NAME                = OPT_PARAMS
  OPTIMIZE               = TOPOLOGY_OPT
  AUTO_FROZEN            = BOTH
  DENSITY_UPDATE         = NORMAL
  DENSITY_LOWER          = 0.001
  DENSITY_UPPER          = 1.
  DENSITY_MOVE           = 0.25
  MAT_INTERPOLATION      = SIMP
  MAT_PENALTY            = 3.
  TOPO_FILTER_RADIUS     = 5.0
  STOP_CRITERION_LEVEL   = BOTH
  STOP_CRITERION_OBJ     = 0.001
  STOP_CRITERION_DENSITY = 0.005
  STOP_CRITERION_ITER    = 4
  SUM_Q_FACTOR           = 6.
END_

STOP
  ID_NAME                = global_stop
  ITER_MAX               = 60
END_

SMOOTH
  ID_NAME                = ISO_SMOOTHING
  TASK                   = iso
  ISO_VALUE              = 0.3
  SELF_INTERSECTION_CHECK = runtime
  SMOOTH_CYCLES          = 10
  REDUCTION_RATE         = 60
  REDUCTION_ANGLE        = 5.0
  FORMAT                 = stl
END_
```

**Adapting this pattern:**
- Adjust weight factors to prioritize certain load cases (e.g., `DRESP_SE_LC1, 2.0` doubles its importance)
- Use `TARGET = MINMAX` with reference values for min-max formulation
- Add more `LC_SET` lines or more DRESP blocks for additional load cases
- For load cases from separate .inp files, adjust LC_SET numbering (file 2 starts at 10001)

---

## Pattern 4: Frequency-Constrained Topology Optimization

**Use case:** "Maximize stiffness, but the first natural frequency must stay above 50 Hz."

Combines compliance minimization with eigenfrequency constraints. Requires a modal analysis step in the Abaqus .inp file.

**Key decisions:**
- The .inp must include both a static step and a frequency extraction step
- RAMP interpolation is recommended for dynamic problems (avoids spurious local modes)
- Mode tracking should be enabled to prevent mode switching

```
! Pattern 4: Compliance minimization with frequency constraint
! Objective: MIN strain energy
! Constraints: Volume <= 35%, First eigenfrequency >= 50 Hz

FEM_INPUT
  ID_NAME                = FEA_MODEL
  FILE                   = model.inp
END_

DV_TOPO
  ID_NAME                = design_variables
  EL_GROUP               = ALL_ELEMENTS
END_

DVCON_TOPO
  ID_NAME                = dvcon_frozen
  EL_GROUP               = FrozenElems
  CHECK_TYPE             = FROZEN
END_

DRESP
  ID_NAME                = DRESP_STRAIN_ENERGY
  DEF_TYPE               = SYSTEM
  TYPE                   = STRAIN_ENERGY
  EL_GROUP               = ALL_ELEMENTS
  GROUP_OPER             = SUM
  LC_SET                 = STATIC, ALL, ALL
END_

DRESP
  ID_NAME                = DRESP_VOLUME
  DEF_TYPE               = SYSTEM
  TYPE                   = VOLUME
  EL_GROUP               = ALL_ELEMENTS
  GROUP_OPER             = SUM
END_

! First eigenfrequency
DRESP
  ID_NAME                = DRESP_FREQ_1
  DEF_TYPE               = SYSTEM
  TYPE                   = DYN_FREQ
  LC_SET                 = MODAL, 1, ALL
END_

OBJ_FUNC
  ID_NAME                = min_compliance
  DRESP                  = DRESP_STRAIN_ENERGY
  TARGET                 = MIN
END_

CONSTRAINT
  ID_NAME                = vol_constraint
  DRESP                  = DRESP_VOLUME
  MAGNITUDE              = REL
  LE_VALUE               = 0.35
END_

! Frequency must stay above 50 Hz
CONSTRAINT
  ID_NAME                = freq_constraint
  DRESP                  = DRESP_FREQ_1
  MAGNITUDE              = ABS
  GE_VALUE               = 50.0
END_

OPTIMIZE
  ID_NAME                = TOPOLOGY_OPT
  DV                     = design_variables
  OBJ_FUNC               = min_compliance
  DVCON                  = dvcon_frozen
  CONSTRAINT             = vol_constraint
  CONSTRAINT             = freq_constraint
  STRATEGY               = TOPO_SENSITIVITY
END_

OPT_PARAM
  ID_NAME                = OPT_PARAMS
  OPTIMIZE               = TOPOLOGY_OPT
  AUTO_FROZEN            = BOTH
  DENSITY_UPDATE         = NORMAL
  DENSITY_LOWER          = 0.001
  DENSITY_UPPER          = 1.
  DENSITY_MOVE           = 0.25
  MAT_INTERPOLATION      = RAMP
  MAT_PENALTY            = 3.
  TOPO_FILTER_RADIUS     = 5.0
  MODETRACKING           = ON
  MODENUMBERS            = 5
  STOP_CRITERION_LEVEL   = BOTH
  STOP_CRITERION_OBJ     = 0.001
  STOP_CRITERION_DENSITY = 0.005
  STOP_CRITERION_ITER    = 4
  SUM_Q_FACTOR           = 6.
END_

STOP
  ID_NAME                = global_stop
  ITER_MAX               = 60
END_

SMOOTH
  ID_NAME                = ISO_SMOOTHING
  TASK                   = iso
  ISO_VALUE              = 0.3
  SELF_INTERSECTION_CHECK = runtime
  SMOOTH_CYCLES          = 10
  REDUCTION_RATE         = 60
  REDUCTION_ANGLE        = 5.0
  FORMAT                 = stl
END_
```

**Adapting this pattern:**
- Change `GE_VALUE` to your target minimum frequency
- Add more frequency constraints by defining additional DRESP_FREQ blocks and CONSTRAINT blocks
- For maximize-frequency objective, swap: make DYN_FREQ the OBJ_FUNC (TARGET=MAX) and STRAIN_ENERGY a constraint
- Increase `MODENUMBERS` if higher modes interact

---

## Pattern 5: Manufacturing Constraints (Min Member Size, Symmetry, Frozen Regions)

**Use case:** "Optimize the part, but it must be castable with 5mm minimum thickness and symmetric about the XZ plane."

Demonstrates multiple DVCON_TOPO blocks for practical manufacturing requirements.

**Key decisions:**
- MIN_MEMBER thickness should be >= 2x element edge length
- Cast direction must be a single pull direction
- Symmetry requires a LINK_TOPO definition

```
! Pattern 5: Compliance minimization with manufacturing constraints
! Objective: MIN strain energy
! Constraint: Volume <= 30%
! Manufacturing: Min member 5mm, casting in Z, symmetry about XZ plane

FEM_INPUT
  ID_NAME                = FEA_MODEL
  FILE                   = model.inp
  ADD_FILE               = symmetry_nodes.inp
END_

DV_TOPO
  ID_NAME                = design_variables
  EL_GROUP               = ALL_ELEMENTS
END_

! Frozen region: areas near BCs and loads that must remain solid
DVCON_TOPO
  ID_NAME                = dvcon_frozen
  EL_GROUP               = FrozenElems
  CHECK_TYPE             = FROZEN
END_

! Minimum member size: no structural member thinner than 5mm
DVCON_TOPO
  ID_NAME                = dvcon_min_member
  EL_GROUP               = ALL_ELEMENTS
  CHECK_TYPE             = MIN_MEMBER
  THICKNESS              = 5.0
END_

! Casting constraint: part can be demolded in Z direction
DVCON_TOPO
  ID_NAME                = dvcon_cast
  EL_GROUP               = ALL_ELEMENTS
  CHECK_TYPE             = CAST
  PULL_DIR               = 0., 0., 1.
  MID_PLANE              = AUTO
  CHECK_GROUP            = ALL_ELEMENTS
END_

! Symmetry: link elements across XZ plane
! Requires LINK_TOPO definition:
LINK_TOPO
  ID_NAME                = sym_xz
  TYPE                   = MIRROR
  PLANE                  = XZ
END_

DVCON_TOPO
  ID_NAME                = dvcon_symmetry
  EL_GROUP               = ALL_ELEMENTS
  CHECK_TYPE             = LINK_TOPO
  CHECK_LINK             = sym_xz
END_

DRESP
  ID_NAME                = DRESP_STRAIN_ENERGY
  DEF_TYPE               = SYSTEM
  TYPE                   = STRAIN_ENERGY
  EL_GROUP               = ALL_ELEMENTS
  GROUP_OPER             = SUM
END_

DRESP
  ID_NAME                = DRESP_VOLUME
  DEF_TYPE               = SYSTEM
  TYPE                   = VOLUME
  EL_GROUP               = ALL_ELEMENTS
  GROUP_OPER             = SUM
END_

OBJ_FUNC
  ID_NAME                = min_compliance
  DRESP                  = DRESP_STRAIN_ENERGY
  TARGET                 = MIN
END_

CONSTRAINT
  ID_NAME                = vol_constraint
  DRESP                  = DRESP_VOLUME
  MAGNITUDE              = REL
  LE_VALUE               = 0.3
END_

OPTIMIZE
  ID_NAME                = TOPOLOGY_OPT
  DV                     = design_variables
  OBJ_FUNC               = min_compliance
  DVCON                  = dvcon_frozen
  DVCON                  = dvcon_min_member
  DVCON                  = dvcon_cast
  DVCON                  = dvcon_symmetry
  CONSTRAINT             = vol_constraint
  STRATEGY               = TOPO_SENSITIVITY
END_

OPT_PARAM
  ID_NAME                = OPT_PARAMS
  OPTIMIZE               = TOPOLOGY_OPT
  AUTO_FROZEN            = BOTH
  DENSITY_UPDATE         = NORMAL
  DENSITY_LOWER          = 0.001
  DENSITY_UPPER          = 1.
  DENSITY_MOVE           = 0.25
  MAT_INTERPOLATION      = SIMP
  MAT_PENALTY            = 3.
  TOPO_FILTER_RADIUS     = 5.0
  STOP_CRITERION_LEVEL   = BOTH
  STOP_CRITERION_OBJ     = 0.001
  STOP_CRITERION_DENSITY = 0.005
  STOP_CRITERION_ITER    = 4
  SUM_Q_FACTOR           = 6.
END_

STOP
  ID_NAME                = global_stop
  ITER_MAX               = 60
END_

SMOOTH
  ID_NAME                = ISO_SMOOTHING
  TASK                   = iso
  ISO_VALUE              = 0.3
  SELF_INTERSECTION_CHECK = runtime
  SMOOTH_CYCLES          = 10
  REDUCTION_RATE         = 60
  REDUCTION_ANGLE        = 5.0
  FORMAT                 = stl
  FORMAT                 = inp
END_
```

**DVCON_TOPO options summary:**

| CHECK_TYPE | Purpose | Key params |
|------------|---------|------------|
| `FROZEN` | Keep elements solid | None extra |
| `MIN_MEMBER` | Minimum thickness | `THICKNESS` |
| `MAX_MEMBER` | Maximum thickness | `THICKNESS`, `DISTANCE`, `MIN_THICKNESS` |
| `CAST` | Mold pull direction | `PULL_DIR`, `MID_PLANE`, `CHECK_GROUP` |
| `MILLING` | Milling access | `MILLING_DIR` (repeatable for multiple directions) |
| `OVERHANG` | Additive manufacturing | `PRINT_DIR`, `ANGLE` (default 45 degrees) |
| `LINK_TOPO` | Symmetry/pattern | `CHECK_LINK` (references LINK_TOPO block) |

**Adapting this pattern:**
- For additive manufacturing, replace CAST with OVERHANG: `CHECK_TYPE = OVERHANG`, `PRINT_DIR = 0.,1.,0.`, `ANGLE = 45`
- For milling, use: `CHECK_TYPE = MILLING`, `MILLING_DIR = 1.,0.,0.`, `MILLING_DIR = 0.,1.,0.` (multiple directions allowed)
- Multiple DVCON blocks can be combined; order matters (later entries can modify earlier ones)
- Use `AUTO_FROZEN = ALL` in OPT_PARAM to automatically freeze BC/load elements instead of manual DVCON_TOPO FROZEN

---

## Pattern Selection Guide

| Scenario | Pattern | Objective | Constraint(s) |
|----------|---------|-----------|----------------|
| "Make it stiff at target weight" | 1 | MIN compliance | Volume <= X% |
| "Make it light within stress limit" | 2 | MIN volume | Stress <= sigma |
| "Stiff for multiple loads" | 3 | MIN weighted compliance | Volume <= X% |
| "Stiff but avoid resonance" | 4 | MIN compliance | Volume + frequency |
| "Castable / printable / symmetric" | 5 | MIN compliance | Volume + manufacturing |

**Combining patterns:** Patterns can be combined freely. For example, stress constraint (Pattern 2) + manufacturing constraints (Pattern 5) + multi-load-case (Pattern 3) by including the relevant DRESP, CONSTRAINT, and DVCON blocks from each pattern.
