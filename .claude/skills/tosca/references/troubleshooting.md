# Tosca .par File Troubleshooting

Diagnosis and fixes for common Tosca optimization failures, organized by symptom.

---

## ⚠ CRITICAL: Missing Volume Constraint Causes Full Material Removal

**A volume constraint is ALWAYS required — even when the objective is to minimize volume.**

Without a volume upper bound (e.g., `LE_VALUE = 0.5`), the optimizer can remove all material in a single design cycle because there is no limit on how fast densities can decrease globally. The volume constraint acts as a "speed limit" on material removal per cycle.

**Symptoms of a missing volume constraint:**
- Volume drops to near-zero in the first 1-3 cycles
- Final design is empty or has only frozen regions
- Optimization terminates quickly with "converged" but trivial result

**Fix:** Always include a volume constraint, even for min-volume problems:
```
CONSTRAINT
  ID_NAME   = vol_constraint
  DRESP     = DRESP_VOLUME
  MAGNITUDE = REL
  LE_VALUE  = 0.5          ! Adjust based on expected final volume fraction
END_
```

And reference it in the OPTIMIZE block:
```
OPTIMIZE
  ...
  CONSTRAINT = vol_constraint
  CONSTRAINT = stress_constraint    ! or other constraints
  ...
END_
```

---

## 1. TOSCA.OUT Error Parsing

The primary diagnostic file is `TOSCA.OUT` in the working directory. Always read this file first when an optimization fails.

### How to read TOSCA.OUT

```bash
# Look for errors
grep -i "error" TOSCA.OUT

# Look for warnings
grep -i "warning" TOSCA.OUT

# Check iteration progress
grep "Iteration" TOSCA.OUT

# Check objective/constraint values
grep -i "objective\|constraint" TOSCA.OUT
```

### Common TOSCA.OUT messages

| Message | Cause | Fix |
|---------|-------|-----|
| `ERROR: Element group ... not found` | GROUP_DEF or EL_GROUP name does not match any set in the .inp | Check spelling and case of element set names; Tosca reads Abaqus `*ELSET` definitions |
| `ERROR: Node group ... not found` | ND_GROUP name does not match any node set | Check Abaqus `*NSET` definitions |
| `ERROR: Unknown type ...` | Invalid DRESP TYPE | Check spelling against the allowed types list |
| `ERROR: ... not referenced` | A DRESP, DV, or DVCON is defined but not used in OPTIMIZE | Either reference it in OPTIMIZE or remove the definition |
| `ERROR: Multiple definitions` | Two blocks share the same ID_NAME | All ID_NAMEs must be unique across the entire .par file |
| `ERROR: Missing END_` | A block is not properly terminated | Add `END_` on its own line after the block |
| `WARNING: Element type ... not supported` | Design space contains unsupported element types | Use hex8, hex20, tet10, pent6, or pent15. Remove tet4 if stress-constrained |
| `Optimization converged` | Success -- optimization found a stable solution | Check objective value and constraint satisfaction |
| `Maximum iterations reached` | Stopped at ITER_MAX without convergence | Increase ITER_MAX, or check if constraints are too tight |
| `Constraint violated` | A constraint is not satisfied at termination | Relax the constraint value or increase iterations |

---

## 2. DB_ERROR Directory

**Symptom:** A `DB_ERROR` directory appears in the working directory.

**What it means:** Tosca detected an inconsistency in its internal database. This typically happens when:
1. A previous run was interrupted mid-iteration
2. Files from a previous run conflict with the current run
3. The .inp file was modified between iterations of a resumed run

**Fix:**
```bash
# Clean up and start fresh
rm -rf DB_ERROR/
rm -f TP_*.onf
rm -f *.odb *.dat *.msg *.sta *.com *.prt *.sim *.log
rm -f opt_res_database*
# Then re-run the optimization
```

**Prevention:** Always clean the working directory before starting a new optimization. Do not modify the .inp file between runs unless starting completely fresh.

---

## 3. Stress Singularities

**Symptom:** Stress constraint is never satisfied; stress values shoot to infinity; optimization oscillates wildly.

**Cause:** Elements at loaded nodes or boundary condition nodes have artificial stress concentrations (singularities). These are not physical -- they are artifacts of point loads and point constraints.

**Fix:** Exclude loaded and constrained elements from the stress DRESP evaluation group:

```
! Create a group that excludes BC and load regions
GROUP_DEF
  ID_NAME = STRESS_EVAL_ELEMENTS
  TYPE    = ELEM
  FORMAT  = LIST_SUBTRACT_GROUP
  LIST_BEGIN
  ALL_ELEMENTS, LoadedElements, BCElements
END_

DRESP
  ID_NAME  = DRESP_STRESS
  DEF_TYPE = SYSTEM
  TYPE     = SIG_SENS_MISES
  EL_GROUP = STRESS_EVAL_ELEMENTS     ! NOT ALL_ELEMENTS
END_
```

**Alternative:** Use `AUTO_FROZEN = ALL` in OPT_PARAM to automatically freeze loaded/BC elements:
```
OPT_PARAM
  ...
  AUTO_FROZEN = ALL
  ...
END_
```

**Tip:** The frozen regions (near BCs and loads) are where singularities live. By freezing them, they stay at density=1.0 and their stress is well-defined but excluded from optimization sensitivity.

---

## 4. Convergence Issues

### Oscillating objective function (bounces up and down)

**Cause:** Move limit too large; optimizer overshoots each iteration.

**Fix:**
```
OPT_PARAM
  ...
  DENSITY_MOVE   = 0.10        ! Reduce from default 0.25
  DENSITY_UPDATE = CONSERVATIVE ! More cautious updates
  ...
END_
```

### Slow convergence (many iterations, small changes)

**Cause:** Move limit too small, or filter radius too large.

**Fix:**
```
OPT_PARAM
  ...
  DENSITY_MOVE       = 0.30        ! Increase for faster convergence
  DENSITY_UPDATE     = AGGRESSIVE  ! More aggressive updates
  TOPO_FILTER_RADIUS = 2.0        ! Smaller radius = more freedom
  ...
END_
```

### Ill-posed problem (min-volume without sufficient constraints)

**Symptom:** Volume collapses to near-zero; disconnected floating elements.

**Cause:** When minimizing volume, the problem is mathematically ill-posed without a lower bound on some structural response.

**Fix:**
```
OPT_PARAM
  ...
  STABILIZATION = YES    ! Helps with min-volume problems
  ...
END_
```

Or add a displacement or compliance constraint to prevent the structure from becoming trivially empty.

### Too many intermediate densities (gray elements)

**Symptom:** Final result has many elements at 0.3-0.7 density instead of clear solid/void.

**Fixes (in order of preference):**
1. Increase penalty factor:
   ```
   MAT_PENALTY = 4.0     ! Higher penalizes intermediate densities more
   ```
2. Enable post-convergence cleanup:
   ```
   SOLID_VOID_POST_STRATEGY = DENSITY_MEASURE
   ```
3. Increase filter radius (promotes larger, clearer members)
4. Run more iterations

---

## 5. Line Length > 160 Characters (Silent Parse Failure)

**Symptom:** Optimization runs but uses wrong parameter values, or a block appears to be ignored.

**Cause:** Tosca silently truncates lines longer than 160 characters. Any parameter value after the 160th character is lost. This is especially dangerous with:
- Long file paths in FEM_INPUT
- Long GROUP_DEF LIST entries
- Long comments on the same line as a parameter

**Fix:** Break long lines. For GROUP_DEF lists, put entries on separate lines:
```
! BAD: This line might exceed 160 chars
GROUP_DEF
  ID_NAME = ALL_FROZEN
  TYPE    = ELEM
  FORMAT  = LIST_GROUP
LIST_BEGIN
FrozenUpperSurface, FrozenLowerLeftCorner, FrozenLowerRightCorner, FrozenMiddleSection, FrozenBottomPlate
END_

! GOOD: Split across lines
GROUP_DEF
  ID_NAME = ALL_FROZEN
  TYPE    = ELEM
  FORMAT  = LIST_GROUP
LIST_BEGIN
FrozenUpperSurface, FrozenLowerLeftCorner,
FrozenLowerRightCorner, FrozenMiddleSection,
FrozenBottomPlate
END_
```

**Prevention:** Check line lengths before running:
```bash
awk 'length > 160 {print NR": "length" chars: "$0}' model.par
```

---

## 6. GROUP_DEF Referencing Non-Existent Elements

**Symptom:** `ERROR: Element group ... not found` or `WARNING: ... elements removed from group`.

**Common causes:**
1. Element set name in .par does not match the Abaqus .inp `*ELSET` name (case-sensitive)
2. The .inp file was re-meshed, changing element numbering
3. GROUP_DEF uses LIST format with element IDs that do not exist in the model

**Diagnosis:**
```bash
# Check what element sets exist in the .inp
grep -i "ELSET" model.inp

# Check what node sets exist
grep -i "NSET" model.inp
```

