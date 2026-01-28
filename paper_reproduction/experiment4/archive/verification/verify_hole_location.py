# -*- coding: utf-8 -*-
"""
Verify that the upper pin hole is actually IN THE TOP SUPPORT BLOCK,
not in the center/neck of the specimen.
"""
import os
from odbAccess import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')

odb = openOdb('Job_100kN.odb', readOnly=True)
instance = odb.rootAssembly.instances['TO_SPECIMEN-1']

# Get all nodes
all_nodes = instance.nodes

# Find the bounding box of the entire model
all_x = [n.coordinates[0] for n in all_nodes]
all_y = [n.coordinates[1] for n in all_nodes]
all_z = [n.coordinates[2] for n in all_nodes]

output = []
output.append("=" * 70)
output.append("SPECIMEN GEOMETRY AND PIN HOLE LOCATION VERIFICATION")
output.append("=" * 70)
output.append("")
output.append("OVERALL MODEL BOUNDING BOX:")
output.append("  X: {:.1f} to {:.1f} (width: {:.1f} mm)".format(min(all_x), max(all_x), max(all_x)-min(all_x)))
output.append("  Y: {:.1f} to {:.1f} (height: {:.1f} mm)".format(min(all_y), max(all_y), max(all_y)-min(all_y)))
output.append("  Z: {:.1f} to {:.1f} (thickness: {:.1f} mm)".format(min(all_z), max(all_z), max(all_z)-min(all_z)))
output.append("")

# Expected dimensions from plan:
# Total height: 146.17 mm
# Upper block: Y from ~118 to 146 (top 28mm of specimen)
# Neck/center: Y from ~28 to 118 (middle)
# Lower blocks: Y from 0 to 28 (bottom 28mm)

output.append("EXPECTED SPECIMEN REGIONS:")
output.append("  UPPER BLOCK (top support): Y = 118 to 146 mm")
output.append("  NECK/CENTER: Y = 28 to 118 mm")
output.append("  LOWER BLOCKS (bottom supports): Y = 0 to 28 mm")
output.append("")

# Get upper pin hole nodes
upper_pin_set = odb.rootAssembly.nodeSets['UPPERPINHOLE']
pin_nodes = upper_pin_set.nodes[0]

pin_x = [n.coordinates[0] for n in pin_nodes]
pin_y = [n.coordinates[1] for n in pin_nodes]
pin_z = [n.coordinates[2] for n in pin_nodes]

output.append("UPPER PIN HOLE LOCATION:")
output.append("  X range: {:.1f} to {:.1f}".format(min(pin_x), max(pin_x)))
output.append("  Y range: {:.1f} to {:.1f}".format(min(pin_y), max(pin_y)))
output.append("  Z range: {:.1f} to {:.1f}".format(min(pin_z), max(pin_z)))
output.append("")

# Calculate center of pin hole
pin_center_y = (min(pin_y) + max(pin_y)) / 2
output.append("  Pin hole center Y: {:.1f} mm".format(pin_center_y))
output.append("")

# Determine if pin hole is in correct region
output.append("=" * 70)
output.append("LOCATION VERIFICATION:")
output.append("=" * 70)
output.append("")

if pin_center_y > 118:
    output.append("  Pin hole Y center ({:.1f}) is in UPPER BLOCK region (Y > 118)".format(pin_center_y))
    output.append("  STATUS: CORRECT - Pin hole is in the TOP SUPPORT")
elif pin_center_y > 28:
    output.append("  Pin hole Y center ({:.1f}) is in NECK/CENTER region (28 < Y < 118)".format(pin_center_y))
    output.append("  STATUS: WRONG - Pin hole is in the CENTER, not the top support!")
else:
    output.append("  Pin hole Y center ({:.1f}) is in LOWER region (Y < 28)".format(pin_center_y))
    output.append("  STATUS: WRONG - Pin hole is at the bottom!")

output.append("")
output.append("=" * 70)

# Also verify lower pin holes
try:
    lower_left_set = odb.rootAssembly.nodeSets['LOWERLEFTPINHOLE']
    ll_nodes = lower_left_set.nodes[0]
    ll_y = [n.coordinates[1] for n in ll_nodes]
    ll_center_y = (min(ll_y) + max(ll_y)) / 2

    lower_right_set = odb.rootAssembly.nodeSets['LOWERRIGHTPINHOLE']
    lr_nodes = lower_right_set.nodes[0]
    lr_y = [n.coordinates[1] for n in lr_nodes]
    lr_center_y = (min(lr_y) + max(lr_y)) / 2

    output.append("")
    output.append("LOWER PIN HOLES:")
    output.append("  Lower Left pin center Y: {:.1f} mm".format(ll_center_y))
    output.append("  Lower Right pin center Y: {:.1f} mm".format(lr_center_y))

    if ll_center_y < 28 and lr_center_y < 28:
        output.append("  STATUS: CORRECT - Both lower pins are in bottom blocks")
    else:
        output.append("  STATUS: CHECK - Lower pins may be mispositioned")
except:
    output.append("  (Could not find lower pin hole sets)")

output.append("")
output.append("=" * 70)

with open('hole_location_verification.txt', 'w') as f:
    f.write('\n'.join(output))

print('\n'.join(output))

odb.close()
