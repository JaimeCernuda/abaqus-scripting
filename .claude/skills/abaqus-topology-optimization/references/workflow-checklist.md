# Topology Optimization Workflow Checklist

Two workflow paths available:
- **Path A: CAE API** — TopologyTask + ObjectiveFunction (4-tuple!) + OptimizationProcess + `optimizationProcesses[name].Job()` for Abaqus built-in optimization
- **Path B: Tosca CLI** — CAE builds model, `noPartsInputFile=ON` + `writeInput()` generates flat .inp, hand-written .par, `tosca optimize` runs it

**CRITICAL (Path A):** The Job must be created via `mdb.optimizationProcesses[name].Job()`, NOT `mdb.Job()`. Using `mdb.Job()` causes C++ registration failures.

## Pre-Flight Checks

- [ ] Full Abaqus license with Tosca module available (not Learning Edition)
- [ ] `tosca optimize --help` runs without error
- [ ] Objective and constraints decided (min volume + stress limit, OR min compliance + volume limit)
- [ ] Frozen regions identified (all BC/load attachment areas)
- [ ] Element type chosen: **C3D10** for stress-constrained, **C3D8R** for compliance

## Phase 1: Build FE Model in CAE

### Geometry
- [ ] Design space envelope created (bounding volume)
- [ ] Pin/bolt holes cut if needed
- [ ] **Frozen regions partitioned** via `DatumPlaneByPrincipalPlane` + `PartitionCellByDatumPlane`
- [ ] Each frozen block is a separate cell (enables set creation)

### Sets (on Part, not Instance)
- [ ] `AllCells` set covering entire part
- [ ] Frozen region sets created using `getByBoundingBox()` on partitioned cells
- [ ] Set names are short, no spaces (they map directly to .par GROUP references)

### Material
- [ ] Elastic properties defined (Young's modulus, Poisson's ratio)
- [ ] **Density defined** (required for VOLUME design response)
- [ ] Section created and assigned to `AllCells`

### Mesh
- [ ] Mesh controls set: `TET` + `FREE` for tet meshing, or `HEX` + `STRUCTURED` for hex
- [ ] Element type explicitly set (C3D10 or C3D8R -- do NOT rely on defaults)
- [ ] For C3D10: need 3 element types `(C3D20R, C3D15, C3D10)` -- position 3 is the tet type
- [ ] Seed size appropriate (2-5mm typical for TO)
- [ ] Mesh generated, node/element count reasonable

### Assembly + Step
- [ ] Instance created with `dependent=ON`
- [ ] `StaticStep` created with appropriate parameters
- [ ] Field output includes `S`, `U`, `RF`, `ENER`

### BCs and Loads (via RP coupling)
- [ ] Reference points created at load application centers
- [ ] RP sets created (e.g., `UpperRP`, `LowerLeftRP`)
- [ ] Surfaces created on pin hole faces via `getByBoundingCylinder`
- [ ] `KINEMATIC` coupling connects RP to surface
- [ ] BCs applied to RP sets (not directly to faces)
- [ ] Loads applied to RP sets (not directly to faces)

### Generate Flat .inp
- [ ] `noPartsInputFile=ON` set: `mdb.models[model_name].setValues(noPartsInputFile=ON)`
- [ ] `Job` created: `mdb.Job(name=..., model=..., numCpus=N, numDomains=N)` (for .inp generation only)
- [ ] `job.writeInput()` called successfully
- [ ] `.inp` file exists and has reasonable size
- [ ] Verify: no `*Part`/`*Instance`/`*Assembly` keywords in the `.inp` (flat format)

## Phase 2 (Path B only): Prepare for Tosca CLI

If using the Tosca CLI path, the flat `.inp` from `noPartsInputFile=ON` is ready to use directly. No manual flattening or RP node renumbering is needed.

## Phase 2b (Path A only): CAE API Optimization Setup

