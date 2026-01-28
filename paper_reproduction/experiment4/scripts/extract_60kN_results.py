import os
from odbAccess import *
from abaqusConstants import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')

odb = openOdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Job_v19_60kN.odb')

step = odb.steps['FatigueTest']
frame = step.frames[-1]

stress = frame.fieldOutputs['S']
max_mises = 0.0
for value in stress.values:
    if value.mises > max_mises:
        max_mises = value.mises

disp = frame.fieldOutputs['U']
max_u2 = 0.0
for value in disp.values:
    if abs(value.data[1]) > abs(max_u2):
        max_u2 = value.data[1]

peeq = frame.fieldOutputs['PEEQ']
max_peeq = 0.0
for value in peeq.values:
    if value.data > max_peeq:
        max_peeq = value.data

with open('results_60kN.txt', 'w') as f:
    f.write('Job_v19_60kN Results (60 kN vertical load)\n')
    f.write('=' * 50 + '\n')
    f.write('Max von Mises stress: {:.2f} MPa\n'.format(max_mises))
    f.write('Max Y displacement: {:.4f} mm\n'.format(max_u2))
    f.write('Max PEEQ (plastic strain): {:.6f}\n'.format(max_peeq))
    if max_mises > 980:
        f.write('\nNOTE: Stress exceeds yield (980 MPa) - plastic deformation occurred\n')

odb.close()
