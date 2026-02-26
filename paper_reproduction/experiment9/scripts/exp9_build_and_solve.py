# -*- coding: utf-8 -*-
"""
Experiment 9 - Step 1: Build IN718 fatigue specimen and run static FEA.
Combines experiment 4 geometry + mesh + material + 20kN load case into one script.
Run with: abaqus cae noGUI=exp9_build_and_solve.py
"""

import os
import sys
from abaqus import *
from abaqusConstants import *
from caeModules import *
import mesh

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, os.pardir))
WORK_DIR = os.path.join(PROJECT_DIR, 'run')
if not os.path.isdir(WORK_DIR):
    os.makedirs(WORK_DIR)
os.chdir(WORK_DIR)

MESH_SIZE = float(os.environ.get('ABAQUS_MESH_SIZE', '3.0'))
NUM_CPUS = int(os.environ.get('ABAQUS_NUM_CPUS', '1'))

print('[1/8] Creating model and sketch...')

# =========================================================================
# DIMENSIONS (from experiment 4)
# =========================================================================
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

# =========================================================================
# CREATE MODEL AND GEOMETRY
# =========================================================================
model_name = 'Experiment9'
part_name = 'TO_Specimen'

if model_name in mdb.models.keys():
    del mdb.models[model_name]
model = mdb.Model(name=model_name)
if 'Model-1' in mdb.models.keys():
    del mdb.models['Model-1']

part = model.Part(name=part_name, dimensionality=THREE_D, type=DEFORMABLE_BODY)

# --- Base sketch (exact experiment 4 profile) ---
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
print('[2/8] Base geometry created. Cutting pin holes...')


# =========================================================================
# HELPER: find vertical edge on a face
# =========================================================================
def find_vertical_edge_on_face(part_obj, face_obj, thickness):
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


# --- Upper pin hole ---
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
        print('  Upper pin hole cut.')

# --- Lower right pin hole ---
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
        print('  Lower right pin hole cut.')

# --- Lower left pin hole ---
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
        print('  Lower left pin hole cut.')

# Verify pin holes
circular_count = 0
for edge in part.edges:
    try:
        r = edge.getRadius()
        if r is not None and abs(r - PIN_RADIUS) < 0.5:
            circular_count += 1
    except:
        pass
print('  Pin hole circular edges found: {} (expect 6 for 3 holes)'.format(circular_count))

# =========================================================================
# MESH (part-level, TET free mesh — same as experiment 4)
# =========================================================================
print('[3/8] Meshing part (size={})...'.format(MESH_SIZE))
part.setMeshControls(regions=part.cells, elemShape=TET, technique=FREE)
part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)
elemType1 = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType1, elemType2))
part.generateMesh()
print('  Nodes: {}, Elements: {}'.format(len(part.nodes), len(part.elements)))

# =========================================================================
# MATERIAL + SECTION
# =========================================================================
print('[4/8] Applying material IN718 and section...')
mat = model.Material(name='IN718')
mat.Elastic(table=((200000.0, 0.3),))
mat.Density(table=((8.19e-9,),))
mat.Plastic(table=((980.0, 0.0), (1100.0, 0.05), (1241.0, 0.10)))

model.HomogeneousSolidSection(name='SolidSection', material='IN718', thickness=None)
region = part.Set(cells=part.cells, name='AllCells')
part.SectionAssignment(region=region, sectionName='SolidSection')

# =========================================================================
# ASSEMBLY
# =========================================================================
print('[5/8] Creating assembly...')
assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
instance = assembly.Instance(name=part_name + '-1', part=part, dependent=ON)

# =========================================================================
# STEP + BCS + LOADS (from experiment 4 setup_20kN.py)
# =========================================================================
print('[6/8] Applying step, BCs, and 20kN load...')
model.StaticStep(name='FatigueTest', previous='Initial', nlgeom=ON,
    initialInc=0.1, maxNumInc=100, minInc=1e-8)

# Find pin hole surfaces via bounding cylinder
lower_left_faces = instance.faces.getByBoundingCylinder(
    center1=(LB_LEFT_XMIN - 1, LOWER_PIN_Y, HALF_THICK),
    center2=(LB_LEFT_XMAX + 1, LOWER_PIN_Y, HALF_THICK),
    radius=PIN_RADIUS + 0.5)
