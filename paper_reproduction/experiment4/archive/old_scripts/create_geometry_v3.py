# -*- coding: utf-8 -*-
"""
Experiment 4: TO Specimen - CORRECT PIN HOLE ORIENTATION
Pin holes go through X-axis (horizontal) so pins can be inserted
for mounting in tensile testing machine (3442-003M-020-ST Extensometer)

Coordinate system:
- X: horizontal (width direction) - PINS GO THROUGH HERE
- Y: vertical (height/load direction)
- Z: thickness direction (into page)
"""

from abaqus import *
from abaqusConstants import *
from caeModules import *

# =============================================================================
# DIMENSIONS
# =============================================================================
TOTAL_HEIGHT = 146.17      # Y direction
TOTAL_WIDTH = 64.60        # X direction
THICKNESS = 25.0           # Z direction

BLOCK_WIDTH_X = 18.0       # Width of upper/lower blocks in X
BLOCK_HEIGHT_Y = 28.0      # Height of blocks in Y
NECK_WIDTH = 10.0

PIN_DIAMETER = 12.7
PIN_RADIUS = PIN_DIAMETER / 2.0

CUTOUT_WIDTH = 18.0
CUTOUT_HEIGHT = 25.0

# =============================================================================
# POSITIONS
# =============================================================================
HALF_WIDTH = TOTAL_WIDTH / 2.0
HALF_THICK = THICKNESS / 2.0

# Upper block bounds
UB_LEFT = -BLOCK_WIDTH_X / 2.0
UB_RIGHT = BLOCK_WIDTH_X / 2.0
UB_BOTTOM = TOTAL_HEIGHT - BLOCK_HEIGHT_Y
UB_TOP = TOTAL_HEIGHT

# Upper pin center (goes through X direction)
UPPER_PIN_Y = TOTAL_HEIGHT - BLOCK_HEIGHT_Y / 2.0  # Y position
UPPER_PIN_Z = HALF_THICK                            # Z position (center of thickness)

# Lower block bounds
LB_LEFT_XMIN = -HALF_WIDTH
LB_LEFT_XMAX = -HALF_WIDTH + BLOCK_WIDTH_X
LB_RIGHT_XMIN = HALF_WIDTH - BLOCK_WIDTH_X
LB_RIGHT_XMAX = HALF_WIDTH

# Lower pin center Y position
LOWER_PIN_Y = BLOCK_HEIGHT_Y / 2.0

# Neck and junction
NECK_TOP_Y = UB_BOTTOM
NECK_BOT_Y = NECK_TOP_Y - 12.0
JUNCTION_Y = BLOCK_HEIGHT_Y + 35.0
JUNCTION_HALF_W = 4.0
CUTOUT_Y = (JUNCTION_Y + NECK_BOT_Y) / 2.0

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
# SKETCH - Create the Y-shaped profile in XY plane (at Z=0)
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

# Extrude in Z direction
part.BaseSolidExtrude(sketch=s, depth=THICKNESS)
print("Base extrusion done")

# =============================================================================
# PIN HOLES - Cut cylinders through X direction (horizontal)
# Pins go through the WIDTH of the blocks, not the thickness
# =============================================================================

# UPPER PIN HOLE - goes through upper block in X direction
# Sketch on YZ plane (right side face at X = UB_RIGHT)
right_face_upper = part.faces.getByBoundingBox(
    xMin=UB_RIGHT-0.1, xMax=UB_RIGHT+0.1,
    yMin=UB_BOTTOM-1, yMax=UB_TOP+1,
    zMin=-0.1, zMax=THICKNESS+0.1
)
print("Found {} faces for upper block right side".format(len(right_face_upper)))

