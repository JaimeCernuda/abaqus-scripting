# 01_create_geometry_rotated.py
#
# EXPERIMENT 2: Y-shape bracket with holes through X axis
# REDESIGNED with proper proportions matching paper Figure 3
#
# The paper shows substantial cube-like lower blocks (~35mm)
# Holes go through the full block width
#
# Run with: abaqus cae noGUI=paper_reproduction/scripts/experiment2/01_create_geometry_rotated.py

from abaqus import *
from abaqusConstants import *
from caeModules import *

# Debug log file - write all output here since print may not capture
debug_log = []

def log(msg):
    debug_log.append(str(msg))
    print(msg)

def save_log():
    with open('paper_reproduction/outputs/experiment2/geometry_full_log.txt', 'w') as f:
        f.write('\n'.join(debug_log))

log("\n" + "=" * 70)
log("EXPERIMENT 2 - GEOMETRY (HOLES THROUGH X - PROPER PROPORTIONS)")
log("=" * 70)

# =============================================================================
# REVISED PARAMETERS - Matching paper Figure 3 proportions
# =============================================================================

# Overall dimensions
TOTAL_HEIGHT = 146.17  # Y direction (vertical) - from paper

# Lower blocks - substantial cubes for horizontal pins
LOWER_BLOCK_SIZE = 35.0   # Cube-like blocks ~35mm
LOWER_BLOCK_WIDTH = LOWER_BLOCK_SIZE   # X extent (holes go through this)
LOWER_BLOCK_HEIGHT = LOWER_BLOCK_SIZE  # Y extent (vertical)
THICKNESS = LOWER_BLOCK_SIZE           # Z extent (depth)

# Pin holes
PIN_DIAMETER = 12.0   # Slightly larger for proportions
PIN_RADIUS = PIN_DIAMETER / 2
LOWER_PIN_CENTER_Y = LOWER_BLOCK_HEIGHT / 2  # Centered in block

# Lower block positions (X distance between centers)
TOTAL_WIDTH = 64.60  # Distance between lower pin centers
LOWER_LEFT_X = -TOTAL_WIDTH / 2    # -32.3
LOWER_RIGHT_X = TOTAL_WIDTH / 2    # +32.3

# Upper tab - also substantial
UPPER_TAB_WIDTH = 30.0   # X extent
UPPER_TAB_HEIGHT = 30.0  # Y extent
UPPER_PIN_CENTER_Y = TOTAL_HEIGHT - UPPER_TAB_HEIGHT / 2  # Centered

# Derived coordinates
x_left_outer = LOWER_LEFT_X - LOWER_BLOCK_WIDTH / 2    # -49.8
x_left_inner = LOWER_LEFT_X + LOWER_BLOCK_WIDTH / 2    # -14.8
x_right_inner = LOWER_RIGHT_X - LOWER_BLOCK_WIDTH / 2  # +14.8
x_right_outer = LOWER_RIGHT_X + LOWER_BLOCK_WIDTH / 2  # +49.8

x_upper_left = -UPPER_TAB_WIDTH / 2   # -15
x_upper_right = UPPER_TAB_WIDTH / 2   # +15

y_bottom = 0.0
y_lower_top = LOWER_BLOCK_HEIGHT              # 35
y_upper_bottom = TOTAL_HEIGHT - UPPER_TAB_HEIGHT  # 116.17
y_top = TOTAL_HEIGHT                          # 146.17

MODEL_NAME = 'TO_Bracket_Exp2'
PART_NAME = 'Bracket'

log(f"\nRevised dimensions (matching paper):")
log(f"  Lower blocks: {LOWER_BLOCK_WIDTH:.1f} x {LOWER_BLOCK_HEIGHT:.1f} x {THICKNESS:.1f} mm")
log(f"  Upper tab: {UPPER_TAB_WIDTH:.1f} x {UPPER_TAB_HEIGHT:.1f} mm")
log(f"  Pin diameter: {PIN_DIAMETER} mm")
log(f"  Holes through X axis")

# =============================================================================
# CREATE MODEL AND Y-SHAPE SOLID
# =============================================================================

log("\n[1/5] Creating Y-shape solid...")

