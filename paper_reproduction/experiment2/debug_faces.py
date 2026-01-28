# Debug script to examine faces of Y-shape solid

from abaqus import *
from abaqusConstants import *
from caeModules import *

# Parameters
TOTAL_HEIGHT = 146.17
TOTAL_WIDTH = 64.60
THICKNESS = 12.0
LOWER_BLOCK_WIDTH = 25.0
LOWER_BLOCK_HEIGHT = 25.0
UPPER_TAB_WIDTH = 25.0
UPPER_TAB_HEIGHT = 25.0
LOWER_LEFT_X = -TOTAL_WIDTH / 2
LOWER_RIGHT_X = TOTAL_WIDTH / 2

x_left_outer = LOWER_LEFT_X - LOWER_BLOCK_WIDTH / 2
x_right_outer = LOWER_RIGHT_X + LOWER_BLOCK_WIDTH / 2
x_upper_right = UPPER_TAB_WIDTH / 2
y_lower_top = LOWER_BLOCK_HEIGHT
y_upper_bottom = TOTAL_HEIGHT - UPPER_TAB_HEIGHT
y_top = TOTAL_HEIGHT

# Open model
openMdb(pathName='paper_reproduction/outputs/experiment2/TO_Bracket_Geometry.cae')
model = mdb.models['TO_Bracket_Exp2']
part = model.parts['Bracket']

output = []
output.append("=== FACE ANALYSIS ===")
output.append(f"Total faces: {len(part.faces)}")

side_faces = []

for i, face in enumerate(part.faces):
    pt = face.pointOn[0]
    edges = face.getEdges()
    normal = face.getNormal(pt)

    output.append(f"\nFace {i}:")
    output.append(f"  pointOn: ({pt[0]:.2f}, {pt[1]:.2f}, {pt[2]:.2f})")
    output.append(f"  normal:  ({normal[0]:.2f}, {normal[1]:.2f}, {normal[2]:.2f})")
    output.append(f"  edges: {len(edges)}")

    # Check if this could be a side face (normal pointing in X direction)
    if abs(normal[0]) > 0.9:
        output.append(f"  >>> SIDE FACE (X-normal)")
        side_faces.append((i, pt[0], normal[0]))

output.append("\n=== TARGET FACES FOR HOLES ===")
output.append(f"Upper tab right side: X = {x_upper_right:.2f}")
output.append(f"Lower right block right side: X = {x_right_outer:.2f}")
output.append(f"Lower left block left side: X = {x_left_outer:.2f}")

output.append("\n=== SIDE FACES FOUND ===")
for idx, x, nx in side_faces:
    output.append(f"Face {idx}: X={x:.2f}, normalX={nx:.2f}")

with open('paper_reproduction/outputs/experiment2/face_debug.txt', 'w') as f:
    f.write('\n'.join(output))

print("Debug written to face_debug.txt")