lower_right_faces = instance.faces.getByBoundingCylinder(
    center1=(LB_RIGHT_XMIN - 1, LOWER_PIN_Y, HALF_THICK),
    center2=(LB_RIGHT_XMAX + 1, LOWER_PIN_Y, HALF_THICK),
    radius=PIN_RADIUS + 0.5)
upper_faces = instance.faces.getByBoundingCylinder(
    center1=(UB_LEFT - 1, UPPER_PIN_Y, HALF_THICK),
    center2=(UB_RIGHT + 1, UPPER_PIN_Y, HALF_THICK),
    radius=PIN_RADIUS + 0.5)

print('  Lower left faces: {}, Lower right: {}, Upper: {}'.format(
    len(lower_left_faces), len(lower_right_faces), len(upper_faces)))

if len(lower_left_faces) > 0:
    assembly.Set(faces=lower_left_faces, name='LowerLeftPinHole')
    model.DisplacementBC(name='LowerLeftPin_BC', createStepName='Initial',
        region=assembly.sets['LowerLeftPinHole'], u1=UNSET, u2=0.0, u3=0.0)

if len(lower_right_faces) > 0:
    assembly.Set(faces=lower_right_faces, name='LowerRightPinHole')
    model.DisplacementBC(name='LowerRightPin_BC', createStepName='Initial',
        region=assembly.sets['LowerRightPinHole'], u1=UNSET, u2=0.0, u3=0.0)

if len(upper_faces) > 0:
    assembly.Set(faces=upper_faces, name='UpperPinHole')
    assembly.Surface(side1Faces=upper_faces, name='UpperPinSurface')

# Reference point + coupling for upper pin
upper_rp = assembly.ReferencePoint(point=(0.0, UPPER_PIN_Y, HALF_THICK))
upper_rp_region = assembly.Set(
    referencePoints=(assembly.referencePoints[upper_rp.id],), name='UpperRP')

if len(upper_faces) > 0:
    model.Coupling(name='UpperPinCoupling', controlPoint=upper_rp_region,
        surface=assembly.surfaces['UpperPinSurface'], influenceRadius=WHOLE_SURFACE,
        couplingType=KINEMATIC, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)

# 20 kN concentrated force in Y direction
model.ConcentratedForce(name='VerticalLoad_20kN', createStepName='FatigueTest',
    region=upper_rp_region, cf2=20000.0)

# Field output
model.fieldOutputRequests['F-Output-1'].setValues(
    variables=('S', 'E', 'PE', 'PEEQ', 'U', 'RF'))

# =========================================================================
# JOB: SUBMIT AND WAIT
# =========================================================================
print('[7/8] Submitting Job_20kN...')
job_name = 'Job_20kN'
if job_name in mdb.jobs.keys():
    del mdb.jobs[job_name]
mdb.Job(name=job_name, model=model_name, type=ANALYSIS,
    numCpus=NUM_CPUS, numDomains=NUM_CPUS)

mdb.saveAs(os.path.join(WORK_DIR, 'exp9.cae'))

mdb.jobs[job_name].submit()
mdb.jobs[job_name].waitForCompletion()

# =========================================================================
# VERIFY
# =========================================================================
print('[8/8] Verifying results...')
odb_file = os.path.join(WORK_DIR, job_name + '.odb')
if os.path.exists(odb_file):
    print('  ODB file: {} ({} bytes)'.format(odb_file, os.path.getsize(odb_file)))
else:
    print('  ERROR: ODB file not found!')

sta_file = os.path.join(WORK_DIR, job_name + '.sta')
if os.path.exists(sta_file):
    with open(sta_file) as f:
        lines = f.readlines()
    for line in lines[-5:]:
        print('  .sta: ' + line.rstrip())

msg_file = os.path.join(WORK_DIR, job_name + '.msg')
if os.path.exists(msg_file):
    with open(msg_file) as f:
        content = f.read()
    if 'error' in content.lower():
        print('  WARNING: errors found in .msg file')
    else:
        print('  .msg: no errors')

print('')
print('Experiment 9 Step 1 complete.')
print('Working directory: ' + WORK_DIR)
