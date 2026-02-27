# -*- coding: utf-8 -*-
"""
Experiment 10: Full IN718 Topology Optimization (Stress-Constrained).

Reproduces the topology optimization from "Fatigue Response of a Topology
Optimized Feature-based Component" (Carr, Quach, Hochhalter, Sangid).

Minimizes volume subject to von Mises stress <= 800 MPa on an IN718 specimen
with rectangular envelope geometry.

Uses the proven hybrid pipeline:
  CAE API -> writeInput() -> flatten .inp -> generate .par -> tosca optimize CLI

Run with: abaqus cae noGUI=exp10_optimize.py
"""

from abaqus import *
from abaqusConstants import *
from caeModules import *
import mesh
import os
import sys
import re
import subprocess
import traceback

# =============================================================================
# PHASE 1: Configuration
# =============================================================================

SEPARATOR = "=" * 70

MESH_SIZE = float(os.environ.get('ABAQUS_MESH_SIZE', '3.0'))
NUM_CPUS = int(os.environ.get('ABAQUS_NUM_CPUS', '4'))
MAX_CYCLES = int(os.environ.get('ABAQUS_MAX_CYCLES', '20'))
STRESS_LIMIT = float(os.environ.get('ABAQUS_STRESS_LIMIT', '800.0'))

# Working directory
WORK_DIR = os.path.join(os.environ['HOME'], 'Abaqus', 'paper_reproduction',
                        'experiment10', 'run')
if not os.path.exists(WORK_DIR):
    os.makedirs(WORK_DIR)
os.chdir(WORK_DIR)

# Specimen dimensions (mm)
TOTAL_HEIGHT = 146.17
TOTAL_WIDTH = 64.60
THICKNESS = 25.0
BLOCK_WIDTH_X = 18.0
BLOCK_HEIGHT_Y = 28.0
PIN_DIAMETER = 12.7
PIN_RADIUS = PIN_DIAMETER / 2.0
HALF_WIDTH = TOTAL_WIDTH / 2.0
HALF_THICK = THICKNESS / 2.0
UB_BOTTOM = 118.17  # Y where upper block meets design space

# Pin centers
UPPER_PIN_Y = TOTAL_HEIGHT - BLOCK_HEIGHT_Y / 2.0  # 132.17
LOWER_PIN_Y = BLOCK_HEIGHT_Y / 2.0  # 14.0
LR_PIN_X = HALF_WIDTH - BLOCK_WIDTH_X / 2.0  # 23.30
LL_PIN_X = -HALF_WIDTH + BLOCK_WIDTH_X / 2.0  # -23.30

# Upper block half-width
UB_HALF = BLOCK_WIDTH_X / 2.0  # 9.0

# Lower block boundaries
LB_LEFT_XMIN = -HALF_WIDTH       # -32.30
LB_LEFT_XMAX = -HALF_WIDTH + BLOCK_WIDTH_X  # -14.30
LB_RIGHT_XMIN = HALF_WIDTH - BLOCK_WIDTH_X  # 14.30
LB_RIGHT_XMAX = HALF_WIDTH       # 32.30

print("")
print(SEPARATOR)
print("  EXPERIMENT 10: IN718 STRESS-CONSTRAINED TOPOLOGY OPTIMIZATION")
print("  Mesh: {} mm, CPUs: {}, Max cycles: {}, Stress limit: {} MPa".format(
    MESH_SIZE, NUM_CPUS, MAX_CYCLES, STRESS_LIMIT))
print("  Working dir: {}".format(WORK_DIR))
print(SEPARATOR)
sys.stdout.flush()

# =============================================================================
# PHASE 2: Rectangular Envelope Geometry
# =============================================================================

print("\n[1/9] Creating rectangular envelope geometry...")
sys.stdout.flush()

model_name = 'Experiment10_TO'
part_name = 'TO_Specimen'

if model_name in mdb.models.keys():
    del mdb.models[model_name]
model = mdb.Model(name=model_name)
if 'Model-1' in mdb.models.keys():
    del mdb.models['Model-1']

part = model.Part(name=part_name, dimensionality=THREE_D, type=DEFORMABLE_BODY)

s = model.ConstrainedSketch(name='Profile', sheetSize=300.0)

