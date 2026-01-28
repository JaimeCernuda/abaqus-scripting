import os
from abaqus import *
from abaqusConstants import *
import mesh

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')
openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v17.cae')

model = mdb.models['Experiment4_TO_Specimen']
part = model.parts['TO_Specimen']
assembly = model.rootAssembly
instance_name = 'TO_Specimen-1'

# Delete old instance
if instance_name in assembly.instances.keys():
    del assembly.instances[instance_name]

# Clear mesh
try:
    part.deleteMesh()
except:
    pass

# Regenerate
assembly.regenerate()

# Seed and mesh
mesh_size = 5.0
part.seedPart(size=mesh_size, deviationFactor=0.1, minSizeFactor=0.1)
elemType1 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType1,))
part.generateMesh()

with open('mesh_status2.txt', 'w') as f:
    f.write('Nodes: {}\n'.format(len(part.nodes)))
    f.write('Elements: {}\n'.format(len(part.elements)))

# Create independent instance
assembly.Instance(name=instance_name, part=part, dependent=OFF)
assembly.regenerate()

# Save
mdb.saveAs(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v18.cae')
print('Model saved')
