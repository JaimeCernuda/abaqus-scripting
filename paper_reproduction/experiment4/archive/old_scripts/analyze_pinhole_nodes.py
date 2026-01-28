# -*- coding: utf-8 -*-
"""
Analyze UpperPinHole nodes to determine hole direction definitively
"""
import os
from odbAccess import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')

odb = openOdb('Job_100kN.odb', readOnly=True)
instance = odb.rootAssembly.instances['TO_SPECIMEN-1']

# Get the UpperPinHole node set
upper_pin_set = odb.rootAssembly.nodeSets['UPPERPINHOLE']
nodes = upper_pin_set.nodes[0]  # First (and only) instance's nodes

output = []
output.append("=" * 70)
output.append("DEFINITIVE UPPER PIN HOLE ANALYSIS")
output.append("=" * 70)
output.append("")
output.append("Nodes in UpperPinHole set:")

x_vals = []
y_vals = []
z_vals = []

for node in nodes:
    x, y, z = node.coordinates
    x_vals.append(x)
    y_vals.append(y)
    z_vals.append(z)
    output.append("  Node {}: ({:.2f}, {:.2f}, {:.2f})".format(node.label, x, y, z))

output.append("")
output.append("=" * 70)
output.append("STATISTICAL ANALYSIS:")
output.append("=" * 70)
output.append("")
output.append("X coordinates:")
output.append("  Min: {:.2f}".format(min(x_vals)))
output.append("  Max: {:.2f}".format(max(x_vals)))
output.append("  Span: {:.2f}".format(max(x_vals) - min(x_vals)))
output.append("")
output.append("Y coordinates:")
output.append("  Min: {:.2f}".format(min(y_vals)))
output.append("  Max: {:.2f}".format(max(y_vals)))
output.append("  Span: {:.2f}".format(max(y_vals) - min(y_vals)))
output.append("")
output.append("Z coordinates:")
output.append("  Min: {:.2f}".format(min(z_vals)))
output.append("  Max: {:.2f}".format(max(z_vals)))
output.append("  Span: {:.2f}".format(max(z_vals) - min(z_vals)))

output.append("")
output.append("=" * 70)
output.append("INTERPRETATION:")
output.append("=" * 70)
output.append("")
output.append("Pin hole diameter: 12.7 mm (radius 6.35 mm)")
output.append("Block thickness (Z): 25 mm")
output.append("Block width (X): 18 mm (-9 to +9)")
output.append("")

x_span = max(x_vals) - min(x_vals)
z_span = max(z_vals) - min(z_vals)
y_span = max(y_vals) - min(y_vals)

if x_span > 15 and z_span < 15:
    direction = "X-DIRECTION (horizontal through block width) - CORRECT!"
elif z_span > 20 and x_span < 15:
    direction = "Z-DIRECTION (front-to-back through thickness) - WRONG!"
else:
    direction = "UNCLEAR - need visual inspection"

output.append("X span: {:.2f} mm".format(x_span))
output.append("Z span: {:.2f} mm".format(z_span))
output.append("Y span: {:.2f} mm (should be ~12.7 = pin diameter)".format(y_span))
output.append("")
output.append("CONCLUSION: Hole goes through {}".format(direction))
output.append("")
output.append("Explanation:")
if x_span > 15:
    output.append("- X span ({:.1f} mm) matches block width (18 mm)".format(x_span))
    output.append("- This means nodes span from X=-9 to X=+9")
    output.append("- Therefore hole axis is parallel to X (horizontal)")
if z_span > 20:
    output.append("- Z span ({:.1f} mm) matches block thickness (25 mm)".format(z_span))
    output.append("- This means nodes span from Z=0 to Z=25")
    output.append("- Therefore hole axis is parallel to Z (front-to-back)")

output.append("=" * 70)

# Write to file
with open('pinhole_analysis.txt', 'w') as f:
    f.write('\n'.join(output))

print('\n'.join(output))

odb.close()