# I-beam cross section: 14 vertices, clockwise from top-left
pts = [
    (-UB_HALF,    TOTAL_HEIGHT),  # 0: top-left upper block
    ( UB_HALF,    TOTAL_HEIGHT),  # 1: top-right upper block
    ( UB_HALF,    UB_BOTTOM),     # 2: step-out right
    ( HALF_WIDTH, UB_BOTTOM),     # 3: full-width right top
    ( HALF_WIDTH, BLOCK_HEIGHT_Y),# 4: full-width right bottom
    ( HALF_WIDTH, 0.0),           # 5: lower-right outer bottom
    ( LB_RIGHT_XMIN, 0.0),       # 6: lower-right inner bottom
    ( LB_RIGHT_XMIN, BLOCK_HEIGHT_Y), # 7: lower-right inner top
    ( LB_LEFT_XMAX,  BLOCK_HEIGHT_Y), # 8: lower-left inner top
    ( LB_LEFT_XMAX,  0.0),       # 9: lower-left inner bottom
    (-HALF_WIDTH, 0.0),           # 10: lower-left outer bottom
    (-HALF_WIDTH, BLOCK_HEIGHT_Y),# 11: lower-left outer top
    (-HALF_WIDTH, UB_BOTTOM),     # 12: full-width left top
    (-UB_HALF,    UB_BOTTOM),     # 13: step-in left
]

for i in range(len(pts)):
    j = (i + 1) % len(pts)
    s.Line(point1=pts[i], point2=pts[j])

part.BaseSolidExtrude(sketch=s, depth=THICKNESS)
print("  Base I-beam geometry created ({} vertices)".format(len(pts)))

# =============================================================================
# PHASE 3: Pin Holes
# =============================================================================

print("\n[2/9] Cutting pin holes...")
sys.stdout.flush()


def find_vertical_edge_on_face(part_obj, face_obj, thickness):
    """Find a vertical edge (Y-direction) on the given face."""
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
    # Fallback: any vertical edge on the face
    for idx in edge_indices:
        edge = part_obj.edges[idx]
        verts = edge.getVertices()
        if len(verts) == 2:
            v1 = part_obj.vertices[verts[0]].pointOn[0]
            v2 = part_obj.vertices[verts[1]].pointOn[0]
            if abs(v1[0] - v2[0]) < 0.1 and abs(v1[2] - v2[2]) < 0.1:
                return edge
    return None


def cut_pin_hole(part_obj, model_obj, face_coords, origin, sketch_name,
                 cut_depth, pin_radius, thickness):
    """Cut a circular through-hole at the given location."""
    # Try multiple face coordinates
    if not isinstance(face_coords[0], tuple):
        face_coords = [face_coords]

    face = None
    for coords in face_coords:
        try:
            result = part_obj.faces.findAt((coords,))
            if result:
                face = result
                break
        except Exception:
            continue

    if not face or len(face) == 0:
        print("  WARNING: Could not find face for {} at any coordinates".format(sketch_name))
        return False

    edge = find_vertical_edge_on_face(part_obj, face[0], thickness)
    if not edge:
        print("  WARNING: No vertical edge found for {}".format(sketch_name))
        return False

    t = part_obj.MakeSketchTransform(
        sketchPlane=face[0], sketchUpEdge=edge,
        sketchPlaneSide=SIDE1, sketchOrientation=RIGHT,
        origin=origin)
    ps = model_obj.ConstrainedSketch(name=sketch_name, sheetSize=50.0, transform=t)
    ps.CircleByCenterPerimeter(center=(0, 0), point1=(pin_radius, 0))
    part_obj.CutExtrude(
        sketchPlane=face[0], sketchUpEdge=edge,
        sketchPlaneSide=SIDE1, sketchOrientation=RIGHT,
        sketch=ps, depth=cut_depth, flipExtrudeDirection=OFF)
    return True


# Upper pin hole: face on the side of the upper block (X = UB_HALF = 9.0)
upper_face_coords = [
    (UB_HALF, UPPER_PIN_Y, HALF_THICK - 2.0),
    (-UB_HALF, UPPER_PIN_Y, HALF_THICK - 2.0),
    (UB_HALF, UPPER_PIN_Y, HALF_THICK),
]
if cut_pin_hole(part, model, upper_face_coords,
                (UB_HALF, UPPER_PIN_Y, HALF_THICK),
                'UpperHole', BLOCK_WIDTH_X, PIN_RADIUS, THICKNESS):
    print("  Upper pin hole cut at Y={:.2f}".format(UPPER_PIN_Y))
else:
    print("  ERROR: Upper pin hole failed!")

