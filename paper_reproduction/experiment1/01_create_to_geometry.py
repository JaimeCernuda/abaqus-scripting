# 01_create_to_geometry.py
#
# Creates simplified topology-optimized bracket geometry based on
# "Fatigue Response of a Topology Optimized Feature-based Component"
#
# The geometry approximates the final TO shape from Figure 2(f):
# - Upper tab with centered pin hole (load application point)
# - Two lower blocks with pin holes (support points)
# - Tapered legs connecting upper tab to lower blocks
#
# NOTE: This is a SIMPLIFIED geometry. The actual TO result has organic curves.
# We approximate it with straight-line transitions for simplicity.
#
# Coordinate system: X = width, Y = height (loading axis), Z = thickness
#
# Run with: abaqus cae noGUI=paper_reproduction/scripts/01_create_to_geometry.py

from abaqus import *
from abaqusConstants import *
from caeModules import *

print("\n" + "=" * 70)
print("PAPER REPRODUCTION - STEP 1: CREATE TO BRACKET GEOMETRY")
print("=" * 70)

# =============================================================================
# GEOMETRY PARAMETERS (from paper Figures 1 & 2)
# =============================================================================

# Overall dimensions (mm)
TOTAL_HEIGHT = 146.17  # Figure 1 value
TOTAL_WIDTH = 64.60    # Figure 1 - distance between lower pin block centers
THICKNESS = 12.0       # Estimated from image depth

# Upper tab dimensions
UPPER_TAB_WIDTH = 25.0
UPPER_TAB_HEIGHT = 25.0
UPPER_PIN_DIAMETER = 10.0
UPPER_PIN_CENTER_Y = TOTAL_HEIGHT - UPPER_TAB_HEIGHT / 2

# Lower block dimensions
LOWER_BLOCK_WIDTH = 25.0
LOWER_BLOCK_HEIGHT = 25.0
LOWER_PIN_DIAMETER = 10.0
LOWER_PIN_CENTER_Y = LOWER_BLOCK_HEIGHT / 2

# Lower block center positions (X coordinates)
LOWER_LEFT_CENTER_X = -TOTAL_WIDTH / 2
LOWER_RIGHT_CENTER_X = TOTAL_WIDTH / 2

# Calculate derived dimensions
x_left_outer = LOWER_LEFT_CENTER_X - LOWER_BLOCK_WIDTH / 2   # -44.8
x_left_inner = LOWER_LEFT_CENTER_X + LOWER_BLOCK_WIDTH / 2   # -19.8
x_right_inner = LOWER_RIGHT_CENTER_X - LOWER_BLOCK_WIDTH / 2  # 19.8
x_right_outer = LOWER_RIGHT_CENTER_X + LOWER_BLOCK_WIDTH / 2  # 44.8

x_upper_left = -UPPER_TAB_WIDTH / 2   # -12.5
x_upper_right = UPPER_TAB_WIDTH / 2    # 12.5

y_bottom = 0.0
y_lower_top = LOWER_BLOCK_HEIGHT      # 25.0
y_upper_bottom = TOTAL_HEIGHT - UPPER_TAB_HEIGHT  # 121.17
y_top = TOTAL_HEIGHT                  # 146.17

# Full width
FULL_WIDTH = x_right_outer - x_left_outer

# Model names
MODEL_NAME = 'TO_Bracket'
PART_NAME = 'Bracket'

print("\nGeometry Parameters:")
print(f"  Total height:     {TOTAL_HEIGHT} mm")
print(f"  Full width:       {FULL_WIDTH:.1f} mm")
print(f"  Thickness:        {THICKNESS} mm")
print(f"  Upper tab:        {UPPER_TAB_WIDTH} x {UPPER_TAB_HEIGHT} mm")
print(f"  Lower blocks:     {LOWER_BLOCK_WIDTH} x {LOWER_BLOCK_HEIGHT} mm each")
print(f"  Pin diameters:    {UPPER_PIN_DIAMETER} mm (all)")

# =============================================================================
# CREATE MODEL
# =============================================================================

print("\n[1/5] Creating model...")

model = mdb.Model(name=MODEL_NAME)
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']

