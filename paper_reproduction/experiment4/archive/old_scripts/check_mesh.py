import os
from abaqus import *
from abaqusConstants import *
os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')
openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v17.cae')
model = mdb.models['Experiment4_TO_Specimen']
part = model.parts['TO_Specimen']
with open('mesh_status.txt', 'w') as f:
    f.write('Nodes: {}\n'.format(len(part.nodes)))
    f.write('Elements: {}\n'.format(len(part.elements)))
    f.write('Cells: {}\n'.format(len(part.cells)))
