# -*- coding: utf-8 -*-
"""
Experiment 4: TO Specimen - DEBUG VERSION
Print all found faces/edges to debug pin hole cutting
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

CUTOUT_WIDTH = 18.0
CUTOUT_HEIGHT = 25.0

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
UPPER_PIN_Z = HALF_THICK

LB_LEFT_XMIN = -HALF_WIDTH
LB_LEFT_XMAX = -HALF_WIDTH + BLOCK_WIDTH_X
LB_RIGHT_XMIN = HALF_WIDTH - BLOCK_WIDTH_X
LB_RIGHT_XMAX = HALF_WIDTH

LOWER_PIN_Y = BLOCK_HEIGHT_Y / 2.0
LOWER_PIN_Z = HALF_THICK

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
# SKETCH
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
print("Base extrusion done")

# =============================================================================
# DEBUG: Print all faces
# =============================================================================
print("\n=== ALL FACES ===")
for i, f in enumerate(part.faces):
    bb = f.getBoundingBox()
    print("Face {}: X=[{:.1f},{:.1f}] Y=[{:.1f},{:.1f}] Z=[{:.1f},{:.1f}]".format(
        i, bb['low'][0], bb['high'][0], bb['low'][1], bb['high'][1], bb['low'][2], bb['high'][2]))

# =============================================================================
# PIN HOLES - Use HoleBlindFromEdges or simpler approach
# =============================================================================

# Let's try using getByBoundingBox instead of findAt
# Upper block right face (X = UB_RIGHT)
print("\nLooking for upper block right face at X={:.1f}".format(UB_RIGHT))
upper_side_faces = part.faces.getByBoundingBox(
    xMin=UB_RIGHT-0.1, xMax=UB_RIGHT+0.1,
    yMin=UB_BOTTOM-1, yMax=UB_TOP+1,
    zMin=-0.1, zMax=THICKNESS+0.1
)
print("Found {} faces".format(len(upper_side_faces)))

if len(upper_side_faces) > 0:
    # Get edges on this face for sketchUpEdge
    upper_edges = part.edges.getByBoundingBox(
        xMin=UB_RIGHT-0.1, xMax=UB_RIGHT+0.1,
        yMin=UB_TOP-0.1, yMax=UB_TOP+0.1,
        zMin=-0.1, zMax=THICKNESS+0.1
    )
    print("Found {} edges at top".format(len(upper_edges)))

    if len(upper_edges) > 0:
        # Create sketch for upper pin hole
        t = part.MakeSketchTransform(
            sketchPlane=upper_side_faces[0],
            sketchUpEdge=upper_edges[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            origin=(UB_RIGHT, 0.0, 0.0)
        )
        ps1 = model.ConstrainedSketch(name='UpperPin', sheetSize=50.0, transform=t)
        # On face at X=UB_RIGHT: Y is vertical, Z is horizontal
        # Pin center: Y=UPPER_PIN_Y, Z=HALF_THICK
        ps1.CircleByCenterPerimeter(
            center=(HALF_THICK, UPPER_PIN_Y),
            point1=(HALF_THICK + PIN_RADIUS, UPPER_PIN_Y)
        )
        part.CutExtrude(
            sketchPlane=upper_side_faces[0],
            sketchUpEdge=upper_edges[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            sketch=ps1,
            flipExtrudeDirection=ON,
            depth=BLOCK_WIDTH_X
        )
        print("Upper pin hole CUT DONE")

# Lower block - right face (X = LB_RIGHT_XMAX)
print("\nLooking for lower right block face at X={:.1f}".format(LB_RIGHT_XMAX))
lower_side_faces = part.faces.getByBoundingBox(
    xMin=LB_RIGHT_XMAX-0.1, xMax=LB_RIGHT_XMAX+0.1,
    yMin=-0.1, yMax=BLOCK_HEIGHT_Y+0.1,
    zMin=-0.1, zMax=THICKNESS+0.1
)
print("Found {} faces".format(len(lower_side_faces)))

if len(lower_side_faces) > 0:
    lower_edges = part.edges.getByBoundingBox(
        xMin=LB_RIGHT_XMAX-0.1, xMax=LB_RIGHT_XMAX+0.1,
        yMin=BLOCK_HEIGHT_Y-0.1, yMax=BLOCK_HEIGHT_Y+0.1,
        zMin=-0.1, zMax=THICKNESS+0.1
    )
    print("Found {} edges".format(len(lower_edges)))

    if len(lower_edges) > 0:
        t2 = part.MakeSketchTransform(
            sketchPlane=lower_side_faces[0],
            sketchUpEdge=lower_edges[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            origin=(LB_RIGHT_XMAX, 0.0, 0.0)
        )
        ps2 = model.ConstrainedSketch(name='LowerPin', sheetSize=50.0, transform=t2)
        ps2.CircleByCenterPerimeter(
            center=(HALF_THICK, LOWER_PIN_Y),
            point1=(HALF_THICK + PIN_RADIUS, LOWER_PIN_Y)
        )
        # Cut through entire width
        part.CutExtrude(
            sketchPlane=lower_side_faces[0],
            sketchUpEdge=lower_edges[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            sketch=ps2,
            flipExtrudeDirection=ON,
            depth=TOTAL_WIDTH
        )
        print("Lower pin holes CUT DONE (aligned through both blocks)")

# Elliptical cutout - front face (Z=0)
print("\nLooking for front face at Z=0")
front_faces = part.faces.getByBoundingBox(
    xMin=-HALF_WIDTH-1, xMax=HALF_WIDTH+1,
    yMin=-1, yMax=TOTAL_HEIGHT+1,
    zMin=-0.1, zMax=0.1
)
print("Found {} front faces".format(len(front_faces)))

if len(front_faces) > 0:
    front_edges = part.edges.getByBoundingBox(
        xMin=UB_LEFT-0.1, xMax=UB_LEFT+0.1,
        yMin=NECK_TOP_Y-0.1, yMax=UB_TOP+0.1,
        zMin=-0.1, zMax=0.1
    )
    print("Found {} vertical edges".format(len(front_edges)))

    if len(front_edges) > 0:
        t3 = part.MakeSketchTransform(
            sketchPlane=front_faces[0],
            sketchUpEdge=front_edges[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            origin=(0.0, 0.0, 0.0)
        )
        cs = model.ConstrainedSketch(name='Cutout', sheetSize=100.0, transform=t3)
        cs.EllipseByCenterPerimeter(
            center=(0.0, CUTOUT_Y),
            axisPoint1=(CUTOUT_WIDTH/2.0, CUTOUT_Y),
            axisPoint2=(0.0, CUTOUT_Y + CUTOUT_HEIGHT/2.0)
        )
        part.CutExtrude(
            sketchPlane=front_faces[0],
            sketchUpEdge=front_edges[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            sketch=cs,
            flipExtrudeDirection=OFF,
            depth=THICKNESS
        )
        print("Elliptical cutout DONE")

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
print("\n" + "="*50)
print("GEOMETRY COMPLETE - Check for pin holes")
print("="*50)
