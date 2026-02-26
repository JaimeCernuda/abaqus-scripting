# -*- coding: utf-8 -*-
"""
Experiment 8d: Full OptimizationProcess.submit() pipeline.

Same model + optimization setup, attempts submit() with systematic variations:
  A: submit() with default validate=True
  B: submit(validate=False)
  C: Run proto FEA first -> OptProcess -> submit()
  D: No .cae save before submit
  E: dependent=OFF + assembly-level mesh (cantilever pattern)
"""

from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import *
import os, sys, traceback, signal

executeOnCaeStartup()

SEPARATOR = "=" * 70
MESH_SIZE = float(os.environ.get('ABAQUS_MESH_SIZE', '5.0'))
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

def list_dirs():
    """List subdirectories that might contain optimization output."""
    for d in sorted(os.listdir('.')):
        if os.path.isdir(d) and d != '.':
            print("  Directory: {}/".format(d))
            contents = os.listdir(d)
            for c in sorted(contents)[:10]:
                fp = os.path.join(d, c)
                if os.path.isfile(fp):
                    print("    {}: {} bytes".format(c, os.path.getsize(fp)))
                else:
                    print("    {}/".format(c))
            if len(contents) > 10:
                print("    ... and {} more".format(len(contents) - 10))


def build_model_dependent_on():
    """Build model with dependent=ON, part-level mesh (compression pattern)."""
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
    print("  Model built (dependent=ON): {} nodes, {} elements".format(
        len(part.nodes), len(part.elements)))

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
    return model, task, instance


def build_model_dependent_off():
    """Build model with dependent=OFF, assembly-level mesh (cantilever pattern)."""
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
    instance = model.rootAssembly.Instance(name='Block-1', part=part, dependent=OFF)

    model.StaticStep(name='LoadStep', previous='Initial',
        timePeriod=1.0, initialInc=1.0, maxInc=1.0, minInc=1e-6)
    model.FieldOutputRequest('F-Output-1', createStepName='LoadStep',
        variables=('S', 'E', 'U', 'RF', 'ENER'))
    model.EncastreBC(name='Fixed', createStepName='Initial',
        region=instance.sets['FixedFace'])
    model.Pressure(name='Load', createStepName='LoadStep',
        region=instance.surfaces['LoadSurface'], magnitude=1.0)

    # Assembly-level mesh (cantilever pattern)
    assembly = model.rootAssembly
    elem1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
    elem2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elem3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
    assembly.setElementType(regions=(instance.cells,), elemTypes=(elem1, elem2, elem3))
    assembly.seedPartInstance(regions=(instance,), size=MESH_SIZE)
    assembly.generateMesh(regions=(instance,))
    print("  Model built (dependent=OFF): {} nodes, {} elements".format(
        len(instance.nodes), len(instance.elements)))

    # Frozen elements (dependent=OFF: mesh lives on instance)
    frozen_labels = set()
    for elem in instance.elements:
        for node in elem.getNodes():
            if abs(node.coordinates[0]) < 0.01:
                frozen_labels.add(elem.label)
                break
    frozen_inst_elems = [e for e in instance.elements if e.label in frozen_labels]
    if frozen_inst_elems:
        model.rootAssembly.Set(name='FrozenElems',
            elements=mesh.MeshElementArray(frozen_inst_elems))
    print("  Frozen elements: {}".format(len(frozen_inst_elems)))

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
        name='FrozenBC', region=model.rootAssembly.sets['FrozenElems'])

    print("  Optimization setup complete")
    return model, task, instance


def reset_model():
    """Delete Model-1 and recreate it fresh."""
    if 'Model-1' in mdb.models:
        del mdb.models['Model-1']
    mdb.Model(name='Model-1')
    # Clean up jobs and opt processes
    for name in list(mdb.optimizationProcesses.keys()):
        try:
            del mdb.optimizationProcesses[name]
        except:
            pass
    for name in list(mdb.jobs.keys()):
        try:
            del mdb.jobs[name]
        except:
            pass


TOTAL = 6

print(SEPARATOR)
print("  EXPERIMENT 8d: Full submit() Pipeline")
print("  Mesh size: {}, Max cycles: {}".format(MESH_SIZE, MAX_CYCLES))
print(SEPARATOR)

# ============================================================================
# [1/6] Variation A: submit() with defaults (validate=True implied)
# ============================================================================
phase_header(1, TOTAL, "Variation A: submit() with defaults")

try:
    model, task, instance = build_model_dependent_on()

    protoJob = mdb.Job(name='Block_Proto', model='Model-1',
        numCpus=1, numDomains=1)
    mdb.saveAs('exp8d.cae')

    optProcess = mdb.OptimizationProcess(
        name='BlockOpt', model='Model-1', task='TopOpt',
        prototypeJob='Block_Proto', maxDesignCycle=MAX_CYCLES)
    print("  OptimizationProcess created")
    print("  Calling submit()...")
    sys.stdout.flush()

    optProcess.submit()
    optProcess.waitForCompletion()
    print("  [OK] submit() SUCCEEDED (Variation A)")
    list_files()
    list_dirs()
    print("")
    print(SEPARATOR)
    print("  Experiment 8d COMPLETE - Variation A worked")
    print(SEPARATOR)
    sys.exit(0)

except SystemExit:
    raise
except Exception as e:
    print("  [FAIL] Variation A: {} - {}".format(type(e).__name__, e))
    traceback.print_exc()
    sys.stdout.flush()

