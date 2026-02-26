# -*- coding: utf-8 -*-
"""
Experiment 8e: writeParAndInputFiles() -> Tosca CLI.

Uses the Abaqus API to generate .par and .inp via writeParAndInputFiles(),
then runs Tosca CLI on the generated files. No manual file creation.

If writeParAndInputFiles() fails, falls back to writeInput() + manual .par
generation (proven approach from experiment 7).
"""

from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import *
import os, sys, traceback, subprocess, glob as globmod

executeOnCaeStartup()

SEPARATOR = "=" * 70
MESH_SIZE = float(os.environ.get('ABAQUS_MESH_SIZE', '5.0'))
NUM_CPUS = int(os.environ.get('ABAQUS_NUM_CPUS', '1'))
MAX_CYCLES = int(os.environ.get('ABAQUS_MAX_CYCLES', '20'))

def phase_header(num, total, title):
    print("")
    print(SEPARATOR)
    print("  [{}/{}] {}".format(num, total, title))
    print(SEPARATOR)
    sys.stdout.flush()

def list_files(label="Files"):
    print("  {}:".format(label))
    for f in sorted(os.listdir('.')):
        if os.path.isfile(f):
            print("    {}: {} bytes".format(f, os.path.getsize(f)))
        else:
            print("    {}/".format(f))
    sys.stdout.flush()


