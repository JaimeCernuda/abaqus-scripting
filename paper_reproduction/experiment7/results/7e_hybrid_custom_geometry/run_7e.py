# -*- coding: utf-8 -*-
"""
Experiment 7e: Build custom geometry + topology optimization (hybrid approach)

Full end-to-end: Create a simple block model from scratch in CAE, generate .inp
via writeInput(), generate .par manually, run optimization via CLI.

Model: 100x40x20 block, steel, encastre on left face, pressure on right face.
Optimization: Minimize strain energy, volume <= 50%, frozen elements near BC face.
"""

from abaqus import *
from abaqusConstants import *
from caeModules import *
import os, sys, subprocess, traceback

SEPARATOR = "=" * 70
NUM_CPUS = int(os.environ.get('ABAQUS_NUM_CPUS', '1'))
MAX_CYCLES = int(os.environ.get('ABAQUS_MAX_CYCLES', '20'))
MESH_SIZE = float(os.environ.get('ABAQUS_MESH_SIZE', '10.0'))

def phase_header(num, total, title):
    print("")
    print(SEPARATOR)
    print("  [{}/{}] {}".format(num, total, title))
    print(SEPARATOR)
    sys.stdout.flush()

def safe_run(label, func):
    try:
        result = func()
        print("  [OK] {}".format(label))
        sys.stdout.flush()
        return True, result
    except Exception as e:
        print("  [FAIL] {}: {} - {}".format(label, type(e).__name__, e))
        traceback.print_exc()
        sys.stdout.flush()
        return False, None

TOTAL = 8

print(SEPARATOR)
print("  EXPERIMENT 7e: Custom Geometry + TO (Hybrid)")
print("  CPUs: {}, Max cycles: {}, Mesh size: {}".format(NUM_CPUS, MAX_CYCLES, MESH_SIZE))
print(SEPARATOR)

# ============================================================================
# Phase 1: Create model and part
# ============================================================================
phase_header(1, TOTAL, "Create model and part (100x40x20 block)")

model = mdb.Model(name='Block_TO')
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']

part = model.Part(name='Block', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='BlockSketch', sheetSize=200.0)
sketch.rectangle(point1=(0.0, 0.0), point2=(100.0, 40.0))
part.BaseSolidExtrude(sketch=sketch, depth=20.0)
print("  Part 'Block' created: 100 x 40 x 20 mm")

# ============================================================================
# Phase 2: Material and section
# ============================================================================
phase_header(2, TOTAL, "Material and section")

mat = model.Material(name='Steel')
mat.Elastic(table=((210000.0, 0.3),))
mat.Density(table=((7.85e-9,),))

model.HomogeneousSolidSection(name='Section', material='Steel', thickness=None)
part.SectionAssignment(
    region=part.Set(cells=part.cells, name='AllCells'),
    sectionName='Section')
print("  Steel: E=210000 MPa, nu=0.3, rho=7.85e-9 tonne/mm^3")

# ============================================================================
# Phase 3: Assembly, BCs, loads
# ============================================================================
phase_header(3, TOTAL, "Assembly, BCs, loads")

assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
instance = assembly.Instance(name='Block-1', part=part, dependent=ON)

# Fixed face (x=0)
fixed_face = instance.faces.findAt(((0.0, 20.0, 10.0),))
assembly.Set(faces=fixed_face, name='FixedFace')

# Load face (x=100)
load_face = instance.faces.findAt(((100.0, 20.0, 10.0),))
assembly.Surface(side1Faces=load_face, name='LoadSurface')

# Step
model.StaticStep(name='LoadStep', previous='Initial',
                 initialInc=1.0, maxInc=1.0, minInc=1e-6)
model.FieldOutputRequest(name='F-Output-1', createStepName='LoadStep',
                         variables=('S', 'U', 'RF', 'ENER'))

# BCs and load
model.EncastreBC(name='Fixed', createStepName='Initial',
                 region=assembly.sets['FixedFace'])
model.Pressure(name='Load', createStepName='LoadStep',
               region=assembly.surfaces['LoadSurface'],
               magnitude=1.0)

print("  Encastre BC on x=0 face, 1 MPa pressure on x=100 face")