# Lower right pin hole: face on inner side (X = LB_RIGHT_XMIN = 14.30)
lr_face_coords = [
    (LB_RIGHT_XMIN, LOWER_PIN_Y, HALF_THICK - 2.0),
    (LB_RIGHT_XMAX, LOWER_PIN_Y, HALF_THICK - 2.0),
    (LB_RIGHT_XMIN, LOWER_PIN_Y, HALF_THICK),
]
if cut_pin_hole(part, model, lr_face_coords,
                (LB_RIGHT_XMIN, LOWER_PIN_Y, HALF_THICK),
                'LRHole', BLOCK_WIDTH_X, PIN_RADIUS, THICKNESS):
    print("  Lower right pin hole cut at X={:.2f}".format(LR_PIN_X))
else:
    print("  ERROR: Lower right pin hole failed!")

# Lower left pin hole: face on inner side (X = LB_LEFT_XMAX = -14.30)
ll_face_coords = [
    (-HALF_WIDTH, LOWER_PIN_Y, HALF_THICK - 2.0),
    (LB_LEFT_XMAX, LOWER_PIN_Y, HALF_THICK - 2.0),
    (-HALF_WIDTH, LOWER_PIN_Y, HALF_THICK),
]
if cut_pin_hole(part, model, ll_face_coords,
                (-HALF_WIDTH, LOWER_PIN_Y, HALF_THICK),
                'LLHole', BLOCK_WIDTH_X, PIN_RADIUS, THICKNESS):
    print("  Lower left pin hole cut at X={:.2f}".format(LL_PIN_X))
else:
    print("  ERROR: Lower left pin hole failed!")

# =============================================================================
# PHASE 4: Partition Frozen Regions
# =============================================================================

print("\n[3/9] Partitioning frozen regions...")
sys.stdout.flush()

# Upper block boundary at Y = UB_BOTTOM (118.17)
dp_upper = part.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=UB_BOTTOM)
part.PartitionCellByDatumPlane(datumPlane=part.datums[dp_upper.id], cells=part.cells)
print("  Partitioned at Y={:.2f} (upper block boundary)".format(UB_BOTTOM))

# Lower block boundary at Y = BLOCK_HEIGHT_Y (28.0)
dp_lower = part.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=BLOCK_HEIGHT_Y)
cells_below = part.cells.getByBoundingBox(
    xMin=-HALF_WIDTH - 1, yMin=-1, zMin=-1,
    xMax=HALF_WIDTH + 1, yMax=UB_BOTTOM + 1, zMax=THICKNESS + 1)
if len(cells_below) > 0:
    part.PartitionCellByDatumPlane(datumPlane=part.datums[dp_lower.id],
                                   cells=cells_below)
print("  Partitioned at Y={:.2f} (lower block boundary)".format(BLOCK_HEIGHT_Y))
print("  Total cells after partitioning: {}".format(len(part.cells)))

# =============================================================================
# PHASE 5: Sets, Material, Mesh
# =============================================================================

print("\n[4/9] Creating sets, material, and mesh...")
sys.stdout.flush()

# Sets on the PART (critical: dependent=ON makes instance iteration fail)
# FrozenUpper: cells in the upper block (narrow 18mm section above UB_BOTTOM)
upper_cells = part.cells.getByBoundingBox(
    xMin=-UB_HALF - 0.1, yMin=UB_BOTTOM - 0.1, zMin=-1,
    xMax=UB_HALF + 0.1, yMax=TOTAL_HEIGHT + 1, zMax=THICKNESS + 1)
if len(upper_cells) > 0:
    part.Set(cells=upper_cells, name='FrozenUpper')
    print("  FrozenUpper: {} cells".format(len(upper_cells)))

# FrozenLowerLeft: cells in the lower-left block
ll_cells = part.cells.getByBoundingBox(
    xMin=LB_LEFT_XMIN - 0.1, yMin=-1, zMin=-1,
    xMax=LB_LEFT_XMAX + 0.1, yMax=BLOCK_HEIGHT_Y + 0.1, zMax=THICKNESS + 1)
if len(ll_cells) > 0:
    part.Set(cells=ll_cells, name='FrozenLowerLeft')
    print("  FrozenLowerLeft: {} cells".format(len(ll_cells)))

# FrozenLowerRight: cells in the lower-right block
lr_cells = part.cells.getByBoundingBox(
    xMin=LB_RIGHT_XMIN - 0.1, yMin=-1, zMin=-1,
    xMax=LB_RIGHT_XMAX + 0.1, yMax=BLOCK_HEIGHT_Y + 0.1, zMax=THICKNESS + 1)
if len(lr_cells) > 0:
    part.Set(cells=lr_cells, name='FrozenLowerRight')
    print("  FrozenLowerRight: {} cells".format(len(lr_cells)))

