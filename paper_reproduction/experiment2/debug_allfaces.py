# Debug ALL faces in the geometry

from abaqus import *
from abaqusConstants import *
from caeModules import *

openMdb(pathName='paper_reproduction/outputs/experiment2/TO_Bracket_Geometry.cae')
part = mdb.models['TO_Bracket_Exp2'].parts['Bracket']

output = []
output.append(f"Total faces: {len(part.faces)}")
output.append("\n=== ALL FACES ===")

for i, face in enumerate(part.faces):
    pt = face.pointOn[0]
    normal = face.getNormal(pt)
    edges = len(face.getEdges())
    output.append(f"Face {i}: pos=({pt[0]:.1f}, {pt[1]:.1f}, {pt[2]:.1f}), normal=({normal[0]:.2f}, {normal[1]:.2f}, {normal[2]:.2f}), edges={edges}")

output.append("\n=== X-NORMAL FACES (potential cut targets) ===")
for face in part.faces:
    pt = face.pointOn[0]
    normal = face.getNormal(pt)
    if abs(normal[0]) > 0.9:
        output.append(f"X={pt[0]:.2f}, Y={pt[1]:.2f}, normalX={normal[0]:.2f}")

output.append("\n=== TARGET X VALUES ===")
output.append(f"x_left_outer = -32.3 - 35/2 = -49.8")
output.append(f"x_upper_right = 30/2 = 15.0")
output.append(f"x_right_outer = 32.3 + 35/2 = 49.8")

with open('paper_reproduction/outputs/experiment2/allfaces_debug.txt', 'w') as f:
    f.write('\n'.join(output))

print("Debug written to allfaces_debug.txt")