model = mdb.Model(name=MODEL_NAME)
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']

part = model.Part(name=PART_NAME, dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='ProfileSketch', sheetSize=200.0)

# Y-shape profile (closed loop)
profile = [
    (x_left_outer, y_bottom),
    (x_left_outer, y_lower_top),
    (x_upper_left, y_upper_bottom),
    (x_upper_left, y_top),
    (x_upper_right, y_top),
    (x_upper_right, y_upper_bottom),
    (x_right_outer, y_lower_top),
    (x_right_outer, y_bottom),
    (x_right_inner, y_bottom),
    (x_right_inner, y_lower_top),
    (x_left_inner, y_lower_top),
    (x_left_inner, y_bottom),
]

for i in range(len(profile)):
    sketch.Line(point1=profile[i], point2=profile[(i + 1) % len(profile)])

part.BaseSolidExtrude(sketch=sketch, depth=THICKNESS)
log(f"       Solid: {len(part.faces)} faces")

# =============================================================================
# CUT HOLES THROUGH X AXIS
# =============================================================================

log("\n[2/5] Cutting holes through X axis...")

def find_face_fresh(part, target_x, tol=1.0):
    """Find face with X-normal at target X position - FRESH lookup"""
    for face in part.faces:
        pt = face.pointOn[0]
        normal = face.getNormal(pt)
        if abs(normal[0]) > 0.99 and abs(pt[0] - target_x) < tol:
            return face
    return None

def cut_hole_robust(part, model, target_x, name, center_y, depth):
    """Cut circular hole through X-normal face at target_x - with fresh face lookup"""
    faces_before = len(part.faces)

    # Fresh lookup of face (important after previous cuts!)
    face = find_face_fresh(part, target_x)
    if face is None:
        log(f"       {name}: SKIPPED - no X-normal face at X={target_x:.1f}")
        return False

    face_pt = face.pointOn[0]
    face_normal = face.getNormal(face_pt)
    log(f"       {name}: Found face at ({face_pt[0]:.1f}, {face_pt[1]:.1f}, {face_pt[2]:.1f})")
    log(f"       {name}: Normal = ({face_normal[0]:.2f}, {face_normal[1]:.2f}, {face_normal[2]:.2f})")

    # Get edges of this face
    edge_indices = face.getEdges()
    log(f"       {name}: Face has {len(edge_indices)} edges")

    errors = []
    # Try each edge as sketchUpEdge, both flip directions, both sides
    for edge_idx in edge_indices:
        edge = part.edges[edge_idx]

        for flip in [False, True]:  # Try both flip directions
            for side in [SIDE1, SIDE2]:
                try:
                    sketch_name = f'{name}_{edge_idx}_{side}_flip{flip}'
                    sk = model.ConstrainedSketch(
                        name=sketch_name,
                        sheetSize=50.0,
                        transform=part.MakeSketchTransform(
                            sketchPlane=face,
                            sketchUpEdge=edge,
                            sketchPlaneSide=side,
                            sketchOrientation=RIGHT,
                            origin=(target_x, center_y, THICKNESS / 2.0)
                        )
                    )
                    sk.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(PIN_RADIUS, 0.0))

                    part.CutExtrude(
                        sketchPlane=face,
                        sketchUpEdge=edge,
                        sketchPlaneSide=side,
                        sketchOrientation=RIGHT,
                        sketch=sk,
                        depth=depth,
                        flipExtrudeDirection=flip
                    )

                    faces_after = len(part.faces)
                    # Check if cut actually changed geometry
                    if faces_after > faces_before:
                        log(f"       {name}: CUT SUCCESS with flip={flip} (faces: {faces_before} -> {faces_after})")
                        return True
                    else:
                        log(f"       {name}: Cut completed but no geometry change (flip={flip}), trying next...")
                        # The cut didn't actually do anything useful, continue trying
                except Exception as e:
                    errors.append(f"edge{edge_idx}_{side}_flip{flip}: {str(e)[:50]}")
                    continue

    log(f"       {name}: FAILED - all combinations tried, none changed geometry")
    for err in errors[:4]:  # Show first 4 errors
        log(f"         {err}")
    return False

