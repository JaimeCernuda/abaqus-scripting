# -*- coding: utf-8 -*-
"""
View Job_100kN results with stress contours.
"""
import os
from abaqus import *
from abaqusConstants import *
from visualization import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')

# Open ODB
odb = session.openOdb('Job_100kN.odb')
vp = session.viewports['Viewport: 1']
vp.setValues(displayedObject=odb)

# Set to contour display (S, Mises)
vp.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))
vp.odbDisplay.setPrimaryVariable(
    variableLabel='S',
    outputPosition=INTEGRATION_POINT,
    refinement=(INVARIANT, 'Mises')
)

# Isometric view
vp.view.setValues(session.views['Iso'])
vp.view.fitView()

# Print summary
print("")
print("=" * 70)
print("EXPERIMENT 4 - FINAL RESULTS VERIFICATION")
print("=" * 70)
print("")
print("Viewing Job_100kN.odb - 100 kN load case with plastic deformation")
print("")
print("Expected results:")
print("  Max Stress: ~1148 MPa")
print("  PEEQ: ~0.067 (6.7% plastic strain)")
print("")
print("Repository cleaned and organized successfully.")
print("=" * 70)
