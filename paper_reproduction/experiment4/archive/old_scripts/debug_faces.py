# -*- coding: utf-8 -*-
"""Debug: Print all faces and edges to file"""

from abaqus import *
from abaqusConstants import *
from caeModules import *

# Open model
openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen.cae')

model = mdb.models['Experiment4_TO_Specimen']
part = model.parts['TO_Specimen']

with open(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/face_debug.txt', 'w') as f:
    f.write("=== ALL FACES ===\n")
    for i, face in enumerate(part.faces):
        pt = face.pointOn[0]
        norm = face.getNormal()
        f.write("Face {}: pt=({:.1f},{:.1f},{:.1f}) norm=({:.1f},{:.1f},{:.1f})\n".format(
            i, pt[0], pt[1], pt[2], norm[0], norm[1], norm[2]))

    f.write("\n=== FACES WITH X-NORMAL (side faces for X-direction holes) ===\n")
    for i, face in enumerate(part.faces):
        norm = face.getNormal()
        if abs(norm[0]) > 0.9:
            pt = face.pointOn[0]
            f.write("Face {}: pt=({:.1f},{:.1f},{:.1f}) norm=({:.1f},{:.1f},{:.1f})\n".format(
                i, pt[0], pt[1], pt[2], norm[0], norm[1], norm[2]))
