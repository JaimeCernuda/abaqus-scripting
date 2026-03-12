# Topology Optimization Troubleshooting

Issues discovered through experiments 7-10 with Abaqus 2025 and Tosca.

## Common Mistake #1: Wrong ObjectiveFunction Tuple Format (5-tuple vs 4-tuple)

### OptimizationProcess.submit() Segfaults

**Symptom:** Abaqus crashes with a segfault when calling `opt.submit()`, or `KeyError` when calling `writeParAndInputFiles()`.

**Root cause:** The `ObjectiveFunction.objectives` parameter was passed a **5-tuple** instead of the correct **4-tuple**. The trailing element (typically an empty string `''`) corrupts internal C++ state, causing segfaults or KeyErrors on subsequent API calls.

```python
# WRONG — 5-tuple corrupts C++ state:
objectives=((OFF, 'DR_StrainEnergy', 1.0, 0.0, ''),)  # 5 elements!

# CORRECT — 4-tuple:
objectives=((OFF, 'DR_StrainEnergy', 1.0, 0.0),)  # 4 elements
```

The 4 members of `OptimizationObjective` are:
1. `suppress` (Boolean) — OFF to include, ON to suppress
2. `designResponse` (String) — name of the DesignResponse
3. `weight` (Float) — weighting factor
4. `referenceValue` (Float) — reference value for normalization

**Solution:** Ensure all `objectives` tuples have exactly 4 elements. If you see segfaults or KeyErrors from `OptimizationProcess`, check the tuple format first.

### writeParAndInputFiles() KeyError

**Symptom:** `KeyError: 'JobName'` when calling `optProcess.writeParAndInputFiles()`.

**Root cause:** This is typically a downstream consequence of corrupted C++ state from a wrong tuple format in `ObjectiveFunction`. The prototype job reference becomes invalid.

**Solution:** Fix the `ObjectiveFunction.objectives` tuple format (must be 4-tuple). If using the Tosca CLI path, write the `.par` file manually instead.

## Common Mistake #2: Hierarchical .inp Incompatible with Tosca

### Tosca Cannot Read CAE-Generated .inp

**Symptom:** Tosca reports errors reading the `.inp` file, cannot find element sets, or crashes during input parsing.

**Root cause:** By default, `Job.writeInput()` generates hierarchical `.inp` with `*Part`/`*Instance`/`*Assembly` wrappers. Tosca expects a flat `.inp` without this hierarchy.

**Solution (preferred):** Set `noPartsInputFile=ON` before calling `writeInput()`:

```python
mdb.models['Model-1'].setValues(noPartsInputFile=ON)
mdb.jobs[job_name].writeInput()
```

This produces a flat `.inp` directly — no manual flattening needed.

**Solution (alternative):** Tosca can auto-flatten hierarchical `.inp` during its data check, but set names will be prefixed with `<assembly>_<instance>_`.

**Solution (legacy):** Manually flatten the `.inp` by removing wrapper keywords, stripping `instance=` qualifiers, and renumbering RP nodes. See Pattern 3 in `common-patterns.md`.

### Assembly-Level Sets Not Found

**Symptom:** Tosca reports that element set names referenced in .par are not found in the .inp.

**Root cause:** In the hierarchical format, sets defined at assembly level have `instance=` qualifiers. After stripping wrappers, the `instance=` must also be removed or the set becomes orphaned.

**Solution:** Use regex to strip `instance=<name>` from all `*Nset`, `*Elset`, `*Surface` keyword lines:
```python
line = re.sub(r',\s*instance=' + re.escape(instance_name), '', line,
              flags=re.IGNORECASE)
```

## RP Node ID Collision

### Reference Point Nodes Collide with Mesh Nodes

**Symptom:** Tosca or Abaqus FEA produces nonsensical results, or nodes appear at wrong coordinates. The flat .inp has duplicate node IDs.

**Root cause:** In the hierarchical `.inp`, assembly-level reference point nodes are numbered 1, 2, 3 (independent namespace from part nodes). When flattened into a single file, these collide with mesh node IDs 1, 2, 3.