def build_model():
    """Build complete model + optimization setup."""
    model = mdb.models['Model-1']

    sketch = model.ConstrainedSketch(name='sketch', sheetSize=200.0)
    sketch.rectangle(point1=(0.0, 0.0), point2=(100.0, 40.0))
    part = model.Part(name='Block', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    part.BaseSolidExtrude(sketch=sketch, depth=20.0)

    part.Set(name='AllCells', cells=part.cells.findAt(coordinates=((50.0, 20.0, 10.0),)))
    part.Set(name='FixedFace', faces=part.faces.findAt(coordinates=((0.0, 20.0, 10.0),)))
    part.Surface(name='LoadSurface', side1Faces=part.faces.findAt(coordinates=((100.0, 20.0, 10.0),)))

    mat = model.Material(name='Steel')
    mat.Elastic(table=((210000.0, 0.3),))
    mat.Density(table=((7.85e-9,),))

    model.HomogeneousSolidSection(name='Section', material='Steel', thickness=None)
    part.SectionAssignment(region=part.sets['AllCells'], sectionName='Section')

    model.rootAssembly.DatumCsysByDefault(CARTESIAN)
    instance = model.rootAssembly.Instance(name='Block-1', part=part, dependent=ON)

    model.StaticStep(name='LoadStep', previous='Initial',
        timePeriod=1.0, initialInc=1.0, maxInc=1.0, minInc=1e-6)
    model.FieldOutputRequest('F-Output-1', createStepName='LoadStep',
        variables=('S', 'E', 'U', 'RF', 'ENER'))
    model.EncastreBC(name='Fixed', createStepName='Initial',
        region=instance.sets['FixedFace'])
    model.Pressure(name='Load', createStepName='LoadStep',
        region=instance.surfaces['LoadSurface'], magnitude=1.0)

    elem1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
    elem2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elem3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
    part.setElementType(regions=(part.cells,), elemTypes=(elem1, elem2, elem3))
    part.seedPart(size=MESH_SIZE)
    part.generateMesh()
    print("  Model: {} nodes, {} elements".format(len(part.nodes), len(part.elements)))

    # Frozen elements — create set on part (dependent=ON inherits to instance)
    frozen_labels = set()
    for elem in part.elements:
        for nidx in elem.connectivity:
            if abs(part.nodes[nidx].coordinates[0]) < 0.01:
                frozen_labels.add(elem.label)
                break
    frozen_part_elems = [e for e in part.elements if e.label in frozen_labels]
    if frozen_part_elems:
        part.Set(name='FrozenElems', elements=mesh.MeshElementArray(frozen_part_elems))
    print("  Frozen elements: {}".format(len(frozen_part_elems)))

    # Optimization setup
    model.TopologyTask(
        name='TopOpt', region=MODEL,
        freezeBoundaryConditionRegions=ON, freezeLoadRegions=ON,
        materialInterpolationTechnique=SIMP, materialInterpolationPenalty=3.0)
    task = model.optimizationTasks['TopOpt']

    task.SingleTermDesignResponse(
        name='DR_StrainEnergy', identifier='STRAIN_ENERGY',
        region=MODEL, operation=SUM)
    task.SingleTermDesignResponse(
        name='DR_Volume', identifier='VOLUME',
        region=MODEL, operation=SUM)
    task.ObjectiveFunction(
        name='MinStrainEnergy',
        objectives=((OFF, 'DR_StrainEnergy', 1.0, 0.0, ''),),
        target=MINIMIZE)
    task.OptimizationConstraint(
        name='VolumeConstraint', designResponse='DR_Volume',
        restrictionValue=0.5, restrictionMethod=RELATIVE_LESS_THAN_EQUAL)
    task.FrozenArea(
        name='FrozenBC', region=instance.sets['FrozenElems'])

    print("  Optimization setup complete")
    return model, task, instance, part, frozen_labels


TOTAL = 5

print(SEPARATOR)
print("  EXPERIMENT 8e: writeParAndInputFiles() -> Tosca CLI")
print("  Mesh: {}, CPUs: {}, Max cycles: {}".format(MESH_SIZE, NUM_CPUS, MAX_CYCLES))
print(SEPARATOR)

# ============================================================================
# [1/5] Build model
# ============================================================================
phase_header(1, TOTAL, "Build model")
model, task, instance, part, frozen_labels = build_model()

# ============================================================================
# [2/5] Try writeParAndInputFiles()
# ============================================================================
phase_header(2, TOTAL, "writeParAndInputFiles()")

par_generated = False
par_file = None
inp_file = None

try:
    protoJob = mdb.Job(name='Block_Proto', model='Model-1',
        numCpus=NUM_CPUS, numDomains=NUM_CPUS)
    mdb.saveAs('exp8e.cae')

    optProcess = mdb.OptimizationProcess(
        name='BlockOpt', model='Model-1', task='TopOpt',
        prototypeJob='Block_Proto', maxDesignCycle=MAX_CYCLES)

    optProcess.writeParAndInputFiles()
    print("  [OK] writeParAndInputFiles() succeeded!")

    # Find generated files
    par_files = [f for f in os.listdir('.') if f.endswith('.par')]
    inp_files = [f for f in os.listdir('.') if f.endswith('.inp')]
    print("  .par files: {}".format(par_files))
    print("  .inp files: {}".format(inp_files))

    if par_files:
        par_file = par_files[0]
        par_generated = True
    if inp_files:
        inp_file = inp_files[0]

    list_files("After writeParAndInputFiles")

except Exception as e:
    print("  [FAIL] writeParAndInputFiles(): {} - {}".format(type(e).__name__, e))
    traceback.print_exc()
    sys.stdout.flush()

# ============================================================================
# [3/5] Fallback: writeInput() + manual .par if needed
# ============================================================================
if not par_generated:
    phase_header(3, TOTAL, "Fallback: writeInput() + manual .par")

    # Clean up failed opt process
    try:
        del mdb.optimizationProcesses['BlockOpt']
    except:
        pass
    try:
        del mdb.jobs['Block_Proto']
    except:
        pass

    try:
        fallbackJob = mdb.Job(name='Block_Fallback', model='Model-1',
            numCpus=NUM_CPUS, numDomains=NUM_CPUS)
        fallbackJob.writeInput()
        print("  writeInput() done: Block_Fallback.inp exists: {}".format(
            os.path.exists('Block_Fallback.inp')))
        inp_file = 'Block_Fallback.inp'

        # Read .inp content
        with open(inp_file) as f:
            inp_content = f.read()

        # Flatten .inp for Tosca: remove Part/Instance/Assembly wrappers
        # but KEEP all content inside them (nodes, elements, sets, etc.)
        import re
        lines = inp_content.split('\n')
        flat_lines = []

        for line in lines:
            upper = line.upper().strip()

            # Remove wrapper lines only (keep content inside)
            if upper.startswith('*PART'):
                continue
            if upper.startswith('*END PART'):
                continue
            if upper.startswith('*INSTANCE'):
                continue
            if upper.startswith('*END INSTANCE'):
                continue
            if upper.startswith('*ASSEMBLY'):
                continue
            if upper.startswith('*END ASSEMBLY'):
                continue

            # Remove 'internal' keyword from set definitions
            if upper.startswith('*ELSET') or upper.startswith('*NSET'):
                parts = line.split(',')
                parts = [p for p in parts if 'INTERNAL' not in p.upper()]
                line = ','.join(parts)

            flat_lines.append(line)

        flat_inp = '\n'.join(flat_lines)

        # Strip instance prefixes from set references
        flat_inp = flat_inp.replace('Block-1.', '')
        flat_inp = flat_inp.replace('BLOCK-1.', '')
        flat_inp = flat_inp.replace('block-1.', '')

        # Remove instance= from set/surface defs
        flat_inp = re.sub(r',\s*instance=\S+', '', flat_inp, flags=re.IGNORECASE)

        # Check if FrozenElems set already exists in .inp
        frozen_set = None
        for fline in flat_inp.split('\n'):
            if '*ELSET' in fline.upper() and 'FROZEN' in fline.upper():
                for fpart in fline.split(','):
                    if 'ELSET=' in fpart.upper():
                        frozen_set = fpart.split('=')[1].strip()
                        break

        # If no frozen set, insert FROZEN_ELEMS *ELSET BEFORE *Step
        if not frozen_set:
            frozen_set = 'FROZEN_ELEMS'
            elset_block = '*ELSET, ELSET={}\n'.format(frozen_set)
            labels = sorted(frozen_labels)
            for i in range(0, len(labels), 8):
                chunk = labels[i:i+8]
                elset_block += ', '.join(str(l) for l in chunk)
                if i + 8 < len(labels):
                    elset_block += ',\n'
                else:
                    elset_block += '\n'

            # Insert before *Step
            step_match = re.search(r'^\*Step', flat_inp, re.MULTILINE | re.IGNORECASE)
            if step_match:
                insert_pos = step_match.start()
                flat_inp = flat_inp[:insert_pos] + elset_block + flat_inp[insert_pos:]
                print("  Inserted FROZEN_ELEMS set before *Step")
            else:
                flat_inp += '\n' + elset_block
                print("  WARNING: No *Step found, appended FROZEN_ELEMS at end")

            print("  Frozen set '{}' ({} elements)".format(frozen_set, len(labels)))

        flat_name = 'Block_flat.inp'
        with open(flat_name, 'w') as f:
            f.write(flat_inp)
        print("  Flattened .inp: {} ({} bytes)".format(flat_name, os.path.getsize(flat_name)))
        inp_file = flat_name

        # Generate .par file (proven syntax from experiment 7d/7e)
        par_file = 'Block_opt.par'
        par_content = """! Experiment 8e: Block Topology Optimization
! Generated by exp8e_par_to_tosca.py (hybrid approach)

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
  EL_GROUP               = {frozen}
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
  TOPO_FILTER_RADIUS     = {filter_r}
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
            inp_file=inp_file,
            frozen=frozen_set,
            max_cycles=MAX_CYCLES,
            filter_r=MESH_SIZE * 2.0,
        )

        with open(par_file, 'w') as f:
            f.write(par_content)
        print("  Generated {}: {} bytes".format(par_file, os.path.getsize(par_file)))
        par_generated = True

    except Exception as e:
        print("  [FAIL] Fallback: {} - {}".format(type(e).__name__, e))
        traceback.print_exc()
        sys.stdout.flush()
else:
    phase_header(3, TOTAL, "Fallback (skipped - API method worked)")

# ============================================================================
# [4/5] Print .par content for verification
# ============================================================================
phase_header(4, TOTAL, "Verify .par content")

if par_file and os.path.exists(par_file):
    with open(par_file) as f:
        par_text = f.read()
    print("  --- {} ({} bytes) ---".format(par_file, len(par_text)))
    print(par_text[:3000])
    if len(par_text) > 3000:
        print("  ... ({} bytes total)".format(len(par_text)))
else:
    print("  ERROR: No .par file available!")
    sys.exit(1)

if inp_file and os.path.exists(inp_file):
    print("  .inp file: {} ({} bytes)".format(inp_file, os.path.getsize(inp_file)))
else:
    print("  ERROR: No .inp file available!")
    sys.exit(1)

# ============================================================================
# [5/5] Run Tosca CLI
# ============================================================================
phase_header(5, TOTAL, "Run Tosca CLI")

# Try different Tosca command names
tosca_cmds = ['tosca', 'abaqus tosca']
tosca_found = False

for tcmd in tosca_cmds:
    try:
        parts = tcmd.split()
        test = subprocess.Popen(parts + ['--help'],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out, _ = test.communicate()
        print("  Found Tosca via: '{}'".format(tcmd))
        tosca_found = True
        break
    except OSError:
        continue

if not tosca_found:
    # Try 'abaqus' with tosca subcommand
    try:
        test = subprocess.Popen(['abaqus', 'optimization', '-help'],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out, _ = test.communicate()
        print("  Found via 'abaqus optimization'")
        print("  Output: {}".format(out.decode('utf-8', errors='replace')[:500]))
        tcmd = 'abaqus optimization'
        tosca_found = True
    except:
        pass

if not tosca_found:
    print("  WARNING: Could not find Tosca CLI, trying direct invocation anyway")
    tcmd = 'tosca'

# Build and run the optimization command
print("  Using command: '{}'".format(tcmd))
print("  Par file: {}".format(par_file))
print("  Inp file: {}".format(inp_file))
sys.stdout.flush()

cmd_parts = tcmd.split() + ['optimize', '-j', 'block_8e_tosca',
    '-p', par_file, '-s', 'abaqus', '-scpus', str(NUM_CPUS)]
print("  Full command: {}".format(' '.join(cmd_parts)))
sys.stdout.flush()

proc = subprocess.Popen(cmd_parts,
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout, _ = proc.communicate()
output = stdout.decode('utf-8', errors='replace')

print("  Tosca exit code: {}".format(proc.returncode))
print("")
# Print last 5000 chars of output
if len(output) > 5000:
    print("  ... (truncated, showing last 5000 chars)")
print(output[-5000:])

# Check for output files
print("")
list_files("Final files")

# Check for optimization output directories
for d in sorted(os.listdir('.')):
    if os.path.isdir(d):
        print("  Directory: {}/".format(d))
        contents = os.listdir(d)
        for c in sorted(contents)[:15]:
            fp = os.path.join(d, c)
            if os.path.isfile(fp):
                print("    {}: {} bytes".format(c, os.path.getsize(fp)))
            else:
                print("    {}/".format(c))
        if len(contents) > 15:
            print("    ... and {} more".format(len(contents) - 15))

# Check for STL output
stl_files = globmod.glob('*.stl') + globmod.glob('*/*.stl') + globmod.glob('*/*/*.stl')
if stl_files:
    print("  STL files found: {}".format(stl_files))
else:
    print("  No STL files found")

print("")
print(SEPARATOR)
print("  Experiment 8e COMPLETE (exit code: {})".format(proc.returncode))
print(SEPARATOR)
