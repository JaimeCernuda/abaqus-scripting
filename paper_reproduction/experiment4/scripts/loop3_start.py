# -*- coding: utf-8 -*-
"""
Loop 3 Start - Open ODB and set wireframe right-side view.
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

# Set to wireframe
vp.odbDisplay.commonOptions.setValues(renderStyle=WIREFRAME)

# View from RIGHT side
vp.view.setValues(session.views['Right'])
vp.view.fitView()

print("")
print("=" * 70)
print("LOOP 3 START - WIREFRAME RIGHT VIEW")
print("=" * 70)
print("In this view, X-direction holes appear as CIRCLES")
print("Check: Upper hole should be CIRCLE at TOP (Y~132)")
print("       Lower holes should be CIRCLES at BOTTOM (Y~14)")
print("=" * 70)