# AllCells
part.Set(cells=part.cells, name='AllCells')

# Material: IN718 linear elastic
mat = model.Material(name='IN718')
mat.Elastic(table=((200000.0, 0.3),))
mat.Density(table=((8.19e-9,),))

model.HomogeneousSolidSection(name='SolidSection', material='IN718', thickness=None)
part.SectionAssignment(region=part.sets['AllCells'], sectionName='SolidSection')
print("  Material: IN718 (E=200 GPa, nu=0.3, rho=8.19e-9)")

# Mesh: TET/FREE with C3D10 (quadratic tet — critical for stress accuracy)
# For 3D regions, setElementType needs 3 types: (hex, wedge, tet)
# Position 2 (third) is the tet type actually used with TET/FREE
part.setMeshControls(regions=part.cells, elemShape=TET, technique=FREE)
part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)
elemType_hex = mesh.ElemType(elemCode=C3D20R, elemLibrary=STANDARD)
elemType_wedge = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
elemType_tet = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,),
                    elemTypes=(elemType_hex, elemType_wedge, elemType_tet))
part.generateMesh()
print("  Mesh: {} nodes, {} elements (size={} mm)".format(
    len(part.nodes), len(part.elements), MESH_SIZE))

# =============================================================================
# PHASE 6: Assembly, Step, BCs, Loads
# =============================================================================

print("\n[5/9] Assembly, step, BCs, and loads...")
sys.stdout.flush()

assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
instance = assembly.Instance(name=part_name + '-1', part=part, dependent=ON)

# Static step
model.StaticStep(name='LoadStep', previous='Initial', nlgeom=OFF,
                 initialInc=1.0, maxInc=1.0, minInc=1e-6)
model.FieldOutputRequest('F-Output-1', createStepName='LoadStep',
                         variables=('S', 'U', 'RF', 'ENER'))
print("  Static step created")

# --- Upper pin: RP + coupling + load ---
upper_pin_faces = instance.faces.getByBoundingCylinder(
    center1=(-UB_HALF - 1, UPPER_PIN_Y, HALF_THICK),
    center2=(UB_HALF + 1, UPPER_PIN_Y, HALF_THICK),
    radius=PIN_RADIUS + 0.5)
print("  Upper pin faces: {}".format(len(upper_pin_faces)))

