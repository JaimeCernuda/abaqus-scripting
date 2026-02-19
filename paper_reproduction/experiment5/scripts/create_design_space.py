# -*- coding: utf-8 -*-
"""
Experiment 5: Create design space for topology optimization.

Reuses the Experiment 4 IN718 specimen geometry but partitions it into
frozen regions (pin hole areas) and a design space (everything else).
Meshes with quadratic tet elements for TO accuracy.
"""

import os
from abaqus import *
from abaqusConstants import *
from caeModules import *
import mesh

try:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    # __file__ is not defined inside Abaqus CAE; use cwd instead
    SCRIPT_DIR = os.path.join(os.getcwd(), 'scripts')
PROJECT_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, os.pardir))
os.chdir(PROJECT_DIR)

MESH_SIZE = float(os.environ.get('ABAQUS_MESH_SIZE', '3.0'))

print("\n" + "=" * 70)
print("EXPERIMENT 5: TOPOLOGY OPTIMIZATION - DESIGN SPACE CREATION")
print("=" * 70)

# =============================================================================
# DIMENSIONS (same as Experiment 4)
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

# Frozen region margin around pin holes (mm)
FROZEN_MARGIN = 2.0

# =============================================================================
# CREATE MODEL
# =============================================================================
print("\n[1/7] Creating model...")

model_name = 'Experiment5_TO'
part_name = 'TO_Specimen'

if model_name in mdb.models.keys():
    del mdb.models[model_name]
model = mdb.Model(name=model_name)
if 'Model-1' in mdb.models.keys():
    del mdb.models['Model-1']

part = model.Part(name=part_name, dimensionality=THREE_D, type=DEFORMABLE_BODY)

# =============================================================================
# BASE SKETCH (identical to Experiment 4)
# =============================================================================
print("[2/7] Creating base geometry...")

s = model.ConstrainedSketch(name='Profile', sheetSize=300.0)

p1 = (UB_LEFT, UB_TOP)
p2 = (UB_RIGHT, UB_TOP)
p3 = (UB_RIGHT, NECK_TOP_Y)
p5 = (NECK_WIDTH / 2.0, NECK_BOT_Y)
p6 = (-NECK_WIDTH / 2.0, NECK_BOT_Y)
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
s.Spline(points=[p5, (NECK_WIDTH / 2.0 + 8.0, NECK_BOT_Y - 20.0),
                 (LB_RIGHT_XMAX - 5.0, BLOCK_HEIGHT_Y + 30.0), p9])
s.Line(point1=p9, point2=p10)
s.Line(point1=p10, point2=p11)
s.Line(point1=p11, point2=p12)
s.Spline(points=[p12, (LB_RIGHT_XMIN + 5.0, BLOCK_HEIGHT_Y + 25.0),
                 (JUNCTION_HALF_W + 10.0, JUNCTION_Y + 15.0), p7])
s.Line(point1=p7, point2=p8)
s.Spline(points=[p8, (-JUNCTION_HALF_W - 10.0, JUNCTION_Y + 15.0),
                 (LB_LEFT_XMAX - 5.0, BLOCK_HEIGHT_Y + 25.0), p13])
s.Line(point1=p13, point2=p14)
s.Line(point1=p14, point2=p15)
s.Line(point1=p15, point2=p16)
s.Spline(points=[p16, (LB_LEFT_XMIN + 5.0, BLOCK_HEIGHT_Y + 30.0),
                 (-NECK_WIDTH / 2.0 - 8.0, NECK_BOT_Y - 20.0), p6])
s.Line(point1=p6, point2=p4)
s.Line(point1=p4, point2=p1)

part.BaseSolidExtrude(sketch=s, depth=THICKNESS)
print("  Base geometry created")

