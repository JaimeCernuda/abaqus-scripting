# 01_create_geometry.py - EXPERIMENT 3
#
# Paper-aligned coordinate system (after rotation):
# - X = horizontal spreading direction
# - Y = pin axis / thickness
# - Z = vertical / loading direction
#
# Strategy: Create part with default orientation (Y vertical), then
# rotate the instance -90° around X-axis to swap Y<->Z.
#
# Run with: abaqus cae noGUI=paper_reproduction/scripts/experiment3/01_create_geometry.py

from abaqus import *
from abaqusConstants import *
from caeModules import *
import math

debug_log = []


def log(msg):
    """Log message to console and debug file."""
    debug_log.append(str(msg))
    print(msg)


def save_log():
    """Save debug log to file."""
    import codecs
    with codecs.open('paper_reproduction/outputs/experiment3/geometry_log.txt', 'w', 'utf-8') as f:
        f.write('\n'.join(debug_log))


log("\n" + "=" * 70)
log("EXPERIMENT 3 - GEOMETRY (PAPER-ALIGNED: Z VERTICAL)")
log("=" * 70)

# =============================================================================
# PARAMETERS - Use native Abaqus coords first, then rotate
# In native (before rotation):
#   X = horizontal spreading
#   Y = vertical (will become Z after rotation)
#   Z = thickness (will become Y after rotation)
# =============================================================================

# Overall dimensions (final paper-aligned values)
TOTAL_HEIGHT = 146.17      # Final Z direction (vertical)
TOTAL_WIDTH = 64.60        # X direction (pin center spacing)
THICKNESS = 35.0           # Final Y direction (pin axis)

# Lower blocks
LOWER_BLOCK_SIZE = 35.0

# Upper tab
UPPER_TAB_WIDTH = 30.0
UPPER_TAB_HEIGHT = 30.0

# Pin holes
PIN_DIAMETER = 12.0
PIN_RADIUS = PIN_DIAMETER / 2

# In native coords (before rotation):
# X = horizontal, Y = vertical, Z = thickness/extrusion
# Pin positions in native coords:
LOWER_PIN_CENTER_Y = LOWER_BLOCK_SIZE / 2     # 17.5 mm (vertical before rotation)
UPPER_PIN_CENTER_Y = TOTAL_HEIGHT - UPPER_TAB_HEIGHT / 2  # 131.17 mm

LOWER_LEFT_X = -TOTAL_WIDTH / 2    # -32.3
LOWER_RIGHT_X = TOTAL_WIDTH / 2    # +32.3

# Derived X coordinates for profile (in native X)
x_left_outer = LOWER_LEFT_X - LOWER_BLOCK_SIZE / 2     # -49.8
x_left_inner = LOWER_LEFT_X + LOWER_BLOCK_SIZE / 2     # -14.8
x_right_inner = LOWER_RIGHT_X - LOWER_BLOCK_SIZE / 2   # +14.8
x_right_outer = LOWER_RIGHT_X + LOWER_BLOCK_SIZE / 2   # +49.8

x_upper_left = -UPPER_TAB_WIDTH / 2
x_upper_right = UPPER_TAB_WIDTH / 2

# Y coordinates for profile (native - will become Z after rotation)
y_bottom = 0.0
y_lower_top = LOWER_BLOCK_SIZE                      # 35
y_upper_bottom = TOTAL_HEIGHT - UPPER_TAB_HEIGHT    # 116.17
y_top = TOTAL_HEIGHT                                # 146.17

MODEL_NAME = 'TO_Bracket_Exp3'
PART_NAME = 'Bracket'

log("\nStrategy:")
log("  1. Create part with Y vertical (native Abaqus)")
log("  2. Rotate instance +90 deg around X to swap Y<->Z")
log("  3. Final: X=horizontal, Y=thickness, Z=vertical")
log(f"\nDimensions (final paper-aligned):")
log(f"  Total height (Z): {TOTAL_HEIGHT:.2f} mm")
log(f"  Total width (X): {TOTAL_WIDTH:.2f} mm")
log(f"  Thickness (Y): {THICKNESS:.2f} mm")

# =============================================================================
# CREATE MODEL AND Y-SHAPE SOLID (Native coords: Y vertical)
# =============================================================================

log("\n[1/6] Creating Y-shape solid (native coords: Y vertical)...")

model = mdb.Model(name=MODEL_NAME)
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']

part = model.Part(name=PART_NAME, dimensionality=THREE_D, type=DEFORMABLE_BODY)