**Fix:** Ensure exact name match between .par EL_GROUP references and .inp `*ELSET` names. Tosca reads Abaqus set definitions directly -- you only need GROUP_DEF for custom grouping (combining, subtracting, or listing specific IDs).

---

## 7. File Naming Conflicts (TP_XXX.onf)

**Symptom:** Post-processing shows wrong iteration as final result; SMOOTH output looks like an earlier iteration.

**Cause:** Tosca writes optimization results to files named `TP_001.onf`, `TP_002.onf`, etc. If leftover files from a previous run have higher numbers (e.g., `TP_080.onf`), post-processing may pick those up as the "latest" iteration.

**Fix:**
```bash
# Before starting a new optimization, clean up ONF files
rm -f TP_*.onf
```

**If using INITIAL_DV_FIELD:** Rename the ONF file to something that will not conflict:
```
DV_TOPO
  ID_NAME          = design_variables
  EL_GROUP         = ALL_ELEMENTS
  INITIAL_DV_FIELD = INITIAL_MAT.onf    ! NOT TP_080.onf
END_
```

---

## 8. Material Interpolation Selection Guide (SIMP vs MIMP vs RAMP)

Choosing the wrong interpolation scheme is a common source of convergence problems.

### SIMP (Solid Isotropic Material with Penalization)

**Formula:** `E = E0 * rho^p`

| Pros | Cons |
|------|------|
| Simple, well-understood | Not ideal for frequency/dynamic |
| Fast convergence for compliance | Can struggle with stress constraints |
| Default choice | Body loads (gravity) cause issues |

**When to use:** Compliance minimization without body loads or frequency constraints.

```
OPT_PARAM
  ...
  MAT_INTERPOLATION = SIMP
  MAT_PENALTY       = 3.0
  ...
END_
```

### RAMP (Rational Approximation of Material Properties)

**Formula:** `E = E0 * rho / (1 + p*(1-rho))`

| Pros | Cons |
|------|------|
| Better for frequency/dynamic problems | Slightly slower convergence |
| Concave interpolation avoids spurious modes | Less common in literature |
| Good for modal analysis | |

**When to use:** Any problem involving eigenfrequencies or dynamic loads.

```
OPT_PARAM
  ...
  MAT_INTERPOLATION = RAMP
  MAT_PENALTY       = 3.0
  ...
END_
```

### MIMP (Mass Interpolation Material Penalization)

**Formula:** Proprietary (combination of SIMP for stiffness + custom mass interpolation)

| Pros | Cons |
|------|------|
| Best for stress-constrained optimization | Proprietary -- less literature guidance |
| Handles body loads correctly | Uses DV filter instead of sensitivity filter |
| Recommended when mass-dependent responses present | |

**When to use:** Stress-constrained problems, problems with gravity/acceleration loads, problems with frequency constraints where stress also matters.

```
OPT_PARAM
  ...
  MAT_INTERPOLATION = MIMP
  FILTER_TYPE       = DV    ! Recommended with MIMP (set automatically by AUTO)
  ...
END_
```

### PEDE (Niels-Pedersen approach)

**Formula:** Proprietary

**When to use:** Automatically selected when body loads or dynamic load cases are present. Do not manually select unless you have a specific reason.

**Caution:** PEDE can cause convergence problems with stress constraints. If stress is involved, override with MIMP:
```
OPT_PARAM
  ...
  MAT_INTERPOLATION = MIMP   ! Override auto-selected PEDE
  ...
END_
```

### Decision Tree

```
Is stress in the optimization (SIG_SENS_MISES)?
  YES -> Use MIMP
  NO  -> Are eigenfrequencies or body loads involved?
           YES -> Use RAMP
           NO  -> Use SIMP (default)
```

### Penalty Factor Guidance

| Penalty | Effect |
|---------|--------|
| 1.0 | No penalization -- thickness optimization (many gray elements) |
| 2.0 | Mild penalization -- some intermediate densities remain |
| 3.0 | Standard (recommended default) |
| 4.0 | Strong penalization -- sharper solid/void boundary |
| 5.0+ | Very strong -- high risk of local minima |

**Rule of thumb:** Start with 3.0. Only increase if the result has too many intermediate densities. Only decrease if convergence fails.

---

## 9. Filter Radius Issues

### Checkerboard patterns

**Symptom:** Alternating solid/void elements in a checkerboard pattern.

**Cause:** Filter radius too small (or zero).

