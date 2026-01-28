# -*- coding: utf-8 -*-
"""
Experiment 4: TO Specimen v8 - Boolean subtraction approach
Create pin cylinders as separate parts and subtract them
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

# =============================================================================
# CREATE MAIN BODY
# =============================================================================
part = model.Part(name=part_name, dimensionality=THREE_D, type=DEFORMABLE_BODY)

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
# CREATE PIN HOLE CYLINDERS (extruded in X direction)
# These will be subtracted from the main body
# =============================================================================

# For a horizontal cylinder along X, we need to:
# 1. Create sketch in YZ plane (circle at Y, Z position)
# 2. Extrude along X direction

# Upper pin cylinder
upper_cyl = model.Part(name='UpperPinCyl', dimensionality=THREE_D, type=DEFORMABLE_BODY)
upper_sketch = model.ConstrainedSketch(name='UpperCylSketch', sheetSize=50.0)
# Circle centered at (Z, Y) in the YZ sketch plane
# But sketch is in XY plane by default, so we create in XY then position in assembly
upper_sketch.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))
upper_cyl.BaseSolidExtrude(sketch=upper_sketch, depth=BLOCK_WIDTH_X + 2)  # Slightly longer to ensure full cut
print("Upper pin cylinder created")

# Lower left pin cylinder
left_cyl = model.Part(name='LeftPinCyl', dimensionality=THREE_D, type=DEFORMABLE_BODY)
left_sketch = model.ConstrainedSketch(name='LeftCylSketch', sheetSize=50.0)
left_sketch.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))
left_cyl.BaseSolidExtrude(sketch=left_sketch, depth=BLOCK_WIDTH_X + 2)
print("Left pin cylinder created")

# Lower right pin cylinder
right_cyl = model.Part(name='RightPinCyl', dimensionality=THREE_D, type=DEFORMABLE_BODY)
right_sketch = model.ConstrainedSketch(name='RightCylSketch', sheetSize=50.0)
right_sketch.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))
right_cyl.BaseSolidExtrude(sketch=right_sketch, depth=BLOCK_WIDTH_X + 2)
print("Right pin cylinder created")

# =============================================================================
# ASSEMBLY - Position cylinders and perform Boolean cut
# =============================================================================
assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)

# Main body instance
main_inst = assembly.Instance(name='Main-1', part=part, dependent=OFF)

# Cylinder instances - need to rotate and translate to correct position
# Cylinders are created along Z axis (default extrude), need to rotate to X axis

# Upper pin: rotate 90° about Y axis, then translate to position
upper_inst = assembly.Instance(name='UpperCyl-1', part=upper_cyl, dependent=OFF)
# Rotate to align along X (cylinder axis becomes X axis)
assembly.rotate(
    instanceList=('UpperCyl-1',),
    axisPoint=(0, 0, 0),
    axisDirection=(0, 1, 0),  # Y axis
    angle=90.0
)
# Translate to position (X=UB_RIGHT+1 to start outside, Y=UPPER_PIN_Y, Z=HALF_THICK)
assembly.translate(
    instanceList=('UpperCyl-1',),
    vector=(UB_RIGHT + 1, UPPER_PIN_Y, HALF_THICK)
)
print("Upper cylinder positioned")

# Left pin
left_inst = assembly.Instance(name='LeftCyl-1', part=left_cyl, dependent=OFF)
assembly.rotate(
    instanceList=('LeftCyl-1',),
    axisPoint=(0, 0, 0),
    axisDirection=(0, 1, 0),
    angle=90.0
)
assembly.translate(
    instanceList=('LeftCyl-1',),
    vector=(LB_LEFT_XMAX + 1, LOWER_PIN_Y, HALF_THICK)
)
print("Left cylinder positioned")

# Right pin
right_inst = assembly.Instance(name='RightCyl-1', part=right_cyl, dependent=OFF)
assembly.rotate(
    instanceList=('RightCyl-1',),
    axisPoint=(0, 0, 0),
    axisDirection=(0, 1, 0),
    angle=90.0
)
assembly.translate(
    instanceList=('RightCyl-1',),
    vector=(LB_RIGHT_XMAX + 1, LOWER_PIN_Y, HALF_THICK)
)
print("Right cylinder positioned")

# =============================================================================
# BOOLEAN CUT - Subtract cylinders from main body
# =============================================================================
# Cut upper pin
assembly.InstanceFromBooleanCut(
    name='TO_Specimen_Cut1',
    instanceToBeCut=main_inst,
    cuttingInstances=(upper_inst,),
    originalInstances=SUPPRESS
)
print("Upper pin hole cut")

# Get the new instance
cut1_inst = assembly.instances['TO_Specimen_Cut1-1']

# Cut left pin
assembly.InstanceFromBooleanCut(
    name='TO_Specimen_Cut2',
    instanceToBeCut=cut1_inst,
    cuttingInstances=(left_inst,),
    originalInstances=SUPPRESS
)
print("Left pin hole cut")

cut2_inst = assembly.instances['TO_Specimen_Cut2-1']

# Cut right pin
assembly.InstanceFromBooleanCut(
    name='TO_Specimen_Final',
    instanceToBeCut=cut2_inst,
    cuttingInstances=(right_inst,),
    originalInstances=SUPPRESS
)
print("Right pin hole cut")

# =============================================================================
# CLEANUP - Delete suppressed instances and cylinder parts
# =============================================================================
# The final geometry is in TO_Specimen_Final-1

# =============================================================================
# SAVE
# =============================================================================
mdb.saveAs(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen.cae')

print("\n" + "="*60)
print("GEOMETRY v8 COMPLETE - Boolean cut approach")
print("Final part: TO_Specimen_Final")
print("="*60)
