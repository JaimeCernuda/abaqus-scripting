# -*- coding: utf-8 -*-
"""
Loop 3 - Set wireframe right-side view for critical geometry verification.
"""
import os
from abaqus import *
from abaqusConstants import *
from visualization import *

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, os.pardir))
os.chdir(PROJECT_DIR)

# Get current viewport
vp = session.viewports['Viewport: 1']

# Set to wireframe for clear hole visibility
vp.odbDisplay.commonOptions.setValues(renderStyle=WIREFRAME)

# View from RIGHT side (looking down -X axis)
# In this view: X-direction holes appear as CIRCLES
#               Z-direction holes appear as RECTANGLES
vp.view.setValues(session.views['Right'])
vp.view.fitView()

print("")
print("=" * 70)
print("LOOP 3 - CRITICAL GEOMETRY VERIFICATION")
print("=" * 70)
print("")
print("Viewing from RIGHT side (looking down -X axis)")
print("")
print("CRITICAL CHECK:")
print("  - UPPER PIN HOLE: Should be a CIRCLE at the TOP of the specimen")
print("  - LOWER PIN HOLES: Should be CIRCLES at the BOTTOM")
print("")
print("If upper hole appears as RECTANGLE -> Z-direction (WRONG)")
print("If upper hole appears as CIRCLE -> X-direction (CORRECT)")
print("")
print("WARNING: The narrowing in the middle is the topology-optimized")
print("shape, NOT a pin hole. Pin holes are only at top and bottom.")
print("=" * 70)