# Sketch in X-Y plane (native), extrude in Z (which becomes Y after rotation)
sketch = model.ConstrainedSketch(name='ProfileSketch', sheetSize=200.0)

# Y-shape profile in X-Y plane (X horizontal, Y vertical in native)
profile = [
    (x_left_outer, y_bottom),        # 0: Bottom left outer corner
    (x_left_outer, y_lower_top),     # 1: Top of left block
    (x_upper_left, y_upper_bottom),  # 2: Taper to upper tab (left)
    (x_upper_left, y_top),           # 3: Top left of upper tab
    (x_upper_right, y_top),          # 4: Top right of upper tab
    (x_upper_right, y_upper_bottom), # 5: Taper to upper tab (right)
    (x_right_outer, y_lower_top),    # 6: Top of right block
    (x_right_outer, y_bottom),       # 7: Bottom right outer corner
    (x_right_inner, y_bottom),       # 8: Bottom right inner corner
    (x_right_inner, y_lower_top),    # 9: Top of inner gap (right)
    (x_left_inner, y_lower_top),     # 10: Top of inner gap (left)
    (x_left_inner, y_bottom),        # 11: Bottom left inner corner
]

log(f"       Profile points: {len(profile)}")

for i in range(len(profile)):
    sketch.Line(point1=profile[i], point2=profile[(i + 1) % len(profile)])

# Extrude in Z direction (native thickness direction)
part.BaseSolidExtrude(sketch=sketch, depth=THICKNESS)
log(f"       Solid created: {len(part.faces)} faces, {len(part.cells)} cells")

# =============================================================================
# CUT PIN HOLES THROUGH Z AXIS (native coords)
# =============================================================================

log("\n[2/6] Cutting holes through Z axis (native thickness)...")


def find_z_normal_face(part, z_val, tol=1.0):
    """Find face with Z-normal at given Z."""
    for face in part.faces:
        pt = face.pointOn[0]
        normal = face.getNormal(pt)
        if abs(normal[2]) > 0.9 and abs(pt[2] - z_val) < tol:
            return face
    return None