print(f"       Model '{MODEL_NAME}' created")

# =============================================================================
# CREATE BRACKET SOLID (simple approach: two separate lower blocks + upper)
# =============================================================================

print("\n[2/5] Creating bracket geometry...")

# We'll create this as a sketch that traces the OUTER boundary of the Y-shape
# This is a connected solid (not separate pieces)

part = model.Part(name=PART_NAME, dimensionality=THREE_D, type=DEFORMABLE_BODY)

# Create sketch on X-Y plane
sketch = model.ConstrainedSketch(name='BracketSketch', sheetSize=200.0)

# The Y-shape profile (outer boundary only, going counter-clockwise from bottom-left)
# This creates a shape like:
#
#          ___________
#         |           |  <- upper tab
#         |_____^_____|
#              / \
#             /   \       <- tapered legs
#            /     \
#     ______/       \______
#    |                     |
#    |  []           []    |  <- lower blocks ([] = pin holes, added later)
#    |_____|       |_______|
#
# Note: We create the outer boundary, and the "gap" at bottom is part of the profile

# Define the profile points
profile_points = [
    # Start at bottom-left corner of left block
    (x_left_outer, y_bottom),
    # Up left side of left block
    (x_left_outer, y_lower_top),
    # Diagonal to upper tab (left transition)
    (x_upper_left, y_upper_bottom),
    # Up left side of upper tab
    (x_upper_left, y_top),
    # Across top of upper tab
    (x_upper_right, y_top),
    # Down right side of upper tab
    (x_upper_right, y_upper_bottom),
    # Diagonal to right block (right transition)
    (x_right_outer, y_lower_top),
    # Down right side of right block
    (x_right_outer, y_bottom),
    # Across bottom of right block (inward toward gap)
    (x_right_inner, y_bottom),
    # Up right side of gap
    (x_right_inner, y_lower_top),
    # Across top of gap
    (x_left_inner, y_lower_top),
    # Down left side of gap
    (x_left_inner, y_bottom),
    # Across bottom of left block (back to start)
    # (This closes back to the first point)
]

# Draw the profile
for i in range(len(profile_points)):
    p1 = profile_points[i]
    p2 = profile_points[(i + 1) % len(profile_points)]
    sketch.Line(point1=p1, point2=p2)

# Add pin hole circles to the same sketch (they will create holes when extruded)
# Upper pin hole
sketch.CircleByCenterPerimeter(
    center=(0.0, UPPER_PIN_CENTER_Y),
    point1=(UPPER_PIN_DIAMETER / 2, UPPER_PIN_CENTER_Y)
)
# Lower left pin hole
sketch.CircleByCenterPerimeter(
    center=(LOWER_LEFT_CENTER_X, LOWER_PIN_CENTER_Y),
    point1=(LOWER_LEFT_CENTER_X + LOWER_PIN_DIAMETER / 2, LOWER_PIN_CENTER_Y)
)
# Lower right pin hole
sketch.CircleByCenterPerimeter(
    center=(LOWER_RIGHT_CENTER_X, LOWER_PIN_CENTER_Y),
    point1=(LOWER_RIGHT_CENTER_X + LOWER_PIN_DIAMETER / 2, LOWER_PIN_CENTER_Y)
)

print("       Y-shape profile sketch with pin holes created")

# Extrude the profile (circles inside will become holes)
part.BaseSolidExtrude(sketch=sketch, depth=THICKNESS)

print(f"       Extruded to {THICKNESS} mm thickness")
print(f"       Part has {len(part.faces)} faces")

# Write debug info
with open('paper_reproduction/outputs/debug/geometry_debug.txt', 'w') as debug_log:
    debug_log.write("=== GEOMETRY DEBUG ===\n\n")
    debug_log.write(f"Part has {len(part.faces)} faces after extrusion\n")
    debug_log.write(f"Pin holes included in base sketch:\n")
    debug_log.write(f"  Upper: center=(0, {UPPER_PIN_CENTER_Y:.2f}), D={UPPER_PIN_DIAMETER}\n")
    debug_log.write(f"  LowerLeft: center=({LOWER_LEFT_CENTER_X:.2f}, {LOWER_PIN_CENTER_Y:.2f}), D={LOWER_PIN_DIAMETER}\n")
    debug_log.write(f"  LowerRight: center=({LOWER_RIGHT_CENTER_X:.2f}, {LOWER_PIN_CENTER_Y:.2f}), D={LOWER_PIN_DIAMETER}\n")

