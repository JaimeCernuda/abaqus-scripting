import os
from abaqus import *
from abaqusConstants import *
import mesh

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')
openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v17.cae')

model = mdb.models['Experiment4_TO_Specimen']
part = model.parts['TO_Specimen']
assembly = model.rootAssembly

# Regenerate
assembly.regenerate()

# Clear existing mesh
part.deleteMesh()

# Seed part with larger size to avoid node limit
mesh_size = 5.0
part.seedPart(size=mesh_size, deviationFactor=0.1, minSizeFactor=0.1)

# Set element type - C3D4 tet
elemType1 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType1,))

# Generate mesh
part.generateMesh()

print('Nodes: {}'.format(len(part.nodes)))
print('Elements: {}'.format(len(part.elements)))

# Save
mdb.saveAs(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v17.cae')

# Write input and submit job
job = mdb.jobs['Job_FatigueTest_v16']
job.writeInput()
print('Input file written')
