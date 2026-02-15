# -*- coding: utf-8 -*-
"""
Stage 1 test: Capture a screenshot of the meshed geometry.

Opens Experiment5_TO.cae and saves an isometric view of the meshed part.
Run with: abaqus cae script=scripts/capture_geometry.py
         (or: xvfb-run -a abaqus cae script=scripts/capture_geometry.py)
"""
import os
from abaqus import *
from abaqusConstants import *
from visualization import *

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, os.pardir))
os.chdir(PROJECT_DIR)

# Create screenshots directory
screenshots_dir = os.path.join(PROJECT_DIR, 'screenshots')
if not os.path.exists(screenshots_dir):
    os.makedirs(screenshots_dir)

print("Opening Experiment5_TO.cae...")
openMdb(os.path.join(PROJECT_DIR, 'Experiment5_TO.cae'))

vp = session.viewports['Viewport: 1']

# Display the part mesh
part = mdb.models['Experiment5_TO'].parts['TO_Specimen']
vp.setValues(displayedObject=part)
vp.view.setValues(session.views['Iso'])
vp.view.fitView()

# Show mesh overlay
vp.partDisplay.setValues(mesh=ON)
vp.partDisplay.meshOptions.setValues(meshTechnique=ON)

# Capture screenshot
session.printToFile(
    fileName='screenshots/geometry_mesh',
    format=PNG,
    canvasObjects=(vp,)
)

print("Saved: screenshots/geometry_mesh.png")
print("Stage 1 screenshot test PASSED")
