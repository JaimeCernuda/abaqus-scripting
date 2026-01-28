# -*- coding: utf-8 -*-
"""
Experiment 4: Setup Analysis - Steps, BCs, Loads
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
# GEOMETRY PARAMETERS (from create_geometry_v2.py)
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

# Upper pin Y position
UPPER_PIN_Y = TOTAL_HEIGHT - BLOCK_HEIGHT_Y / 2.0  # 132.17

# Lower pin Y position
LOWER_PIN_Y = BLOCK_HEIGHT_Y / 2.0  # 14.0

# Lower block X centers
LEFT_BLOCK_CENTER_X = -HALF_WIDTH + BLOCK_WIDTH_X / 2.0  # -23.3
RIGHT_BLOCK_CENTER_X = HALF_WIDTH - BLOCK_WIDTH_X / 2.0  # 23.3

# =============================================================================
# DELETE EXISTING STEPS (if any, except Initial)
# =============================================================================
step_names = model.steps.keys()
for name in step_names:
    if name != 'Initial':
        del model.steps[name]

# =============================================================================
# CREATE ANALYSIS STEPS
# =============================================================================
# Step 1: FatigueTest - 20 kN vertical load only
model.StaticStep(
    name='FatigueTest',
    previous='Initial',
    nlgeom=ON,          # Nonlinear geometry
    initialInc=0.1,
    maxNumInc=100,
    minInc=1e-8,
)
print("Step 'FatigueTest' created")

# Step 2: TODesign - Additional horizontal loads (builds on step 1)
model.StaticStep(
    name='TODesign',
    previous='FatigueTest',
    nlgeom=ON,
    initialInc=0.1,
    maxNumInc=100,
    minInc=1e-8,
)
print("Step 'TODesign' created")

# =============================================================================
# FIND PIN HOLE SURFACES FOR BCs
# Using cylindrical pin hole interior surfaces
# =============================================================================

# Lower left pin hole - find the cylindrical surface inside the left block
# The pin hole is at X = LEFT_BLOCK_CENTER_X, Y = LOWER_PIN_Y, Z = 0 to THICKNESS
lower_left_faces = instance.faces.getByBoundingCylinder(
    center1=(LEFT_BLOCK_CENTER_X, LOWER_PIN_Y, -0.1),
    center2=(LEFT_BLOCK_CENTER_X, LOWER_PIN_Y, THICKNESS + 0.1),
    radius=PIN_RADIUS + 0.5
)
print("Found {} faces for lower left pin".format(len(lower_left_faces)))

# Lower right pin hole
lower_right_faces = instance.faces.getByBoundingCylinder(
    center1=(RIGHT_BLOCK_CENTER_X, LOWER_PIN_Y, -0.1),
    center2=(RIGHT_BLOCK_CENTER_X, LOWER_PIN_Y, THICKNESS + 0.1),
    radius=PIN_RADIUS + 0.5
)
print("Found {} faces for lower right pin".format(len(lower_right_faces)))

# Upper pin hole
upper_faces = instance.faces.getByBoundingCylinder(
    center1=(0.0, UPPER_PIN_Y, -0.1),
    center2=(0.0, UPPER_PIN_Y, THICKNESS + 0.1),
    radius=PIN_RADIUS + 0.5
)
print("Found {} faces for upper pin".format(len(upper_faces)))

# Create sets for the pin hole surfaces
if len(lower_left_faces) > 0:
    assembly.Set(faces=lower_left_faces, name='LowerLeftPinHole')
if len(lower_right_faces) > 0:
    assembly.Set(faces=lower_right_faces, name='LowerRightPinHole')
if len(upper_faces) > 0:
    assembly.Set(faces=upper_faces, name='UpperPinHole')
    assembly.Surface(side1Faces=upper_faces, name='UpperPinSurface')

# =============================================================================
# BOUNDARY CONDITIONS
# Paper: "Fixed in Y and Z at lower pins; translation along and rotation about X permitted"
# =============================================================================

# Lower left pin BC
if len(lower_left_faces) > 0:
    lower_left_region = assembly.sets['LowerLeftPinHole']
    model.DisplacementBC(
        name='LowerLeftPin_BC',
        createStepName='Initial',
        region=lower_left_region,
        u1=UNSET,    # X translation FREE
        u2=0.0,      # Y translation FIXED
        u3=0.0,      # Z translation FIXED
        ur1=UNSET,   # X rotation FREE (if DOFs exist)
        ur2=UNSET,   # Y rotation - let it be free for solid elements
        ur3=UNSET,   # Z rotation - let it be free for solid elements
    )
    print("BC 'LowerLeftPin_BC' created")

# Lower right pin BC
if len(lower_right_faces) > 0:
    lower_right_region = assembly.sets['LowerRightPinHole']
    model.DisplacementBC(
        name='LowerRightPin_BC',
        createStepName='Initial',
        region=lower_right_region,
        u1=UNSET,
        u2=0.0,
        u3=0.0,
        ur1=UNSET,
        ur2=UNSET,
        ur3=UNSET,
    )
    print("BC 'LowerRightPin_BC' created")

# =============================================================================
# REFERENCE POINTS FOR LOAD APPLICATION
# =============================================================================
# Upper pin reference point (for applying vertical load via coupling)
upper_rp = assembly.ReferencePoint(point=(0.0, UPPER_PIN_Y, HALF_THICK))
upper_rp_id = upper_rp.id
upper_rp_region = assembly.Set(referencePoints=(assembly.referencePoints[upper_rp_id],), name='UpperRP')
print("Upper reference point created at (0, {:.1f}, {:.1f})".format(UPPER_PIN_Y, HALF_THICK))

# Lower left reference point
lower_left_rp = assembly.ReferencePoint(point=(LEFT_BLOCK_CENTER_X, LOWER_PIN_Y, HALF_THICK))
lower_left_rp_id = lower_left_rp.id
lower_left_rp_region = assembly.Set(referencePoints=(assembly.referencePoints[lower_left_rp_id],), name='LowerLeftRP')
print("Lower left RP created at ({:.1f}, {:.1f}, {:.1f})".format(LEFT_BLOCK_CENTER_X, LOWER_PIN_Y, HALF_THICK))

# Lower right reference point
lower_right_rp = assembly.ReferencePoint(point=(RIGHT_BLOCK_CENTER_X, LOWER_PIN_Y, HALF_THICK))
lower_right_rp_id = lower_right_rp.id
lower_right_rp_region = assembly.Set(referencePoints=(assembly.referencePoints[lower_right_rp_id],), name='LowerRightRP')
print("Lower right RP created at ({:.1f}, {:.1f}, {:.1f})".format(RIGHT_BLOCK_CENTER_X, LOWER_PIN_Y, HALF_THICK))

# =============================================================================
# COUPLING CONSTRAINTS
# Couple pin hole surfaces to reference points for load application
# =============================================================================
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
# LOADS
# =============================================================================
# Load Case 1: Fatigue Test - 20 kN vertical (in +Y direction, pulling up)
model.ConcentratedForce(
    name='VerticalLoad_20kN',
    createStepName='FatigueTest',
    region=upper_rp_region,
    cf2=20000.0,  # 20 kN in Y direction (vertical)
)
print("Vertical load 20 kN applied in FatigueTest step")

# Load Case 2: TO Design - Add horizontal loads at lower pins
# Left: -5 kN in X direction (pushing inward)
# Right: +5 kN in X direction (pushing inward)
model.ConcentratedForce(
    name='HorizontalLeft_5kN',
    createStepName='TODesign',
    region=lower_left_rp_region,
    cf1=-5000.0,  # -5 kN in X direction
)
print("Horizontal load -5 kN applied to left pin in TODesign step")

model.ConcentratedForce(
    name='HorizontalRight_5kN',
    createStepName='TODesign',
    region=lower_right_rp_region,
    cf1=5000.0,   # +5 kN in X direction
)
print("Horizontal load +5 kN applied to right pin in TODesign step")

# =============================================================================
# SAVE
# =============================================================================
mdb.saveAs(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen.cae')

print("\n" + "="*50)
print("ANALYSIS SETUP COMPLETE")
print("Steps: FatigueTest, TODesign")
print("BCs: Lower pins fixed in Y,Z; free in X")
print("Loads: 20 kN vertical + 5 kN horizontal (TODesign)")
print("="*50)
