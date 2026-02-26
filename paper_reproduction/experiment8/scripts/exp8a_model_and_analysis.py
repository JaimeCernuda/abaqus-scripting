# -*- coding: utf-8 -*-
"""
Experiment 8a: Validate model + static analysis in noGUI mode.

Creates a 100x40x20 block, steel, encastre on x=0 face, pressure on x=100 face.
Submits a static analysis job and waits for completion.

Follows abqpy compression.py pattern exactly.
"""

from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import *
import os, sys

executeOnCaeStartup()

SEPARATOR = "=" * 70
MESH_SIZE = float(os.environ.get('ABAQUS_MESH_SIZE', '5.0'))

def phase_header(num, total, title):
    print("")
    print(SEPARATOR)
    print("  [{}/{}] {}".format(num, total, title))
    print(SEPARATOR)
    sys.stdout.flush()

TOTAL = 7

print(SEPARATOR)
print("  EXPERIMENT 8a: Model Validation + Static Analysis")
print("  Mesh size: {}".format(MESH_SIZE))
print(SEPARATOR)

# ============================================================================
# [1/7] Create model and part
# ============================================================================
phase_header(1, TOTAL, "Create model and part")

model = mdb.models['Model-1']

sketch = model.ConstrainedSketch(name='sketch', sheetSize=200.0)
sketch.rectangle(point1=(0.0, 0.0), point2=(100.0, 40.0))
part = model.Part(name='Block', dimensionality=THREE_D, type=DEFORMABLE_BODY)
part.BaseSolidExtrude(sketch=sketch, depth=20.0)
print("  Part 'Block' created: 100x40x20 mm")

# ============================================================================
# [2/7] Create sets and surfaces on part
# ============================================================================
phase_header(2, TOTAL, "Create sets and surfaces")

part.Set(name='AllCells', cells=part.cells.findAt(coordinates=((50.0, 20.0, 10.0),)))
part.Set(name='FixedFace', faces=part.faces.findAt(coordinates=((0.0, 20.0, 10.0),)))
part.Surface(name='LoadSurface', side1Faces=part.faces.findAt(coordinates=((100.0, 20.0, 10.0),)))
print("  Sets: AllCells, FixedFace")
print("  Surfaces: LoadSurface")

# ============================================================================
# [3/7] Material and section
# ============================================================================
phase_header(3, TOTAL, "Material and section")

mat = model.Material(name='Steel')
mat.Elastic(table=((210000.0, 0.3),))
mat.Density(table=((7.85e-9,),))
print("  Material 'Steel': E=210000 MPa, nu=0.3, rho=7.85e-9 tonne/mm^3")

model.HomogeneousSolidSection(name='Section', material='Steel', thickness=None)
part.SectionAssignment(region=part.sets['AllCells'], sectionName='Section')
print("  Section assigned to AllCells")

# ============================================================================
# [4/7] Assembly
# ============================================================================
phase_header(4, TOTAL, "Assembly")

model.rootAssembly.DatumCsysByDefault(CARTESIAN)
instance = model.rootAssembly.Instance(name='Block-1', part=part, dependent=ON)
print("  Instance 'Block-1' created (dependent=ON)")

# ============================================================================
# [5/7] Step, output, BC, load
# ============================================================================
phase_header(5, TOTAL, "Step, output, BC, load")

model.StaticStep(name='LoadStep', previous='Initial',
    timePeriod=1.0, initialInc=1.0, maxInc=1.0, minInc=1e-6)
print("  StaticStep 'LoadStep' created")

model.FieldOutputRequest('F-Output-1', createStepName='LoadStep',
    variables=('S', 'E', 'U', 'RF', 'ENER'))
print("  Field output request created")

model.EncastreBC(name='Fixed', createStepName='Initial',
    region=instance.sets['FixedFace'])
print("  Encastre BC on x=0 face")

model.Pressure(name='Load', createStepName='LoadStep',
    region=instance.surfaces['LoadSurface'], magnitude=1.0)
print("  Pressure load (1.0 MPa) on x=100 face")

# ============================================================================
# [6/7] Mesh (part-level, compression.py pattern)
# ============================================================================
phase_header(6, TOTAL, "Mesh")

elem1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
elem2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elem3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elem1, elem2, elem3))
part.seedPart(size=MESH_SIZE)
part.generateMesh()
print("  Mesh generated: {} nodes, {} elements".format(
    len(part.nodes), len(part.elements)))

# ============================================================================
# [7/7] Job: submit and wait
# ============================================================================
phase_header(7, TOTAL, "Submit job")

job = mdb.Job(name='Block_Analysis', model='Model-1')
print("  Submitting 'Block_Analysis'...")
sys.stdout.flush()

job.submit()
job.waitForCompletion()

print("  Job completed.")

# Check for .odb
if os.path.exists('Block_Analysis.odb'):
    print("  Block_Analysis.odb exists ({} bytes)".format(
        os.path.getsize('Block_Analysis.odb')))
else:
    print("  WARNING: Block_Analysis.odb NOT found!")

# Print .dat summary
if os.path.exists('Block_Analysis.dat'):
    with open('Block_Analysis.dat') as f:
        dat = f.read()
    if 'ERROR' in dat.upper():
        print("  WARNING: Errors found in .dat file!")
        for line in dat.split('\n'):
            if 'ERROR' in line.upper():
                print("    " + line.strip())
    else:
        print("  No errors in .dat file")

# Save
mdb.saveAs('exp8a.cae')

print("")
print(SEPARATOR)
print("  Experiment 8a COMPLETE")
print(SEPARATOR)
