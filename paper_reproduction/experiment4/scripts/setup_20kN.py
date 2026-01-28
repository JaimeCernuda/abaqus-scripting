import os
from abaqus import *
from abaqusConstants import *
from caeModules import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')
openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v19.cae')

model = mdb.models['Experiment4_TO_Specimen']
part = model.parts['TO_Specimen']
assembly = model.rootAssembly
instance = assembly.instances['TO_Specimen-1']

TOTAL_HEIGHT = 146.17
BLOCK_HEIGHT_Y = 28.0
BLOCK_WIDTH_X = 18.0
PIN_RADIUS = 6.35
HALF_WIDTH = 32.3
HALF_THICK = 12.5

UPPER_PIN_Y = TOTAL_HEIGHT - BLOCK_HEIGHT_Y / 2.0
LOWER_PIN_Y = BLOCK_HEIGHT_Y / 2.0
UB_LEFT = -BLOCK_WIDTH_X / 2.0
UB_RIGHT = BLOCK_WIDTH_X / 2.0
LB_LEFT_XMIN = -HALF_WIDTH
LB_LEFT_XMAX = -HALF_WIDTH + BLOCK_WIDTH_X
LB_RIGHT_XMIN = HALF_WIDTH - BLOCK_WIDTH_X
LB_RIGHT_XMAX = HALF_WIDTH

# Create step
model.StaticStep(name='FatigueTest', previous='Initial', nlgeom=ON, initialInc=0.1, maxNumInc=100, minInc=1e-8)

# Find pin hole surfaces
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

with open('setup_debug.txt', 'w') as f:
    f.write('Lower left faces: {}\n'.format(len(lower_left_faces)))
    f.write('Lower right faces: {}\n'.format(len(lower_right_faces)))
    f.write('Upper faces: {}\n'.format(len(upper_faces)))

if len(lower_left_faces) > 0:
    assembly.Set(faces=lower_left_faces, name='LowerLeftPinHole')
    model.DisplacementBC(name='LowerLeftPin_BC', createStepName='Initial',
        region=assembly.sets['LowerLeftPinHole'], u1=UNSET, u2=0.0, u3=0.0)
if len(lower_right_faces) > 0:
    assembly.Set(faces=lower_right_faces, name='LowerRightPinHole')
    model.DisplacementBC(name='LowerRightPin_BC', createStepName='Initial',
        region=assembly.sets['LowerRightPinHole'], u1=UNSET, u2=0.0, u3=0.0)
if len(upper_faces) > 0:
    assembly.Set(faces=upper_faces, name='UpperPinHole')
    assembly.Surface(side1Faces=upper_faces, name='UpperPinSurface')

upper_rp = assembly.ReferencePoint(point=(0.0, UPPER_PIN_Y, HALF_THICK))
upper_rp_region = assembly.Set(referencePoints=(assembly.referencePoints[upper_rp.id],), name='UpperRP')

if len(upper_faces) > 0:
    model.Coupling(name='UpperPinCoupling', controlPoint=upper_rp_region,
        surface=assembly.surfaces['UpperPinSurface'], influenceRadius=WHOLE_SURFACE,
        couplingType=KINEMATIC, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)

model.ConcentratedForce(name='VerticalLoad_20kN', createStepName='FatigueTest',
    region=upper_rp_region, cf2=20000.0)

model.fieldOutputRequests['F-Output-1'].setValues(variables=('S', 'E', 'PE', 'PEEQ', 'U', 'RF'))

job_name = 'Job_v19'
mdb.Job(name=job_name, model='Experiment4_TO_Specimen', type=ANALYSIS, numCpus=1)

mdb.saveAs(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v19.cae')

# Write input
mdb.jobs[job_name].writeInput()
print('Setup complete, input written')
