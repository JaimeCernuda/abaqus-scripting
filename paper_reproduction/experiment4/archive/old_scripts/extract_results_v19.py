import os
from odbAccess import *
from abaqusConstants import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')

odb = openOdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Job_v19.odb')

step = odb.steps['FatigueTest']
frame = step.frames[-1]

# Get stress field
stress = frame.fieldOutputs['S']

# Find max von Mises stress
max_mises = 0.0
for value in stress.values:
    mises = value.mises
    if mises > max_mises:
        max_mises = mises

# Get displacement
disp = frame.fieldOutputs['U']
max_u2 = 0.0
for value in disp.values:
    if abs(value.data[1]) > abs(max_u2):
        max_u2 = value.data[1]

# Get PEEQ (plastic strain)
peeq = frame.fieldOutputs['PEEQ']
max_peeq = 0.0
for value in peeq.values:
    if value.data > max_peeq:
        max_peeq = value.data

with open('results_v19.txt', 'w') as f:
    f.write('Job_v19 Results (20 kN vertical load)\n')
    f.write('=' * 50 + '\n')
    f.write('Max von Mises stress: {:.2f} MPa\n'.format(max_mises))
    f.write('Max Y displacement: {:.4f} mm\n'.format(max_u2))
    f.write('Max PEEQ (plastic strain): {:.6f}\n'.format(max_peeq))
    if max_mises > 980:
        f.write('\nNOTE: Stress exceeds yield (980 MPa) - plastic deformation occurred\n')

odb.close()