- [ ] `TopologyTask` created with design space region
- [ ] `DesignResponse` objects created (VOLUME, STRAIN_ENERGY, etc.)
- [ ] `ObjectiveFunction` created with **4-tuple** objectives format: `(OFF, 'DR_Name', 1.0, 0.0)`
- [ ] `TopologyVolumeConstraint` or other constraints created
- [ ] `OptimizationProcess` created with `maxDesignCycle`, `odbMergeFrequency`, `dataSaveFrequency`
- [ ] **Job created via `mdb.optimizationProcesses[name].Job()`** (NOT `mdb.Job()`)
- [ ] `mdb.optimizationProcesses[name].submit()` called
- [ ] Post-processing: `mdb.CombineOptResults(optResultLocation=..., includeResultsFrom=LAST, optIter=LAST, models=ALL, steps=(...), analysisFieldVariables=('S', 'U'))`
- [ ] Open merged ODB: `session.openOdb(name='<process>/TOSCA_POST/<job>_post.odb')`

## Phase 3 (Path B only): Generate .par File

- [ ] `OPTIONS` block with `DRESP_GROUP_OPER_AGGREGATION = ON`
- [ ] `FEM_INPUT.FILE` points to the **flattened** `.inp` (not the original)
- [ ] `DV_TOPO.EL_GROUP = ALL_ELEMENTS`
- [ ] Frozen groups defined via `GROUP_DEF` (LIST_GROUP of element set names)
- [ ] `DVCON_TOPO` references frozen group with `CHECK_TYPE = FROZEN`
- [ ] Design responses defined:
  - For compliance: `STRAIN_ENERGY` (SUM, with `LC_SET`) + `VOLUME` (SUM)
  - For stress: `SIG_SENS_MISES` + `VOLUME` (SUM)
- [ ] Objective function set (`TARGET = MIN`)
- [ ] **Volume constraint ALWAYS present** (even when minimizing volume):
  - Compliance: `MAGNITUDE = REL`, `LE_VALUE = 0.3` (30%)
  - Stress: `MAGNITUDE = REL`, `LE_VALUE = 0.5` (upper bound to prevent full removal)
- [ ] Stress constraint (if applicable): `MAGNITUDE = ABS`, `LE_VALUE = 800.0` (MPa)
- [ ] `OPTIMIZE` block ties DV + OBJ_FUNC + DVCON + CONSTRAINT + `STRATEGY = TOPO_SENSITIVITY`
- [ ] `OPT_PARAM` with full production settings: `AUTO_FROZEN`, `DENSITY_*`, `MAT_*`, `STOP_CRITERION_*`, `SUM_Q_FACTOR`
- [ ] `STOP.ITER_MAX` set (20-75 depending on complexity)
- [ ] `SMOOTH` block configured for STL export (`ISO_VALUE = 0.3-0.51`)

## Phase 4: Run Tosca CLI

- [ ] Command: `tosca optimize -j <job> -p <par_file> -s abaqus -scpus <N>`
- [ ] Tosca starts and reports reading .inp successfully
- [ ] FEA solver (Abaqus) runs on first cycle
- [ ] Objective value decreasing across iterations
- [ ] Tosca exits with code 0

## Phase 5: Post-Process

- [ ] Output directory `<job>/` created with cycle results
- [ ] `SAVE.inp/<last_cycle>/` contains final `.inp` + `tosca_distribution.inp`
- [ ] (Optional) Run FEA on last-cycle `.inp` for stress visualization: `abaqus job=Optimized input=<last_cycle>.inp cpus=N interactive`
- [ ] ODB created for visualization
- [ ] STL file exported (from `SMOOTH` block)
- [ ] Final design has intact load paths, no disconnected regions

## Common Volume Fraction Targets

| Volume Fraction | Result | Use Case |
|-----------------|--------|----------|
| 20-30% | Aggressive lightweighting | Aerospace, weight-critical |
| 30-40% | Balanced | General structural |
| 40-50% | Conservative | Safety-critical, fatigue |

## Common Stress Limits

| Material | Yield (MPa) | Typical Limit (MPa) | Safety Factor |
|----------|-------------|---------------------|---------------|
| Steel | 250 | 150-200 | 1.25-1.67 |
| Aluminum 6061 | 276 | 170-220 | 1.25-1.6 |
| IN718 | 1034 | 700-900 | 1.15-1.5 |
| Ti-6Al-4V | 880 | 550-700 | 1.25-1.6 |
