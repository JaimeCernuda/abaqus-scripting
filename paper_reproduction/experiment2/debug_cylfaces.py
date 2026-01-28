# Debug cylindrical faces

from abaqus import *
from abaqusConstants import *
from caeModules import *

openMdb(pathName='paper_reproduction/outputs/experiment2/TO_Bracket_Geometry.cae')
part = mdb.models['TO_Bracket_Exp2'].parts['Bracket']

output = []
output.append("=== CYLINDRICAL FACES (2 edges) ===")
for face in part.faces:
    if len(face.getEdges()) == 2:
        pt = face.pointOn[0]
        output.append(f"Face {face.index}: ({pt[0]:.2f}, {pt[1]:.2f}, {pt[2]:.2f})")

output.append("\n=== Expected positions ===")
output.append("Upper: Y = 131.17 (146.17 - 30/2)")
output.append("Lower: Y = 17.5 (35/2)")

with open('paper_reproduction/outputs/experiment2/cylface_debug.txt', 'w') as f:
    f.write('\n'.join(output))

print("Debug written")
