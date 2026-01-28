# -*- coding: utf-8 -*-
"""
View from RIGHT side to definitively show hole orientations.
Looking down -X axis:
- X-direction holes appear as CIRCLES
- Z-direction holes appear as RECTANGLES
"""
import os
from abaqus import *
from abaqusConstants import *
from visualization import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')

# Open ODB in viewer
odb = session.openOdb('Job_100kN.odb')
vp = session.viewports['Viewport: 1']
vp.setValues(displayedObject=odb)

# Set to wireframe for clear visibility
vp.odbDisplay.commonOptions.setValues(renderStyle=WIREFRAME)

# View from RIGHT side (looking down -X axis)
# This shows Y vertical, Z horizontal
vp.view.setValues(session.views['Right'])
vp.view.fitView()

# Print instructions
print("")
print("=" * 70)
print("VIEWING FROM RIGHT SIDE (looking down -X axis)")
print("=" * 70)
print("")
print("In this view:")
print("  Y axis: vertical (up)")
print("  Z axis: horizontal (left-right)")
print("  X axis: into the screen")
print("")
print("How holes appear:")
print("  X-direction holes: CIRCLES (you're looking down the hole)")
print("  Z-direction holes: RECTANGLES (you're seeing the side)")
print("")
print("CHECK THE UPPER BLOCK:")
print("  If upper hole is CIRCULAR -> X-direction (CORRECT)")
print("  If upper hole is RECTANGULAR -> Z-direction (WRONG)")
print("=" * 70)
