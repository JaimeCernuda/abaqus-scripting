# -*- coding: utf-8 -*-
"""
Experiment 4: TO Specimen v11 - Debug edge finding and try different approach
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

log_file = open(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/geometry_debug_v16.txt', 'w')

def log(msg):
    log_file.write(msg + '\n')
    log_file.flush()

def find_vertical_edge_on_face(part_obj, face_obj, thickness):
    """Find an edge that is vertical (runs in Y direction) on the given face."""
    edge_indices = face_obj.getEdges()
    for idx in edge_indices:
        edge = part_obj.edges[idx]
        verts = edge.getVertices()
        if len(verts) == 2:
            v1 = part_obj.vertices[verts[0]].pointOn[0]
            v2 = part_obj.vertices[verts[1]].pointOn[0]
            # Check if edge is vertical (same X and Z, different Y)
            if abs(v1[0] - v2[0]) < 0.1 and abs(v1[2] - v2[2]) < 0.1:
                # This edge is vertical - prefer ones at Z=0 or Z=THICKNESS
                if abs(v1[2]) < 0.1 or abs(v1[2] - thickness) < 0.1:
                    log("Found vertical edge {} at Z={:.1f}".format(idx, v1[2]))
                    return edge
    # Fallback: return first vertical edge found
    for idx in edge_indices:
        edge = part_obj.edges[idx]
        verts = edge.getVertices()
        if len(verts) == 2:
            v1 = part_obj.vertices[verts[0]].pointOn[0]
            v2 = part_obj.vertices[verts[1]].pointOn[0]
            if abs(v1[0] - v2[0]) < 0.1 and abs(v1[2] - v2[2]) < 0.1:
                log("Fallback: vertical edge {} at Z={:.1f}".format(idx, v1[2]))
                return edge
    log("No vertical edge found!")
    return None

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
log("Base geometry created")

# =============================================================================
# UPPER PIN HOLE - Use INNER face (Face 15 at X=-9, norm=-X) like the working lower left
# =============================================================================
log("\n=== UPPER PIN HOLE ===")
# Use inner face at X=-9 with norm=(-1,0,0) - same orientation as working lower left
upper_face = part.faces.findAt(((-9.0, 127.5, 16.7),))
log("Upper face (inner) found: {}".format(upper_face))

if upper_face:
    edge_indices = upper_face[0].getEdges()
    log("Edge indices on face: {}".format(edge_indices))

    for idx in edge_indices:
        edge = part.edges[idx]
        pt = edge.pointOn[0]
        verts = edge.getVertices()
        if len(verts) == 2:
            v1 = part.vertices[verts[0]].pointOn[0]
            v2 = part.vertices[verts[1]].pointOn[0]
            log("  Edge {}: pt=({:.1f}, {:.1f}, {:.1f}) v1=({:.1f},{:.1f},{:.1f}) v2=({:.1f},{:.1f},{:.1f})".format(
                idx, pt[0], pt[1], pt[2], v1[0], v1[1], v1[2], v2[0], v2[1], v2[2]))

    # Find a vertical edge (runs in Y direction)
    vertical_edge = find_vertical_edge_on_face(part, upper_face[0], THICKNESS)

    if vertical_edge:
        try:
            t = part.MakeSketchTransform(
                sketchPlane=upper_face[0],
                sketchUpEdge=vertical_edge,
                sketchPlaneSide=SIDE1,
                sketchOrientation=RIGHT,
                origin=(-9.0, UPPER_PIN_Y, HALF_THICK)
            )
            ps = model.ConstrainedSketch(name='UpperHole', sheetSize=50.0, transform=t)
            ps.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

            # Same settings as working lower left: flipExtrudeDirection=OFF
            part.CutExtrude(
                sketchPlane=upper_face[0],
                sketchUpEdge=vertical_edge,
                sketchPlaneSide=SIDE1,
                sketchOrientation=RIGHT,
                sketch=ps,
                depth=BLOCK_WIDTH_X,
                flipExtrudeDirection=OFF
            )
            log("UPPER PIN HOLE CUT SUCCESS")
        except Exception as e:
            log("UPPER PIN HOLE ERROR: {}".format(str(e)))

# =============================================================================
# LOWER RIGHT PIN HOLE - Use INNER face (Face 6 at X=14.3, norm=-X) like the working lower left
# =============================================================================
log("\n=== LOWER RIGHT PIN HOLE ===")
# Use inner face at X=14.3 with norm=(-1,0,0) - same orientation as working lower left
# LB_RIGHT_XMIN = 14.3
lr_face = part.faces.findAt(((14.3, 9.3, 16.7),))
log("Lower right face (inner) found: {}".format(lr_face))

if lr_face:
    edge_indices = lr_face[0].getEdges()
    log("Edge indices on face: {}".format(edge_indices))

    for idx in edge_indices:
        edge = part.edges[idx]
        pt = edge.pointOn[0]
        verts = edge.getVertices()
        if len(verts) == 2:
            v1 = part.vertices[verts[0]].pointOn[0]
            v2 = part.vertices[verts[1]].pointOn[0]
            log("  Edge {}: pt=({:.1f}, {:.1f}, {:.1f}) v1=({:.1f},{:.1f},{:.1f}) v2=({:.1f},{:.1f},{:.1f})".format(
                idx, pt[0], pt[1], pt[2], v1[0], v1[1], v1[2], v2[0], v2[1], v2[2]))

    # Find a vertical edge
    vertical_edge = find_vertical_edge_on_face(part, lr_face[0], THICKNESS)

    if vertical_edge:
        try:
            t = part.MakeSketchTransform(
                sketchPlane=lr_face[0],
                sketchUpEdge=vertical_edge,
                sketchPlaneSide=SIDE1,
                sketchOrientation=RIGHT,
                origin=(LB_RIGHT_XMIN, LOWER_PIN_Y, HALF_THICK)
            )
            ps = model.ConstrainedSketch(name='LRHole', sheetSize=50.0, transform=t)
            ps.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

            # Same settings as working lower left: flipExtrudeDirection=OFF
            part.CutExtrude(
                sketchPlane=lr_face[0],
                sketchUpEdge=vertical_edge,
                sketchPlaneSide=SIDE1,
                sketchOrientation=RIGHT,
                sketch=ps,
                depth=BLOCK_WIDTH_X,
                flipExtrudeDirection=OFF
            )
            log("LOWER RIGHT PIN HOLE CUT SUCCESS")
        except Exception as e:
            log("LOWER RIGHT PIN HOLE ERROR: {}".format(str(e)))

# =============================================================================
# LOWER LEFT PIN HOLE
# =============================================================================
log("\n=== LOWER LEFT PIN HOLE ===")
ll_face = part.faces.findAt(((-32.3, 9.3, 16.7),))
log("Lower left face found: {}".format(ll_face))

if ll_face:
    edge_indices = ll_face[0].getEdges()
    log("Edge indices on face: {}".format(edge_indices))

    for idx in edge_indices:
        edge = part.edges[idx]
        pt = edge.pointOn[0]
        verts = edge.getVertices()
        if len(verts) == 2:
            v1 = part.vertices[verts[0]].pointOn[0]
            v2 = part.vertices[verts[1]].pointOn[0]
            log("  Edge {}: pt=({:.1f}, {:.1f}, {:.1f}) v1=({:.1f},{:.1f},{:.1f}) v2=({:.1f},{:.1f},{:.1f})".format(
                idx, pt[0], pt[1], pt[2], v1[0], v1[1], v1[2], v2[0], v2[1], v2[2]))

    # Find a vertical edge
    vertical_edge = find_vertical_edge_on_face(part, ll_face[0], THICKNESS)

    if vertical_edge:
        try:
            t = part.MakeSketchTransform(
                sketchPlane=ll_face[0],
                sketchUpEdge=vertical_edge,
                sketchPlaneSide=SIDE1,
                sketchOrientation=RIGHT,
                origin=(-32.3, LOWER_PIN_Y, HALF_THICK)
            )
            ps = model.ConstrainedSketch(name='LLHole', sheetSize=50.0, transform=t)
            ps.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

            part.CutExtrude(
                sketchPlane=ll_face[0],
                sketchUpEdge=vertical_edge,
                sketchPlaneSide=SIDE1,
                sketchOrientation=RIGHT,
                sketch=ps,
                depth=BLOCK_WIDTH_X,
                flipExtrudeDirection=OFF
            )
            log("LOWER LEFT PIN HOLE CUT SUCCESS")
        except Exception as e:
            log("LOWER LEFT PIN HOLE ERROR: {}".format(str(e)))

# =============================================================================
# VERIFY HOLES EXIST
# =============================================================================
log("\n=== VERIFYING HOLES ===")
circular_count = 0
for i, edge in enumerate(part.edges):
    try:
        radius = edge.getRadius()
        if radius is not None and abs(radius - PIN_RADIUS) < 0.5:
            pt = edge.pointOn[0]
            log("Circular edge {} at ({:.1f}, {:.1f}, {:.1f}) with radius {:.2f}".format(
                i, pt[0], pt[1], pt[2], radius))
            circular_count += 1
    except:
        pass

log("Total pin hole edges found: {}".format(circular_count))
# Each through-hole has 2 circular edges (front and back), so 3 holes = 6 edges
if circular_count >= 6:
    log("SUCCESS: All 3 holes appear to exist!")
else:
    log("WARNING: Expected 6 circular edges (3 holes), found {}".format(circular_count))

log_file.close()

# =============================================================================
# ASSEMBLY
# =============================================================================
assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
assembly.Instance(name=part_name+'-1', part=part, dependent=ON)

# =============================================================================
# SAVE
# =============================================================================
mdb.saveAs(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v16.cae')
