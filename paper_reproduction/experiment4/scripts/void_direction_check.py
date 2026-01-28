# -*- coding: utf-8 -*-
"""
DEFINITIVE void direction check.
If there's an X-direction hole: material is MISSING along a cylinder axis in X
If there's a Z-direction hole: material is MISSING along a cylinder axis in Z

Test: Look for nodes at the hole CENTER location. If no nodes exist there, there's a void.
"""
import os
from odbAccess import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')

odb = openOdb('Job_100kN.odb', readOnly=True)
instance = odb.rootAssembly.instances['TO_SPECIMEN-1']
nodes = instance.nodes

output = []
output.append("=" * 70)
output.append("DEFINITIVE VOID DIRECTION CHECK")
output.append("=" * 70)
output.append("")

# Upper hole - check for void at expected locations
UPPER_Y = 132.17
HALF_THICK = 12.5  # Z center
PIN_RADIUS = 6.35

output.append("UPPER HOLE CHECK:")
output.append("-" * 50)

# If X-direction hole: void runs from X=-9 to X=+9 at (Y=132.17, Z=12.5)
# Test: Are there nodes at X=0, Y=132.17, Z=12.5? (center of hole)
# If X-direction hole: NO nodes should be at X=0, Y=132, Z=12.5 (inside the void)

output.append("")
output.append("Test 1: Check for void at X=0, Y=132, Z=12.5 (X-dir hole center)")
center_x_nodes = []
for node in nodes:
    x, y, z = node.coordinates
    if abs(x) < 2 and abs(y - UPPER_Y) < 2 and abs(z - HALF_THICK) < 2:
        center_x_nodes.append((x, y, z))

if center_x_nodes:
    output.append("  Found {} nodes near X=0, Y=132, Z=12.5".format(len(center_x_nodes)))
    for n in center_x_nodes[:5]:
        output.append("    Node at ({:.2f}, {:.2f}, {:.2f})".format(n[0], n[1], n[2]))
    output.append("  ==> Material EXISTS here - NO X-direction hole through center")
else:
    output.append("  NO nodes found near X=0, Y=132, Z=12.5")
    output.append("  ==> VOID EXISTS here - CONFIRMS X-direction hole")

# If Z-direction hole: void runs from Z=0 to Z=25 at (X=0, Y=132.17)
# Test: Are there nodes at X=0, Y=132.17, Z=5? (inside a Z-dir hole)
output.append("")
output.append("Test 2: Check for void at X=0, Y=132, Z=5 (Z-dir hole interior)")
center_z_nodes = []
for node in nodes:
    x, y, z = node.coordinates
    if abs(x) < 2 and abs(y - UPPER_Y) < 2 and abs(z - 5) < 2:
        center_z_nodes.append((x, y, z))

if center_z_nodes:
    output.append("  Found {} nodes near X=0, Y=132, Z=5".format(len(center_z_nodes)))
    for n in center_z_nodes[:5]:
        output.append("    Node at ({:.2f}, {:.2f}, {:.2f})".format(n[0], n[1], n[2]))
    output.append("  ==> Material EXISTS here - NO Z-direction hole")
else:
    output.append("  NO nodes found near X=0, Y=132, Z=5")
    output.append("  ==> VOID EXISTS here - Would indicate Z-direction hole")

# Additional check: nodes at Z=12.5 (mid-thickness) along the X centerline
output.append("")
output.append("Test 3: Scan along X axis at Y=132, Z=12.5")
x_scan_nodes = []
for node in nodes:
    x, y, z = node.coordinates
    if abs(y - UPPER_Y) < 2 and abs(z - HALF_THICK) < 2:
        x_scan_nodes.append((x, y, z))

if x_scan_nodes:
    x_vals = sorted(set([round(n[0], 1) for n in x_scan_nodes]))
    output.append("  Found nodes at X positions: {}".format(x_vals[:20]))

    # Check for gap in X values (would indicate X-direction hole)
    if len(x_vals) > 2:
        gaps = []
        for i in range(len(x_vals)-1):
            gap = x_vals[i+1] - x_vals[i]
            if gap > 5:
                gaps.append((x_vals[i], x_vals[i+1], gap))
        if gaps:
            output.append("  GAPS found in X direction:")
            for g in gaps:
                output.append("    Gap from X={:.1f} to X={:.1f} (size: {:.1f}mm)".format(g[0], g[1], g[2]))
            output.append("  ==> CONFIRMS void (hole) runs through X direction")
else:
    output.append("  No nodes found at Y=132, Z=12.5")

output.append("")
output.append("=" * 70)
output.append("FINAL VERDICT:")
output.append("=" * 70)

odb.close()

result_text = '\n'.join(output)
print(result_text)

with open('void_direction_check.txt', 'w') as f:
    f.write(result_text)
