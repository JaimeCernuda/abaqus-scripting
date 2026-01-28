import os
from abaqus import *
from abaqusConstants import *
import mesh

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')
openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v17.cae')

model = mdb.models['Experiment4_TO_Specimen']
part = model.parts['TO_Specimen']

# Delete existing mesh
try:
    part.deleteMesh()
except:
    pass

# Set mesh controls to free mesh (tetrahedral)
part.setMeshControls(regions=part.cells, elemShape=TET, technique=FREE)

# Seed
part.seedPart(size=6.0, deviationFactor=0.1, minSizeFactor=0.1)

# Element type
elemType1 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType1,))

# Generate mesh
try:
    part.generateMesh()
    with open('mesh_result.txt', 'w') as f:
        f.write('SUCCESS\n')
        f.write('Nodes: {}\n'.format(len(part.nodes)))
        f.write('Elements: {}\n'.format(len(part.elements)))
except Exception as e:
    with open('mesh_result.txt', 'w') as f:
        f.write('FAILED: {}\n'.format(str(e)))

# Save
mdb.saveAs(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v18.cae')
