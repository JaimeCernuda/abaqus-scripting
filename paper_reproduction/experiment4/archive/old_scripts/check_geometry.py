# -*- coding: utf-8 -*-
from abaqus import *
from abaqusConstants import *
from caeModules import *

openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v14.cae')

model = mdb.models['Experiment4_TO_Specimen']
part = model.parts['TO_Specimen']

# Print volume
print("Number of cells: {}".format(len(part.cells)))
for i, cell in enumerate(part.cells):
    print("Cell {}: volume = {}".format(i, cell.getSize()))

# Print number of faces
print("\nNumber of faces: {}".format(len(part.faces)))

# Check for circular edges (which would indicate holes)
circular_edges = 0
for edge in part.edges:
    try:
        radius = edge.getRadius()
        if radius is not None:
            print("Found circular edge with radius: {}".format(radius))
            circular_edges += 1
    except:
        pass

print("\nTotal circular edges found: {}".format(circular_edges))
