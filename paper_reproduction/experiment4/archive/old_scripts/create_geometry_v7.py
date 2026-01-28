# -*- coding: utf-8 -*-
"""
Experiment 4: TO Specimen v7 - Using findAt with exact coordinates
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
# PIN HOLES - Using findAt with coordinates known to be on the faces
# =============================================================================

# Face center coordinates:
# Upper block right face: X=UB_RIGHT, Y=center of block, Z=center of thickness
upper_face_pt = (UB_RIGHT, (UB_BOTTOM + UB_TOP)/2, HALF_THICK)
# Edge on that face (vertical edge at front, Z=0)
upper_edge_pt = (UB_RIGHT, (UB_BOTTOM + UB_TOP)/2, 0.0)

# Lower right block outer face: X=LB_RIGHT_XMAX
lower_right_face_pt = (LB_RIGHT_XMAX, BLOCK_HEIGHT_Y/2, HALF_THICK)
lower_right_edge_pt = (LB_RIGHT_XMAX, BLOCK_HEIGHT_Y/2, 0.0)

# Lower left block outer face: X=LB_LEFT_XMIN
lower_left_face_pt = (LB_LEFT_XMIN, BLOCK_HEIGHT_Y/2, HALF_THICK)
lower_left_edge_pt = (LB_LEFT_XMIN, BLOCK_HEIGHT_Y/2, 0.0)

print("Face points:")
print("  Upper: {}".format(upper_face_pt))
print("  Lower right: {}".format(lower_right_face_pt))
print("  Lower left: {}".format(lower_left_face_pt))

# UPPER PIN HOLE
print("\n--- UPPER PIN HOLE ---")
try:
    upper_face = part.faces.findAt((upper_face_pt,))
    upper_edge = part.edges.findAt((upper_edge_pt,))

    if upper_face and upper_edge:
        print("Found face and edge")
        t = part.MakeSketchTransform(
            sketchPlane=upper_face[0],
            sketchUpEdge=upper_edge[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            origin=(UB_RIGHT, UPPER_PIN_Y, HALF_THICK)
        )
        ps = model.ConstrainedSketch(name='UpperPinHole', sheetSize=50.0, transform=t)
        ps.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

        part.CutExtrude(
            sketchPlane=upper_face[0],
            sketchUpEdge=upper_edge[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            sketch=ps,
            depth=BLOCK_WIDTH_X,
            flipExtrudeDirection=ON
        )
        print("UPPER PIN HOLE SUCCESS")
except Exception as e:
    print("Upper pin hole error: {}".format(str(e)))

# LOWER RIGHT PIN HOLE
print("\n--- LOWER RIGHT PIN HOLE ---")
try:
    lr_face = part.faces.findAt((lower_right_face_pt,))
    lr_edge = part.edges.findAt((lower_right_edge_pt,))

    if lr_face and lr_edge:
        print("Found face and edge")
        t = part.MakeSketchTransform(
            sketchPlane=lr_face[0],
            sketchUpEdge=lr_edge[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            origin=(LB_RIGHT_XMAX, LOWER_PIN_Y, HALF_THICK)
        )
        ps = model.ConstrainedSketch(name='LowerRightHole', sheetSize=50.0, transform=t)
        ps.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

        part.CutExtrude(
            sketchPlane=lr_face[0],
            sketchUpEdge=lr_edge[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            sketch=ps,
            depth=BLOCK_WIDTH_X,
            flipExtrudeDirection=ON
        )
        print("LOWER RIGHT PIN HOLE SUCCESS")
except Exception as e:
    print("Lower right error: {}".format(str(e)))

# LOWER LEFT PIN HOLE
print("\n--- LOWER LEFT PIN HOLE ---")
try:
    ll_face = part.faces.findAt((lower_left_face_pt,))
    ll_edge = part.edges.findAt((lower_left_edge_pt,))

    if ll_face and ll_edge:
        print("Found face and edge")
        t = part.MakeSketchTransform(
            sketchPlane=ll_face[0],
            sketchUpEdge=ll_edge[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            origin=(LB_LEFT_XMIN, LOWER_PIN_Y, HALF_THICK)
        )
        ps = model.ConstrainedSketch(name='LowerLeftHole', sheetSize=50.0, transform=t)
        ps.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

        part.CutExtrude(
            sketchPlane=ll_face[0],
            sketchUpEdge=ll_edge[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            sketch=ps,
            depth=BLOCK_WIDTH_X,
            flipExtrudeDirection=OFF
        )
        print("LOWER LEFT PIN HOLE SUCCESS")
except Exception as e:
    print("Lower left error: {}".format(str(e)))

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
print("GEOMETRY v7 COMPLETE")
print("="*60)
