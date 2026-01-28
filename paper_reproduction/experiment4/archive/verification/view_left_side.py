# -*- coding: utf-8 -*-
"""
View model from LEFT side (looking down +X axis)
X-direction holes will appear as RECTANGLES (side view of cylinder)
Z-direction holes will appear as CIRCLES (end view of cylinder)
"""
import os
from abaqus import *
from abaqusConstants import *
from caeModules import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')
openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v19.cae')

model = mdb.models['Experiment4_TO_Specimen']
assembly = model.rootAssembly

# Set viewport to show assembly
vp = session.viewports['Viewport: 1']
vp.setValues(displayedObject=assembly)

# Set to wireframe for clear visibility of hole geometry
vp.assemblyDisplay.setValues(renderStyle=WIREFRAME)

# View from LEFT side (looking in +X direction, so seeing YZ plane)
# This is the "Left" view
vp.view.setValues(session.views['Left'])
vp.view.fitView()

print("")
print("=" * 60)
print("VIEWING FROM LEFT SIDE (looking down +X axis)")
print("=" * 60)
print("")
print("How to interpret what you see:")
print("")
print("For X-direction holes (CORRECT):")
print("  - You see RECTANGLES (side view of cylindrical hole)")
print("  - The cylinder axis goes left-right (into the screen)")
print("")
print("For Z-direction holes (WRONG):")
print("  - You see CIRCLES (end view of cylindrical hole)")
print("  - The cylinder axis goes up-down in this view")
print("")
print("Check all three pin holes:")
print("  1. Upper pin hole (top of specimen)")
print("  2. Lower left pin hole")
print("  3. Lower right pin hole")
print("")
print("All should appear as rectangles (slots) not circles!")
print("=" * 60)
