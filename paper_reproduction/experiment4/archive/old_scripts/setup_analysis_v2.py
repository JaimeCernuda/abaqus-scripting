# -*- coding: utf-8 -*-
"""
Experiment 4: Setup Analysis - Simplified Version
Only FatigueTest step with vertical load
"""

from abaqus import *
from abaqusConstants import *
from caeModules import *
import regionToolset

# Open existing model
openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen.cae')

model_name = 'Experiment4_TO_Specimen'
part_name = 'TO_Specimen'
instance_name = part_name + '-1'

model = mdb.models[model_name]
part = model.parts[part_name]
assembly = model.rootAssembly
instance = assembly.instances[instance_name]

# =============================================================================
# GEOMETRY PARAMETERS
# =============================================================================
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
LEFT_BLOCK_CENTER_X = -HALF_WIDTH + BLOCK_WIDTH_X / 2.0
RIGHT_BLOCK_CENTER_X = HALF_WIDTH - BLOCK_WIDTH_X / 2.0

# =============================================================================
# CLEAN UP - Delete existing steps, BCs, loads, constraints
# =============================================================================
# Delete steps except Initial
for name in list(model.steps.keys()):
    if name != 'Initial':
        del model.steps[name]

# Delete all BCs
for name in list(model.boundaryConditions.keys()):
    del model.boundaryConditions[name]

# Delete all loads
for name in list(model.loads.keys()):
    del model.loads[name]

# Delete all constraints
for name in list(model.constraints.keys()):
    del model.constraints[name]

# Reference points will be overwritten if they exist

# Delete sets/surfaces that we'll recreate
sets_to_delete = ['LowerLeftPinHole', 'LowerRightPinHole', 'UpperPinHole',
                  'UpperRP', 'LowerLeftRP', 'LowerRightRP', 'UpperPinSurface']
for name in sets_to_delete:
    if name in assembly.sets.keys():
        del assembly.sets[name]
    if name in assembly.surfaces.keys():
        del assembly.surfaces[name]

print("Cleanup complete")

# =============================================================================
# CREATE SINGLE STEP
# =============================================================================
model.StaticStep(
    name='FatigueTest',
    previous='Initial',
    nlgeom=ON,
    initialInc=0.1,
    maxNumInc=100,
    minInc=1e-8,
)
print("Step 'FatigueTest' created")

# =============================================================================
# FIND PIN HOLE SURFACES
# =============================================================================
lower_left_faces = instance.faces.getByBoundingCylinder(
    center1=(LEFT_BLOCK_CENTER_X, LOWER_PIN_Y, -0.1),
    center2=(LEFT_BLOCK_CENTER_X, LOWER_PIN_Y, THICKNESS + 0.1),
    radius=PIN_RADIUS + 0.5
)
print("Found {} faces for lower left pin".format(len(lower_left_faces)))

lower_right_faces = instance.faces.getByBoundingCylinder(
    center1=(RIGHT_BLOCK_CENTER_X, LOWER_PIN_Y, -0.1),
    center2=(RIGHT_BLOCK_CENTER_X, LOWER_PIN_Y, THICKNESS + 0.1),
    radius=PIN_RADIUS + 0.5
)
print("Found {} faces for lower right pin".format(len(lower_right_faces)))

upper_faces = instance.faces.getByBoundingCylinder(
    center1=(0.0, UPPER_PIN_Y, -0.1),
    center2=(0.0, UPPER_PIN_Y, THICKNESS + 0.1),
    radius=PIN_RADIUS + 0.5
)
print("Found {} faces for upper pin".format(len(upper_faces)))

# Create sets
if len(lower_left_faces) > 0:
    assembly.Set(faces=lower_left_faces, name='LowerLeftPinHole')
if len(lower_right_faces) > 0:
    assembly.Set(faces=lower_right_faces, name='LowerRightPinHole')
if len(upper_faces) > 0:
    assembly.Set(faces=upper_faces, name='UpperPinHole')
    assembly.Surface(side1Faces=upper_faces, name='UpperPinSurface')

# =============================================================================
# BOUNDARY CONDITIONS - Fix lower pin holes in Y and Z
# =============================================================================
if len(lower_left_faces) > 0:
    model.DisplacementBC(
        name='LowerLeftPin_BC',
        createStepName='Initial',
        region=assembly.sets['LowerLeftPinHole'],
        u1=UNSET,  # X free
        u2=0.0,    # Y fixed
        u3=0.0,    # Z fixed
    )
    print("BC 'LowerLeftPin_BC' created")

if len(lower_right_faces) > 0:
    model.DisplacementBC(
        name='LowerRightPin_BC',
        createStepName='Initial',
        region=assembly.sets['LowerRightPinHole'],
        u1=UNSET,
        u2=0.0,
        u3=0.0,
    )
    print("BC 'LowerRightPin_BC' created")

# =============================================================================
# REFERENCE POINT AND COUPLING FOR UPPER PIN
# =============================================================================
upper_rp = assembly.ReferencePoint(point=(0.0, UPPER_PIN_Y, HALF_THICK))
upper_rp_id = upper_rp.id
upper_rp_region = assembly.Set(referencePoints=(assembly.referencePoints[upper_rp_id],), name='UpperRP')
print("Upper reference point created")

if len(upper_faces) > 0:
    model.Coupling(
        name='UpperPinCoupling',
        controlPoint=upper_rp_region,
        surface=assembly.surfaces['UpperPinSurface'],
        influenceRadius=WHOLE_SURFACE,
        couplingType=KINEMATIC,
        u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON
    )
    print("Upper pin coupling created")

# =============================================================================
# LOAD - 20 kN vertical (Y direction)
# =============================================================================
model.ConcentratedForce(
    name='VerticalLoad_20kN',
    createStepName='FatigueTest',
    region=upper_rp_region,
    cf2=20000.0,  # 20 kN in +Y direction
)
print("Load 20 kN applied in Y direction")

# =============================================================================
# SAVE
# =============================================================================
mdb.saveAs(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen.cae')

print("\n" + "="*50)
print("SIMPLIFIED ANALYSIS SETUP COMPLETE")
print("Step: FatigueTest")
print("BCs: Lower pins fixed in Y,Z")
print("Load: 20 kN vertical at upper pin")
print("="*50)
