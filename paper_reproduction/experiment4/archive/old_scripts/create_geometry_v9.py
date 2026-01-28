# -*- coding: utf-8 -*-
"""
Experiment 4: TO Specimen v9 - Using HoleFeature
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
print("Main body created")

# =============================================================================
# Print all faces to understand the geometry
# =============================================================================
print("\n=== FACE ANALYSIS ===")
for i, face in enumerate(part.faces):
    pt = face.pointOn[0]
    edges = face.getEdges()
    print("Face {}: point=({:.1f}, {:.1f}, {:.1f}), {} edges".format(
        i, pt[0], pt[1], pt[2], len(edges)))

print("\n=== EDGE ANALYSIS ===")
for i, edge in enumerate(part.edges):
    pt = edge.pointOn[0]
    print("Edge {}: point=({:.1f}, {:.1f}, {:.1f})".format(
        i, pt[0], pt[1], pt[2]))

# =============================================================================
# Create holes using Cut Revolve with datum axis
# =============================================================================

# Create datum axis along X direction for each pin location
# Upper pin axis: passes through (0, UPPER_PIN_Y, HALF_THICK), direction (1, 0, 0)
upper_axis = part.DatumAxisByTwoPoint(
    point1=(UB_LEFT - 5, UPPER_PIN_Y, HALF_THICK),
    point2=(UB_RIGHT + 5, UPPER_PIN_Y, HALF_THICK)
)
upper_axis_id = upper_axis.id
print("\nCreated upper pin axis")

# Lower left pin axis
left_axis = part.DatumAxisByTwoPoint(
    point1=(LB_LEFT_XMIN - 5, LOWER_PIN_Y, HALF_THICK),
    point2=(LB_LEFT_XMAX + 5, LOWER_PIN_Y, HALF_THICK)
)
left_axis_id = left_axis.id
print("Created left pin axis")

# Lower right pin axis
right_axis = part.DatumAxisByTwoPoint(
    point1=(LB_RIGHT_XMIN - 5, LOWER_PIN_Y, HALF_THICK),
    point2=(LB_RIGHT_XMAX + 5, LOWER_PIN_Y, HALF_THICK)
)
right_axis_id = right_axis.id
print("Created right pin axis")

# Create datum planes perpendicular to axes for sketching
# Upper pin plane (perpendicular to X at X=UB_RIGHT)
upper_plane = part.DatumPlaneByPointNormal(
    point=(UB_RIGHT, UPPER_PIN_Y, HALF_THICK),
    normal=part.datums[upper_axis_id]
)
upper_plane_id = upper_plane.id

# Get the actual face at x=UB_RIGHT for the upper block
# Use the printed face info to find correct face
upper_face_candidates = part.faces.getByBoundingBox(
    xMin=UB_RIGHT-0.01, xMax=UB_RIGHT+0.01,
    yMin=UB_BOTTOM, yMax=UB_TOP,
    zMin=0, zMax=THICKNESS
)
print("Upper face candidates: {}".format(len(upper_face_candidates)))

if len(upper_face_candidates) > 0:
    # Find edge on this face
    edge_candidates = part.edges.getByBoundingBox(
        xMin=UB_RIGHT-0.01, xMax=UB_RIGHT+0.01,
        yMin=UB_TOP-0.1, yMax=UB_TOP+0.1,
        zMin=0, zMax=THICKNESS
    )
    print("Upper edge candidates: {}".format(len(edge_candidates)))

    if len(edge_candidates) > 0:
        # Create cut sketch
        t = part.MakeSketchTransform(
            sketchPlane=upper_face_candidates[0],
            sketchUpEdge=edge_candidates[0],
            sketchPlaneSide=SIDE1,
            origin=(0, 0, 0)
        )
        ps = model.ConstrainedSketch(name='UpperHole', sheetSize=50.0, transform=t)
        # Circle at pin center
        ps.CircleByCenterPerimeter(center=(HALF_THICK, UPPER_PIN_Y), point1=(HALF_THICK + PIN_RADIUS, UPPER_PIN_Y))

        part.CutExtrude(
            sketchPlane=upper_face_candidates[0],
            sketchUpEdge=edge_candidates[0],
            sketchPlaneSide=SIDE1,
            sketch=ps,
            depth=BLOCK_WIDTH_X,
            flipExtrudeDirection=ON
        )
        print("UPPER PIN HOLE CUT")

# Lower right - similar approach
lr_faces = part.faces.getByBoundingBox(
    xMin=LB_RIGHT_XMAX-0.01, xMax=LB_RIGHT_XMAX+0.01,
    yMin=0, yMax=BLOCK_HEIGHT_Y,
    zMin=0, zMax=THICKNESS
)
print("Lower right face candidates: {}".format(len(lr_faces)))

if len(lr_faces) > 0:
    lr_edges = part.edges.getByBoundingBox(
        xMin=LB_RIGHT_XMAX-0.01, xMax=LB_RIGHT_XMAX+0.01,
        yMin=BLOCK_HEIGHT_Y-0.1, yMax=BLOCK_HEIGHT_Y+0.1,
        zMin=0, zMax=THICKNESS
    )
    print("Lower right edge candidates: {}".format(len(lr_edges)))

    if len(lr_edges) > 0:
        t = part.MakeSketchTransform(
            sketchPlane=lr_faces[0],
            sketchUpEdge=lr_edges[0],
            sketchPlaneSide=SIDE1,
            origin=(0, 0, 0)
        )
        ps = model.ConstrainedSketch(name='LRHole', sheetSize=50.0, transform=t)
        ps.CircleByCenterPerimeter(center=(HALF_THICK, LOWER_PIN_Y), point1=(HALF_THICK + PIN_RADIUS, LOWER_PIN_Y))

        part.CutExtrude(
            sketchPlane=lr_faces[0],
            sketchUpEdge=lr_edges[0],
            sketchPlaneSide=SIDE1,
            sketch=ps,
            depth=BLOCK_WIDTH_X,
            flipExtrudeDirection=ON
        )
        print("LOWER RIGHT PIN HOLE CUT")

# Lower left
ll_faces = part.faces.getByBoundingBox(
    xMin=LB_LEFT_XMIN-0.01, xMax=LB_LEFT_XMIN+0.01,
    yMin=0, yMax=BLOCK_HEIGHT_Y,
    zMin=0, zMax=THICKNESS
)
print("Lower left face candidates: {}".format(len(ll_faces)))

if len(ll_faces) > 0:
    ll_edges = part.edges.getByBoundingBox(
        xMin=LB_LEFT_XMIN-0.01, xMax=LB_LEFT_XMIN+0.01,
        yMin=BLOCK_HEIGHT_Y-0.1, yMax=BLOCK_HEIGHT_Y+0.1,
        zMin=0, zMax=THICKNESS
    )
    print("Lower left edge candidates: {}".format(len(ll_edges)))

    if len(ll_edges) > 0:
        t = part.MakeSketchTransform(
            sketchPlane=ll_faces[0],
            sketchUpEdge=ll_edges[0],
            sketchPlaneSide=SIDE1,
            origin=(0, 0, 0)
        )
        ps = model.ConstrainedSketch(name='LLHole', sheetSize=50.0, transform=t)
        ps.CircleByCenterPerimeter(center=(HALF_THICK, LOWER_PIN_Y), point1=(HALF_THICK + PIN_RADIUS, LOWER_PIN_Y))

        part.CutExtrude(
            sketchPlane=ll_faces[0],
            sketchUpEdge=ll_edges[0],
            sketchPlaneSide=SIDE1,
            sketch=ps,
            depth=BLOCK_WIDTH_X,
            flipExtrudeDirection=OFF
        )
        print("LOWER LEFT PIN HOLE CUT")

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
print("GEOMETRY v9 COMPLETE")
print("="*60)
