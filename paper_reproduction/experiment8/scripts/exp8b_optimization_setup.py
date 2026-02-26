# -*- coding: utf-8 -*-
"""
Experiment 8b: Optimization setup validation (no run).

Same model as 8a, plus: TopologyTask, design responses, objective function,
constraint, and frozen area. Does NOT create OptimizationProcess.

Validates that all optimization API calls succeed in noGUI mode.
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

TOTAL = 9

print(SEPARATOR)
print("  EXPERIMENT 8b: Optimization Setup Validation")
print("  Mesh size: {}".format(MESH_SIZE))
print(SEPARATOR)

# ============================================================================
# [1/9] Create model and part
# ============================================================================
phase_header(1, TOTAL, "Create model and part")

model = mdb.models['Model-1']

sketch = model.ConstrainedSketch(name='sketch', sheetSize=200.0)
sketch.rectangle(point1=(0.0, 0.0), point2=(100.0, 40.0))
part = model.Part(name='Block', dimensionality=THREE_D, type=DEFORMABLE_BODY)
part.BaseSolidExtrude(sketch=sketch, depth=20.0)
print("  Part 'Block' created: 100x40x20 mm")

# ============================================================================
# [2/9] Create sets and surfaces on part
# ============================================================================
phase_header(2, TOTAL, "Create sets and surfaces")

part.Set(name='AllCells', cells=part.cells.findAt(coordinates=((50.0, 20.0, 10.0),)))
part.Set(name='FixedFace', faces=part.faces.findAt(coordinates=((0.0, 20.0, 10.0),)))
part.Surface(name='LoadSurface', side1Faces=part.faces.findAt(coordinates=((100.0, 20.0, 10.0),)))
print("  Sets: AllCells, FixedFace")
print("  Surfaces: LoadSurface")

# ============================================================================
# [3/9] Material and section
# ============================================================================
phase_header(3, TOTAL, "Material and section")

mat = model.Material(name='Steel')
mat.Elastic(table=((210000.0, 0.3),))
mat.Density(table=((7.85e-9,),))

model.HomogeneousSolidSection(name='Section', material='Steel', thickness=None)
part.SectionAssignment(region=part.sets['AllCells'], sectionName='Section')
print("  Material 'Steel' and section assigned")

# ============================================================================
# [4/9] Assembly
# ============================================================================
phase_header(4, TOTAL, "Assembly")

model.rootAssembly.DatumCsysByDefault(CARTESIAN)
instance = model.rootAssembly.Instance(name='Block-1', part=part, dependent=ON)
print("  Instance 'Block-1' created (dependent=ON)")

# ============================================================================
# [5/9] Step, output, BC, load
# ============================================================================
phase_header(5, TOTAL, "Step, output, BC, load")

model.StaticStep(name='LoadStep', previous='Initial',
    timePeriod=1.0, initialInc=1.0, maxInc=1.0, minInc=1e-6)

model.FieldOutputRequest('F-Output-1', createStepName='LoadStep',
    variables=('S', 'E', 'U', 'RF', 'ENER'))

model.EncastreBC(name='Fixed', createStepName='Initial',
    region=instance.sets['FixedFace'])

model.Pressure(name='Load', createStepName='LoadStep',
    region=instance.surfaces['LoadSurface'], magnitude=1.0)
print("  Step, output, BC, load configured")

# ============================================================================
# [6/9] Mesh
# ============================================================================
phase_header(6, TOTAL, "Mesh")

elem1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
elem2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elem3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elem1, elem2, elem3))
part.seedPart(size=MESH_SIZE)
part.generateMesh()
print("  Mesh: {} nodes, {} elements".format(len(part.nodes), len(part.elements)))

# ============================================================================
# [7/9] Frozen elements set
# ============================================================================
phase_header(7, TOTAL, "Frozen elements set")

p = model.parts['Block']
frozen_labels = set()
for elem in p.elements:
    for nidx in elem.connectivity:
        if abs(p.nodes[nidx].coordinates[0]) < 0.01:
            frozen_labels.add(elem.label)
            break

print("  Found {} frozen element labels (touching x=0 face)".format(len(frozen_labels)))

# Create set on PART (dependent=ON instances inherit part sets)
frozen_part_elems = [e for e in p.elements if e.label in frozen_labels]
if frozen_part_elems:
    p.Set(name='FrozenElems', elements=mesh.MeshElementArray(frozen_part_elems))
    print("  Part set 'FrozenElems' created with {} elements".format(len(frozen_part_elems)))
    print("  Available via instance.sets['FrozenElems'] (dependent=ON)")
else:
    print("  WARNING: No frozen elements found on part!")

# ============================================================================
# [8/9] Topology optimization setup
# ============================================================================
phase_header(8, TOTAL, "Topology optimization setup")

# TopologyTask
try:
    model.TopologyTask(
        name='TopOpt',
        region=MODEL,
        freezeBoundaryConditionRegions=ON,
        freezeLoadRegions=ON,
        materialInterpolationTechnique=SIMP,
        materialInterpolationPenalty=3.0,
    )
    task = model.optimizationTasks['TopOpt']
    print("  [OK] TopologyTask 'TopOpt' created")
except Exception as e:
    print("  [FAIL] TopologyTask: {} - {}".format(type(e).__name__, e))
    traceback.print_exc()
    sys.exit(1)

# Design response: strain energy
try:
    task.SingleTermDesignResponse(
        name='DR_StrainEnergy',
        identifier='STRAIN_ENERGY',
        region=MODEL,
        operation=SUM,
    )
    print("  [OK] DR_StrainEnergy created")
except Exception as e:
    print("  [FAIL] DR_StrainEnergy: {} - {}".format(type(e).__name__, e))
    traceback.print_exc()

# Design response: volume
try:
    task.SingleTermDesignResponse(
        name='DR_Volume',
        identifier='VOLUME',
        region=MODEL,
        operation=SUM,
    )
    print("  [OK] DR_Volume created")
except Exception as e:
    print("  [FAIL] DR_Volume: {} - {}".format(type(e).__name__, e))
    traceback.print_exc()

# Objective function
try:
    task.ObjectiveFunction(
        name='MinStrainEnergy',
        objectives=((OFF, 'DR_StrainEnergy', 1.0, 0.0, ''),),
        target=MINIMIZE,
    )
    print("  [OK] ObjectiveFunction 'MinStrainEnergy' created")
except Exception as e:
    print("  [FAIL] ObjectiveFunction: {} - {}".format(type(e).__name__, e))
    traceback.print_exc()

# Constraint
try:
    task.OptimizationConstraint(
        name='VolumeConstraint',
        designResponse='DR_Volume',
        restrictionValue=0.5,
        restrictionMethod=RELATIVE_LESS_THAN_EQUAL,
    )
    print("  [OK] OptimizationConstraint 'VolumeConstraint' created")
except Exception as e:
    print("  [FAIL] OptimizationConstraint: {} - {}".format(type(e).__name__, e))
    traceback.print_exc()

# Frozen area
try:
    task.FrozenArea(
        name='FrozenBC',
        region=instance.sets['FrozenElems'],
    )
    print("  [OK] FrozenArea 'FrozenBC' created")
except Exception as e:
    print("  [FAIL] FrozenArea: {} - {}".format(type(e).__name__, e))
    traceback.print_exc()

# ============================================================================
# [9/9] Verification and save
# ============================================================================
phase_header(9, TOTAL, "Verification and save")

print("  Design responses: {}".format(task.designResponses.keys()))
print("  Objective functions: {}".format(task.objectiveFunctions.keys()))
print("  Constraints: {}".format(task.optimizationConstraints.keys()))
print("  Geometric restrictions: {}".format(task.geometricRestrictions.keys()))

mdb.saveAs('exp8b.cae')
print("  Saved exp8b.cae")

print("")
print(SEPARATOR)
print("  Experiment 8b COMPLETE")
print(SEPARATOR)
