# -*- coding: utf-8 -*-
"""
Experiment 10 - Visualization: Open optimized-design ODB and capture images.
Run with: abaqus cae script=exp10_visualize.py  (requires DISPLAY, e.g. Xvfb)

The ODB is produced by running Abaqus FEA on the LAST-CYCLE .inp from Tosca
(SAVE.inp/<N>/), which includes SIMP-penalized element stiffnesses. This shows
stress/displacement on the actual optimized topology, not the original geometry.

Captures:
  1. Von Mises stress contour on deformed shape
  2. Displacement magnitude contour on deformed shape
  3. Deformed shape (clean view)

Uses sys.exit(0) at end to prevent script= mode from hanging.
"""

import os
import sys
from abaqus import *
from abaqusConstants import *
from caeModules import *
import visualization
import glob

WORK_DIR = os.path.join(os.environ['HOME'], 'Abaqus', 'paper_reproduction',
                        'experiment10', 'run')
os.chdir(WORK_DIR)

# Find the optimized-design ODB
# Phase 9 of exp10_optimize.py runs FEA on SAVE.inp/<last_cycle>/ and
# produces Exp10_optimized.odb there.
tosca_dir = os.path.join(WORK_DIR, 'exp10_tosca')
save_inp_dir = os.path.join(tosca_dir, 'SAVE.inp')
odb_path = None

if os.path.isdir(save_inp_dir):
    cycle_dirs = [d for d in os.listdir(save_inp_dir)
                  if d.isdigit() and os.path.isdir(os.path.join(save_inp_dir, d))]
    if cycle_dirs:
        last_cycle = max(cycle_dirs, key=int)
        candidate = os.path.join(save_inp_dir, last_cycle, 'Exp10_optimized.odb')
        if os.path.exists(candidate):
            odb_path = candidate
            print('Found optimized-design ODB in cycle {}'.format(last_cycle))

# Fallback: any ODB in tosca dir or work dir
if not odb_path:
    for search_dir in [tosca_dir, WORK_DIR]:
        if os.path.isdir(search_dir):
            candidates = sorted(glob.glob(os.path.join(search_dir, '*.odb')))
            if candidates:
                odb_path = candidates[-1]
                print('Fallback ODB: {}'.format(os.path.basename(odb_path)))
                break

# Also search one level deeper (SAVE.inp/*/*.odb)
if not odb_path and os.path.isdir(save_inp_dir):
    candidates = sorted(glob.glob(os.path.join(save_inp_dir, '*', '*.odb')))
    if candidates:
        odb_path = candidates[-1]
        print('Found ODB in SAVE.inp: {}'.format(odb_path))

if not odb_path or not os.path.exists(odb_path):
    print('ERROR: No ODB file found.')
    print('  Searched: {}'.format(save_inp_dir))
    print('  Searched: {}'.format(tosca_dir))
    print('  Searched: {}'.format(WORK_DIR))
    sys.exit(1)

print('[1/5] Opening ODB: {}'.format(odb_path))
odb = session.openOdb(name=odb_path)

vp = session.viewports['Viewport: 1']
vp.setValues(displayedObject=odb)

# Go to last frame
step_name = odb.steps.keys()[-1]
last_frame = odb.steps[step_name].frames[-1]
vp.odbDisplay.setFrame(step=0, frame=-1)

print('  Step: {}, Frame: {} (time={})'.format(
    step_name, last_frame.frameId, last_frame.frameValue))

# List available field outputs
print('  Field outputs: {}'.format(list(last_frame.fieldOutputs.keys())))

# Set isometric view
vp.view.setValues(session.views['Iso'])
vp.view.fitView()
session.printOptions.setValues(vpDecorations=OFF, compass=OFF)

# =========================================================================
# IMAGE 1: Von Mises stress contour
# =========================================================================
print('[2/5] Capturing Mises stress contour...')
vp.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))
vp.odbDisplay.setPrimaryVariable(
    variableLabel='S',
    outputPosition=INTEGRATION_POINT,
    refinement=(INVARIANT, 'Mises'))
vp.odbDisplay.commonOptions.setValues(
    deformationScaling=UNIFORM, uniformScaleFactor=1.0)

session.printToFile(
    fileName=os.path.join(WORK_DIR, 'stress_mises'),
    format=PNG,
    canvasObjects=(vp,))
print('  Saved: stress_mises.png')

# =========================================================================
# IMAGE 2: Displacement magnitude contour
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
# IMAGE 3: Deformed shape
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

print('')
print('Experiment 10 visualization complete: {} images captured.'.format(image_count))

sys.exit(0)