# ============================================================================
# [2/6] Variation B: submit(validate=False)
# ============================================================================
phase_header(2, TOTAL, "Variation B: submit(validate=False)")

reset_model()

try:
    model, task, instance = build_model_dependent_on()

    protoJob = mdb.Job(name='Block_Proto', model='Model-1',
        numCpus=1, numDomains=1)
    mdb.saveAs('exp8d.cae')

    optProcess = mdb.OptimizationProcess(
        name='BlockOpt', model='Model-1', task='TopOpt',
        prototypeJob='Block_Proto', maxDesignCycle=MAX_CYCLES)
    print("  Calling submit(validate=False)...")
    sys.stdout.flush()

    optProcess.submit(validate=False)
    optProcess.waitForCompletion()
    print("  [OK] submit(validate=False) SUCCEEDED (Variation B)")
    list_files()
    list_dirs()
    print("")
    print(SEPARATOR)
    print("  Experiment 8d COMPLETE - Variation B worked")
    print(SEPARATOR)
    sys.exit(0)

except SystemExit:
    raise
except Exception as e:
    print("  [FAIL] Variation B: {} - {}".format(type(e).__name__, e))
    traceback.print_exc()
    sys.stdout.flush()

# ============================================================================
# [3/6] Variation C: Run proto FEA first -> submit()
# ============================================================================
phase_header(3, TOTAL, "Variation C: run FEA -> submit()")

reset_model()

try:
    model, task, instance = build_model_dependent_on()

    protoJob = mdb.Job(name='Block_Proto', model='Model-1',
        numCpus=1, numDomains=1)
    print("  Running proto FEA first...")
    sys.stdout.flush()
    protoJob.submit()
    protoJob.waitForCompletion()
    print("  Proto FEA done. ODB: {}".format(os.path.exists('Block_Proto.odb')))

    mdb.saveAs('exp8d.cae')

    optProcess = mdb.OptimizationProcess(
        name='BlockOpt', model='Model-1', task='TopOpt',
        prototypeJob='Block_Proto', maxDesignCycle=MAX_CYCLES)
    print("  Calling submit()...")
    sys.stdout.flush()

    optProcess.submit()
    optProcess.waitForCompletion()
    print("  [OK] submit() SUCCEEDED (Variation C)")
    list_files()
    list_dirs()
    print("")
    print(SEPARATOR)
    print("  Experiment 8d COMPLETE - Variation C worked")
    print(SEPARATOR)
    sys.exit(0)

except SystemExit:
    raise
except Exception as e:
    print("  [FAIL] Variation C: {} - {}".format(type(e).__name__, e))
    traceback.print_exc()
    sys.stdout.flush()

# ============================================================================
# [4/6] Variation D: No .cae save before submit
# ============================================================================
phase_header(4, TOTAL, "Variation D: no save before submit()")

reset_model()

try:
    model, task, instance = build_model_dependent_on()

    protoJob = mdb.Job(name='Block_Proto', model='Model-1',
        numCpus=1, numDomains=1)
    # Deliberately NOT saving .cae

    optProcess = mdb.OptimizationProcess(
        name='BlockOpt', model='Model-1', task='TopOpt',
        prototypeJob='Block_Proto', maxDesignCycle=MAX_CYCLES)
    print("  Calling submit() (no .cae save)...")
    sys.stdout.flush()

    optProcess.submit()
    optProcess.waitForCompletion()
    print("  [OK] submit() SUCCEEDED (Variation D)")
    list_files()
    list_dirs()
    print("")
    print(SEPARATOR)
    print("  Experiment 8d COMPLETE - Variation D worked")
    print(SEPARATOR)
    sys.exit(0)

except SystemExit:
    raise
except Exception as e:
    print("  [FAIL] Variation D: {} - {}".format(type(e).__name__, e))
    traceback.print_exc()
    sys.stdout.flush()

# ============================================================================
# [5/6] Variation E: dependent=OFF + assembly-level mesh
# ============================================================================
phase_header(5, TOTAL, "Variation E: dependent=OFF + assembly mesh")

reset_model()

try:
    model, task, instance = build_model_dependent_off()

    protoJob = mdb.Job(name='Block_Proto', model='Model-1',
        numCpus=1, numDomains=1)
    mdb.saveAs('exp8d.cae')

    optProcess = mdb.OptimizationProcess(
        name='BlockOpt', model='Model-1', task='TopOpt',
        prototypeJob='Block_Proto', maxDesignCycle=MAX_CYCLES)
    print("  Calling submit()...")
    sys.stdout.flush()

    optProcess.submit()
    optProcess.waitForCompletion()
    print("  [OK] submit() SUCCEEDED (Variation E)")
    list_files()
    list_dirs()
    print("")
    print(SEPARATOR)
    print("  Experiment 8d COMPLETE - Variation E worked")
    print(SEPARATOR)
    sys.exit(0)

except SystemExit:
    raise
except Exception as e:
    print("  [FAIL] Variation E: {} - {}".format(type(e).__name__, e))
    traceback.print_exc()
    sys.stdout.flush()

# ============================================================================
# [6/6] All variations failed
# ============================================================================
phase_header(6, TOTAL, "Summary")

print("  ALL VARIATIONS FAILED")
list_files("Final state")
list_dirs()

print("")
print(SEPARATOR)
print("  Experiment 8d: ALL VARIATIONS FAILED")
print(SEPARATOR)
sys.exit(1)
