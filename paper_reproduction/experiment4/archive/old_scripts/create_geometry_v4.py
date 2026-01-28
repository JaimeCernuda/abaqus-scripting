# -*- coding: utf-8 -*-
"""
Experiment 4: TO Specimen - CORRECT PIN HOLES v4
Using datum planes and simpler approach for horizontal pin holes

Pin configuration for clevis-type loading:
- 1 pin at top (upper block) - goes through X (left to right)
- 2 pins at bottom (lower blocks) - each goes through X

Coordinate system:
- X: width (left/right) - PINS GO THROUGH THIS DIRECTION
- Y: height (up/down) - LOAD DIRECTION
- Z: thickness (front/back)
"""

from abaqus import *
from abaqusConstants import *
from caeModules import *

# =============================================================================
# DIMENSIONS
# =============================================================================
TOTAL_HEIGHT = 146.17
TOTAL_WIDTH = 64.60
THICKNESS = 25.0

BLOCK_WIDTH_X = 18.0
BLOCK_HEIGHT_Y = 28.0
NECK_WIDTH = 10.0

PIN_DIAMETER = 12.7
PIN_RADIUS = PIN_DIAMETER / 2.0

# =============================================================================
# POSITIONS
# =============================================================================
HALF_WIDTH = TOTAL_WIDTH / 2.0
HALF_THICK = THICKNESS / 2.0

UB_LEFT = -BLOCK_WIDTH_X / 2.0
UB_RIGHT = BLOCK_WIDTH_X / 2.0
UB_BOTTOM = TOTAL_HEIGHT - BLOCK_HEIGHT_Y
UB_TOP = TOTAL_HEIGHT

UPPER_PIN_Y = TOTAL_HEIGHT - BLOCK_HEIGHT_Y / 2.0

LB_LEFT_XMIN = -HALF_WIDTH
LB_LEFT_XMAX = -HALF_WIDTH + BLOCK_WIDTH_X
LB_RIGHT_XMIN = HALF_WIDTH - BLOCK_WIDTH_X
LB_RIGHT_XMAX = HALF_WIDTH

LOWER_PIN_Y = BLOCK_HEIGHT_Y / 2.0

NECK_TOP_Y = UB_BOTTOM
NECK_BOT_Y = NECK_TOP_Y - 12.0
JUNCTION_Y = BLOCK_HEIGHT_Y + 35.0
JUNCTION_HALF_W = 4.0

# =============================================================================
# CREATE MODEL
# =============================================================================
model_name = 'Experiment4_TO_Specimen'
part_name = 'TO_Specimen'

if model_name in mdb.models.keys():
    del mdb.models[model_name]
model = mdb.Model(name=model_name)
if 'Model-1' in mdb.models.keys():
    del mdb.models['Model-1']

part = model.Part(name=part_name, dimensionality=THREE_D, type=DEFORMABLE_BODY)

# =============================================================================
# BASE SKETCH - Y-shaped profile in XY plane
# =============================================================================
s = model.ConstrainedSketch(name='Profile', sheetSize=300.0)

p1 = (UB_LEFT, UB_TOP)
p2 = (UB_RIGHT, UB_TOP)
p3 = (UB_RIGHT, NECK_TOP_Y)
p5 = (NECK_WIDTH/2.0, NECK_BOT_Y)
p6 = (-NECK_WIDTH/2.0, NECK_BOT_Y)
p4 = (UB_LEFT, NECK_TOP_Y)
p7 = (JUNCTION_HALF_W, JUNCTION_Y)
p8 = (-JUNCTION_HALF_W, JUNCTION_Y)
p9 = (LB_RIGHT_XMAX, BLOCK_HEIGHT_Y)
p10 = (LB_RIGHT_XMAX, 0.0)
p11 = (LB_RIGHT_XMIN, 0.0)
p12 = (LB_RIGHT_XMIN, BLOCK_HEIGHT_Y)
p13 = (LB_LEFT_XMAX, BLOCK_HEIGHT_Y)
p14 = (LB_LEFT_XMAX, 0.0)
p15 = (LB_LEFT_XMIN, 0.0)
p16 = (LB_LEFT_XMIN, BLOCK_HEIGHT_Y)

s.Line(point1=p1, point2=p2)
s.Line(point1=p2, point2=p3)
s.Line(point1=p3, point2=p5)
s.Spline(points=[p5, (NECK_WIDTH/2.0+8.0, NECK_BOT_Y-20.0), (LB_RIGHT_XMAX-5.0, BLOCK_HEIGHT_Y+30.0), p9])
s.Line(point1=p9, point2=p10)
s.Line(point1=p10, point2=p11)
s.Line(point1=p11, point2=p12)
s.Spline(points=[p12, (LB_RIGHT_XMIN+5.0, BLOCK_HEIGHT_Y+25.0), (JUNCTION_HALF_W+10.0, JUNCTION_Y+15.0), p7])
s.Line(point1=p7, point2=p8)
s.Spline(points=[p8, (-JUNCTION_HALF_W-10.0, JUNCTION_Y+15.0), (LB_LEFT_XMAX-5.0, BLOCK_HEIGHT_Y+25.0), p13])
s.Line(point1=p13, point2=p14)
s.Line(point1=p14, point2=p15)
s.Line(point1=p15, point2=p16)
s.Spline(points=[p16, (LB_LEFT_XMIN+5.0, BLOCK_HEIGHT_Y+30.0), (-NECK_WIDTH/2.0-8.0, NECK_BOT_Y-20.0), p6])
s.Line(point1=p6, point2=p4)
s.Line(point1=p4, point2=p1)

part.BaseSolidExtrude(sketch=s, depth=THICKNESS)
print("Base geometry created")

