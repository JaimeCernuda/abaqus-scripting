# Common Topology Optimization Patterns

Patterns from experiments 7-10. Two paths available: CAE API (Abaqus built-in optimization) and Tosca CLI hybrid pipeline.

## Pattern 0: Correct CAE API Usage (Abaqus Built-In Optimization)

The CAE optimization API works correctly when `ObjectiveFunction.objectives` uses the proper **4-tuple** format.

```python
from abaqus import *
from abaqusConstants import *

model = mdb.models['Model-1']

# 1. TopologyTask — defines design space
model.TopologyTask(name='Task',
                   region=model.rootAssembly.sets['DesignSpace'])

# 2. DesignResponse — each has 4 members:
#    name, region, response type, step
model.optimizationTasks['Task'].DesignResponse(
    name='DR_Volume', region=MODEL, response=VOLUME)
model.optimizationTasks['Task'].DesignResponse(
    name='DR_StrainEnergy', region=MODEL, response=STRAIN_ENERGY)

# 3. ObjectiveFunction — objectives is a tuple of 4-tuples:
#    (suppress, designResponse, weight, referenceValue)
#
#    CORRECT:  (OFF, 'DR_StrainEnergy', 1.0, 0.0)     -- 4 elements
#    WRONG:    (OFF, 'DR_StrainEnergy', 1.0, 0.0, '')  -- 5 elements (corrupts C++ state!)
model.optimizationTasks['Task'].ObjectiveFunction(
    name='ObjFunc',
    objectives=((OFF, 'DR_StrainEnergy', 1.0, 0.0),))

# 4. GeometricRestriction (optional — volume constraint)
model.optimizationTasks['Task'].TopologyVolumeConstraint(
    name='VolConstraint',
    region=MODEL,
    fraction=0.3)

# 5. OptimizationProcess — create process, job, and submit
#    IMPORTANT: The Job must be created on the OptimizationProcess, NOT via mdb.Job()
mdb.OptimizationProcess(name='Opt-Process-1',
                         model='Model-1',
                         task='Task',
                         prototypeJob='Opt-Process-1-Job',
                         maxDesignCycle=20,
                         odbMergeFrequency=2,
                         dataSaveFrequency=OPT_DATASAVE_SPECIFY_CYCLE,
                         saveInitial=False)
mdb.optimizationProcesses['Opt-Process-1'].Job(
    name='Opt-Process-1-Job', model='Model-1',
    memory=90, memoryUnits=PERCENTAGE,
    getMemoryFromAnalysis=True,
    numCpus=1, numGPUs=0)
mdb.optimizationProcesses['Opt-Process-1'].submit()

# 6. Post-processing — merge optimization results into a single ODB
mdb.CombineOptResults(
    optResultLocation='Opt-Process-1',   # path to optimization output directory
    includeResultsFrom=LAST,
    optIter=LAST,
    models=ALL,
    steps=('LoadStep',),
    analysisFieldVariables=('S', 'U'))

# Open the merged post-processing ODB
post_odb = session.openOdb(
    name='Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb')
```

**CRITICAL: Job Creation Pattern**

The job for topology optimization **must** be created via `mdb.optimizationProcesses[name].Job()`, **NOT** via `mdb.Job()`. Using `mdb.Job()` causes C++ registration failures and segfaults because the job is not registered with the optimization process.

```python
# WRONG — causes C++ registration failures:
mdb.Job(name='Job-1', model='Model-1')
mdb.OptimizationProcess(name='OptProcess', ..., prototypeJob='Job-1')

# CORRECT — job is owned by the optimization process:
mdb.OptimizationProcess(name='Opt-Process-1', ..., prototypeJob='Opt-Process-1-Job')
mdb.optimizationProcesses['Opt-Process-1'].Job(name='Opt-Process-1-Job', model='Model-1', ...)
```

**Critical:** The 4-tuple members of `OptimizationObjective` are:
1. `suppress` (Boolean) — OFF to include, ON to suppress
2. `designResponse` (String) — name of DesignResponse
3. `weight` (Float) — weighting factor
4. `referenceValue` (Float) — reference value for normalization

Passing a 5-tuple (e.g., with a trailing empty string `''`) corrupts the internal C++ state and causes segfaults or KeyErrors on subsequent API calls.

