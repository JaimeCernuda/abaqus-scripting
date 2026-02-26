# -*- coding: utf-8 -*-
"""
Experiment 8c: Test writeParAndInputFiles().

Same model + optimization setup as 8b, plus OptimizationProcess creation
and writeParAndInputFiles() call. This is the call that failed with KeyError
in experiment 7.

Tries systematic variations if the first attempt fails:
  A: Save .cae -> OptimizationProcess -> writeParAndInputFiles()
  B: OptimizationProcess -> save .cae -> writeParAndInputFiles()
  C: writeInput() on proto job -> OptimizationProcess -> writeParAndInputFiles()
  D: submit() proto job (run FEA) -> OptimizationProcess -> writeParAndInputFiles()
"""

from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import *
import os, sys, traceback

executeOnCaeStartup()

SEPARATOR = "=" * 70
MESH_SIZE = float(os.environ.get('ABAQUS_MESH_SIZE', '5.0'))

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
    """Build the complete model + optimization setup. Returns (model, task, instance)."""
    model = mdb.models['Model-1']

    # Part
    sketch = model.ConstrainedSketch(name='sketch', sheetSize=200.0)
    sketch.rectangle(point1=(0.0, 0.0), point2=(100.0, 40.0))
    part = model.Part(name='Block', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    part.BaseSolidExtrude(sketch=sketch, depth=20.0)

    # Sets
    part.Set(name='AllCells', cells=part.cells.findAt(coordinates=((50.0, 20.0, 10.0),)))
    part.Set(name='FixedFace', faces=part.faces.findAt(coordinates=((0.0, 20.0, 10.0),)))
    part.Surface(name='LoadSurface', side1Faces=part.faces.findAt(coordinates=((100.0, 20.0, 10.0),)))

    # Material
    mat = model.Material(name='Steel')
    mat.Elastic(table=((210000.0, 0.3),))
    mat.Density(table=((7.85e-9,),))

    # Section
    model.HomogeneousSolidSection(name='Section', material='Steel', thickness=None)
    part.SectionAssignment(region=part.sets['AllCells'], sectionName='Section')

    # Assembly
    model.rootAssembly.DatumCsysByDefault(CARTESIAN)
    instance = model.rootAssembly.Instance(name='Block-1', part=part, dependent=ON)

    # Step
    model.StaticStep(name='LoadStep', previous='Initial',
        timePeriod=1.0, initialInc=1.0, maxInc=1.0, minInc=1e-6)

    # Output
    model.FieldOutputRequest('F-Output-1', createStepName='LoadStep',
        variables=('S', 'E', 'U', 'RF', 'ENER'))

    # BC and load
    model.EncastreBC(name='Fixed', createStepName='Initial',
        region=instance.sets['FixedFace'])
    model.Pressure(name='Load', createStepName='LoadStep',
        region=instance.surfaces['LoadSurface'], magnitude=1.0)

    # Mesh
    elem1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
    elem2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elem3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
    part.setElementType(regions=(part.cells,), elemTypes=(elem1, elem2, elem3))
    part.seedPart(size=MESH_SIZE)
    part.generateMesh()
    print("  Model built: {} nodes, {} elements".format(len(part.nodes), len(part.elements)))

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

    # TopologyTask
    model.TopologyTask(
        name='TopOpt',
        region=MODEL,
        freezeBoundaryConditionRegions=ON,
        freezeLoadRegions=ON,
        materialInterpolationTechnique=SIMP,
        materialInterpolationPenalty=3.0,
    )
    task = model.optimizationTasks['TopOpt']

    # Design responses
    task.SingleTermDesignResponse(
        name='DR_StrainEnergy', identifier='STRAIN_ENERGY',
        region=MODEL, operation=SUM)
    task.SingleTermDesignResponse(
        name='DR_Volume', identifier='VOLUME',
        region=MODEL, operation=SUM)

    # Objective
    task.ObjectiveFunction(
        name='MinStrainEnergy',
        objectives=((OFF, 'DR_StrainEnergy', 1.0, 0.0, ''),),
        target=MINIMIZE)

    # Constraint
    task.OptimizationConstraint(
        name='VolumeConstraint', designResponse='DR_Volume',
        restrictionValue=0.5, restrictionMethod=RELATIVE_LESS_THAN_EQUAL)

    # Frozen area
    task.FrozenArea(
        name='FrozenBC',
        region=instance.sets['FrozenElems'])

    print("  Optimization setup complete")
    return model, task, instance


TOTAL = 5

print(SEPARATOR)
print("  EXPERIMENT 8c: writeParAndInputFiles() Test")
print("  Mesh size: {}".format(MESH_SIZE))
print(SEPARATOR)

# ============================================================================
# [1/5] Build model + optimization setup
# ============================================================================
phase_header(1, TOTAL, "Build model + optimization setup")
model, task, instance = build_model()

# ============================================================================
# [2/5] Variation A: Save .cae -> OptimizationProcess -> writeParAndInputFiles()
# ============================================================================
phase_header(2, TOTAL, "Variation A: save -> OptProcess -> writePar")

try:
    protoJob = mdb.Job(name='Block_Proto', model='Model-1',
        numCpus=1, numDomains=1)
    print("  Proto job 'Block_Proto' created")

    mdb.saveAs('exp8c.cae')
    print("  Saved exp8c.cae")

    optProcess = mdb.OptimizationProcess(
        name='BlockOpt',
        model='Model-1',
        task='TopOpt',
        prototypeJob='Block_Proto',
        maxDesignCycle=20,
    )
    print("  OptimizationProcess 'BlockOpt' created")

    optProcess.writeParAndInputFiles()
    print("  [OK] writeParAndInputFiles() SUCCEEDED (Variation A)")
    list_files("Generated files")
    # If we get here, we're done
    print("")
    print(SEPARATOR)
    print("  Experiment 8c COMPLETE - Variation A worked")
    print(SEPARATOR)
    sys.exit(0)

except Exception as e:
    print("  [FAIL] Variation A: {} - {}".format(type(e).__name__, e))
    traceback.print_exc()
    sys.stdout.flush()

# Clean up for next variation
try:
    del mdb.optimizationProcesses['BlockOpt']
except:
    pass
try:
    del mdb.jobs['Block_Proto']
except:
    pass

# ============================================================================
# [3/5] Variation B: OptProcess -> save .cae -> writeParAndInputFiles()
# ============================================================================
phase_header(3, TOTAL, "Variation B: OptProcess -> save -> writePar")

try:
    protoJob = mdb.Job(name='Block_Proto', model='Model-1',
        numCpus=1, numDomains=1)

    optProcess = mdb.OptimizationProcess(
        name='BlockOpt',
        model='Model-1',
        task='TopOpt',
        prototypeJob='Block_Proto',
        maxDesignCycle=20,
    )
    print("  OptimizationProcess created (before save)")

    mdb.saveAs('exp8c.cae')
    print("  Saved exp8c.cae (after OptProcess)")

    optProcess.writeParAndInputFiles()
    print("  [OK] writeParAndInputFiles() SUCCEEDED (Variation B)")
    list_files("Generated files")
    print("")
    print(SEPARATOR)
    print("  Experiment 8c COMPLETE - Variation B worked")
    print(SEPARATOR)
    sys.exit(0)

except Exception as e:
    print("  [FAIL] Variation B: {} - {}".format(type(e).__name__, e))
    traceback.print_exc()
    sys.stdout.flush()

# Clean up
try:
    del mdb.optimizationProcesses['BlockOpt']
except:
    pass
try:
    del mdb.jobs['Block_Proto']
except:
    pass

# ============================================================================
# [4/5] Variation C: writeInput() on proto job -> OptProcess -> writePar
# ============================================================================
phase_header(4, TOTAL, "Variation C: writeInput -> OptProcess -> writePar")

try:
    protoJob = mdb.Job(name='Block_Proto', model='Model-1',
        numCpus=1, numDomains=1)
    print("  Proto job created")

    protoJob.writeInput()
    print("  writeInput() done - Block_Proto.inp exists: {}".format(
        os.path.exists('Block_Proto.inp')))

    mdb.saveAs('exp8c.cae')

    optProcess = mdb.OptimizationProcess(
        name='BlockOpt',
        model='Model-1',
        task='TopOpt',
        prototypeJob='Block_Proto',
        maxDesignCycle=20,
    )
    print("  OptimizationProcess created")

    optProcess.writeParAndInputFiles()
    print("  [OK] writeParAndInputFiles() SUCCEEDED (Variation C)")
    list_files("Generated files")
    print("")
    print(SEPARATOR)
    print("  Experiment 8c COMPLETE - Variation C worked")
    print(SEPARATOR)
    sys.exit(0)

except Exception as e:
    print("  [FAIL] Variation C: {} - {}".format(type(e).__name__, e))
    traceback.print_exc()
    sys.stdout.flush()

# Clean up
try:
    del mdb.optimizationProcesses['BlockOpt']
except:
    pass
try:
    del mdb.jobs['Block_Proto']
except:
    pass

# ============================================================================
# [5/5] Variation D: Run FEA first -> OptProcess -> writePar
# ============================================================================
phase_header(5, TOTAL, "Variation D: run FEA -> OptProcess -> writePar")

try:
    protoJob = mdb.Job(name='Block_Proto', model='Model-1',
        numCpus=1, numDomains=1)
    print("  Proto job created")
    print("  Submitting FEA...")
    sys.stdout.flush()

    protoJob.submit()
    protoJob.waitForCompletion()
    print("  FEA completed. ODB exists: {}".format(
        os.path.exists('Block_Proto.odb')))

    mdb.saveAs('exp8c.cae')

    optProcess = mdb.OptimizationProcess(
        name='BlockOpt',
        model='Model-1',
        task='TopOpt',
        prototypeJob='Block_Proto',
        maxDesignCycle=20,
    )
    print("  OptimizationProcess created")

    optProcess.writeParAndInputFiles()
    print("  [OK] writeParAndInputFiles() SUCCEEDED (Variation D)")
    list_files("Generated files")
    print("")
    print(SEPARATOR)
    print("  Experiment 8c COMPLETE - Variation D worked")
    print(SEPARATOR)
    sys.exit(0)

except Exception as e:
    print("  [FAIL] Variation D: {} - {}".format(type(e).__name__, e))
    traceback.print_exc()
    sys.stdout.flush()

# If we get here, all variations failed
print("")
print(SEPARATOR)
print("  Experiment 8c: ALL VARIATIONS FAILED")
print(SEPARATOR)
list_files("Files in working directory")
sys.exit(1)