# =============================================================================
# HELPER FUNCTION
# =============================================================================
def find_vertical_edge_on_face(part_obj, face_obj, thickness):
    """Find an edge that is vertical (runs in Y direction) on the given face."""
    edge_indices = face_obj.getEdges()
    for idx in edge_indices:
        edge = part_obj.edges[idx]
        verts = edge.getVertices()
        if len(verts) == 2:
            v1 = part_obj.vertices[verts[0]].pointOn[0]
            v2 = part_obj.vertices[verts[1]].pointOn[0]
            if abs(v1[0] - v2[0]) < 0.1 and abs(v1[2] - v2[2]) < 0.1:
                if abs(v1[2]) < 0.1 or abs(v1[2] - thickness) < 0.1:
                    return edge
    for idx in edge_indices:
        edge = part_obj.edges[idx]
        verts = edge.getVertices()
        if len(verts) == 2:
            v1 = part_obj.vertices[verts[0]].pointOn[0]
            v2 = part_obj.vertices[verts[1]].pointOn[0]
            if abs(v1[0] - v2[0]) < 0.1 and abs(v1[2] - v2[2]) < 0.1:
                return edge
    return None

# =============================================================================
# PIN HOLES (same as Experiment 4)
# =============================================================================
print("[3/7] Cutting pin holes...")

# Upper pin hole
upper_face = part.faces.findAt(((-9.0, 127.5, 16.7),))
if upper_face:
    vertical_edge = find_vertical_edge_on_face(part, upper_face[0], THICKNESS)
    if vertical_edge:
        t = part.MakeSketchTransform(
            sketchPlane=upper_face[0], sketchUpEdge=vertical_edge,
            sketchPlaneSide=SIDE1, sketchOrientation=RIGHT,
            origin=(-9.0, UPPER_PIN_Y, HALF_THICK))
        ps = model.ConstrainedSketch(name='UpperHole', sheetSize=50.0, transform=t)
        ps.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))
        part.CutExtrude(
            sketchPlane=upper_face[0], sketchUpEdge=vertical_edge,
            sketchPlaneSide=SIDE1, sketchOrientation=RIGHT,
            sketch=ps, depth=BLOCK_WIDTH_X, flipExtrudeDirection=OFF)
        print("  Upper pin hole cut")

# Lower right pin hole
lr_face = part.faces.findAt(((14.3, 9.3, 16.7),))
if lr_face:
    vertical_edge = find_vertical_edge_on_face(part, lr_face[0], THICKNESS)
    if vertical_edge:
        t = part.MakeSketchTransform(
            sketchPlane=lr_face[0], sketchUpEdge=vertical_edge,
            sketchPlaneSide=SIDE1, sketchOrientation=RIGHT,
            origin=(LB_RIGHT_XMIN, LOWER_PIN_Y, HALF_THICK))
        ps = model.ConstrainedSketch(name='LRHole', sheetSize=50.0, transform=t)
        ps.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))
        part.CutExtrude(
            sketchPlane=lr_face[0], sketchUpEdge=vertical_edge,
            sketchPlaneSide=SIDE1, sketchOrientation=RIGHT,
            sketch=ps, depth=BLOCK_WIDTH_X, flipExtrudeDirection=OFF)
        print("  Lower right pin hole cut")

# Lower left pin hole
ll_face = part.faces.findAt(((-32.3, 9.3, 16.7),))
if ll_face:
    vertical_edge = find_vertical_edge_on_face(part, ll_face[0], THICKNESS)
    if vertical_edge:
        t = part.MakeSketchTransform(
            sketchPlane=ll_face[0], sketchUpEdge=vertical_edge,
            sketchPlaneSide=SIDE1, sketchOrientation=RIGHT,
            origin=(-32.3, LOWER_PIN_Y, HALF_THICK))
        ps = model.ConstrainedSketch(name='LLHole', sheetSize=50.0, transform=t)
        ps.CircleByCenterPerimeter(center=(0, 0), point1=(PIN_RADIUS, 0))
        part.CutExtrude(
            sketchPlane=ll_face[0], sketchUpEdge=vertical_edge,
            sketchPlaneSide=SIDE1, sketchOrientation=RIGHT,
            sketch=ps, depth=BLOCK_WIDTH_X, flipExtrudeDirection=OFF)
        print("  Lower left pin hole cut")

# =============================================================================
# PARTITION INTO FROZEN REGIONS
# =============================================================================
print("[4/7] Partitioning frozen regions around pin holes...")

# Create datum planes to partition the upper block from the design space
# Upper block boundary: Y = UB_BOTTOM (118.17)
dp_upper = part.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=UB_BOTTOM)
part.PartitionCellByDatumPlane(datumPlane=part.datums[dp_upper.id], cells=part.cells)