## Pattern 0b: Generate Flat .inp with noPartsInputFile

```python
# Set model to write flat .inp (no *Part/*Instance/*Assembly hierarchy)
mdb.models['Model-1'].setValues(noPartsInputFile=ON)

# Write input file — produces flat .inp directly
mdb.Job(name=job_name, model='Model-1', numCpus=NUM_CPUS, numDomains=NUM_CPUS)
mdb.jobs[job_name].writeInput()
# Result: job_name.inp is flat, ready for Tosca without manual flattening
```

This replaces the manual .inp flattening process. Set names appear directly without `<assembly>_<instance>_` prefixes.

## Pattern 1: Frozen Region Partitioning via Datum Planes

Frozen regions (BC/load attachment areas) must be separate cells so they can be assigned to element sets. Use datum planes to partition the geometry at the boundary between frozen blocks and design space.

```python
# Partition at Y = boundary between frozen block and design space
dp = part.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=BLOCK_HEIGHT_Y)
part.PartitionCellByDatumPlane(datumPlane=part.datums[dp.id], cells=part.cells)

# If partitioning only a subset of cells (after first partition):
cells_subset = part.cells.getByBoundingBox(
    xMin=-50, yMin=-1, zMin=-1,
    xMax=50, yMax=UPPER_BOUND + 1, zMax=THICKNESS + 1)
if len(cells_subset) > 0:
    part.PartitionCellByDatumPlane(datumPlane=part.datums[dp2.id],
                                    cells=cells_subset)

# Create part-level sets from partitioned cells (MUST be on part, not instance)
upper_cells = part.cells.getByBoundingBox(
    xMin=-UB_HALF - 0.1, yMin=UB_BOTTOM - 0.1, zMin=-1,
    xMax=UB_HALF + 0.1, yMax=TOTAL_HEIGHT + 1, zMax=THICKNESS + 1)
if len(upper_cells) > 0:
    part.Set(cells=upper_cells, name='FrozenUpper')

# Repeat for each frozen region
ll_cells = part.cells.getByBoundingBox(
    xMin=LB_LEFT_XMIN - 0.1, yMin=-1, zMin=-1,
    xMax=LB_LEFT_XMAX + 0.1, yMax=BLOCK_HEIGHT_Y + 0.1, zMax=THICKNESS + 1)
if len(ll_cells) > 0:
    part.Set(cells=ll_cells, name='FrozenLowerLeft')

# AllCells set for section assignment
part.Set(cells=part.cells, name='AllCells')
```

**Key points:**
- Use `getByBoundingBox` with small tolerance (0.1mm) on partition boundaries
- Sets must be on the **part** (not instance) when using `dependent=ON`
- Set names become element set names in the `.inp` -- keep them short with no spaces

## Pattern 2: RP Coupling for Pin Loads

Reference points coupled to cylindrical hole surfaces distribute load and avoid stress singularities at loaded nodes.

```python
assembly = model.rootAssembly
instance = assembly.Instance(name=part_name + '-1', part=part, dependent=ON)

# Find faces on the pin hole using bounding cylinder
pin_faces = instance.faces.getByBoundingCylinder(
    center1=(-HALF_WIDTH - 1, PIN_Y, HALF_THICK),   # extend beyond geometry
    center2=(HALF_WIDTH + 1, PIN_Y, HALF_THICK),
    radius=PIN_RADIUS + 0.5)                          # slightly larger than hole

# Create surface, RP, and RP set
assembly.Surface(side1Faces=pin_faces, name='PinSurf')
rp = assembly.ReferencePoint(point=(CENTER_X, PIN_Y, HALF_THICK))
assembly.Set(referencePoints=(assembly.referencePoints[rp.id],), name='PinRP')

# Kinematic coupling: RP controls the surface
model.Coupling(name='PinCoupling',
               controlPoint=assembly.sets['PinRP'],
               surface=assembly.surfaces['PinSurf'],
               influenceRadius=WHOLE_SURFACE,
               couplingType=KINEMATIC,
               u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)

# Apply load to RP (not directly to faces)
model.ConcentratedForce(name='PinLoad', createStepName='LoadStep',
                        region=assembly.sets['PinRP'], cf2=20000.0)

# Apply BC to RP (for support pins)
model.DisplacementBC(name='PinBC', createStepName='Initial',
                     region=assembly.sets['PinRP'],
                     u1=UNSET, u2=0.0, u3=0.0)
```