# Cut holes in order
log(f"       Faces before cuts: {len(part.faces)}")

# List all X-normal faces before cutting
log("       X-normal faces available:")
for face in part.faces:
    pt = face.pointOn[0]
    normal = face.getNormal(pt)
    if abs(normal[0]) > 0.9:
        log(f"         X={pt[0]:.1f}, Y={pt[1]:.1f}, Z={pt[2]:.1f}, normal=({normal[0]:.2f},{normal[1]:.2f},{normal[2]:.2f})")

# Cut in order: Upper, LowerRight, then LowerLeft
cut_hole_robust(part, model, x_upper_right, 'Upper', UPPER_PIN_CENTER_Y, UPPER_TAB_WIDTH)
cut_hole_robust(part, model, x_right_outer, 'LowerRight', LOWER_PIN_CENTER_Y, LOWER_BLOCK_WIDTH)
cut_hole_robust(part, model, x_left_outer, 'LowerLeft', LOWER_PIN_CENTER_Y, LOWER_BLOCK_WIDTH)

log(f"       Final faces: {len(part.faces)}")

# =============================================================================
# CREATE SETS
# =============================================================================

log("\n[3/5] Creating sets...")

# Find cylindrical faces (exactly 2 edges = cylinder)
upper_cyl = ll_cyl = lr_cyl = None
log("       Looking for cylindrical faces (2 edges):")
for face in part.faces:
    if len(face.getEdges()) == 2:
        pt = face.pointOn[0]
        log(f"         Found: ({pt[0]:.1f}, {pt[1]:.1f}, {pt[2]:.1f})")
        if abs(pt[1] - UPPER_PIN_CENTER_Y) < PIN_RADIUS + 5:
            upper_cyl = face
            log(f"           -> Upper pin surface")
        elif abs(pt[1] - LOWER_PIN_CENTER_Y) < PIN_RADIUS + 5:
            if pt[0] < 0:
                ll_cyl = face
                log(f"           -> Lower left pin surface")
            else:
                lr_cyl = face
                log(f"           -> Lower right pin surface")

for cyl, name in [(upper_cyl, 'UpperPinSurface'), (ll_cyl, 'LowerLeftPinSurface'), (lr_cyl, 'LowerRightPinSurface')]:
    if cyl:
        part.Set(faces=part.faces[cyl.index:cyl.index+1], name=name)
        part.Surface(side1Faces=part.faces[cyl.index:cyl.index+1], name=f'Surf-{name.replace("Surface","")}')
        log(f"       {name}: OK")
    else:
        log(f"       {name}: NOT FOUND")

part.Set(cells=part.cells, name='AllCells')

# =============================================================================
# ASSEMBLY AND SAVE
# =============================================================================

log("\n[4/5] Creating assembly...")

assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
assembly.Instance(name='BracketInstance', part=part, dependent=ON)

log("\n[5/5] Saving...")

mdb.saveAs(pathName='paper_reproduction/outputs/experiment2/TO_Bracket_Geometry.cae')

# Write debug info
with open('paper_reproduction/outputs/experiment2/geometry_debug.txt', 'w') as f:
    f.write(f"EXPERIMENT 2 - REVISED GEOMETRY\n")
    f.write(f"Lower blocks: {LOWER_BLOCK_WIDTH} x {LOWER_BLOCK_HEIGHT} x {THICKNESS} mm\n")
    f.write(f"Upper tab: {UPPER_TAB_WIDTH} x {UPPER_TAB_HEIGHT} mm\n")
    f.write(f"Pin diameter: {PIN_DIAMETER} mm\n")
    f.write(f"Faces: {len(part.faces)}\n")
    f.write(f"\nCylindrical faces found:\n")
    f.write(f"  Upper: {'Yes' if upper_cyl else 'No'}\n")
    f.write(f"  Lower Left: {'Yes' if ll_cyl else 'No'}\n")
    f.write(f"  Lower Right: {'Yes' if lr_cyl else 'No'}\n")

log("\n" + "=" * 70)
log("GEOMETRY COMPLETE")
log("=" * 70)

# Save full log
save_log()
