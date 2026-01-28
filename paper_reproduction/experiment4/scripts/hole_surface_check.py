# -*- coding: utf-8 -*-
"""
Check nodes on the actual hole surfaces to determine orientation.
For X-direction hole: surface nodes form a cylinder along X axis
For Z-direction hole: surface nodes form a cylinder along Z axis
"""
import os
import math
from odbAccess import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')

odb = openOdb('Job_100kN.odb', readOnly=True)
instance = odb.rootAssembly.instances['TO_SPECIMEN-1']
nodes = instance.nodes

PIN_RADIUS = 6.35  # mm
THICKNESS = 25.0
HALF_THICK = 12.5

output = []
output.append("=" * 70)
output.append("HOLE SURFACE NODE ANALYSIS")
output.append("=" * 70)
output.append("")

# Upper hole expected center: Y=132.17
# If X-direction: centerline runs along X, surface at radius from (Y=132.17, Z=12.5)
# If Z-direction: centerline runs along Z, surface at radius from (Y=132.17, X=0)

UPPER_Y = 132.17

# Find nodes near the expected hole surface for X-direction assumption
output.append("UPPER HOLE - Testing X-direction assumption:")
output.append("  Centerline: along X axis at Y=132.17, Z=12.5")
output.append("  Looking for surface nodes at radius ~6.35mm from this line")
output.append("")

x_dir_nodes = []
for node in nodes:
    x, y, z = node.coordinates
    # Distance from centerline (Y=132.17, Z=12.5)
    dist = math.sqrt((y - UPPER_Y)**2 + (z - HALF_THICK)**2)
    if 5.5 < dist < 7.5:  # Within tolerance of pin radius
        x_dir_nodes.append((x, y, z, dist))

if x_dir_nodes:
    x_vals = [n[0] for n in x_dir_nodes]
    output.append("  Found {} nodes on cylindrical surface".format(len(x_dir_nodes)))
    output.append("  X range: {:.2f} to {:.2f} (span: {:.2f} mm)".format(
        min(x_vals), max(x_vals), max(x_vals) - min(x_vals)))
    if max(x_vals) - min(x_vals) > 15:
        output.append("  ==> X span > 15mm: CONFIRMS X-DIRECTION HOLE")
else:
    output.append("  No surface nodes found for X-direction assumption")

output.append("")
output.append("UPPER HOLE - Testing Z-direction assumption:")
output.append("  Centerline: along Z axis at Y=132.17, X=0")
output.append("  Looking for surface nodes at radius ~6.35mm from this line")
output.append("")

z_dir_nodes = []
for node in nodes:
    x, y, z = node.coordinates
    # Distance from centerline (Y=132.17, X=0)
    dist = math.sqrt((y - UPPER_Y)**2 + x**2)
    if 5.5 < dist < 7.5:  # Within tolerance of pin radius
        z_dir_nodes.append((x, y, z, dist))

if z_dir_nodes:
    z_vals = [n[2] for n in z_dir_nodes]
    output.append("  Found {} nodes on cylindrical surface".format(len(z_dir_nodes)))
    output.append("  Z range: {:.2f} to {:.2f} (span: {:.2f} mm)".format(
        min(z_vals), max(z_vals), max(z_vals) - min(z_vals)))
    if max(z_vals) - min(z_vals) > 20:
        output.append("  ==> Z span > 20mm: Would indicate Z-DIRECTION HOLE")
else:
    output.append("  No surface nodes found for Z-direction assumption")

output.append("")
output.append("=" * 70)
output.append("CONCLUSION:")
output.append("=" * 70)

if x_dir_nodes and len(x_dir_nodes) > 10:
    x_span = max(n[0] for n in x_dir_nodes) - min(n[0] for n in x_dir_nodes)
    if x_span > 15:
        output.append("UPPER HOLE IS X-DIRECTION (span = {:.1f}mm through thickness)".format(x_span))
    else:
        output.append("UPPER HOLE orientation unclear (X span = {:.1f}mm)".format(x_span))
else:
    output.append("Could not determine upper hole orientation")

output.append("")

# Check lower holes similarly
LOWER_Y = 14.0
LOWER_LEFT_X = -23.3
LOWER_RIGHT_X = 23.3

for name, center_x in [("LOWER LEFT", LOWER_LEFT_X), ("LOWER RIGHT", LOWER_RIGHT_X)]:
    output.append("")
    output.append("{} HOLE - Testing X-direction:".format(name))
    hole_nodes = []
    for node in nodes:
        x, y, z = node.coordinates
        # For X-direction hole centered at (Y=14, Z=12.5), surface at radius from that line
        # But X should be within the block range
        if name == "LOWER LEFT":
            if x < -10:  # Left block
                dist = math.sqrt((y - LOWER_Y)**2 + (z - HALF_THICK)**2)
                if 5.5 < dist < 7.5:
                    hole_nodes.append((x, y, z))
        else:
            if x > 10:  # Right block
                dist = math.sqrt((y - LOWER_Y)**2 + (z - HALF_THICK)**2)
                if 5.5 < dist < 7.5:
                    hole_nodes.append((x, y, z))

    if hole_nodes:
        x_vals = [n[0] for n in hole_nodes]
        x_span = max(x_vals) - min(x_vals)
        output.append("  Found {} surface nodes, X span: {:.1f}mm".format(len(hole_nodes), x_span))
        if x_span > 15:
            output.append("  ==> CONFIRMS X-DIRECTION HOLE")
    else:
        output.append("  No surface nodes found")

odb.close()

result_text = '\n'.join(output)
print(result_text)

with open('hole_surface_check.txt', 'w') as f:
    f.write(result_text)