**Key points:**
- `getByBoundingCylinder` centers should extend slightly beyond the geometry
- Radius should be `PIN_RADIUS + small_tolerance` to catch all hole faces
- `KINEMATIC` coupling is preferred (distributes load evenly)
- Apply BCs/loads to the RP set, never directly to hole faces

## Pattern 3: Job.writeInput() and .inp Generation

**Preferred approach** — use `noPartsInputFile=ON` (see Pattern 0b above) to produce a flat .inp directly. The manual flattening code below is the **legacy approach** for cases where `noPartsInputFile` is not available.

```python
# Preferred: flat .inp via noPartsInputFile=ON
# mdb.models[model_name].setValues(noPartsInputFile=ON)
# mdb.jobs[job_name].writeInput()

# Legacy: Write hierarchical .inp then flatten manually
job_name = 'MyModel_FEA'
mdb.Job(name=job_name, model=model_name, numCpus=NUM_CPUS, numDomains=NUM_CPUS)
mdb.jobs[job_name].writeInput()
inp_file = job_name + '.inp'

# Step 2: Read and parse the .inp
with open(inp_file, 'r') as f:
    inp_text = f.read()

instance_name = part_name + '-1'  # e.g., 'Block-1'
inp_lines = inp_text.split('\n')

# Step 3: Find max mesh node ID (inside *Part) and collect assembly RP nodes
max_mesh_node = 0
rp_nodes = {}       # old_id -> coordinate line
section = None       # 'part', 'instance', 'assembly_post_instance', None
in_node_block = False

for line in inp_lines:
    stripped = line.strip()
    upper = stripped.upper()

    if upper.startswith('*PART'):
        section = 'part'
        in_node_block = False
        continue
    if upper.startswith('*END PART'):
        section = None
        in_node_block = False
        continue
    if upper.startswith('*INSTANCE'):
        section = 'instance'
        continue
    if upper.startswith('*END INSTANCE'):
        section = 'assembly_post_instance'
        continue
    if upper.startswith('*END ASSEMBLY'):
        section = None
        continue

    if section == 'part':
        if upper.startswith('*NODE'):
            in_node_block = True
            continue
        if in_node_block:
            if upper.startswith('*'):
                in_node_block = False
            else:
                parts_list = stripped.split(',')
                if parts_list and parts_list[0].strip().isdigit():
                    nid = int(parts_list[0].strip())
                    if nid > max_mesh_node:
                        max_mesh_node = nid

    if section == 'assembly_post_instance':
        if upper.startswith('*NODE'):
            continue
        if not upper.startswith('*') and not upper.startswith('**'):
            parts_list = stripped.split(',')
            if len(parts_list) >= 4 and parts_list[0].strip().isdigit():
                old_id = int(parts_list[0].strip())
                rp_nodes[old_id] = stripped
```

## Pattern 4: RP Node Renumbering (Legacy — only needed without noPartsInputFile)

Assembly RP nodes are numbered starting at 1, which collides with mesh nodes. This is only needed when manually flattening a hierarchical .inp. When using `noPartsInputFile=ON`, RP nodes are already correctly numbered.

