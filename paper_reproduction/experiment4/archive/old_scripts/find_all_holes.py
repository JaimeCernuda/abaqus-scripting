# -*- coding: utf-8 -*-
"""
Find ALL circular features in the model to check if there are any
unexpected holes besides the three pin holes.
"""
import os
from odbAccess import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')

odb = openOdb('Job_100kN.odb', readOnly=True)
instance = odb.rootAssembly.instances['TO_SPECIMEN-1']

# Get all nodes
nodes = instance.nodes

output = []
output.append("=" * 70)
output.append("SEARCHING FOR ALL CIRCULAR FEATURES / HOLES")
output.append("=" * 70)
output.append("")

# Find all nodes and group by Y position to identify potential hole locations
# Holes would show clusters of nodes at specific Y values forming circles

# Create Y-position histogram
y_positions = {}
for node in nodes:
    y = round(node.coordinates[1], 0)  # Round to nearest mm
    if y not in y_positions:
        y_positions[y] = []
    y_positions[y].append(node.coordinates)

output.append("Node count by Y position:")
for y in sorted(y_positions.keys()):
    count = len(y_positions[y])
    # Circular holes would have many nodes at specific Y values
    marker = ""
    if count > 15:
        marker = " <-- High node count (possible circular feature)"
    output.append("  Y={:6.1f}: {} nodes{}".format(y, count, marker))

output.append("")
output.append("=" * 70)
output.append("ANALYZING POTENTIAL CIRCULAR FEATURES:")
output.append("=" * 70)

# Check specific Y ranges for circular patterns
# Upper pin hole should be at Y ≈ 125.8 to 138.5
# Lower pin holes should be at Y ≈ 7.7 to 20.4
# Any circles in the middle (Y = 28 to 118) would be unexpected

output.append("")
output.append("UPPER REGION (Y = 118 to 146) - Expected: 1 pin hole")
upper_nodes = [n.coordinates for n in nodes if 118 <= n.coordinates[1] <= 146]
if upper_nodes:
    x_range = max(n[0] for n in upper_nodes) - min(n[0] for n in upper_nodes)
    z_range = max(n[2] for n in upper_nodes) - min(n[2] for n in upper_nodes)
    output.append("  Nodes found: {}".format(len(upper_nodes)))
    output.append("  X range: {:.1f} mm".format(x_range))
    output.append("  Z range: {:.1f} mm".format(z_range))

output.append("")
output.append("MIDDLE REGION (Y = 28 to 118) - Expected: NO pin holes")
middle_nodes = [n.coordinates for n in nodes if 28 <= n.coordinates[1] <= 118]
if middle_nodes:
    # Check for circular patterns by looking at X-Z distribution at specific Y levels
    output.append("  Nodes found: {}".format(len(middle_nodes)))

    # Sample some Y levels in the middle region
    for check_y in [40, 50, 60, 70, 80, 90, 100]:
        y_slice = [n for n in middle_nodes if abs(n[1] - check_y) < 3]
        if y_slice:
            x_vals = [n[0] for n in y_slice]
            z_vals = [n[2] for n in y_slice]
            x_range = max(x_vals) - min(x_vals)
            z_range = max(z_vals) - min(z_vals)
            output.append("    Y~{}: {} nodes, X range={:.1f}, Z range={:.1f}".format(
                check_y, len(y_slice), x_range, z_range))

            # Check if this could be a circular hole
            # A Z-direction hole would have nodes spanning full X at constant Z
            # An X-direction hole would have nodes spanning full Z at constant X
            if len(y_slice) > 10 and (x_range < 15 or z_range < 15):
                output.append("      WARNING: Possible circular feature detected!")

output.append("")
output.append("LOWER REGION (Y = 0 to 28) - Expected: 2 pin holes")
lower_nodes = [n.coordinates for n in nodes if 0 <= n.coordinates[1] <= 28]
if lower_nodes:
    output.append("  Nodes found: {}".format(len(lower_nodes)))
    # Separate left and right blocks
    left_nodes = [n for n in lower_nodes if n[0] < 0]
    right_nodes = [n for n in lower_nodes if n[0] > 0]
    output.append("  Left block nodes: {}".format(len(left_nodes)))
    output.append("  Right block nodes: {}".format(len(right_nodes)))

output.append("")
output.append("=" * 70)

with open('all_holes_check.txt', 'w') as f:
    f.write('\n'.join(output))

print('\n'.join(output))

odb.close()
