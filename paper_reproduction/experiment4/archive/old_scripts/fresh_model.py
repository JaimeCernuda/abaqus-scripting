import os
from abaqus import *
from abaqusConstants import *
from caeModules import *
import mesh

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')

# Run the geometry script first to get a fresh part
execfile(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/scripts/create_geometry_v16.py')

model = mdb.models['Experiment4_TO_Specimen']
part = model.parts['TO_Specimen']
assembly = model.rootAssembly
instance = assembly.instances['TO_Specimen-1']

# Delete the dependent instance
del assembly.instances['TO_Specimen-1']

# MESH ON PART BEFORE creating instance
part.setMeshControls(regions=part.cells, elemShape=TET, technique=FREE)
part.seedPart(size=7.0, deviationFactor=0.1, minSizeFactor=0.1)
elemType1 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType1,))
part.generateMesh()

with open('mesh_final.txt', 'w') as f:
    f.write('Nodes: {}\n'.format(len(part.nodes)))
    f.write('Elements: {}\n'.format(len(part.elements)))

# NOW create dependent instance (must be dependent for meshed part)
assembly.Instance(name='TO_Specimen-1', part=part, dependent=ON)
assembly.regenerate()

# Save
mdb.saveAs(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v19.cae')
