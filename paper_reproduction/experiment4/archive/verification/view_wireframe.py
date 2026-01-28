# -*- coding: utf-8 -*-
"""
Open model and set wireframe view for verification
"""
import os
from abaqus import *
from abaqusConstants import *
from caeModules import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')
openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v19.cae')

model = mdb.models['Experiment4_TO_Specimen']
assembly = model.rootAssembly

# Make sure assembly is regenerated
assembly.regenerate()

# Set viewport to show assembly in wireframe
session.viewports['Viewport: 1'].setValues(displayedObject=assembly)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(renderStyle=WIREFRAME)

# Set view to isometric to clearly see hole orientations
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])

# Fit all
session.viewports['Viewport: 1'].view.fitView()

print("Model opened in wireframe mode - check viewport for hole orientations")
print("- X-direction holes: visible as ellipses from side view")
print("- Upper block: X from -9 to 9, hole should go through this direction")
