# -*- coding: utf-8 -*-
"""
View from FRONT to check for any Z-direction holes.
Looking down -Z axis:
- Z-direction holes appear as CIRCLES
- X-direction holes appear as RECTANGLES
"""
import os
from abaqus import *
from abaqusConstants import *
from visualization import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')

odb = session.openOdb('Job_100kN.odb')
vp = session.viewports['Viewport: 1']
vp.setValues(displayedObject=odb)

# Set to wireframe
vp.odbDisplay.commonOptions.setValues(renderStyle=WIREFRAME)

# View from FRONT (looking down -Z axis)
vp.view.setValues(session.views['Front'])
vp.view.fitView()

print("")
print("=" * 70)
print("VIEWING FROM FRONT (looking down -Z axis)")
print("=" * 70)
print("")
print("In this view:")
print("  X axis: horizontal (left-right)")
print("  Y axis: vertical (up-down)")
print("  Z axis: into the screen")
print("")
print("How holes appear:")
print("  Z-direction holes: CIRCLES (looking down the hole)")
print("  X-direction holes: RECTANGLES (side view)")
print("")
print("CHECK FOR UNEXPECTED HOLES:")
print("  If there's a CIRCLE in the CENTER/NECK region -> Z-direction hole (PROBLEM)")
print("  The pin holes should appear as RECTANGLES (slots) from this view")
print("=" * 70)