```python
# Compute renumbering map
rp_offset = max_mesh_node
rp_node_map = {}  # old_id -> new_id
for old_id in rp_nodes:
    rp_node_map[old_id] = old_id + rp_offset

rp_nset_names = {'UpperRP', 'LowerLeftRP', 'LowerRightRP'}  # your RP set names

# Flatten with renumbering
flat_lines = []
current_nset_is_rp = False
section = None
in_rp_node = False

for line in inp_lines:
    stripped = line.strip()
    upper = stripped.upper()

    # Skip wrapper lines
    if upper.startswith('*PART') and not upper.startswith('*PART,'):
        section = 'part'; continue
    if upper.startswith('*PART,'):
        section = 'part'; continue
    if upper.startswith('*END PART'):
        section = None; continue
    if upper.startswith('*INSTANCE'):
        section = 'instance'; continue
    if upper.startswith('*END INSTANCE'):
        section = 'assembly_post'; in_rp_node = False; continue
    if upper.startswith('*ASSEMBLY'):
        continue
    if upper.startswith('*END ASSEMBLY'):
        section = None; continue

    # Handle assembly-level RP *Node block (renumber)
    if section == 'assembly_post':
        if upper.startswith('*NODE'):
            in_rp_node = True
            flat_lines.append(line + '\n')
            continue
        if in_rp_node and not upper.startswith('*') and stripped:
            parts_list = stripped.split(',')
            if parts_list and parts_list[0].strip().isdigit():
                old_id = int(parts_list[0].strip())
                if old_id in rp_node_map:
                    parts_list[0] = '      ' + str(rp_node_map[old_id])
                    flat_lines.append(','.join(parts_list) + '\n')
                    continue
        if upper.startswith('*') and not upper.startswith('**'):
            in_rp_node = False
            section = 'assembly_sets'

    # Remove 'internal' from set definitions
    if upper.startswith('*ELSET') or upper.startswith('*NSET'):
        parts_list = line.split(',')
        parts_list = [p for p in parts_list if 'INTERNAL' not in p.upper()]
        line = ','.join(parts_list)
        stripped = line.strip()
        upper = stripped.upper()

    # Strip instance= from keyword lines
    line = re.sub(r',\s*instance=' + re.escape(instance_name), '', line,
                  flags=re.IGNORECASE)
    # Strip instance prefix from data lines
    line = line.replace(instance_name + '.', '')

    # Track RP nsets and renumber their node references
    if upper.startswith('*NSET'):
        current_nset_is_rp = False
        for p in line.split(','):
            if 'NSET=' in p.upper():
                nset_name = p.split('=')[1].strip()
                if nset_name in rp_nset_names:
                    current_nset_is_rp = True
                break
        flat_lines.append(line + '\n' if not line.endswith('\n') else line)
        continue

    if current_nset_is_rp:
        if upper.startswith('*'):
            current_nset_is_rp = False
        elif stripped:
            tokens = stripped.rstrip(',').split(',')
            new_tokens = []
            for t in tokens:
                t = t.strip()
                if t.isdigit() and int(t) in rp_node_map:
                    new_tokens.append(str(rp_node_map[int(t)]))
                else:
                    new_tokens.append(t)
            flat_lines.append(' ' + ', '.join(new_tokens) + ',\n')
            continue

    flat_lines.append(line + '\n' if not line.endswith('\n') else line)

# Write flattened .inp
flat_name = 'MyModel_FEA_flat.inp'
with open(flat_name, 'w') as f:
    f.write(''.join(flat_lines))
```

## Pattern 5: .par File for Compliance Optimization (Min Strain Energy)

```
OPTIONS
  DRESP_GROUP_OPER_AGGREGATION = ON
END_

FEM_INPUT
  ID_NAME                = FEA_MODEL
  FILE                   = Model_flat.inp
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
  TOPO_FILTER_RADIUS     = 15.0
  STOP_CRITERION_LEVEL   = BOTH
  STOP_CRITERION_OBJ     = 0.001
  STOP_CRITERION_DENSITY = 0.005
  STOP_CRITERION_ITER    = 4
  SUM_Q_FACTOR           = 6.
END_

STOP
  ID_NAME                = global_stop
  ITER_MAX               = 30
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

## Pattern 6: .par File for Stress-Constrained Optimization (Min Volume)

**WARNING:** A volume constraint is ALWAYS needed even when minimizing volume. Without a volume upper bound, the optimizer can remove all material in a single cycle.

```
OPTIONS
  DRESP_GROUP_OPER_AGGREGATION = ON
END_

FEM_INPUT
  ID_NAME                = FEA_MODEL
  FILE                   = Model_flat.inp
END_

DV_TOPO
  ID_NAME                = design_variables
  EL_GROUP               = ALL_ELEMENTS
END_

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

DRESP
  ID_NAME                = DRESP_VOLUME
  LIST                   = NO_LIST
  DEF_TYPE               = SYSTEM
  TYPE                   = VOLUME
  EL_GROUP               = ALL_ELEMENTS
  GROUP_OPER             = SUM
END_

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

! Volume upper bound — REQUIRED to prevent full material removal
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
  TOPO_FILTER_RADIUS     = 9.0
  STOP_CRITERION_LEVEL   = BOTH
  STOP_CRITERION_OBJ     = 0.001
  STOP_CRITERION_DENSITY = 0.005
  STOP_CRITERION_ITER    = 4
  SUM_Q_FACTOR           = 6.
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

