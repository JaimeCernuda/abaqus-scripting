# -*- coding: utf-8 -*-
"""
Experiment 4: TO Specimen - FIXED VERSION
Properly cuts pin holes in ALL three locations:
- Upper block (1 hole)
- Left lower block (1 hole)
- Right lower block (1 hole)
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

# Lower pin center Y coordinate
LOWER_PIN_Y = BLOCK_HEIGHT_Y / 2.0

# Lower block center X coordinates
LEFT_BLOCK_CENTER_X = (LB_LEFT_XMIN + LB_LEFT_XMAX) / 2.0
RIGHT_BLOCK_CENTER_X = (LB_RIGHT_XMIN + LB_RIGHT_XMAX) / 2.0

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
# SKETCH - Create the Y-shaped profile in XY plane (Z=0)
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
# PIN HOLES - Use front face (Z=0) and sketch circles, then cut through Z
# This is simpler and more reliable
# =============================================================================

# Get the front face at Z=0
front_face = part.faces.getByBoundingBox(
    xMin=-HALF_WIDTH-1, xMax=HALF_WIDTH+1,
    yMin=-1, yMax=TOTAL_HEIGHT+1,
    zMin=-0.1, zMax=0.1
)
print("Found {} front faces".format(len(front_face)))

if len(front_face) > 0:
    # Find a vertical edge for sketchUpEdge (on the upper block left edge)
    vertical_edge = part.edges.getByBoundingBox(
        xMin=UB_LEFT-0.1, xMax=UB_LEFT+0.1,
        yMin=NECK_TOP_Y-0.1, yMax=UB_TOP+0.1,
        zMin=-0.1, zMax=0.1
    )

    if len(vertical_edge) > 0:
        # Create transform for front face
        t = part.MakeSketchTransform(
            sketchPlane=front_face[0],
            sketchUpEdge=vertical_edge[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            origin=(0.0, 0.0, 0.0)
        )

        # Sketch all 3 pin holes on front face
        pin_sketch = model.ConstrainedSketch(name='AllPinHoles', sheetSize=200.0, transform=t)

        # Upper pin hole (center of upper block)
        pin_sketch.CircleByCenterPerimeter(
            center=(0.0, UPPER_PIN_Y),
            point1=(PIN_RADIUS, UPPER_PIN_Y)
        )

        # Left lower pin hole
        pin_sketch.CircleByCenterPerimeter(
            center=(LEFT_BLOCK_CENTER_X, LOWER_PIN_Y),
            point1=(LEFT_BLOCK_CENTER_X + PIN_RADIUS, LOWER_PIN_Y)
        )

        # Right lower pin hole
        pin_sketch.CircleByCenterPerimeter(
            center=(RIGHT_BLOCK_CENTER_X, LOWER_PIN_Y),
            point1=(RIGHT_BLOCK_CENTER_X + PIN_RADIUS, LOWER_PIN_Y)
        )

        # Cut all holes through the entire thickness
        part.CutExtrude(
            sketchPlane=front_face[0],
            sketchUpEdge=vertical_edge[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            sketch=pin_sketch,
            flipExtrudeDirection=OFF,
            depth=THICKNESS
        )
        print("ALL 3 PIN HOLES CUT DONE")
    else:
        print("ERROR: Could not find vertical edge for sketchUpEdge")
else:
    print("ERROR: Could not find front face")

# =============================================================================
# ELLIPTICAL CUTOUT - Center cutout between the legs
# =============================================================================
# Need to get updated front face after pin hole cuts
front_faces_new = part.faces.getByBoundingBox(
    xMin=-5, xMax=5,
    yMin=JUNCTION_Y-10, yMax=NECK_BOT_Y+10,
    zMin=-0.1, zMax=0.1
)
print("Found {} faces for cutout".format(len(front_faces_new)))

if len(front_faces_new) > 0:
    # Find vertical edge on front face
    vert_edges = part.edges.getByBoundingBox(
        xMin=JUNCTION_HALF_W-0.5, xMax=JUNCTION_HALF_W+0.5,
        yMin=JUNCTION_Y-1, yMax=JUNCTION_Y+20,
        zMin=-0.1, zMax=0.1
    )

    if len(vert_edges) > 0:
        t2 = part.MakeSketchTransform(
            sketchPlane=front_faces_new[0],
            sketchUpEdge=vert_edges[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            origin=(0.0, 0.0, 0.0)
        )

        cutout_sketch = model.ConstrainedSketch(name='Cutout', sheetSize=100.0, transform=t2)
        cutout_sketch.EllipseByCenterPerimeter(
            center=(0.0, CUTOUT_Y),
            axisPoint1=(CUTOUT_WIDTH/2.0, CUTOUT_Y),
            axisPoint2=(0.0, CUTOUT_Y + CUTOUT_HEIGHT/2.0)
        )

        part.CutExtrude(
            sketchPlane=front_faces_new[0],
            sketchUpEdge=vert_edges[0],
            sketchPlaneSide=SIDE1,
            sketchOrientation=RIGHT,
            sketch=cutout_sketch,
            flipExtrudeDirection=OFF,
            depth=THICKNESS
        )
        print("ELLIPTICAL CUTOUT DONE")
    else:
        print("Could not find edge for cutout - skipping")
else:
    print("Could not find face for cutout - skipping")

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
print("GEOMETRY COMPLETE - ALL 3 PIN HOLES SHOULD BE VISIBLE")
print("Upper pin at Y={:.1f}".format(UPPER_PIN_Y))
print("Lower pins at Y={:.1f}, X={:.1f} and X={:.1f}".format(LOWER_PIN_Y, LEFT_BLOCK_CENTER_X, RIGHT_BLOCK_CENTER_X))
print("="*50)
