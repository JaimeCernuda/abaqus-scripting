# -*- coding: utf-8 -*-
"""
Capture stress contour screenshots for all three jobs.
"""
import os
from abaqus import *
from abaqusConstants import *
from visualization import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')

jobs = [
    ('Job_20kN.odb', '20kN_elastic'),
    ('Job_60kN.odb', '60kN_yield'),
    ('Job_100kN.odb', '100kN_plastic'),
]

vp = session.viewports['Viewport: 1']

for odb_name, result_name in jobs:
    print("Processing {}...".format(odb_name))

    # Open ODB
    odb = session.openOdb(odb_name)
    vp.setValues(displayedObject=odb)

    # Set to stress contours on deformed shape
    vp.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))
    vp.odbDisplay.setPrimaryVariable(
        variableLabel='S',
        outputPosition=INTEGRATION_POINT,
        refinement=(INVARIANT, 'Mises')
    )

    # Set deformation scale factor
    vp.odbDisplay.commonOptions.setValues(deformationScaling=UNIFORM, uniformScaleFactor=10)

    # Isometric view
    vp.view.setValues(session.views['Iso'])
    vp.view.fitView()

    # Save screenshot
    session.printToFile(
        fileName='screenshots/results_{}_iso'.format(result_name),
        format=PNG,
        canvasObjects=(vp,)
    )

    # Front view
    vp.view.setValues(session.views['Front'])
    vp.view.fitView()
    session.printToFile(
        fileName='screenshots/results_{}_front'.format(result_name),
        format=PNG,
        canvasObjects=(vp,)
    )

    # Right view (to see holes)
    vp.view.setValues(session.views['Right'])
    vp.view.fitView()
    session.printToFile(
        fileName='screenshots/results_{}_right'.format(result_name),
        format=PNG,
        canvasObjects=(vp,)
    )

    odb.close()
    print("  Saved screenshots for {}".format(result_name))

print("")
print("All result screenshots saved to screenshots/ folder")
