# -*- coding: utf-8 -*-
"""
Experiment 9 - Step 2: Open ODB and capture visualization images.
Run with: abaqus cae script=exp9_visualize.py  (requires DISPLAY, e.g. Xvfb)

Captures:
  1. Von Mises stress contour on deformed shape
  2. Displacement magnitude contour on deformed shape
  3. Deformed shape (no contour)

Uses sys.exit(0) at end to prevent script= mode from hanging.
"""

import os
import sys
from abaqus import *
from abaqusConstants import *
from caeModules import *
import visualization

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, os.pardir))
WORK_DIR = os.path.join(PROJECT_DIR, 'run')
os.chdir(WORK_DIR)

ODB_NAME = 'Job_20kN.odb'
odb_path = os.path.join(WORK_DIR, ODB_NAME)

if not os.path.exists(odb_path):
    print('ERROR: ODB not found at: ' + odb_path)
    sys.exit(1)

print('[1/5] Opening ODB: ' + ODB_NAME)
odb = session.openOdb(name=odb_path)

# Get default viewport
vp = session.viewports['Viewport: 1']
vp.setValues(displayedObject=odb)

# Go to last frame of last step
step_name = odb.steps.keys()[-1]
last_frame = odb.steps[step_name].frames[-1]
vp.odbDisplay.setFrame(step=0, frame=-1)

print('  Step: {}, Frame: {} (time={})'.format(
    step_name, last_frame.frameId, last_frame.frameValue))

# Set isometric view and fit
vp.view.setValues(session.views['Iso'])
vp.view.fitView()

# Configure print options: no decorations for clean images
session.printOptions.setValues(vpDecorations=OFF, compass=OFF)

# =========================================================================
# IMAGE 1: Von Mises stress contour on deformed shape
# =========================================================================
print('[2/5] Capturing Mises stress contour...')
vp.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))
vp.odbDisplay.setPrimaryVariable(
    variableLabel='S',
    outputPosition=INTEGRATION_POINT,
    refinement=(INVARIANT, 'Mises'))
vp.odbDisplay.commonOptions.setValues(deformationScaling=UNIFORM, uniformScaleFactor=1.0)

session.printToFile(
    fileName=os.path.join(WORK_DIR, 'stress_mises'),
    format=PNG,
    canvasObjects=(vp,))
print('  Saved: stress_mises.png')

# =========================================================================
# IMAGE 2: Displacement magnitude contour on deformed shape
# =========================================================================
print('[3/5] Capturing displacement contour...')
vp.odbDisplay.setPrimaryVariable(
    variableLabel='U',
    outputPosition=NODAL,
    refinement=(INVARIANT, 'Magnitude'))

session.printToFile(
    fileName=os.path.join(WORK_DIR, 'displacement_magnitude'),
    format=PNG,
    canvasObjects=(vp,))
print('  Saved: displacement_magnitude.png')

# =========================================================================
# IMAGE 3: Deformed shape only (no contour)
# =========================================================================
print('[4/5] Capturing deformed shape...')
vp.odbDisplay.display.setValues(plotState=(DEFORMEDSHAPE,))

session.printToFile(
    fileName=os.path.join(WORK_DIR, 'deformed_shape'),
    format=PNG,
    canvasObjects=(vp,))
print('  Saved: deformed_shape.png')

# =========================================================================
# VERIFY AND EXIT
# =========================================================================
print('[5/5] Verification...')
odb.close()

image_count = 0
for f in sorted(os.listdir(WORK_DIR)):
    if f.endswith('.png'):
        fpath = os.path.join(WORK_DIR, f)
        print('  IMAGE: {} ({} bytes)'.format(f, os.path.getsize(fpath)))
        image_count += 1

if image_count >= 3:
    print('')
    print('Experiment 9 Step 2 complete: {} images captured.'.format(image_count))
else:
    print('')
    print('WARNING: Expected 3 images, found {}'.format(image_count))

# Force exit to prevent script= mode from keeping CAE open
sys.exit(0)
