# -*- coding: utf-8 -*-
"""
Verify hole geometry from ODB file (can be opened read-only)
"""
import os
from odbAccess import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')

# Open ODB in read-only mode
odb = openOdb('Job_100kN.odb', readOnly=True)

# Get the instance
instance = odb.rootAssembly.instances['TO_SPECIMEN-1']

# Get nodes and find circular patterns
nodes = instance.nodes

output = []
output.append("=" * 70)
output.append("GEOMETRY VERIFICATION FROM ODB: Job_100kN.odb")
output.append("=" * 70)
output.append("")

# Find nodes near the expected pin hole locations
# Upper pin: Y ~ 132, should have nodes at X=-9 and X=+9 if X-direction hole
# Lower pins: Y ~ 14, should have nodes at X spanning block widths

# Group nodes by approximate Y location
upper_nodes = []  # Y > 100
lower_nodes = []  # Y < 50

for node in nodes:
    coords = node.coordinates
    if coords[1] > 100:  # Y > 100
        upper_nodes.append(coords)
    elif coords[1] < 50:  # Y < 50
        lower_nodes.append(coords)

# Find X range for upper nodes (should indicate hole direction)
if upper_nodes:
    upper_x_vals = [n[0] for n in upper_nodes]
    upper_z_vals = [n[2] for n in upper_nodes]
    output.append("UPPER REGION (Y > 100):")
    output.append("  X range: {:.1f} to {:.1f}".format(min(upper_x_vals), max(upper_x_vals)))
    output.append("  Z range: {:.1f} to {:.1f}".format(min(upper_z_vals), max(upper_z_vals)))

    # Check for pin hole nodes at the circular edges
    # Pin hole at Y~132 should have nodes forming a circle
    pin_y = 132.17
    pin_region_nodes = [n for n in upper_nodes if abs(n[1] - pin_y) < 15]

    if pin_region_nodes:
        pin_x_vals = [n[0] for n in pin_region_nodes]
        pin_z_vals = [n[2] for n in pin_region_nodes]
        output.append("  Pin region nodes (Y near 132):")
        output.append("    X range: {:.1f} to {:.1f} (span: {:.1f})".format(
            min(pin_x_vals), max(pin_x_vals), max(pin_x_vals) - min(pin_x_vals)))
        output.append("    Z range: {:.1f} to {:.1f} (span: {:.1f})".format(
            min(pin_z_vals), max(pin_z_vals), max(pin_z_vals) - min(pin_z_vals)))

output.append("")
output.append("INTERPRETATION:")
output.append("  For X-direction hole: X span should be ~18mm (block width)")
output.append("  For Z-direction hole: Z span should be ~25mm (thickness)")
output.append("")

# Check specific node coordinates for definitive answer
# Look for nodes that form circles at specific X values
output.append("=" * 70)
output.append("CHECKING FOR CIRCULAR HOLE PATTERNS:")
output.append("=" * 70)

# Upper hole should be centered at Y=132.17
# If X-direction: circle nodes at X=-9 and X=+9
# If Z-direction: circle nodes at Z=0 and Z=25

# Find nodes at X ~ -9 and X ~ +9 in upper region
x_minus_9_nodes = [n for n in upper_nodes if abs(n[0] - (-9)) < 1]
x_plus_9_nodes = [n for n in upper_nodes if abs(n[0] - 9) < 1]

output.append("")
output.append("Upper block - Nodes at X ~ -9:")
for n in x_minus_9_nodes[:10]:  # Show first 10
    output.append("  ({:.1f}, {:.1f}, {:.1f})".format(n[0], n[1], n[2]))
output.append("  ... {} total nodes at X~-9".format(len(x_minus_9_nodes)))

output.append("")
output.append("Upper block - Nodes at X ~ +9:")
for n in x_plus_9_nodes[:10]:  # Show first 10
    output.append("  ({:.1f}, {:.1f}, {:.1f})".format(n[0], n[1], n[2]))
output.append("  ... {} total nodes at X~+9".format(len(x_plus_9_nodes)))

# Now check for nodes at Z~0 and Z~25 in upper region (would indicate Z-direction hole)
z_0_nodes = [n for n in upper_nodes if abs(n[2]) < 1]
z_25_nodes = [n for n in upper_nodes if abs(n[2] - 25) < 1]

output.append("")
output.append("Upper block - Nodes at Z ~ 0:")
for n in z_0_nodes[:10]:
    output.append("  ({:.1f}, {:.1f}, {:.1f})".format(n[0], n[1], n[2]))
output.append("  ... {} total nodes at Z~0".format(len(z_0_nodes)))

output.append("")
output.append("Upper block - Nodes at Z ~ 25:")
for n in z_25_nodes[:10]:
    output.append("  ({:.1f}, {:.1f}, {:.1f})".format(n[0], n[1], n[2]))
output.append("  ... {} total nodes at Z~25".format(len(z_25_nodes)))

output.append("")
output.append("=" * 70)
output.append("CONCLUSION:")
# If there are circular patterns of nodes at X=-9 and X=+9, it's an X-direction hole
# If there are circular patterns of nodes at Z=0 and Z=25, it's a Z-direction hole
x_has_circle = len(x_minus_9_nodes) > 5 and len(x_plus_9_nodes) > 5
z_has_circle = len(z_0_nodes) > 5 and len(z_25_nodes) > 5

if x_has_circle and not z_has_circle:
    output.append("Upper hole goes through X-DIRECTION (horizontal) - CORRECT!")
elif z_has_circle and not x_has_circle:
    output.append("Upper hole goes through Z-DIRECTION (front-back) - WRONG!")
elif x_has_circle and z_has_circle:
    output.append("AMBIGUOUS - need more analysis")
else:
    output.append("Could not determine hole direction from node patterns")
output.append("=" * 70)

# Write to file
with open('odb_geometry_check.txt', 'w') as f:
    f.write('\n'.join(output))

print('\n'.join(output))

odb.close()
