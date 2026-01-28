import os
from abaqus import *
from abaqusConstants import *
import mesh

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')
openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v18.cae')

model = mdb.models['Experiment4_TO_Specimen']
part = model.parts['TO_Specimen']
assembly = model.rootAssembly

# Delete existing mesh
part.deleteMesh()

# Set mesh controls
part.setMeshControls(regions=part.cells, elemShape=TET, technique=FREE)

# Larger seed for fewer nodes
part.seedPart(size=7.0, deviationFactor=0.1, minSizeFactor=0.1)

# Element type
elemType1 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType1,))

# Generate mesh
part.generateMesh()
nodes = len(part.nodes)
elements = len(part.elements)

with open('mesh_result.txt', 'w') as f:
    f.write('Nodes: {}\n'.format(nodes))
    f.write('Elements: {}\n'.format(elements))
    if nodes > 1000:
        f.write('WARNING: Exceeds 1000 node limit\n')
    else:
        f.write('OK: Within node limit\n')

# Recreate instance as independent
instance_name = 'TO_Specimen-1'
if instance_name in assembly.instances.keys():
    del assembly.instances[instance_name]
assembly.Instance(name=instance_name, part=part, dependent=OFF)
assembly.regenerate()

# Save
mdb.saveAs(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v18.cae')