# =============================================================================
# CREATE DATUM PLANES FOR PIN HOLE CUTS
# We'll use YZ planes (normal to X) positioned at the block faces
# =============================================================================

# Upper pin - datum plane at X = UB_RIGHT (right side of upper block)
datum_upper = part.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=UB_RIGHT)
datum_upper_id = datum_upper.id
print("Created datum plane for upper pin at X = {}".format(UB_RIGHT))

# Lower right pin - datum plane at X = LB_RIGHT_XMAX (right side of right block)
datum_right = part.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=LB_RIGHT_XMAX)
datum_right_id = datum_right.id
print("Created datum plane for lower right pin at X = {}".format(LB_RIGHT_XMAX))

# Lower left pin - datum plane at X = LB_LEFT_XMIN (left side of left block)
# We'll cut from the left side going right
datum_left = part.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=LB_LEFT_XMIN)
datum_left_id = datum_left.id
print("Created datum plane for lower left pin at X = {}".format(LB_LEFT_XMIN))

# =============================================================================
# UPPER PIN HOLE - Cut through upper block from right to left
# =============================================================================
# Sketch on datum plane (YZ plane at X = UB_RIGHT)
# On YZ plane, coordinates are (Z, Y)
s_upper = model.ConstrainedSketch(
    name='UpperPinSketch',
    sheetSize=100.0,
    gridSpacing=5.0,
    transform=part.MakeSketchTransform(
        sketchPlane=part.datums[datum_upper_id],
        sketchUpEdge=part.edges.findAt((UB_RIGHT, UB_TOP, HALF_THICK)),
        sketchPlaneSide=SIDE1,
        sketchOrientation=RIGHT,
        origin=(0, UPPER_PIN_Y, HALF_THICK)
    )
)
# Draw circle at (0, 0) which is at (Z=HALF_THICK, Y=UPPER_PIN_Y) in part coords
s_upper.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(PIN_RADIUS, 0.0))

part.CutExtrude(
    sketchPlane=part.datums[datum_upper_id],
    sketchUpEdge=part.edges.findAt((UB_RIGHT, UB_TOP, HALF_THICK)),
    sketchPlaneSide=SIDE1,
    sketchOrientation=RIGHT,
    sketch=s_upper,
    flipExtrudeDirection=ON,  # Cut toward -X (left)
    depth=BLOCK_WIDTH_X
)
print("Upper pin hole cut through X direction")

# =============================================================================
# LOWER RIGHT PIN HOLE - Cut through right lower block
# =============================================================================
s_right = model.ConstrainedSketch(
    name='LowerRightPinSketch',
    sheetSize=100.0,
    gridSpacing=5.0,
    transform=part.MakeSketchTransform(
        sketchPlane=part.datums[datum_right_id],
        sketchUpEdge=part.edges.findAt((LB_RIGHT_XMAX, BLOCK_HEIGHT_Y, HALF_THICK)),
        sketchPlaneSide=SIDE1,
        sketchOrientation=RIGHT,
        origin=(0, LOWER_PIN_Y, HALF_THICK)
    )
)
s_right.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(PIN_RADIUS, 0.0))

part.CutExtrude(
    sketchPlane=part.datums[datum_right_id],
    sketchUpEdge=part.edges.findAt((LB_RIGHT_XMAX, BLOCK_HEIGHT_Y, HALF_THICK)),
    sketchPlaneSide=SIDE1,
    sketchOrientation=RIGHT,
    sketch=s_right,
    flipExtrudeDirection=ON,
    depth=BLOCK_WIDTH_X
)
print("Lower right pin hole cut through X direction")

# =============================================================================
# LOWER LEFT PIN HOLE - Cut through left lower block
# =============================================================================
s_left = model.ConstrainedSketch(
    name='LowerLeftPinSketch',
    sheetSize=100.0,
    gridSpacing=5.0,
    transform=part.MakeSketchTransform(
        sketchPlane=part.datums[datum_left_id],
        sketchUpEdge=part.edges.findAt((LB_LEFT_XMIN, BLOCK_HEIGHT_Y, HALF_THICK)),
        sketchPlaneSide=SIDE1,
        sketchOrientation=RIGHT,
        origin=(0, LOWER_PIN_Y, HALF_THICK)
    )
)
s_left.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(PIN_RADIUS, 0.0))

part.CutExtrude(
    sketchPlane=part.datums[datum_left_id],
    sketchUpEdge=part.edges.findAt((LB_LEFT_XMIN, BLOCK_HEIGHT_Y, HALF_THICK)),
    sketchPlaneSide=SIDE1,
    sketchOrientation=RIGHT,
    sketch=s_left,
    flipExtrudeDirection=OFF,  # Cut toward +X (right)
    depth=BLOCK_WIDTH_X
)
print("Lower left pin hole cut through X direction")

# =============================================================================
# ASSEMBLY
# =============================================================================
assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
assembly.Instance(name=part_name+'-1', part=part, dependent=ON)

# =============================================================================
# SAVE
# =============================================================================
mdb.saveAs(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen.cae')

print("\n" + "="*60)
print("GEOMETRY v4 COMPLETE - ALL PIN HOLES THROUGH X AXIS")
print("="*60)
print("Configuration for clevis loading:")
print("  - Upper pin at Y={:.1f}mm, through X direction".format(UPPER_PIN_Y))
print("  - Lower left pin at Y={:.1f}mm, through X direction".format(LOWER_PIN_Y))
print("  - Lower right pin at Y={:.1f}mm, through X direction".format(LOWER_PIN_Y))
print("  - Pin diameter: {:.1f}mm".format(PIN_DIAMETER))
print("="*60)