**Fix:** Increase `TOPO_FILTER_RADIUS` to at least 1.5x the average element edge length:
```
OPT_PARAM
  ...
  TOPO_FILTER_RADIUS = 3.0   ! Increase until checkerboard disappears
  ...
END_
```

### All-gray result (no clear solid/void)

**Cause:** Filter radius too large relative to the design space, or penalty too low.

**Fix:** Reduce filter radius, increase penalty, or increase ITER_MAX.

### Mesh dependency

**Symptom:** Different meshes give completely different topologies.

**Cause:** No filter or filter radius not scaled with mesh.

**Fix:** Always use a filter. Set radius in absolute units based on desired minimum member size, not relative to mesh.

---

## 10. Common .par Syntax Errors

| Error | Symptom | Fix |
|-------|---------|-----|
| Missing `END_` | Next block is parsed as part of previous | Add `END_` after every block |
| `=` missing | Parameter ignored | Ensure `PARAM = value` format |
| Space in ID_NAME | Parse error | Quote names with spaces: `"My Name"` or avoid spaces |
| `!` in filename | Treated as comment | Rename files to avoid `!`, `=`, `#` |
| Trailing whitespace after `\` | Some systems treat as continuation | Avoid trailing whitespace |
| `END` instead of `END_` | Block not terminated | Always use `END_` with underscore |

---

## 11. Abaqus Job Failures During Optimization

Tosca calls Abaqus internally for each iteration. If the Abaqus job fails, the optimization stops.

### Check Abaqus output files

```bash
# Look for Abaqus errors
grep -i "error" *.dat *.msg *.sta 2>/dev/null

# Check if analysis completed
tail -5 *.sta
```

### Common Abaqus-side failures

| Issue | Fix |
|-------|-----|
| `Too many attempts` | Reduce initial time increment in .inp |
| `Element distortion` | Increase DENSITY_LOWER (e.g., 0.01 instead of 0.001) |
| `License not available` | Check license server; Tosca needs both Abaqus and Tosca tokens |
| `Negative eigenvalue` | Stabilize with `DENSITY_LOWER = 0.01` or fix BCs |
| `Memory allocation` | Add `FILE_ADD_CALL = memory="8gb"` in FEM_INPUT |

---

## 12. SMOOTH Block Issues

### No STL file generated

**Cause:** SMOOTH block not in the .par file, or optimization did not complete.

**Fix:** Ensure SMOOTH block exists with `FORMAT = stl`. SMOOTH only runs after optimization completes. To run SMOOTH separately on existing results:
```
SMOOTH
  ID_NAME  = post_smooth
  TASK     = iso
  DATABASE = opt_res_database
  DESIGN_CYCLE = LAST
  ISO_VALUE = 0.3
  FORMAT   = stl
END_
```

### STL has holes or self-intersections

**Fix:** Enable self-intersection checking and increase smoothing:
```
SMOOTH
  ...
  SELF_INTERSECTION_CHECK = ITERATIVE   ! Most thorough
  SMOOTH_CYCLES           = 15          ! More smoothing passes
  SHRINKAGE_CORRECTION    = YES         ! Compensate shrinkage
  REDUCTION_RATE          = 40          ! Less aggressive face removal
  MIN_ANGLE               = 20         ! Prevent degenerate triangles
  ...
END_
```

### STL is too rough / too smooth

- **Too rough:** Increase `SMOOTH_CYCLES` (e.g., 15-20)
- **Too smooth (lost detail):** Decrease `SMOOTH_CYCLES` (e.g., 3-5), enable `SHRINKAGE_CORRECTION = YES`

### Wrong volume in exported geometry

Use `TARGET_VOLUME` instead of `ISO_VALUE` to get a specific volume fraction:
```
SMOOTH
  ...
  TARGET_VOLUME = 0.3    ! Tosca iterates ISO_VALUE to match this volume
  ...
END_
```

---

## 13. Diagnostic Checklist

When an optimization fails, check these in order:

1. **Read TOSCA.OUT** -- search for ERROR and WARNING
2. **Check Abaqus .dat/.msg files** -- look for solver errors
3. **Verify .inp is valid** -- run Abaqus standalone first: `abaqus job=model interactive`
4. **Check element/node set names** -- grep .inp for set definitions, compare with .par
5. **Check line lengths** -- `awk 'length > 160' model.par`
6. **Clean working directory** -- remove TP_*.onf, DB_ERROR, old .odb files
7. **Start simple** -- try Pattern 1 (compliance + volume) before adding stress/frequency constraints
8. **Check license** -- `abaqus licensing lmstat` or check TOSCA.OUT for license messages