if len(upper_pin_faces) > 0:
    assembly.Surface(side1Faces=upper_pin_faces, name='UpperPinSurf')
    upper_rp = assembly.ReferencePoint(point=(0.0, UPPER_PIN_Y, HALF_THICK))
    assembly.Set(referencePoints=(assembly.referencePoints[upper_rp.id],),
                 name='UpperRP')
    model.Coupling(name='UpperPinCoupling',
                   controlPoint=assembly.sets['UpperRP'],
                   surface=assembly.surfaces['UpperPinSurf'],
                   influenceRadius=WHOLE_SURFACE,
                   couplingType=KINEMATIC,
                   u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
    model.ConcentratedForce(name='UpperLoad', createStepName='LoadStep',
                            region=assembly.sets['UpperRP'], cf2=20000.0)
    print("  Upper pin: RP + coupling + 20 kN vertical load")

# --- Lower left pin: RP + coupling + BC + load ---
ll_pin_faces = instance.faces.getByBoundingCylinder(
    center1=(LB_LEFT_XMIN - 1, LOWER_PIN_Y, HALF_THICK),
    center2=(LB_LEFT_XMAX + 1, LOWER_PIN_Y, HALF_THICK),
    radius=PIN_RADIUS + 0.5)
print("  Lower left pin faces: {}".format(len(ll_pin_faces)))

if len(ll_pin_faces) > 0:
    assembly.Surface(side1Faces=ll_pin_faces, name='LLPinSurf')
    ll_rp = assembly.ReferencePoint(point=(LL_PIN_X, LOWER_PIN_Y, HALF_THICK))
    assembly.Set(referencePoints=(assembly.referencePoints[ll_rp.id],),
                 name='LowerLeftRP')
    model.Coupling(name='LLPinCoupling',
                   controlPoint=assembly.sets['LowerLeftRP'],
                   surface=assembly.surfaces['LLPinSurf'],
                   influenceRadius=WHOLE_SURFACE,
                   couplingType=KINEMATIC,
                   u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
    model.DisplacementBC(name='LLPin_BC', createStepName='Initial',
                         region=assembly.sets['LowerLeftRP'],
                         u1=UNSET, u2=0.0, u3=0.0)
    model.ConcentratedForce(name='LLLoad', createStepName='LoadStep',
                            region=assembly.sets['LowerLeftRP'], cf1=-5000.0)
    print("  Lower left pin: RP + coupling + BC(u2=u3=0) + F1=-5kN")

# --- Lower right pin: RP + coupling + BC + load ---
lr_pin_faces = instance.faces.getByBoundingCylinder(
    center1=(LB_RIGHT_XMIN - 1, LOWER_PIN_Y, HALF_THICK),
    center2=(LB_RIGHT_XMAX + 1, LOWER_PIN_Y, HALF_THICK),
    radius=PIN_RADIUS + 0.5)
print("  Lower right pin faces: {}".format(len(lr_pin_faces)))

if len(lr_pin_faces) > 0:
    assembly.Surface(side1Faces=lr_pin_faces, name='LRPinSurf')
    lr_rp = assembly.ReferencePoint(point=(LR_PIN_X, LOWER_PIN_Y, HALF_THICK))
    assembly.Set(referencePoints=(assembly.referencePoints[lr_rp.id],),
                 name='LowerRightRP')
    model.Coupling(name='LRPinCoupling',
                   controlPoint=assembly.sets['LowerRightRP'],
                   surface=assembly.surfaces['LRPinSurf'],
                   influenceRadius=WHOLE_SURFACE,
                   couplingType=KINEMATIC,
                   u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
    model.DisplacementBC(name='LRPin_BC', createStepName='Initial',
                         region=assembly.sets['LowerRightRP'],
                         u1=UNSET, u2=0.0, u3=0.0)
    model.ConcentratedForce(name='LRLoad', createStepName='LoadStep',
                            region=assembly.sets['LowerRightRP'], cf1=5000.0)
    print("  Lower right pin: RP + coupling + BC(u2=u3=0) + F1=+5kN")

# =============================================================================
# PHASE 7: writeInput -> Flatten -> Generate .par
# =============================================================================

print("\n[6/9] Generating input files...")
sys.stdout.flush()

# 7a: writeInput
job_name = 'Exp10_FEA'
mdb.Job(name=job_name, model=model_name, numCpus=NUM_CPUS, numDomains=NUM_CPUS)
mdb.jobs[job_name].writeInput()
inp_file = job_name + '.inp'
print("  Written: {} ({} bytes)".format(inp_file, os.path.getsize(inp_file)))

# 7b: Flatten .inp for Tosca
# The .inp has Part/Instance/Assembly structure. Assembly-level RP nodes
# are numbered 1, 2, 3 which COLLIDE with mesh nodes. We must renumber
# RP nodes to avoid collision.
print("\n[7/9] Flattening .inp and generating .par...")
sys.stdout.flush()

with open(inp_file, 'r') as f:
    inp_text = f.read()

instance_name = part_name + '-1'  # TO_Specimen-1
inp_lines = inp_text.split('\n')

# Step 1: Find max mesh node ID and collect assembly RP node info
# Parse the file structure to identify Part vs Assembly sections
max_mesh_node = 0
rp_nodes = {}  # old_id -> coordinate line
section = None  # 'part', 'instance', 'assembly_post_instance', None
in_node_block = False

for line in inp_lines:
    stripped = line.strip()
    upper = stripped.upper()

    # Track sections
    if upper.startswith('*PART'):
        section = 'part'
        in_node_block = False
        continue
    if upper.startswith('*END PART'):
        section = None
        in_node_block = False
        continue
    if upper.startswith('*INSTANCE'):
        section = 'instance'
        continue
    if upper.startswith('*END INSTANCE'):
        section = 'assembly_post_instance'
        continue
    if upper.startswith('*END ASSEMBLY'):
        section = None
        continue

    # Inside *Part: find max node ID
    if section == 'part':
        if upper.startswith('*NODE'):
            in_node_block = True
            continue
        if in_node_block:
            if upper.startswith('*'):
                in_node_block = False
            else:
                parts_list = stripped.split(',')
                if parts_list and parts_list[0].strip().isdigit():
                    nid = int(parts_list[0].strip())
                    if nid > max_mesh_node:
                        max_mesh_node = nid

    # After *End Instance: collect RP nodes
    if section == 'assembly_post_instance':
        if upper.startswith('*NODE'):
            continue  # skip keyword, read data on next iteration
        if not upper.startswith('*') and not upper.startswith('**'):
            parts_list = stripped.split(',')
            if len(parts_list) >= 4 and parts_list[0].strip().isdigit():
                old_id = int(parts_list[0].strip())
                rp_nodes[old_id] = stripped

rp_offset = max_mesh_node
rp_node_map = {}
for old_id in rp_nodes:
    rp_node_map[old_id] = old_id + rp_offset

print("  Max mesh node ID: {}".format(max_mesh_node))
print("  RP node remapping: {}".format(rp_node_map))

# Step 2: Flatten with renumbering
# Strategy: process line by line, apply all transforms
rp_nset_names = {'UpperRP', 'LowerLeftRP', 'LowerRightRP'}
flat_lines = []
current_nset_is_rp = False
section = None
in_rp_node = False

for line in inp_lines:
    stripped = line.strip()
    upper = stripped.upper()

    # Skip wrapper lines
    if upper.startswith('*PART') and not upper.startswith('*PART,'):
        section = 'part'
        continue
    if upper.startswith('*PART,'):
        section = 'part'
        continue
    if upper.startswith('*END PART'):
        section = None
        continue
    if upper.startswith('*INSTANCE'):
        section = 'instance'
        continue
    if upper.startswith('*END INSTANCE'):
        section = 'assembly_post'
        in_rp_node = False
        continue
    if upper.startswith('*ASSEMBLY'):
        continue
    if upper.startswith('*END ASSEMBLY'):
        section = None
        continue

    # In assembly after instance: handle RP *Node blocks
    if section == 'assembly_post':
        if upper.startswith('*NODE'):
            in_rp_node = True
            flat_lines.append(line + '\n')
            continue
        if in_rp_node and not upper.startswith('*') and not upper.startswith('**') and stripped:
            # Renumber this RP node
            parts_list = stripped.split(',')
            if parts_list and parts_list[0].strip().isdigit():
                old_id = int(parts_list[0].strip())
                if old_id in rp_node_map:
                    parts_list[0] = '      ' + str(rp_node_map[old_id])
                    flat_lines.append(','.join(parts_list) + '\n')
                    continue
        if upper.startswith('*') and not upper.startswith('**'):
            in_rp_node = False
            section = 'assembly_sets'  # now in set/surface/coupling defs

    # Remove 'internal' from set definitions
    if upper.startswith('*ELSET') or upper.startswith('*NSET'):
        parts_list = line.split(',')
        parts_list = [p for p in parts_list if 'INTERNAL' not in p.upper()]
        line = ','.join(parts_list)
        stripped = line.strip()
        upper = stripped.upper()

    # Strip instance= from keyword lines
    line = re.sub(r',\s*instance=' + re.escape(instance_name), '', line,
                  flags=re.IGNORECASE)

    # Strip instance prefix from data lines
    line = line.replace(instance_name + '.', '')

    # Track if we're in an RP nset
    if upper.startswith('*NSET'):
        current_nset_is_rp = False
        for p in line.split(','):
            if 'NSET=' in p.upper():
                nset_name = p.split('=')[1].strip()
                if nset_name in rp_nset_names:
                    current_nset_is_rp = True
                break
        flat_lines.append(line + '\n' if not line.endswith('\n') else line)
        continue

    # Renumber RP node IDs in nset data lines
    if current_nset_is_rp:
        if upper.startswith('*'):
            current_nset_is_rp = False
        elif stripped:
            # Replace node IDs in this data line
            tokens = stripped.rstrip(',').split(',')
            new_tokens = []
            for t in tokens:
                t = t.strip()
                if t.isdigit() and int(t) in rp_node_map:
                    new_tokens.append(str(rp_node_map[int(t)]))
                else:
                    new_tokens.append(t)
            flat_lines.append(' ' + ', '.join(new_tokens) + ',\n')
            continue

    flat_lines.append(line + '\n' if not line.endswith('\n') else line)

flat_inp = ''.join(flat_lines)

flat_name = 'Exp10_FEA_flat.inp'
with open(flat_name, 'w') as f:
    f.write(flat_inp)

# Verify RP nodes were renumbered
for old_id, new_id in rp_node_map.items():
    if str(new_id) in flat_inp:
        print("  Verified: RP node {} -> {} found in flat .inp".format(old_id, new_id))
    else:
        print("  WARNING: RP node {} -> {} NOT found in flat .inp!".format(old_id, new_id))

node_block_count = len([l for l in flat_inp.split('\n') if l.strip().upper().startswith('*NODE') and 'OUTPUT' not in l.upper()])
print("  Flattened: {} ({} bytes, {} *Node blocks)".format(
    flat_name, os.path.getsize(flat_name), node_block_count))

# 7c: Generate .par file
filter_radius = MESH_SIZE * 3.0

par_content = """! Experiment 10: IN718 Stress-Constrained Topology Optimization
! Objective: Minimize volume
! Constraint: Von Mises stress <= {stress_limit} MPa
! Generated by exp10_optimize.py

FEM_INPUT
  ID_NAME                = FEA_MODEL
  FILE                   = {inp_file}
END_

DV_TOPO
  ID_NAME                = design_variables
  EL_GROUP               = ALL_ELEMENTS
END_

GROUP_DEF
  ID_NAME                = ALL_FROZEN
  TYPE                   = ELEM
  FORMAT                 = LIST_GROUP
LIST_BEGIN
FrozenUpper, FrozenLowerLeft, FrozenLowerRight
END_

DVCON_TOPO
  ID_NAME                = dvcon_frozen
  EL_GROUP               = ALL_FROZEN
  CHECK_TYPE             = FROZEN
END_

DRESP
  ID_NAME                = DRESP_VOLUME
  DEF_TYPE               = SYSTEM
  TYPE                   = VOLUME
  EL_GROUP               = ALL_ELEMENTS
  GROUP_OPER             = SUM
END_

DRESP
  ID_NAME                = DRESP_STRESS
  DEF_TYPE               = SYSTEM
  TYPE                   = SIG_SENS_MISES
  EL_GROUP               = ALL_ELEMENTS
END_

OBJ_FUNC
  ID_NAME                = min_volume
  DRESP                  = DRESP_VOLUME
  TARGET                 = MIN
END_

CONSTRAINT
  ID_NAME                = stress_constraint
  DRESP                  = DRESP_STRESS
  MAGNITUDE              = ABS
  LE_VALUE               = {stress_limit}
END_

OPTIMIZE
  ID_NAME                = TOPOLOGY_OPT
  DV                     = design_variables
  OBJ_FUNC               = min_volume
  DVCON                  = dvcon_frozen
  CONSTRAINT             = stress_constraint
  STRATEGY               = TOPO_SENSITIVITY
END_

OPT_PARAM
  ID_NAME                = OPT_PARAMS
  OPTIMIZE               = TOPOLOGY_OPT
  TOPO_FILTER_RADIUS     = {filter_radius}
END_

STOP
  ID_NAME                = global_stop
  ITER_MAX               = {max_cycles}
END_

SMOOTH
  ID_NAME                = ISO_SMOOTHING
  TASK                   = iso
  ISO_VALUE              = 0.51
  SELF_INTERSECTION_CHECK = runtime
  SMOOTH_CYCLES          = 10
  REDUCTION_RATE         = 60
  REDUCTION_ANGLE        = 5.0
  FORMAT                 = stl
END_
""".format(
    inp_file=flat_name,
    stress_limit=STRESS_LIMIT,
    filter_radius=filter_radius,
    max_cycles=MAX_CYCLES,
)

par_file = 'Exp10_TO.par'
with open(par_file, 'w') as f:
    f.write(par_content)
print("  Generated: {} ({} bytes)".format(par_file, os.path.getsize(par_file)))
print("  Filter radius: {} mm".format(filter_radius))
print("  Stress limit: {} MPa".format(STRESS_LIMIT))

# =============================================================================
# PHASE 8: Run Tosca CLI
# =============================================================================

print("\n[8/9] Running Tosca optimization...")
sys.stdout.flush()

# Find Tosca command
tosca_cmds = ['tosca', 'abaqus tosca']
tosca_found = False
tcmd = 'tosca'

for candidate in tosca_cmds:
    try:
        cmd_parts = candidate.split()
        test = subprocess.Popen(cmd_parts + ['--help'],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out, _ = test.communicate()
        print("  Found Tosca via: '{}'".format(candidate))
        tcmd = candidate
        tosca_found = True
        break
    except OSError:
        continue

if not tosca_found:
    try:
        test = subprocess.Popen(['abaqus', 'optimization', '-help'],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out, _ = test.communicate()
        print("  Found via 'abaqus optimization'")
        tcmd = 'abaqus optimization'
        tosca_found = True
    except Exception:
        pass

if not tosca_found:
    print("  WARNING: Tosca CLI not found, trying direct invocation")

cmd_parts = tcmd.split() + ['optimize', '-j', 'exp10_tosca',
                             '-p', par_file, '-s', 'abaqus',
                             '-scpus', str(NUM_CPUS)]
print("  Command: {}".format(' '.join(cmd_parts)))
sys.stdout.flush()

proc = subprocess.Popen(cmd_parts,
                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout, _ = proc.communicate()
output = stdout.decode('utf-8', errors='replace')

print("  Tosca exit code: {}".format(proc.returncode))
print("")
if len(output) > 5000:
    print("  ... (truncated, showing last 5000 chars)")
print(output[-5000:])
sys.stdout.flush()

# List output files
print("")
print("  --- Output files ---")
for f in sorted(os.listdir('.')):
    fp = os.path.join('.', f)
    if os.path.isfile(fp):
        print("    {}: {} bytes".format(f, os.path.getsize(fp)))
    elif os.path.isdir(fp):
        contents = os.listdir(fp)
        print("    {}/  ({} items)".format(f, len(contents)))
        for c in sorted(contents)[:10]:
            cf = os.path.join(fp, c)
            if os.path.isfile(cf):
                print("      {}: {} bytes".format(c, os.path.getsize(cf)))
            else:
                print("      {}/".format(c))
        if len(contents) > 10:
            print("      ... and {} more".format(len(contents) - 10))

# Check for STL output
import glob as globmod
stl_files = (globmod.glob('*.stl') + globmod.glob('*/*.stl') +
             globmod.glob('*/*/*.stl'))
if stl_files:
    print("\n  STL files: {}".format(stl_files))
else:
    print("\n  No STL files found")

# =============================================================================
# PHASE 9: Run FEA on last-cycle .inp (optimized design with SIMP penalties)
# =============================================================================
# Tosca deletes per-cycle ODBs. To visualize stress/displacement on the
# optimized design, we run Abaqus FEA on the last-cycle .inp from SAVE.inp/.
# That .inp includes tosca_distribution.inp with per-element density values.

print("\n[9/9] Running FEA on optimized design...")
sys.stdout.flush()

tosca_dir = os.path.join(WORK_DIR, 'exp10_tosca')
save_inp_dir = os.path.join(tosca_dir, 'SAVE.inp')

# Find the last cycle directory (highest numbered)
last_cycle = None
if os.path.isdir(save_inp_dir):
    cycle_dirs = [d for d in os.listdir(save_inp_dir)
                  if d.isdigit() and os.path.isdir(os.path.join(save_inp_dir, d))]
    if cycle_dirs:
        last_cycle = max(cycle_dirs, key=int)

if last_cycle:
    cycle_dir = os.path.join(save_inp_dir, last_cycle)
    cycle_inp = os.path.join(cycle_dir, flat_name)
    dist_file = os.path.join(cycle_dir, 'tosca_distribution.inp')

    if os.path.exists(cycle_inp) and os.path.exists(dist_file):
        print("  Last cycle: {} (dir: {})".format(last_cycle, cycle_dir))
        print("  Input: {} ({} bytes)".format(cycle_inp, os.path.getsize(cycle_inp)))
        print("  Distribution: {} ({} bytes)".format(dist_file, os.path.getsize(dist_file)))

        # Run Abaqus FEA in the cycle directory (so *INCLUDE finds tosca_distribution.inp)
        fea_job = 'Exp10_optimized'
        fea_cmd = ['abaqus', 'job=' + fea_job,
                   'input=' + cycle_inp,
                   'cpus=' + str(NUM_CPUS), 'interactive']
        print("  Command: {}".format(' '.join(fea_cmd)))
        sys.stdout.flush()

        fea_proc = subprocess.Popen(fea_cmd, cwd=cycle_dir,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        fea_out, _ = fea_proc.communicate()
        fea_output = fea_out.decode('utf-8', errors='replace')

        print("  FEA exit code: {}".format(fea_proc.returncode))
        if len(fea_output) > 2000:
            print("  ... (truncated, showing last 2000 chars)")
        print(fea_output[-2000:])

        # Check for ODB
        odb_path = os.path.join(cycle_dir, fea_job + '.odb')
        if os.path.exists(odb_path):
            print("  ODB created: {} ({} bytes)".format(odb_path, os.path.getsize(odb_path)))
        else:
            print("  WARNING: ODB not created!")
    else:
        print("  WARNING: Last-cycle .inp or distribution not found in {}".format(cycle_dir))
        if not os.path.exists(cycle_inp):
            print("    Missing: {}".format(cycle_inp))
        if not os.path.exists(dist_file):
            print("    Missing: {}".format(dist_file))
else:
    print("  WARNING: No cycle directories found in {}".format(save_inp_dir))

print("")
print(SEPARATOR)
print("  Experiment 10 COMPLETE (Tosca exit code: {})".format(proc.returncode))
print(SEPARATOR)