print("\n[3/5] Pin holes created as part of base extrusion...")

# =============================================================================
# CREATE SETS FOR BCs AND LOADS
# =============================================================================

print("\n[4/5] Creating geometry sets...")

# Use findAt to locate cylindrical faces at pin hole centers
# The cylindrical face of a through hole can be found by a point on its surface

# Upper pin hole - point on inner cylindrical surface at mid-thickness
upper_pin_point = (UPPER_PIN_DIAMETER / 2, UPPER_PIN_CENTER_Y, THICKNESS / 2)
try:
    upper_face = part.faces.findAt((upper_pin_point,))
    part.Set(faces=upper_face, name='UpperPinSurface')
    part.Surface(side1Faces=upper_face, name='Surf-UpperPin')
    print("       Set and Surface 'UpperPinSurface' created")
except Exception as e:
    print(f"       WARNING: Could not find upper pin face: {e}")

# Lower left pin hole
ll_pin_point = (LOWER_LEFT_CENTER_X + LOWER_PIN_DIAMETER / 2, LOWER_PIN_CENTER_Y, THICKNESS / 2)
try:
    ll_face = part.faces.findAt((ll_pin_point,))
    part.Set(faces=ll_face, name='LowerLeftPinSurface')
    part.Surface(side1Faces=ll_face, name='Surf-LowerLeftPin')
    print("       Set and Surface 'LowerLeftPinSurface' created")
except Exception as e:
    print(f"       WARNING: Could not find lower left pin face: {e}")

# Lower right pin hole
lr_pin_point = (LOWER_RIGHT_CENTER_X + LOWER_PIN_DIAMETER / 2, LOWER_PIN_CENTER_Y, THICKNESS / 2)
try:
    lr_face = part.faces.findAt((lr_pin_point,))
    part.Set(faces=lr_face, name='LowerRightPinSurface')
    part.Surface(side1Faces=lr_face, name='Surf-LowerRightPin')
    print("       Set and Surface 'LowerRightPinSurface' created")
except Exception as e:
    print(f"       WARNING: Could not find lower right pin face: {e}")

# All cells for section assignment
part.Set(cells=part.cells, name='AllCells')
print("       Set 'AllCells' created")

# =============================================================================
# SAVE MODEL
# =============================================================================

print("\n[5/5] Saving model...")

mdb.saveAs(pathName='paper_reproduction/outputs/experiment1/TO_Bracket_Geometry.cae')

print("\n" + "=" * 70)
print("STEP 1 COMPLETE - GEOMETRY CREATED")
print("=" * 70)
print(f"""
Output files:
  - paper_reproduction/outputs/experiment1/TO_Bracket_Geometry.cae

Geometry summary:
  - Overall dimensions: {FULL_WIDTH:.1f} x {TOTAL_HEIGHT:.1f} x {THICKNESS:.1f} mm
  - Shape: Simplified Y-bracket (two lower blocks + upper tab)
  - Upper pin hole: D={UPPER_PIN_DIAMETER}mm at (0, {UPPER_PIN_CENTER_Y:.1f})
  - Lower left pin: D={LOWER_PIN_DIAMETER}mm at ({LOWER_LEFT_CENTER_X:.1f}, {LOWER_PIN_CENTER_Y:.1f})
  - Lower right pin: D={LOWER_PIN_DIAMETER}mm at ({LOWER_RIGHT_CENTER_X:.1f}, {LOWER_PIN_CENTER_Y:.1f})

Coordinate system:
  - X = width (horizontal)
  - Y = height (vertical, loading axis)
  - Z = thickness

Sets created:
  - UpperPinSurface (for coupling/load)
  - LowerLeftPinSurface (for BC)
  - LowerRightPinSurface (for BC)
  - AllCells (for section assignment)

Next: Run 02_define_in718_material.py to add material properties
""")