# Lower block boundary: Y = BLOCK_HEIGHT_Y (28.0)
dp_lower = part.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=BLOCK_HEIGHT_Y)
cells_to_partition = part.cells.getByBoundingBox(
    xMin=-HALF_WIDTH - 1, yMin=-1, zMin=-1,
    xMax=HALF_WIDTH + 1, yMax=UB_BOTTOM + 1, zMax=THICKNESS + 1)
if len(cells_to_partition) > 0:
    part.PartitionCellByDatumPlane(datumPlane=part.datums[dp_lower.id],
                                   cells=cells_to_partition)

# =============================================================================
# CREATE NAMED SETS
# =============================================================================
print("[5/7] Creating region sets...")

# Upper pin frozen region (cells above UB_BOTTOM)
upper_cells = part.cells.getByBoundingBox(
    xMin=UB_LEFT - 1, yMin=UB_BOTTOM - 0.1, zMin=-1,
    xMax=UB_RIGHT + 1, yMax=UB_TOP + 1, zMax=THICKNESS + 1)
if len(upper_cells) > 0:
    part.Set(cells=upper_cells, name='FrozenUpperPin')
    print("  FrozenUpperPin: {} cells".format(len(upper_cells)))

# Lower left pin frozen region
ll_cells = part.cells.getByBoundingBox(
    xMin=LB_LEFT_XMIN - 1, yMin=-1, zMin=-1,
    xMax=LB_LEFT_XMAX + 1, yMax=BLOCK_HEIGHT_Y + 0.1, zMax=THICKNESS + 1)
if len(ll_cells) > 0:
    part.Set(cells=ll_cells, name='FrozenLowerLeftPin')
    print("  FrozenLowerLeftPin: {} cells".format(len(ll_cells)))

# Lower right pin frozen region
lr_cells = part.cells.getByBoundingBox(
    xMin=LB_RIGHT_XMIN - 1, yMin=-1, zMin=-1,
    xMax=LB_RIGHT_XMAX + 1, yMax=BLOCK_HEIGHT_Y + 0.1, zMax=THICKNESS + 1)
if len(lr_cells) > 0:
    part.Set(cells=lr_cells, name='FrozenLowerRightPin')
    print("  FrozenLowerRightPin: {} cells".format(len(lr_cells)))

# Design space = all remaining cells (middle region)
design_cells = part.cells.getByBoundingBox(
    xMin=-HALF_WIDTH - 1, yMin=BLOCK_HEIGHT_Y - 0.1, zMin=-1,
    xMax=HALF_WIDTH + 1, yMax=UB_BOTTOM + 0.1, zMax=THICKNESS + 1)
if len(design_cells) > 0:
    part.Set(cells=design_cells, name='DesignSpace')
    print("  DesignSpace: {} cells".format(len(design_cells)))

# All cells
part.Set(cells=part.cells, name='AllCells')

# =============================================================================
# MATERIAL (elastic only - TO uses linear analysis)
# =============================================================================
print("[6/7] Defining material and meshing...")

mat = model.Material(name='IN718')
mat.Elastic(table=((200000.0, 0.3),))
mat.Density(table=((8.19e-9,),))

model.HomogeneousSolidSection(name='SolidSection', material='IN718', thickness=None)
region = part.sets['AllCells']
part.SectionAssignment(region=region, sectionName='SolidSection')

# =============================================================================
# MESH
# =============================================================================
part.setMeshControls(regions=part.cells, elemShape=TET, technique=FREE)
part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)
elemType1 = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType1, elemType2))
part.generateMesh()

print("  Mesh: {} nodes, {} elements".format(len(part.nodes), len(part.elements)))

# =============================================================================
# ASSEMBLY
# =============================================================================
print("[7/7] Creating assembly...")

assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
assembly.Instance(name=part_name + '-1', part=part, dependent=ON)

# =============================================================================
# SAVE
# =============================================================================
mdb.saveAs(os.path.join(PROJECT_DIR, 'Experiment5_TO.cae'))

print("\n" + "=" * 70)
print("Design space created successfully")
print("  Nodes: {}".format(len(part.nodes)))
print("  Elements: {}".format(len(part.elements)))
print("  Mesh size: {} mm".format(MESH_SIZE))
print("  CAE saved: Experiment5_TO.cae")
print("=" * 70)
