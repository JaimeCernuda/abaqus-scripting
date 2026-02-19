# -*- coding: utf-8 -*-
"""
Flatten an Abaqus assembly-format .inp file into a flat (no-assembly) format
that Tosca can read directly.

Transforms:
  - Removes *Part / *End Part wrappers (keeps contents)
  - Removes *Assembly / *Instance / *End Instance / *End Assembly wrappers
  - Removes assembly-level reference point node (not part of the mesh)
  - Strips 'instance=XXX' from *Nset, *Elset, *Surface definitions
  - Keeps material, BC, step, and load sections unchanged
  - Renames element set names that reference internal surface sets

Usage: python3 scripts/flatten_inp.py
  Reads:  Experiment5_FEA.inp
  Writes: Experiment5_FEA_flat.inp
"""

import os
import re

try:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    SCRIPT_DIR = os.path.join(os.getcwd(), 'scripts')
PROJECT_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, os.pardir))

inp_path = os.path.join(PROJECT_DIR, 'Experiment5_FEA.inp')
out_path = os.path.join(PROJECT_DIR, 'Experiment5_FEA_flat.inp')

with open(inp_path, 'r') as f:
    lines = f.readlines()

output = []
skip_until_keyword = False
in_assembly_node = False  # Track assembly-level *Node block (reference point)
instance_name = None

i = 0
while i < len(lines):
    line = lines[i]
    stripped = line.strip().upper()

    # Skip *Part line (keep everything inside the part)
    if stripped.startswith('*PART,') or stripped == '*PART':
        i += 1
        continue

    # Skip *End Part
    if stripped == '*END PART':
        i += 1
        continue

    # Skip *Assembly line
    if stripped.startswith('*ASSEMBLY,') or stripped == '*ASSEMBLY':
        i += 1
        continue

    # Capture instance name, skip the line itself
    if stripped.startswith('*INSTANCE,'):
        # Extract instance name for stripping from set definitions
        match = re.search(r'name=(\S+)', line, re.IGNORECASE)
        if match:
            instance_name = match.group(1).rstrip(',')
        i += 1
        continue

    # Skip *End Instance
    if stripped == '*END INSTANCE':
        i += 1
        continue

    # Skip *End Assembly
    if stripped == '*END ASSEMBLY':
        i += 1
        continue

    # Assembly-level *Node block (reference point, not mesh nodes) — skip it
    # This appears after *End Instance in the assembly section, before *Nset
    # We detect it by checking if we're past the part section and see *Node
    # The reference point is used by *Coupling which we'll keep
    if stripped.startswith('*NODE') and not stripped.startswith('*NODE OUTPUT'):
        # Check if this is the assembly-level RP node (only 1-2 nodes)
        # vs the part-level node block (thousands of nodes)
        # Peek ahead to count data lines
        j = i + 1
        count = 0
        while j < len(lines) and not lines[j].strip().startswith('*'):
            count += 1
            j += 1
        if count <= 5:
            # Small node block — this is the assembly reference point, skip it
            i = j
            continue
        # Otherwise it's the real mesh node block, keep it

    # Strip 'instance=XXX' from *Nset, *Elset, *Surface definitions
    if instance_name and stripped.startswith(('*NSET,', '*ELSET,', '*SURFACE,')):
        # Remove instance=XXX (case insensitive)
        line = re.sub(
            r',\s*instance=' + re.escape(instance_name),
            '', line, flags=re.IGNORECASE)

    # Strip instance name from *Coupling ref node surface references
    if instance_name and stripped.startswith('*COUPLING,'):
        line = re.sub(
            r',\s*instance=' + re.escape(instance_name),
            '', line, flags=re.IGNORECASE)

    # Write the line
    output.append(line)
    i += 1

with open(out_path, 'w') as f:
    f.writelines(output)

print("Flattened: {} -> {}".format(inp_path, out_path))
print("  Input lines:  {}".format(len(lines)))
print("  Output lines: {}".format(len(output)))