# ============================================================================
# Phase 4: Mesh
# ============================================================================
phase_header(4, TOTAL, "Mesh")

part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType1, elemType2, elemType3))
part.generateMesh()
print("  Nodes: {}, Elements: {}".format(len(part.nodes), len(part.elements)))

# ============================================================================
# Phase 5: Create frozen elements set (elements touching x=0 face)
# ============================================================================
phase_header(5, TOTAL, "Create frozen elements set")

assembly.regenerate()

# Find elements touching the x=0 face by checking if any node has x ~= 0.
# Use part.nodes (has getByLabel) since instance.nodes is MeshNodeArray.
p = model.parts['Block']
frozen_elabels = set()
for elem in p.elements:
    for nl in elem.connectivity:
        node = p.nodes[nl]
        if abs(node.coordinates[0]) < 0.01:
            frozen_elabels.add(elem.label)
            break

frozen_elements = [e for e in instance.elements if e.label in frozen_elabels]

if frozen_elements:
    assembly.Set(name='FrozenElements',
                 elements=mesh.MeshElementArray(frozen_elements))
    print("  FrozenElements: {} elements near x=0 face".format(len(frozen_elements)))
else:
    print("  [WARN] No frozen elements found!")

# ============================================================================
# Phase 6: Write .inp via prototype job
# ============================================================================
phase_header(6, TOTAL, "Create prototype job + writeInput()")

ok6a, _ = safe_run("Prototype Job",
    lambda: mdb.Job(name='Block_FEA', model='Block_TO',
                    numCpus=NUM_CPUS, numDomains=NUM_CPUS))

ok6b, _ = safe_run("Job.writeInput()",
    lambda: mdb.jobs['Block_FEA'].writeInput())

cae_inp = 'Block_FEA.inp'
if os.path.exists(cae_inp):
    print("  Generated: {} ({} bytes)".format(cae_inp, os.path.getsize(cae_inp)))
else:
    print("FATAL: {} not generated. Aborting.".format(cae_inp))
    sys.exit(1)

# Save CAE
safe_run("saveAs", lambda: mdb.saveAs('Block_7e.cae'))

# ============================================================================
# Phase 7: Flatten .inp + generate .par + run Tosca CLI
# ============================================================================
phase_header(7, TOTAL, "Flatten .inp + generate .par + run tosca optimize")

# Tosca can't resolve assembly-level sets from CAE-format .inp files.
# Flatten: remove *Part/*Instance wrappers, strip instance= from set defs.
import re

print("  Flattening {} for Tosca compatibility...".format(cae_inp))
with open(cae_inp, 'r') as f:
    lines_in = f.readlines()

output_lines = []
instance_name = None
i = 0
while i < len(lines_in):
    line = lines_in[i]
    stripped = line.strip().upper()

    # Skip structural wrappers
    if stripped.startswith('*PART,') or stripped == '*PART':
        i += 1
        continue
    if stripped == '*END PART':
        i += 1
        continue
    if stripped.startswith('*ASSEMBLY,') or stripped == '*ASSEMBLY':
        i += 1
        continue
    if stripped.startswith('*INSTANCE,'):
        match = re.search(r'name=(\S+)', line, re.IGNORECASE)
        if match:
            instance_name = match.group(1).rstrip(',')
        i += 1
        continue
    if stripped == '*END INSTANCE':
        i += 1
        continue
    if stripped == '*END ASSEMBLY':
        i += 1
        continue

    # Skip assembly-level reference point node (small *Node block)
    if stripped.startswith('*NODE') and not stripped.startswith('*NODE OUTPUT'):
        j = i + 1
        count = 0
        while j < len(lines_in) and not lines_in[j].strip().startswith('*'):
            count += 1
            j += 1
        if count <= 5:
            i = j
            continue

    # Strip instance= and internal keyword from set definitions
    if stripped.startswith(('*NSET,', '*ELSET,', '*SURFACE,')):
        if instance_name:
            line = re.sub(
                r',\s*instance=' + re.escape(instance_name),
                '', line, flags=re.IGNORECASE)
        # Remove 'internal' keyword — valid inside *Part but not in flat format
        line = re.sub(r',\s*internal', '', line, flags=re.IGNORECASE)

    output_lines.append(line)
    i += 1

