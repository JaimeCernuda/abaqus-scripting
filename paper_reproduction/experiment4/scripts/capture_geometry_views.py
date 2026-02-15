# -*- coding: utf-8 -*-
"""
Capture geometry verification screenshots showing hole orientations.
"""
import os
from abaqus import *
from abaqusConstants import *
from visualization import *

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, os.pardir))
os.chdir(PROJECT_DIR)

# Open ODB
odb = session.openOdb('Job_100kN.odb')
vp = session.viewports['Viewport: 1']
vp.setValues(displayedObject=odb)

# Set to wireframe
vp.odbDisplay.commonOptions.setValues(renderStyle=WIREFRAME)
vp.odbDisplay.display.setValues(plotState=(UNDEFORMED,))

# Right view - shows X-direction holes as circles
vp.view.setValues(session.views['Right'])
vp.view.fitView()
session.printToFile(
    fileName='screenshots/geometry/holes_right_view_wireframe',
    format=PNG,
    canvasObjects=(vp,)
)

# Front view
vp.view.setValues(session.views['Front'])
vp.view.fitView()
session.printToFile(
    fileName='screenshots/geometry/holes_front_view_wireframe',
    format=PNG,
    canvasObjects=(vp,)
)

# Isometric view
vp.view.setValues(session.views['Iso'])
vp.view.fitView()
session.printToFile(
    fileName='screenshots/geometry/holes_iso_view_wireframe',
    format=PNG,
    canvasObjects=(vp,)
)

odb.close()
print("Geometry verification screenshots saved")
