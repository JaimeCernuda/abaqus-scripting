# -*- coding: utf-8 -*-
"""
Experiment 4: TO Specimen v5 - Build holes differently
Use Shell Extrude with holes in the base sketch, then use Cut Revolve for cylinders
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

LEFT_BLOCK_CENTER_X = (LB_LEFT_XMIN + LB_LEFT_XMAX) / 2.0
RIGHT_BLOCK_CENTER_X = (LB_RIGHT_XMIN + LB_RIGHT_XMAX) / 2.0

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
# BASE SKETCH - Y-shaped profile in XY plane, extrude in Z
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
# PIN HOLES - Use Sketch on side face (YZ plane) with circle, then cut through X
# =============================================================================

# Get the right side face of the part for the upper block area
# This face is at X = UB_RIGHT, spanning Y from UB_BOTTOM to UB_TOP, Z from 0 to THICKNESS
print("\nSearching for faces...")

# UPPER PIN HOLE
# Find face on right side of upper block
upper_right_faces = part.faces.getByBoundingBox(
    xMin=UB_RIGHT-1, xMax=UB_RIGHT+1,
    yMin=UB_BOTTOM-1, yMax=UB_TOP+1,
    zMin=-1, zMax=THICKNESS+1
)
print("Upper block right faces found: {}".format(len(upper_right_faces)))

for i, face in enumerate(upper_right_faces):
    print("  Face {}: centroid = {}".format(i, face.pointOn))

if len(upper_right_faces) > 0:
    # Get edges for sketchUpEdge - find an edge parallel to Y axis
    upper_right_edges = part.edges.getByBoundingBox(
        xMin=UB_RIGHT-0.5, xMax=UB_RIGHT+0.5,
        yMin=UB_BOTTOM-1, yMax=UB_TOP+1,
        zMin=-0.1, zMax=0.1
    )
    print("Upper block right edges (front): {}".format(len(upper_right_edges)))

    if len(upper_right_edges) > 0:
        # Create sketch on this face
        transform = part.MakeSketchTransform(
            sketchPlane=upper_right_faces[0],
            sketchUpEdge=upper_right_edges[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            origin=(UB_RIGHT, UPPER_PIN_Y, HALF_THICK)
        )
        hole_sketch = model.ConstrainedSketch(name='UpperHole', sheetSize=50.0, transform=transform)
        hole_sketch.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

        part.CutExtrude(
            sketchPlane=upper_right_faces[0],
            sketchUpEdge=upper_right_edges[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            sketch=hole_sketch,
            depth=BLOCK_WIDTH_X,
            flipExtrudeDirection=ON
        )
        print("UPPER PIN HOLE CUT SUCCESS")
    else:
        print("Could not find edge for upper pin")
else:
    print("Could not find face for upper pin")

# LOWER RIGHT PIN HOLE
lower_right_faces = part.faces.getByBoundingBox(
    xMin=LB_RIGHT_XMAX-1, xMax=LB_RIGHT_XMAX+1,
    yMin=-1, yMax=BLOCK_HEIGHT_Y+1,
    zMin=-1, zMax=THICKNESS+1
)
print("\nLower right block faces found: {}".format(len(lower_right_faces)))

if len(lower_right_faces) > 0:
    lower_right_edges = part.edges.getByBoundingBox(
        xMin=LB_RIGHT_XMAX-0.5, xMax=LB_RIGHT_XMAX+0.5,
        yMin=-0.1, yMax=BLOCK_HEIGHT_Y+0.1,
        zMin=-0.1, zMax=0.1
    )
    print("Lower right edges (front): {}".format(len(lower_right_edges)))

    if len(lower_right_edges) > 0:
        transform2 = part.MakeSketchTransform(
            sketchPlane=lower_right_faces[0],
            sketchUpEdge=lower_right_edges[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            origin=(LB_RIGHT_XMAX, LOWER_PIN_Y, HALF_THICK)
        )
        hole_sketch2 = model.ConstrainedSketch(name='LowerRightHole', sheetSize=50.0, transform=transform2)
        hole_sketch2.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

        part.CutExtrude(
            sketchPlane=lower_right_faces[0],
            sketchUpEdge=lower_right_edges[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            sketch=hole_sketch2,
            depth=BLOCK_WIDTH_X,
            flipExtrudeDirection=ON
        )
        print("LOWER RIGHT PIN HOLE CUT SUCCESS")

# LOWER LEFT PIN HOLE
lower_left_faces = part.faces.getByBoundingBox(
    xMin=LB_LEFT_XMIN-1, xMax=LB_LEFT_XMIN+1,
    yMin=-1, yMax=BLOCK_HEIGHT_Y+1,
    zMin=-1, zMax=THICKNESS+1
)
print("\nLower left block faces found: {}".format(len(lower_left_faces)))

if len(lower_left_faces) > 0:
    lower_left_edges = part.edges.getByBoundingBox(
        xMin=LB_LEFT_XMIN-0.5, xMax=LB_LEFT_XMIN+0.5,
        yMin=-0.1, yMax=BLOCK_HEIGHT_Y+0.1,
        zMin=-0.1, zMax=0.1
    )
    print("Lower left edges (front): {}".format(len(lower_left_edges)))

    if len(lower_left_edges) > 0:
        transform3 = part.MakeSketchTransform(
            sketchPlane=lower_left_faces[0],
            sketchUpEdge=lower_left_edges[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            origin=(LB_LEFT_XMIN, LOWER_PIN_Y, HALF_THICK)
        )
        hole_sketch3 = model.ConstrainedSketch(name='LowerLeftHole', sheetSize=50.0, transform=transform3)
        hole_sketch3.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

        part.CutExtrude(
            sketchPlane=lower_left_faces[0],
            sketchUpEdge=lower_left_edges[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            sketch=hole_sketch3,
            depth=BLOCK_WIDTH_X,
            flipExtrudeDirection=OFF  # Cut in +X direction
        )
        print("LOWER LEFT PIN HOLE CUT SUCCESS")

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
print("GEOMETRY v5 COMPLETE")
print("="*60)