if len(right_face_upper) > 0:
    # Find top edge for sketchUpEdge
    top_edge_upper = part.edges.getByBoundingBox(
        xMin=UB_RIGHT-0.1, xMax=UB_RIGHT+0.1,
        yMin=UB_TOP-0.1, yMax=UB_TOP+0.1,
        zMin=-0.1, zMax=THICKNESS+0.1
    )

    if len(top_edge_upper) > 0:
        t1 = part.MakeSketchTransform(
            sketchPlane=right_face_upper[0],
            sketchUpEdge=top_edge_upper[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            origin=(UB_RIGHT, UPPER_PIN_Y, UPPER_PIN_Z)
        )
        ps1 = model.ConstrainedSketch(name='UpperPinHole', sheetSize=50.0, transform=t1)
        # On YZ face: sketch coordinates are (Z, Y) relative to origin
        # Circle at center (0, 0) relative to origin
        ps1.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

        part.CutExtrude(
            sketchPlane=right_face_upper[0],
            sketchUpEdge=top_edge_upper[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            sketch=ps1,
            flipExtrudeDirection=ON,
            depth=BLOCK_WIDTH_X  # Cut through the block width
        )
        print("UPPER PIN HOLE cut through X direction")

# LOWER LEFT PIN HOLE - goes through left lower block in X direction
# This hole goes from the inner face (X = LB_LEFT_XMAX) to outer face (X = LB_LEFT_XMIN)
left_inner_face = part.faces.getByBoundingBox(
    xMin=LB_LEFT_XMAX-0.1, xMax=LB_LEFT_XMAX+0.1,
    yMin=-0.1, yMax=BLOCK_HEIGHT_Y+0.1,
    zMin=-0.1, zMax=THICKNESS+0.1
)
print("Found {} faces for left block inner side".format(len(left_inner_face)))

if len(left_inner_face) > 0:
    top_edge_left = part.edges.getByBoundingBox(
        xMin=LB_LEFT_XMAX-0.1, xMax=LB_LEFT_XMAX+0.1,
        yMin=BLOCK_HEIGHT_Y-0.1, yMax=BLOCK_HEIGHT_Y+0.1,
        zMin=-0.1, zMax=THICKNESS+0.1
    )

    if len(top_edge_left) > 0:
        t2 = part.MakeSketchTransform(
            sketchPlane=left_inner_face[0],
            sketchUpEdge=top_edge_left[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            origin=(LB_LEFT_XMAX, LOWER_PIN_Y, HALF_THICK)
        )
        ps2 = model.ConstrainedSketch(name='LowerLeftPinHole', sheetSize=50.0, transform=t2)
        ps2.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

        part.CutExtrude(
            sketchPlane=left_inner_face[0],
            sketchUpEdge=top_edge_left[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            sketch=ps2,
            flipExtrudeDirection=ON,
            depth=BLOCK_WIDTH_X
        )
        print("LOWER LEFT PIN HOLE cut through X direction")

# LOWER RIGHT PIN HOLE - goes through right lower block in X direction
right_inner_face = part.faces.getByBoundingBox(
    xMin=LB_RIGHT_XMIN-0.1, xMax=LB_RIGHT_XMIN+0.1,
    yMin=-0.1, yMax=BLOCK_HEIGHT_Y+0.1,
    zMin=-0.1, zMax=THICKNESS+0.1
)
print("Found {} faces for right block inner side".format(len(right_inner_face)))

if len(right_inner_face) > 0:
    top_edge_right = part.edges.getByBoundingBox(
        xMin=LB_RIGHT_XMIN-0.1, xMax=LB_RIGHT_XMIN+0.1,
        yMin=BLOCK_HEIGHT_Y-0.1, yMax=BLOCK_HEIGHT_Y+0.1,
        zMin=-0.1, zMax=THICKNESS+0.1
    )

    if len(top_edge_right) > 0:
        t3 = part.MakeSketchTransform(
            sketchPlane=right_inner_face[0],
            sketchUpEdge=top_edge_right[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            origin=(LB_RIGHT_XMIN, LOWER_PIN_Y, HALF_THICK)
        )
        ps3 = model.ConstrainedSketch(name='LowerRightPinHole', sheetSize=50.0, transform=t3)
        ps3.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

        part.CutExtrude(
            sketchPlane=right_inner_face[0],
            sketchUpEdge=top_edge_right[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            sketch=ps3,
            flipExtrudeDirection=OFF,  # Cut outward (positive X)
            depth=BLOCK_WIDTH_X
        )
        print("LOWER RIGHT PIN HOLE cut through X direction")

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
print("GEOMETRY COMPLETE - PIN HOLES NOW GO THROUGH X AXIS")
print("="*60)
print("Upper pin: Y={:.1f}, Z={:.1f}, through X from {:.1f} to {:.1f}".format(
    UPPER_PIN_Y, UPPER_PIN_Z, UB_LEFT, UB_RIGHT))
print("Lower left pin: Y={:.1f}, Z={:.1f}, through X from {:.1f} to {:.1f}".format(
    LOWER_PIN_Y, HALF_THICK, LB_LEFT_XMIN, LB_LEFT_XMAX))
print("Lower right pin: Y={:.1f}, Z={:.1f}, through X from {:.1f} to {:.1f}".format(
    LOWER_PIN_Y, HALF_THICK, LB_RIGHT_XMIN, LB_RIGHT_XMAX))
print("="*60)