flat_inp = 'Block_FEA_flat.inp'
with open(flat_inp, 'w') as f:
    f.writelines(output_lines)

print("  Flattened: {} ({} lines -> {} lines, {} bytes)".format(
    flat_inp, len(lines_in), len(output_lines), os.path.getsize(flat_inp)))

filter_radius = MESH_SIZE * 2.0

PAR_CONTENT = """\
! Experiment 7e: Block Topology Optimization
! Generated by run_7e.py (hybrid approach)

FEM_INPUT
  ID_NAME                = BLOCK_MODEL
  FILE                   = {inp_file}
END_

DV_TOPO
  ID_NAME                = design_variables
  EL_GROUP               = ALL_ELEMENTS
END_

DVCON_TOPO
  ID_NAME                = dvcon_frozen
  EL_GROUP               = FrozenElements
  CHECK_TYPE             = FROZEN
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
  ID_NAME                = min_SE
  DRESP                  = DRESP_STRAIN_ENERGY
  TARGET                 = MIN
END_

CONSTRAINT
  ID_NAME                = vol_constraint
  DRESP                  = DRESP_VOLUME
  MAGNITUDE              = REL
  LE_VALUE               = 0.5
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
  TOPO_FILTER_RADIUS     = {filter_radius}
END_

STOP
  ID_NAME                = global_stop
  ITER_MAX               = {max_cycles}
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
""".format(
    inp_file=flat_inp,
    filter_radius=filter_radius,
    max_cycles=MAX_CYCLES,
)

par_file = 'Block_7e.par'
with open(par_file, 'w') as f:
    f.write(PAR_CONTENT)
print("  Generated: {} ({} bytes)".format(par_file, os.path.getsize(par_file)))
print("  Filter radius: {} mm".format(filter_radius))
print("  Max cycles: {}".format(MAX_CYCLES))

print("\n  Running: tosca optimize -j block_7e_tosca -p {} -s abaqus -scpus {}".format(
    par_file, NUM_CPUS))
sys.stdout.flush()

cmd = [
    'tosca', 'optimize',
    '-j', 'block_7e_tosca',
    '-p', par_file,
    '-s', 'abaqus',
    '-scpus', str(NUM_CPUS),
]

try:
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    stdout, _ = proc.communicate()
    exit_code = proc.returncode

    print("  tosca exit code: {}".format(exit_code))
    lines = stdout.decode('utf-8', errors='replace').split('\n')
    if len(lines) > 50:
        print("  ... ({} lines total, showing last 50)".format(len(lines)))
        for line in lines[-50:]:
            print("  {}".format(line))
    else:
        for line in lines:
            print("  {}".format(line))
except Exception as e:
    print("  [FAIL] tosca optimize: {} - {}".format(type(e).__name__, e))
    traceback.print_exc()
    exit_code = -1

sys.stdout.flush()

# ============================================================================
# Phase 8: Summary
# ============================================================================
phase_header(8, TOTAL, "Summary")

print("  Model creation:  OK")
print("  Mesh:            {} nodes, {} elements".format(len(part.nodes), len(part.elements)))
print("  Frozen elements: {}".format(len(frozen_elements) if frozen_elements else "NONE"))
print("  writeInput():    {}".format("OK" if ok6b else "FAIL"))
print("  tosca optimize:  {}".format("OK (exit {})".format(exit_code) if exit_code == 0 else "FAIL (exit {})".format(exit_code)))

print("\n  Files in CWD:")
for f in sorted(os.listdir('.')):
    if os.path.isdir(f):
        print("    {}/ (dir)".format(f))
    else:
        print("    {} ({} bytes)".format(f, os.path.getsize(f)))

for d in sorted(os.listdir('.')):
    if os.path.isdir(d):
        print("\n  Contents of {}/".format(d))
        try:
            contents = sorted(os.listdir(d))
            for f2 in contents[:20]:
                print("    {}".format(f2))
            if len(contents) > 20:
                print("    ... and {} more files".format(len(contents) - 20))
        except:
            pass

print("\nExperiment 7e finished.")
sys.stdout.flush()
