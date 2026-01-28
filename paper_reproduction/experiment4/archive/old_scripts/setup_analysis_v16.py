# -*- coding: utf-8 -*-
from abaqus import *
from abaqusConstants import *
from caeModules import *
import regionToolset

openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v17.cae')

model_name = 'Experiment4_TO_Specimen'
part_name = 'TO_Specimen'
instance_name = part_name + '-1'

model = mdb.models[model_name]
part = model.parts[part_name]
assembly = model.rootAssembly
instance = assembly.instances[instance_name]

TOTAL_HEIGHT = 146.17
TOTAL_WIDTH = 64.60
THICKNESS = 25.0
BLOCK_WIDTH_X = 18.0
BLOCK_HEIGHT_Y = 28.0
PIN_DIAMETER = 12.7
PIN_RADIUS = PIN_DIAMETER / 2.0

HALF_WIDTH = TOTAL_WIDTH / 2.0
HALF_THICK = THICKNESS / 2.0

UPPER_PIN_Y = TOTAL_HEIGHT - BLOCK_HEIGHT_Y / 2.0
LOWER_PIN_Y = BLOCK_HEIGHT_Y / 2.0

UB_LEFT = -BLOCK_WIDTH_X / 2.0
UB_RIGHT = BLOCK_WIDTH_X / 2.0
LB_LEFT_XMIN = -HALF_WIDTH
LB_LEFT_XMAX = -HALF_WIDTH + BLOCK_WIDTH_X
LB_RIGHT_XMIN = HALF_WIDTH - BLOCK_WIDTH_X
LB_RIGHT_XMAX = HALF_WIDTH

if 'IN718' not in model.materials.keys():
    mat = model.Material(name='IN718')
    mat.Elastic(table=((200000.0, 0.3),))
    mat.Density(table=((8.19e-9,),))
    mat.Plastic(table=((980.0, 0.0), (1100.0, 0.05), (1241.0, 0.10)))

if 'SolidSection' not in model.sections.keys():
    model.HomogeneousSolidSection(name='SolidSection', material='IN718', thickness=None)

all_cells = part.cells
if len(all_cells) > 0:
    region = part.Set(cells=all_cells, name='AllCells')
    part.SectionAssignment(region=region, sectionName='SolidSection')

for name in list(model.steps.keys()):
    if name != 'Initial':
        del model.steps[name]
for name in list(model.boundaryConditions.keys()):
    del model.boundaryConditions[name]
for name in list(model.loads.keys()):
    del model.loads[name]
for name in list(model.constraints.keys()):
    del model.constraints[name]

model.StaticStep(name='FatigueTest', previous='Initial', nlgeom=ON, initialInc=0.1, maxNumInc=100, minInc=1e-8)

lower_left_faces = instance.faces.getByBoundingCylinder(
    center1=(LB_LEFT_XMIN - 1, LOWER_PIN_Y, HALF_THICK),
    center2=(LB_LEFT_XMAX + 1, LOWER_PIN_Y, HALF_THICK),
    radius=PIN_RADIUS + 0.5)
lower_right_faces = instance.faces.getByBoundingCylinder(
    center1=(LB_RIGHT_XMIN - 1, LOWER_PIN_Y, HALF_THICK),
    center2=(LB_RIGHT_XMAX + 1, LOWER_PIN_Y, HALF_THICK),
    radius=PIN_RADIUS + 0.5)
upper_faces = instance.faces.getByBoundingCylinder(
    center1=(UB_LEFT - 1, UPPER_PIN_Y, HALF_THICK),
    center2=(UB_RIGHT + 1, UPPER_PIN_Y, HALF_THICK),
    radius=PIN_RADIUS + 0.5)

if len(lower_left_faces) > 0:
    assembly.Set(faces=lower_left_faces, name='LowerLeftPinHole')
    assembly.Surface(side1Faces=lower_left_faces, name='LowerLeftPinSurface')
if len(lower_right_faces) > 0:
    assembly.Set(faces=lower_right_faces, name='LowerRightPinHole')
    assembly.Surface(side1Faces=lower_right_faces, name='LowerRightPinSurface')
if len(upper_faces) > 0:
    assembly.Set(faces=upper_faces, name='UpperPinHole')
    assembly.Surface(side1Faces=upper_faces, name='UpperPinSurface')

if len(lower_left_faces) > 0:
    model.DisplacementBC(name='LowerLeftPin_BC', createStepName='Initial',
        region=assembly.sets['LowerLeftPinHole'], u1=UNSET, u2=0.0, u3=0.0)
if len(lower_right_faces) > 0:
    model.DisplacementBC(name='LowerRightPin_BC', createStepName='Initial',
        region=assembly.sets['LowerRightPinHole'], u1=UNSET, u2=0.0, u3=0.0)

upper_rp = assembly.ReferencePoint(point=(0.0, UPPER_PIN_Y, HALF_THICK))
upper_rp_region = assembly.Set(referencePoints=(assembly.referencePoints[upper_rp.id],), name='UpperRP')

if len(upper_faces) > 0:
    model.Coupling(name='UpperPinCoupling', controlPoint=upper_rp_region,
        surface=assembly.surfaces['UpperPinSurface'], influenceRadius=WHOLE_SURFACE,
        couplingType=KINEMATIC, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)

model.ConcentratedForce(name='VerticalLoad_20kN', createStepName='FatigueTest',
    region=upper_rp_region, cf2=20000.0)

assembly.regenerate()
part.seedPart(size=4.0, deviationFactor=0.1, minSizeFactor=0.1)
elemType1 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType1,))
part.generateMesh()

model.fieldOutputRequests['F-Output-1'].setValues(variables=('S', 'E', 'PE', 'PEEQ', 'U', 'RF'))

job_name = 'Job_FatigueTest_v16'
if job_name in mdb.jobs.keys():
    del mdb.jobs[job_name]
mdb.Job(name=job_name, model=model_name, type=ANALYSIS, numCpus=1, numDomains=1, memory=90, memoryUnits=PERCENTAGE)

mdb.saveAs(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v17.cae')
print('SETUP COMPLETE - {} nodes, {} elements'.format(len(part.nodes), len(part.elements)))
