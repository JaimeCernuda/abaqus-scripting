# -*- coding: utf-8 -*-
"""
CRITICAL hole verification - check node coordinates around each pin hole.
For X-direction holes: X span should be ~18mm (hole length), Y and Z span ~12.7mm (diameter)
For Z-direction holes: Z span should be ~25mm (thickness), X and Y span ~12.7mm (diameter)
"""
import os
from odbAccess import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')

odb = openOdb('Job_100kN.odb', readOnly=True)
instance = odb.rootAssembly.instances['TO_SPECIMEN-1']
nodes = instance.nodes

output = []
output.append("=" * 70)
output.append("CRITICAL PIN HOLE VERIFICATION")
output.append("=" * 70)
output.append("")

# Define expected hole locations
# Upper hole: Y ~ 132, should be at X ~ 0 (center)
# Lower left: Y ~ 14, X ~ -23 (center of left block)
# Lower right: Y ~ 14, X ~ +23 (center of right block)

hole_regions = [
    ("UPPER", 125, 140, -15, 15),      # Y range, X range for upper
    ("LOWER_LEFT", 7, 21, -35, -10),   # Y range, X range for lower left
    ("LOWER_RIGHT", 7, 21, 10, 35),    # Y range, X range for lower right
]

for name, y_min, y_max, x_min, x_max in hole_regions:
    output.append("=" * 50)
    output.append("CHECKING {} HOLE REGION".format(name))
    output.append("  Y range: {} to {}".format(y_min, y_max))
    output.append("  X range: {} to {}".format(x_min, x_max))
    output.append("=" * 50)

    # Find nodes in this region
    region_nodes = []
    for node in nodes:
        x, y, z = node.coordinates
        if y_min <= y <= y_max and x_min <= x <= x_max:
            region_nodes.append((x, y, z))

    if region_nodes:
        x_vals = [n[0] for n in region_nodes]
        y_vals = [n[1] for n in region_nodes]
        z_vals = [n[2] for n in region_nodes]

        x_span = max(x_vals) - min(x_vals)
        y_span = max(y_vals) - min(y_vals)
        z_span = max(z_vals) - min(z_vals)

        output.append("  Nodes found: {}".format(len(region_nodes)))
        output.append("  X range: {:.2f} to {:.2f} (span: {:.2f} mm)".format(min(x_vals), max(x_vals), x_span))
        output.append("  Y range: {:.2f} to {:.2f} (span: {:.2f} mm)".format(min(y_vals), max(y_vals), y_span))
        output.append("  Z range: {:.2f} to {:.2f} (span: {:.2f} mm)".format(min(z_vals), max(z_vals), z_span))

        output.append("")
        output.append("  ANALYSIS:")

        # For X-direction hole: X span ~ 18mm (block width), Z span ~ 12.7mm (pin diameter)
        # For Z-direction hole: Z span ~ 25mm (thickness), X span ~ 12.7mm (pin diameter)

        if x_span > 15 and z_span < 15:
            output.append("    X span ({:.1f}mm) > Z span ({:.1f}mm)".format(x_span, z_span))
            output.append("    VERDICT: X-DIRECTION HOLE (CORRECT)")
        elif z_span > 20 and x_span < 15:
            output.append("    Z span ({:.1f}mm) > X span ({:.1f}mm)".format(z_span, x_span))
            output.append("    VERDICT: Z-DIRECTION HOLE (WRONG!)")
        else:
            output.append("    X span: {:.1f}mm, Z span: {:.1f}mm".format(x_span, z_span))
            output.append("    VERDICT: UNCLEAR - needs visual inspection")
    else:
        output.append("  WARNING: No nodes found in this region!")

    output.append("")

# Overall verdict
output.append("=" * 70)
output.append("OVERALL VERDICT:")
output.append("=" * 70)

odb.close()

result_text = '\n'.join(output)
print(result_text)

with open('critical_hole_check.txt', 'w') as f:
    f.write(result_text)