**Solution:** Renumber RP nodes by adding `max_mesh_node_id` as an offset:
1. Scan the `*Node` block inside `*Part` to find the maximum mesh node ID
2. Collect RP node definitions from the assembly section (after `*End Instance`)
3. Rewrite RP node IDs as `old_id + max_mesh_node_id`
4. Update all `*Nset` data lines that reference RP nodes

See Pattern 4 in `common-patterns.md` for complete code.

### How to Detect the Problem

Check if the flat `.inp` has duplicate node IDs:
```python
node_ids = set()
duplicates = set()
for line in flat_lines:
    if line.strip().startswith('*'):
        continue
    parts = line.strip().split(',')
    if len(parts) >= 4 and parts[0].strip().isdigit():
        nid = int(parts[0].strip())
        if nid in node_ids:
            duplicates.add(nid)
        node_ids.add(nid)
if duplicates:
    print("DUPLICATE NODE IDS:", duplicates)
```

## Stress Singularities at Loaded Nodes

### Artificially High Stress at Load Application Points

**Symptom:** Optimization fails to converge, or the stress constraint is always violated. Peak stress is at load application point, not in the design space.

**Root cause:** Concentrated forces applied directly to nodes/faces create stress singularities (stress -> infinity as mesh refines).

**Solution:** Use RP coupling to distribute load:
1. Create a reference point at the load application center
2. Create a surface on the hole/face where load acts
3. Use `KINEMATIC` coupling to connect RP to surface
4. Apply load to the RP, not to the surface directly

This distributes the load across many nodes, eliminating the singularity. See Pattern 2 in `common-patterns.md`.

### Stress Still Too High at Coupled Surface

Even with RP coupling, stress concentrations at pin holes can be high. Options:
- **Exclude loaded region from stress response:** Create a `GROUP_DEF` that excludes frozen elements, use that group for the stress DRESP
- **Increase pin hole fillet radius** in the geometry
- **Relax stress limit** to account for local stress concentration

## Element Type Issues

### C3D4 Shear Locking (Linear Tet)

**Symptom:** Stress values are unreliable, optimization produces odd shapes, or displacement is too stiff compared to analytical solutions.

**Root cause:** C3D4 (4-node linear tetrahedron) is overly stiff due to shear locking. It needs many more elements than quadratic tets for the same accuracy.

**Solution:** Use **C3D10** (10-node quadratic tetrahedron) for stress-constrained optimization:
```python
part.setMeshControls(regions=part.cells, elemShape=TET, technique=FREE)
elemType_hex = mesh.ElemType(elemCode=C3D20R, elemLibrary=STANDARD)
elemType_wedge = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
elemType_tet = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,),
                    elemTypes=(elemType_hex, elemType_wedge, elemType_tet))
```

**Note:** `setElementType` requires 3 types for 3D regions: (hex, wedge, tet). Position 3 is what gets used with TET/FREE meshing.

### C3D8R for Compliance Only

C3D8R (8-node reduced-integration hex) is efficient for compliance optimization where stress accuracy is not needed. Do NOT use it for stress-constrained optimization.

## Filter Radius Selection

### Checkerboard Pattern

**Symptom:** Alternating solid/void elements in a checkerboard-like pattern.

**Root cause:** Filter radius too small. The filter smooths density gradients; without sufficient radius, element-level oscillations persist.

**Solution:** Set `TOPO_FILTER_RADIUS` to 2-3x the mesh element size:
```
OPT_PARAM
  ID_NAME                = OPT_PARAMS
  OPTIMIZE               = TOPOLOGY_OPT
  TOPO_FILTER_RADIUS     = 9.0    ! 3x mesh_size for mesh_size=3mm
END_
```

### Members Too Thick / Not Enough Detail

**Symptom:** Optimization produces overly thick members with little topological complexity.

**Root cause:** Filter radius too large. The filter prevents features smaller than ~2x the filter radius.

