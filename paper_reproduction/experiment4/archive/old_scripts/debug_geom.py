import os
from abaqus import *
from abaqusConstants import *
import mesh

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')
openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v17.cae')

model = mdb.models['Experiment4_TO_Specimen']
part = model.parts['TO_Specimen']

with open('debug_geom.txt', 'w') as f:
    f.write('Cells: {}\n'.format(len(part.cells)))
    f.write('Faces: {}\n'.format(len(part.faces)))
    f.write('Edges: {}\n'.format(len(part.edges)))
    f.write('Vertices: {}\n'.format(len(part.vertices)))
    f.write('Section assignments: {}\n'.format(len(part.sectionAssignments)))
    
    # Check if cells are valid
    for i, cell in enumerate(part.cells):
        try:
            f.write('Cell {}: {} faces\n'.format(i, len(cell.getFaces())))
        except Exception as e:
            f.write('Cell {} error: {}\n'.format(i, str(e)))
    
    # Check materials and sections
    f.write('\nMaterials: {}\n'.format(model.materials.keys()))
    f.write('Sections: {}\n'.format(model.sections.keys()))
