import os
from abaqus import *
from abaqusConstants import *
from caeModules import *
import mesh

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, os.pardir))
os.chdir(PROJECT_DIR)

MESH_SIZE = float(os.environ.get('ABAQUS_MESH_SIZE', '3.0'))

# Run the geometry script first to get a fresh part
execfile(os.path.join(SCRIPT_DIR, 'create_geometry.py'))

model = mdb.models['Experiment4_TO_Specimen']
part = model.parts['TO_Specimen']
assembly = model.rootAssembly

# Delete the dependent instance
del assembly.instances['TO_Specimen-1']

# MESH ON PART BEFORE creating instance
part.setMeshControls(regions=part.cells, elemShape=TET, technique=FREE)
part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)
elemType1 = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType1, elemType2))
part.generateMesh()

with open('mesh_final.txt', 'w') as f:
    f.write('Nodes: {}\n'.format(len(part.nodes)))
    f.write('Elements: {}\n'.format(len(part.elements)))

# NOW create dependent instance
assembly.Instance(name='TO_Specimen-1', part=part, dependent=ON)
assembly.regenerate()

# Add material
mat = model.Material(name='IN718')
mat.Elastic(table=((200000.0, 0.3),))
mat.Density(table=((8.19e-9,),))
mat.Plastic(table=((980.0, 0.0), (1100.0, 0.05), (1241.0, 0.10)))

# Section
model.HomogeneousSolidSection(name='SolidSection', material='IN718', thickness=None)
region = part.Set(cells=part.cells, name='AllCells')
part.SectionAssignment(region=region, sectionName='SolidSection')

# Save
mdb.saveAs(os.path.join(PROJECT_DIR, 'Experiment4_TO_Specimen.cae'))
print('Model saved with {} nodes'.format(len(part.nodes)))