**Solution:** Reduce filter radius or refine the mesh:
- Minimum useful: `filter_radius = 2 * mesh_size`
- For more detail: reduce mesh size AND filter radius proportionally

## Convergence Issues

### Stress-Constrained Optimization Not Converging

**Symptom:** Objective oscillates, stress constraint is never satisfied, or iteration limit reached without convergence.

**Root cause:** Stress-constrained optimization is inherently harder than compliance. The stress field is non-smooth and changes dramatically with topology.

**Solutions:**
1. **Increase `ITER_MAX`** to 50-75 (stress needs more iterations than compliance)
2. **Relax stress limit** by 10-20% initially, then tighten
3. **Use finer mesh** (stress accuracy depends on mesh quality)
4. **Check for singularities** at loaded/constrained nodes

### Disconnected Regions in Result

**Symptom:** Floating islands of material not connected to any load path.

**Solutions:**
1. Increase volume fraction (allow more material)
2. Add more frozen regions along expected load paths
3. Increase filter radius (forces thicker, more connected members)
4. Check that all loads and BCs are properly connected

### Objective Not Decreasing

**Symptom:** The objective value stays flat or increases across iterations.

**Solutions:**
1. Check that design variables cover the right element group
2. Verify frozen regions are not too large (leaving too little design freedom)
3. Check .par syntax -- ensure DRESP, OBJ_FUNC, and CONSTRAINT are properly linked
4. Try running with fewer constraints first to verify the optimization loop works

## Tosca CLI Issues

### "tosca: command not found"

**Solution:** Try these alternatives in order:
1. `tosca optimize ...` (if Tosca is on PATH)
2. `abaqus tosca optimize ...` (via Abaqus launcher)
3. `abaqus optimization optimize ...` (alternate subcommand)
4. Check that Tosca is installed: look for `tosca` executable in the Abaqus installation directory

### Tosca Exits with Non-Zero Code but Produced Results

Tosca sometimes exits with code 1 even when the optimization ran partially. Check:
- Does the output directory exist (`<job_name>/`)?
- Are there `SAVE.inp/<cycle>/` directories with `.inp` files?
- Is there a `.stl` file?

If results exist, they may be usable even with a non-zero exit code.

## Learning Edition Limitation

Topology optimization requires the Tosca module, which is NOT available in the Learning Edition.

**Alternatives:**
- Use academic license with full Tosca access
- Use a university HPC cluster with Abaqus/Tosca installed
- Use third-party topology optimization tools (BESO, TopOpt, etc.)

## Mesh Guidelines for TO

| Element Size | Design Freedom | Compute Time | Use Case |
|--------------|----------------|--------------|----------|
| 1-2mm | Maximum | Very long | Final optimization |
| 2-4mm | High | Moderate | General use |
| 4-6mm | Medium | Fast | Initial exploration |

**Rule:** At least 3 elements across the expected minimum member thickness.

## Post-Processing Issues

### No ODB After Optimization

Tosca deletes per-cycle ODBs to save disk space. To get an ODB:
1. Navigate to `<tosca_job>/SAVE.inp/<last_cycle>/`
2. Run: `abaqus job=Optimized input=<flat_name>.inp cpus=N interactive`
3. The `cwd` must be the cycle directory so `*INCLUDE, input=tosca_distribution.inp` resolves

### STL Not Generated

Check that the `.par` file has a `SMOOTH` block:
```
SMOOTH
  ID_NAME                = ISO_SMOOTHING
  TASK                   = iso
  ISO_VALUE              = 0.3
  FORMAT                 = stl
END_
```

If it exists but no STL appears, the optimization may not have converged. Check the Tosca log for errors.

### Visualizing Density Distribution

The `tosca_distribution.inp` file in each cycle directory contains per-element density values as `*INITIAL CONDITIONS, TYPE=SOLUTION`. This is included via `*INCLUDE` in the cycle's `.inp` file. Running FEA on this `.inp` applies the SIMP density penalties and produces an ODB with the effective stiffness distribution.