**Key differences from compliance optimization:**
- `GROUP_DEF` with `LIST_GROUP` to combine multiple frozen sets into one group
- `SIG_SENS_MISES` for von Mises stress response (NOT `STRESS_MEASURE`)
- `MAGNITUDE = ABS` for absolute stress limit (MPa), not relative
- **Volume constraint is REQUIRED** even though volume is the objective — prevents full material removal
- Higher `ITER_MAX` (stress-constrained converges slower)
- Lower `DENSITY_MOVE` (0.10 vs 0.25) for stability
- Higher `ISO_VALUE` (0.51 vs 0.3) for cleaner boundary

## Pattern 7: Running Tosca CLI from Python

```python
import subprocess

# Find Tosca command (try multiple candidates)
tosca_cmds = ['tosca', 'abaqus tosca']
tosca_found = False
tcmd = 'tosca'

for candidate in tosca_cmds:
    try:
        cmd_parts = candidate.split()
        test = subprocess.Popen(cmd_parts + ['--help'],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out, _ = test.communicate()
        tcmd = candidate
        tosca_found = True
        break
    except OSError:
        continue

if not tosca_found:
    try:
        test = subprocess.Popen(['abaqus', 'optimization', '-help'],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out, _ = test.communicate()
        tcmd = 'abaqus optimization'
        tosca_found = True
    except Exception:
        pass

# Run optimization
cmd_parts = tcmd.split() + ['optimize', '-j', 'my_tosca_job',
                             '-p', 'my_model.par', '-s', 'abaqus',
                             '-scpus', str(NUM_CPUS)]
proc = subprocess.Popen(cmd_parts,
                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout, _ = proc.communicate()
output = stdout.decode('utf-8', errors='replace')
print("Tosca exit code:", proc.returncode)
```

**CLI flags:**
- `-j` -- job name (creates output directory with this name)
- `-p` -- path to .par file
- `-s abaqus` -- solver is Abaqus
- `-scpus N` -- number of CPUs for the FEA solver

## Pattern 8: Post-Processing (FEA on Optimized Design)

Tosca deletes per-cycle ODBs. To visualize the optimized design, run FEA on the last-cycle `.inp`:

```python
import os

tosca_dir = os.path.join(WORK_DIR, 'my_tosca_job')
save_inp_dir = os.path.join(tosca_dir, 'SAVE.inp')

# Find last cycle directory
cycle_dirs = [d for d in os.listdir(save_inp_dir)
              if d.isdigit() and os.path.isdir(os.path.join(save_inp_dir, d))]
last_cycle = max(cycle_dirs, key=int)
cycle_dir = os.path.join(save_inp_dir, last_cycle)

# The cycle directory contains the flat .inp and tosca_distribution.inp
# Run FEA in that directory so *INCLUDE resolves correctly
fea_cmd = ['abaqus', 'job=Optimized',
           'input=' + os.path.join(cycle_dir, 'Model_flat.inp'),
           'cpus=' + str(NUM_CPUS), 'interactive']
fea_proc = subprocess.Popen(fea_cmd, cwd=cycle_dir,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
fea_out, _ = fea_proc.communicate()

# ODB is created in cycle_dir
odb_path = os.path.join(cycle_dir, 'Optimized.odb')
```

## Mesh Configuration: C3D10 for Stress, C3D8R for Compliance

```python
import mesh

# For stress-constrained optimization: C3D10 (quadratic tet)
# Avoids shear locking; accurate stress recovery
part.setMeshControls(regions=part.cells, elemShape=TET, technique=FREE)
part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)
elemType_hex = mesh.ElemType(elemCode=C3D20R, elemLibrary=STANDARD)
elemType_wedge = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
elemType_tet = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,),
                    elemTypes=(elemType_hex, elemType_wedge, elemType_tet))

# For compliance optimization: C3D8R (reduced-integration hex)
# Faster, adequate for stiffness-only metrics
part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType1, elemType2, elemType3))
```

**NEVER use C3D4** (linear tet) for stress-constrained optimization -- it exhibits shear locking and gives unreliable stress results. Always use **C3D10** (quadratic tet).