def cut_hole_through_z(part, model, center_x, center_y, name, depth):
    """Cut circular hole through Z-normal face."""
    faces_before = len(part.faces)

    # Find front face (Z=0)
    face = find_z_normal_face(part, 0.0)
    if face is None:
        face = find_z_normal_face(part, THICKNESS)

    if face is None:
        log(f"       {name}: SKIPPED - no Z-normal face found")
        return False

    face_pt = face.pointOn[0]
    log(f"       {name}: Cutting at X={center_x:.1f}, Y={center_y:.1f}")

    edge_indices = face.getEdges()
    for edge_idx in edge_indices:
        edge = part.edges[edge_idx]
        for flip in [False, True]:
            for side in [SIDE1, SIDE2]:
                try:
                    sk = model.ConstrainedSketch(
                        name=f'{name}_sketch',
                        sheetSize=50.0,
                        transform=part.MakeSketchTransform(
                            sketchPlane=face,
                            sketchUpEdge=edge,
                            sketchPlaneSide=side,
                            sketchOrientation=RIGHT,
                            origin=(center_x, center_y, face_pt[2])
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
                    if faces_after > faces_before:
                        log(f"       {name}: SUCCESS (faces: {faces_before} -> {faces_after})")
                        return True
                except Exception:
                    continue

    log(f"       {name}: FAILED")
    return False


# Cut holes (in native coords: X, Y positions, cut through Z)
cut_hole_through_z(part, model, 0.0, UPPER_PIN_CENTER_Y, 'Upper', THICKNESS)
cut_hole_through_z(part, model, LOWER_RIGHT_X, LOWER_PIN_CENTER_Y, 'LowerRight', THICKNESS)
cut_hole_through_z(part, model, LOWER_LEFT_X, LOWER_PIN_CENTER_Y, 'LowerLeft', THICKNESS)

log(f"       Final faces: {len(part.faces)}")

# =============================================================================
# CREATE SETS FOR PIN SURFACES (native coords)
# =============================================================================

log("\n[3/6] Creating sets for pin surfaces...")

# Find cylindrical faces (exactly 2 edges)
upper_cyl = ll_cyl = lr_cyl = None
for face in part.faces:
    if len(face.getEdges()) == 2:
        pt = face.pointOn[0]
        # In native coords: Y is vertical position
        if abs(pt[1] - UPPER_PIN_CENTER_Y) < PIN_RADIUS + 5:
            upper_cyl = face
            log(f"       Upper pin found at Y={pt[1]:.1f}")
        elif abs(pt[1] - LOWER_PIN_CENTER_Y) < PIN_RADIUS + 5:
            if pt[0] < 0:
                ll_cyl = face
                log(f"       Lower left pin found at X={pt[0]:.1f}")
            else:
                lr_cyl = face
                log(f"       Lower right pin found at X={pt[0]:.1f}")

for cyl, name in [(upper_cyl, 'UpperPinSurface'),
                  (ll_cyl, 'LowerLeftPinSurface'),
                  (lr_cyl, 'LowerRightPinSurface')]:
    if cyl:
        part.Set(faces=part.faces[cyl.index:cyl.index + 1], name=name)
        part.Surface(side1Faces=part.faces[cyl.index:cyl.index + 1],
                     name=f'Surf-{name.replace("Surface", "")}')
        log(f"       {name}: OK")
    else:
        log(f"       {name}: NOT FOUND")

part.Set(cells=part.cells, name='AllCells')

# =============================================================================
# CREATE ASSEMBLY WITH ROTATED INSTANCE
# =============================================================================

log("\n[4/6] Creating assembly with rotation...")

assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
instance = assembly.Instance(name='BracketInstance', part=part, dependent=ON)

# Rotate +90° around X-axis to swap Y<->Z
# After +90° rotation: (x,y,z) -> (x,-z,y)
#   native Y (0 to 146) becomes final Z (0 to 146) - vertical ✓
#   native Z (0 to 35) becomes final -Y (-35 to 0) - need translate
assembly.rotate(instanceList=('BracketInstance',),
                axisPoint=(0.0, 0.0, 0.0),
                axisDirection=(1.0, 0.0, 0.0),
                angle=90.0)
log("       Rotated instance +90 deg around X-axis")

# Translate to shift Y from (-35,0) to (0,35)
assembly.translate(instanceList=('BracketInstance',),
                   vector=(0.0, THICKNESS, 0.0))
log(f"       Translated +{THICKNESS} in Y direction")

# Translate to put base at Z=0 (base was at Y=0 in native, now at Z=0)
# No translation needed since we rotated around origin

# Verify final coordinate ranges
log("       Final coordinate ranges (paper-aligned):")
x_coords, y_coords, z_coords = [], [], []
for vertex in instance.vertices:
    pt = vertex.pointOn[0]
    x_coords.append(pt[0])
    y_coords.append(pt[1])
    z_coords.append(pt[2])
log(f"         X: {min(x_coords):.1f} to {max(x_coords):.1f} (expect ~-50 to +50)")
log(f"         Y: {min(y_coords):.1f} to {max(y_coords):.1f} (expect ~-35 to 0 or 0 to 35)")
log(f"         Z: {min(z_coords):.1f} to {max(z_coords):.1f} (expect 0 to 146)")

# =============================================================================
# SAVE
# =============================================================================

log("\n[5/6] Saving...")
mdb.saveAs(pathName='paper_reproduction/outputs/experiment3/models/TO_Bracket_Geometry.cae')

# Write debug info
with open('paper_reproduction/outputs/experiment3/geometry_debug.txt', 'w') as f:
    f.write("EXPERIMENT 3 - PAPER-ALIGNED GEOMETRY\n")
    f.write("=" * 50 + "\n\n")
    f.write("Coordinate System (Paper-Aligned, after rotation):\n")
    f.write("  X = horizontal spreading direction\n")
    f.write("  Y = pin axis / thickness\n")
    f.write("  Z = vertical loading direction\n\n")
    f.write("Transformation applied:\n")
    f.write("  Instance rotated -90 deg around X-axis\n")
    f.write("  Native Y (vertical) -> Final Z (vertical)\n")
    f.write("  Native Z (thickness) -> Final -Y (thickness)\n\n")
    f.write(f"Faces: {len(part.faces)}\n")
    f.write(f"Cells: {len(part.cells)}\n\n")
    f.write("Pin surfaces found:\n")
    f.write(f"  Upper: {'Yes' if upper_cyl else 'No'}\n")
    f.write(f"  Lower Left: {'Yes' if ll_cyl else 'No'}\n")
    f.write(f"  Lower Right: {'Yes' if lr_cyl else 'No'}\n")

log("\n[6/6] Done!")
log("\n" + "=" * 70)
log("EXPERIMENT 3 - GEOMETRY COMPLETE")
log("=" * 70)

save_log()
