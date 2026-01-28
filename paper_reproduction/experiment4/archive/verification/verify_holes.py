# -*- coding: utf-8 -*-
"""
Verify hole orientations by examining circular edge positions
"""
import os
from abaqus import *
from abaqusConstants import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')
openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v19.cae')

model = mdb.models['Experiment4_TO_Specimen']
part = model.parts['TO_Specimen']

PIN_RADIUS = 6.35

output = []
output.append("=" * 60)
output.append("HOLE ORIENTATION VERIFICATION")
output.append("=" * 60)
output.append("")
output.append("For X-direction holes (correct):")
output.append("  - Circular edges at DIFFERENT X values (front/back of block)")
output.append("  - Circular edges at SAME Z values (within the hole)")
output.append("")
output.append("For Z-direction holes (WRONG):")
output.append("  - Circular edges at SAME X values")
output.append("  - Circular edges at DIFFERENT Z values (front/back)")
output.append("")
output.append("=" * 60)

# Find all circular edges with pin radius
circular_edges = []
for i, edge in enumerate(part.edges):
    try:
        radius = edge.getRadius()
        if radius is not None and abs(radius - PIN_RADIUS) < 0.5:
            pt = edge.pointOn[0]
            # Get all vertices to determine the plane of the circle
            verts = edge.getVertices()
            circular_edges.append({
                'index': i,
                'x': pt[0],
                'y': pt[1],
                'z': pt[2],
                'radius': radius
            })
    except:
        pass

output.append("Found {} circular edges with radius ~{:.2f} mm".format(len(circular_edges), PIN_RADIUS))
output.append("")

# Group edges by Y position (to identify which hole they belong to)
# Upper hole: Y ~ 132
# Lower holes: Y ~ 14
upper_edges = [e for e in circular_edges if e['y'] > 100]
lower_edges = [e for e in circular_edges if e['y'] < 50]

output.append("UPPER HOLE EDGES (Y > 100):")
for e in upper_edges:
    output.append("  Edge {} at X={:.1f}, Y={:.1f}, Z={:.1f}".format(
        e['index'], e['x'], e['y'], e['z']))

if len(upper_edges) >= 2:
    x_vals = [e['x'] for e in upper_edges]
    z_vals = [e['z'] for e in upper_edges]
    x_span = max(x_vals) - min(x_vals)
    z_span = max(z_vals) - min(z_vals)
    output.append("  X span: {:.1f} mm, Z span: {:.1f} mm".format(x_span, z_span))
    if x_span > 5 and z_span < 5:
        output.append("  --> CORRECT: Hole goes through X-direction (horizontal)")
    elif z_span > 5 and x_span < 5:
        output.append("  --> WRONG: Hole goes through Z-direction (vertical)")
    else:
        output.append("  --> UNCLEAR: Need more investigation")

output.append("")
output.append("LOWER HOLE EDGES (Y < 50):")
for e in lower_edges:
    output.append("  Edge {} at X={:.1f}, Y={:.1f}, Z={:.1f}".format(
        e['index'], e['x'], e['y'], e['z']))

# Group lower edges by X position to separate left and right holes
lower_left = [e for e in lower_edges if e['x'] < 0]
lower_right = [e for e in lower_edges if e['x'] > 0]

output.append("")
output.append("  Lower LEFT hole edges:")
for e in lower_left:
    output.append("    X={:.1f}, Y={:.1f}, Z={:.1f}".format(e['x'], e['y'], e['z']))
if len(lower_left) >= 2:
    x_vals = [e['x'] for e in lower_left]
    z_vals = [e['z'] for e in lower_left]
    x_span = max(x_vals) - min(x_vals)
    z_span = max(z_vals) - min(z_vals)
    output.append("    X span: {:.1f} mm, Z span: {:.1f} mm".format(x_span, z_span))
    if x_span > 5:
        output.append("    --> CORRECT: X-direction hole")
    elif z_span > 5:
        output.append("    --> WRONG: Z-direction hole")

output.append("")
output.append("  Lower RIGHT hole edges:")
for e in lower_right:
    output.append("    X={:.1f}, Y={:.1f}, Z={:.1f}".format(e['x'], e['y'], e['z']))
if len(lower_right) >= 2:
    x_vals = [e['x'] for e in lower_right]
    z_vals = [e['z'] for e in lower_right]
    x_span = max(x_vals) - min(x_vals)
    z_span = max(z_vals) - min(z_vals)
    output.append("    X span: {:.1f} mm, Z span: {:.1f} mm".format(x_span, z_span))
    if x_span > 5:
        output.append("    --> CORRECT: X-direction hole")
    elif z_span > 5:
        output.append("    --> WRONG: Z-direction hole")

output.append("")
output.append("=" * 60)
output.append("CONCLUSION:")
# Check all holes
all_correct = True
# Upper
if len(upper_edges) >= 2:
    x_vals = [e['x'] for e in upper_edges]
    x_span = max(x_vals) - min(x_vals)
    if x_span < 5:
        all_correct = False
        output.append("  UPPER HOLE: WRONG DIRECTION")
    else:
        output.append("  UPPER HOLE: Correct (X-direction)")
else:
    all_correct = False
    output.append("  UPPER HOLE: MISSING")

# Lower left
if len(lower_left) >= 2:
    x_vals = [e['x'] for e in lower_left]
    x_span = max(x_vals) - min(x_vals)
    if x_span < 5:
        all_correct = False
        output.append("  LOWER LEFT: WRONG DIRECTION")
    else:
        output.append("  LOWER LEFT: Correct (X-direction)")
else:
    all_correct = False
    output.append("  LOWER LEFT: MISSING")

# Lower right
if len(lower_right) >= 2:
    x_vals = [e['x'] for e in lower_right]
    x_span = max(x_vals) - min(x_vals)
    if x_span < 5:
        all_correct = False
        output.append("  LOWER RIGHT: WRONG DIRECTION")
    else:
        output.append("  LOWER RIGHT: Correct (X-direction)")
else:
    all_correct = False
    output.append("  LOWER RIGHT: MISSING")

output.append("")
if all_correct:
    output.append("*** ALL HOLES CORRECTLY ORIENTED IN X-DIRECTION ***")
else:
    output.append("*** HOLES NEED FIXING ***")
output.append("=" * 60)

# Write to file
with open('hole_verification.txt', 'w') as f:
    f.write('\n'.join(output))

print('\n'.join(output))
