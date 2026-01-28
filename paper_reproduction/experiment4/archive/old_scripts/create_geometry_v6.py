# -*- coding: utf-8 -*-
"""
Experiment 4: TO Specimen v6 - Fixed face selection
More precise bounding boxes to find correct faces for pin holes
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

UB_LEFT = -BLOCK_WIDTH_X / 2.0      # -9.0
UB_RIGHT = BLOCK_WIDTH_X / 2.0       # 9.0
UB_BOTTOM = TOTAL_HEIGHT - BLOCK_HEIGHT_Y  # 118.17
UB_TOP = TOTAL_HEIGHT                # 146.17

UPPER_PIN_Y = TOTAL_HEIGHT - BLOCK_HEIGHT_Y / 2.0  # 132.17

LB_LEFT_XMIN = -HALF_WIDTH                    # -32.3
LB_LEFT_XMAX = -HALF_WIDTH + BLOCK_WIDTH_X    # -14.3
LB_RIGHT_XMIN = HALF_WIDTH - BLOCK_WIDTH_X    # 14.3
LB_RIGHT_XMAX = HALF_WIDTH                    # 32.3

LEFT_BLOCK_CENTER_X = (LB_LEFT_XMIN + LB_LEFT_XMAX) / 2.0   # -23.3
RIGHT_BLOCK_CENTER_X = (LB_RIGHT_XMIN + LB_RIGHT_XMAX) / 2.0 # 23.3

LOWER_PIN_Y = BLOCK_HEIGHT_Y / 2.0  # 14.0

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
# BASE SKETCH
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
# PIN HOLES - Using more precise face selection
# =============================================================================

# UPPER PIN HOLE
# The upper block right face is a small rectangle at X=UB_RIGHT
# It spans Y from UB_BOTTOM to UB_TOP, and Z from 0 to THICKNESS
# We need to be very specific to not pick up neck faces
print("\n--- UPPER PIN HOLE ---")
# Find the face at X=UB_RIGHT within ONLY the upper block Y range
all_faces = part.faces
for face in all_faces:
    bb = face.getBoundingBox()
    # Check if this is the right side face of the upper block
    if (abs(bb['low'][0] - UB_RIGHT) < 0.5 and abs(bb['high'][0] - UB_RIGHT) < 0.5 and
        bb['low'][1] > UB_BOTTOM - 1 and bb['high'][1] < UB_TOP + 1):
        print("Found upper block right face: X={}, Y=[{},{}]".format(
            bb['low'][0], bb['low'][1], bb['high'][1]))

        # Find vertical edge on this face at Z=0 (front edge)
        face_edges = face.getEdges()
        up_edge = None
        for edge_idx in face_edges:
            edge = part.edges[edge_idx]
            edge_bb = edge.getBoundingBox()
            # Vertical edge at Z=0
            if (abs(edge_bb['low'][2]) < 0.5 and abs(edge_bb['high'][2]) < 0.5 and
                edge_bb['high'][1] - edge_bb['low'][1] > 5):
                up_edge = edge
                print("Found vertical edge for sketchUpEdge")
                break

        if up_edge:
            t = part.MakeSketchTransform(
                sketchPlane=face,
                sketchUpEdge=up_edge,
                sketchPlaneSide=SIDE1,
                sketchOrientation=RIGHT,
                origin=(UB_RIGHT, UPPER_PIN_Y, HALF_THICK)
            )
            ps = model.ConstrainedSketch(name='UpperPinHole', sheetSize=50.0, transform=t)
            ps.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

            part.CutExtrude(
                sketchPlane=face,
                sketchUpEdge=up_edge,
                sketchPlaneSide=SIDE1,
                sketchOrientation=RIGHT,
                sketch=ps,
                depth=BLOCK_WIDTH_X,
                flipExtrudeDirection=ON
            )
            print("UPPER PIN HOLE CUT SUCCESS")
        break

# LOWER RIGHT PIN HOLE
print("\n--- LOWER RIGHT PIN HOLE ---")
for face in all_faces:
    bb = face.getBoundingBox()
    # Right face of right lower block (X = LB_RIGHT_XMAX, Y = 0 to BLOCK_HEIGHT_Y)
    if (abs(bb['low'][0] - LB_RIGHT_XMAX) < 0.5 and abs(bb['high'][0] - LB_RIGHT_XMAX) < 0.5 and
        bb['low'][1] < 1 and bb['high'][1] > BLOCK_HEIGHT_Y - 1 and bb['high'][1] < BLOCK_HEIGHT_Y + 1):
        print("Found lower right block face: Y=[{},{}]".format(bb['low'][1], bb['high'][1]))

        face_edges = face.getEdges()
        up_edge = None
        for edge_idx in face_edges:
            edge = part.edges[edge_idx]
            edge_bb = edge.getBoundingBox()
            if (abs(edge_bb['low'][2]) < 0.5 and abs(edge_bb['high'][2]) < 0.5 and
                edge_bb['high'][1] - edge_bb['low'][1] > 5):
                up_edge = edge
                print("Found vertical edge")
                break

        if up_edge:
            t = part.MakeSketchTransform(
                sketchPlane=face,
                sketchUpEdge=up_edge,
                sketchPlaneSide=SIDE1,
                sketchOrientation=RIGHT,
                origin=(LB_RIGHT_XMAX, LOWER_PIN_Y, HALF_THICK)
            )
            ps = model.ConstrainedSketch(name='LowerRightHole', sheetSize=50.0, transform=t)
            ps.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

            part.CutExtrude(
                sketchPlane=face,
                sketchUpEdge=up_edge,
                sketchPlaneSide=SIDE1,
                sketchOrientation=RIGHT,
                sketch=ps,
                depth=BLOCK_WIDTH_X,
                flipExtrudeDirection=ON
            )
            print("LOWER RIGHT PIN HOLE CUT SUCCESS")
        break

# LOWER LEFT PIN HOLE
print("\n--- LOWER LEFT PIN HOLE ---")
for face in all_faces:
    bb = face.getBoundingBox()
    # Left face of left lower block (X = LB_LEFT_XMIN)
    if (abs(bb['low'][0] - LB_LEFT_XMIN) < 0.5 and abs(bb['high'][0] - LB_LEFT_XMIN) < 0.5 and
        bb['low'][1] < 1 and bb['high'][1] > BLOCK_HEIGHT_Y - 1 and bb['high'][1] < BLOCK_HEIGHT_Y + 1):
        print("Found lower left block face: Y=[{},{}]".format(bb['low'][1], bb['high'][1]))

        face_edges = face.getEdges()
        up_edge = None
        for edge_idx in face_edges:
            edge = part.edges[edge_idx]
            edge_bb = edge.getBoundingBox()
            if (abs(edge_bb['low'][2]) < 0.5 and abs(edge_bb['high'][2]) < 0.5 and
                edge_bb['high'][1] - edge_bb['low'][1] > 5):
                up_edge = edge
                print("Found vertical edge")
                break

        if up_edge:
            t = part.MakeSketchTransform(
                sketchPlane=face,
                sketchUpEdge=up_edge,
                sketchPlaneSide=SIDE1,
                sketchOrientation=RIGHT,
                origin=(LB_LEFT_XMIN, LOWER_PIN_Y, HALF_THICK)
            )
            ps = model.ConstrainedSketch(name='LowerLeftHole', sheetSize=50.0, transform=t)
            ps.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

            part.CutExtrude(
                sketchPlane=face,
                sketchUpEdge=up_edge,
                sketchPlaneSide=SIDE1,
                sketchOrientation=RIGHT,
                sketch=ps,
                depth=BLOCK_WIDTH_X,
                flipExtrudeDirection=OFF  # Cut in +X direction
            )
            print("LOWER LEFT PIN HOLE CUT SUCCESS")
        break

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
print("GEOMETRY v6 COMPLETE")
print("="*60)
