# -*- coding: utf-8 -*-
"""
Experiment 4: TO Specimen v10 - Using exact face coordinates from debug
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

# =============================================================================
# CUT PIN HOLES using exact coordinates from debug
# =============================================================================

# UPPER PIN HOLE
# Face 1: pt=(9.0, 136.8, 16.7) norm=(1.0, 0.0, 0.0)
upper_face = part.faces.findAt(((9.0, 136.8, 16.7),))
# Find an edge on this face for sketchUpEdge - vertical edge at Z=0
# The face spans Y from ~118 to 146, so find edge at Y=146 or Y=118
upper_edge_candidates = []
for edge_idx in upper_face[0].getEdges():
    edge = part.edges[edge_idx]
    pt = edge.pointOn[0]
    # Look for edge at Z=0 (front) or Z=25 (back) that's vertical
    if abs(pt[2]) < 1 or abs(pt[2] - THICKNESS) < 1:
        upper_edge_candidates.append(edge)

if len(upper_edge_candidates) > 0:
    upper_edge = upper_edge_candidates[0]

    # Create sketch - on YZ face, coordinates are (z, y) relative to origin
    t = part.MakeSketchTransform(
        sketchPlane=upper_face[0],
        sketchUpEdge=upper_edge,
        sketchPlaneSide=SIDE1,
        sketchOrientation=RIGHT,
        origin=(9.0, UPPER_PIN_Y, HALF_THICK)
    )
    ps = model.ConstrainedSketch(name='UpperHole', sheetSize=50.0, transform=t)
    ps.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

    part.CutExtrude(
        sketchPlane=upper_face[0],
        sketchUpEdge=upper_edge,
        sketchPlaneSide=SIDE1,
        sketchOrientation=RIGHT,
        sketch=ps,
        depth=BLOCK_WIDTH_X,
        flipExtrudeDirection=ON  # Cut toward -X
    )
    print("UPPER PIN HOLE SUCCESS")
else:
    print("No edge found for upper face")

# LOWER RIGHT PIN HOLE
# Face 4: pt=(32.3, 18.7, 20.8) norm=(1.0, 0.0, 0.0)
lr_face = part.faces.findAt(((32.3, 18.7, 20.8),))
lr_edge_candidates = []
for edge_idx in lr_face[0].getEdges():
    edge = part.edges[edge_idx]
    pt = edge.pointOn[0]
    if abs(pt[2]) < 1 or abs(pt[2] - THICKNESS) < 1:
        lr_edge_candidates.append(edge)

if len(lr_edge_candidates) > 0:
    lr_edge = lr_edge_candidates[0]

    t = part.MakeSketchTransform(
        sketchPlane=lr_face[0],
        sketchUpEdge=lr_edge,
        sketchPlaneSide=SIDE1,
        sketchOrientation=RIGHT,
        origin=(32.3, LOWER_PIN_Y, HALF_THICK)
    )
    ps = model.ConstrainedSketch(name='LRHole', sheetSize=50.0, transform=t)
    ps.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

    part.CutExtrude(
        sketchPlane=lr_face[0],
        sketchUpEdge=lr_edge,
        sketchPlaneSide=SIDE1,
        sketchOrientation=RIGHT,
        sketch=ps,
        depth=BLOCK_WIDTH_X,
        flipExtrudeDirection=ON
    )
    print("LOWER RIGHT PIN HOLE SUCCESS")
else:
    print("No edge found for lower right face")

# LOWER LEFT PIN HOLE
# Face 12: pt=(-32.3, 9.3, 16.7) norm=(-1.0, 0.0, 0.0)
ll_face = part.faces.findAt(((-32.3, 9.3, 16.7),))
ll_edge_candidates = []
for edge_idx in ll_face[0].getEdges():
    edge = part.edges[edge_idx]
    pt = edge.pointOn[0]
    if abs(pt[2]) < 1 or abs(pt[2] - THICKNESS) < 1:
        ll_edge_candidates.append(edge)

if len(ll_edge_candidates) > 0:
    ll_edge = ll_edge_candidates[0]

    t = part.MakeSketchTransform(
        sketchPlane=ll_face[0],
        sketchUpEdge=ll_edge,
        sketchPlaneSide=SIDE1,
        sketchOrientation=RIGHT,
        origin=(-32.3, LOWER_PIN_Y, HALF_THICK)
    )
    ps = model.ConstrainedSketch(name='LLHole', sheetSize=50.0, transform=t)
    ps.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

    part.CutExtrude(
        sketchPlane=ll_face[0],
        sketchUpEdge=ll_edge,
        sketchPlaneSide=SIDE1,
        sketchOrientation=RIGHT,
        sketch=ps,
        depth=BLOCK_WIDTH_X,
        flipExtrudeDirection=OFF  # Cut toward +X (norm is -X, so OFF to go into material)
    )
    print("LOWER LEFT PIN HOLE SUCCESS")
else:
    print("No edge found for lower left face")

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
print("GEOMETRY v10 COMPLETE")
print("="*60)
