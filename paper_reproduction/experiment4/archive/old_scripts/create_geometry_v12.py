# -*- coding: utf-8 -*-
"""
Experiment 4: TO Specimen v12 - Using datum planes for reliable hole creation
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
# CREATE DATUM PLANES FOR PIN HOLES
# =============================================================================
# Upper pin hole: Create datum plane at X=UB_RIGHT (YZ plane offset in X)
upper_datum = part.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=UB_RIGHT)
upper_datum_id = upper_datum.id

# Lower right pin hole: Datum plane at X=LB_RIGHT_XMAX
lr_datum = part.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=LB_RIGHT_XMAX)
lr_datum_id = lr_datum.id

# Lower left pin hole: Datum plane at X=LB_LEFT_XMIN
ll_datum = part.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=LB_LEFT_XMIN)
ll_datum_id = ll_datum.id

print("Datum planes created")

# =============================================================================
# UPPER PIN HOLE - Cut on datum plane
# =============================================================================
# Find an edge on the upper block for sketchUpEdge
# Top edge of upper block at Y=TOTAL_HEIGHT
upper_edge = part.edges.findAt(((0.0, TOTAL_HEIGHT, HALF_THICK),))

# Create sketch on datum plane
t = part.MakeSketchTransform(
    sketchPlane=part.datums[upper_datum_id],
    sketchUpEdge=upper_edge[0],
    sketchPlaneSide=SIDE1,
    sketchOrientation=RIGHT,
    origin=(UB_RIGHT, UPPER_PIN_Y, HALF_THICK)
)
ps = model.ConstrainedSketch(name='UpperHole', sheetSize=50.0, transform=t)
ps.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

part.CutExtrude(
    sketchPlane=part.datums[upper_datum_id],
    sketchUpEdge=upper_edge[0],
    sketchPlaneSide=SIDE1,
    sketchOrientation=RIGHT,
    sketch=ps,
    depth=BLOCK_WIDTH_X,
    flipExtrudeDirection=ON  # Cut toward -X (into upper block)
)
print("Upper pin hole created")

# =============================================================================
# LOWER RIGHT PIN HOLE
# =============================================================================
# Find edge on lower right block
lr_edge = part.edges.findAt(((LB_RIGHT_XMAX, BLOCK_HEIGHT_Y, HALF_THICK),))

t = part.MakeSketchTransform(
    sketchPlane=part.datums[lr_datum_id],
    sketchUpEdge=lr_edge[0],
    sketchPlaneSide=SIDE1,
    sketchOrientation=RIGHT,
    origin=(LB_RIGHT_XMAX, LOWER_PIN_Y, HALF_THICK)
)
ps = model.ConstrainedSketch(name='LRHole', sheetSize=50.0, transform=t)
ps.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

part.CutExtrude(
    sketchPlane=part.datums[lr_datum_id],
    sketchUpEdge=lr_edge[0],
    sketchPlaneSide=SIDE1,
    sketchOrientation=RIGHT,
    sketch=ps,
    depth=BLOCK_WIDTH_X,
    flipExtrudeDirection=ON  # Cut toward -X (into lower right block)
)
print("Lower right pin hole created")

# =============================================================================
# LOWER LEFT PIN HOLE
# =============================================================================
# Find edge on lower left block
ll_edge = part.edges.findAt(((LB_LEFT_XMIN, BLOCK_HEIGHT_Y, HALF_THICK),))

t = part.MakeSketchTransform(
    sketchPlane=part.datums[ll_datum_id],
    sketchUpEdge=ll_edge[0],
    sketchPlaneSide=SIDE1,
    sketchOrientation=RIGHT,
    origin=(LB_LEFT_XMIN, LOWER_PIN_Y, HALF_THICK)
)
ps = model.ConstrainedSketch(name='LLHole', sheetSize=50.0, transform=t)
ps.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))

part.CutExtrude(
    sketchPlane=part.datums[ll_datum_id],
    sketchUpEdge=ll_edge[0],
    sketchPlaneSide=SIDE1,
    sketchOrientation=RIGHT,
    sketch=ps,
    depth=BLOCK_WIDTH_X,
    flipExtrudeDirection=OFF  # Cut toward +X (into lower left block)
)
print("Lower left pin hole created")

# =============================================================================
# ASSEMBLY
# =============================================================================
assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
assembly.Instance(name=part_name+'-1', part=part, dependent=ON)

# =============================================================================
# SAVE
# =============================================================================
mdb.saveAs(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v12.cae')

print("\n" + "="*60)
print("GEOMETRY v12 COMPLETE")
print("="*60)
