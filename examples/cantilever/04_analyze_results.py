# 04_analyze_results.py
#
# STEP 4: Analyze Results from ODB
#
# This script reads the output database (ODB) and extracts:
# - Displacement field
# - Stress field
# - Reaction forces
# - Creates a summary report
#
# Purpose: Demonstrate post-processing of FEA results.
#
# Run with: abaqus python 04_analyze_results.py
#   or:     abaqus python 04_analyze_results.py path/to/results.odb
#
# Note: This uses 'abaqus python', not 'abaqus cae', since it only
#       accesses the ODB API and doesn't need the CAE GUI.

from __future__ import print_function
import sys
import os

# Import Abaqus ODB API
from odbAccess import *
from abaqusConstants import *

print("\n" + "="*60)
print("STEP 4: ANALYZE RESULTS")
print("="*60)

# =============================================================================
# GET ODB PATH
# =============================================================================

# Default ODB name
DEFAULT_ODB = 'files/CantileverBeam.odb'

# Check command line arguments
if len(sys.argv) > 1:
    odb_path = sys.argv[1]
else:
    odb_path = DEFAULT_ODB

# Check if file exists
if not os.path.exists(odb_path):
    print(f"\nERROR: ODB file not found: {odb_path}")
    print(f"\nUsage: abaqus python 04_analyze_results.py [odb_file]")
    print(f"       Default: {DEFAULT_ODB}")
    sys.exit(1)

print(f"\n  Opening: {odb_path}")

# =============================================================================
# OPEN ODB
# =============================================================================

odb = openOdb(path=odb_path, readOnly=True)

print(f"  ✓ ODB opened successfully")
print(f"")
print(f"  Model: {odb.name}")
print(f"  Description: {odb.description}")

# =============================================================================
# LIST AVAILABLE DATA
# =============================================================================

print("\n" + "-"*60)
print("AVAILABLE DATA IN ODB")
print("-"*60)

print(f"\n  Steps: {list(odb.steps.keys())}")

for step_name, step in odb.steps.items():
    print(f"\n  Step '{step_name}':")
    print(f"    - Frames: {len(step.frames)}")
    print(f"    - Time: {step.totalTime}")
    
    if len(step.frames) > 0:
        last_frame = step.frames[-1]
        print(f"    - Field outputs: {list(last_frame.fieldOutputs.keys())}")
        
        if len(step.historyRegions) > 0:
            print(f"    - History regions: {len(step.historyRegions)}")

# =============================================================================
# GET LAST FRAME OF ANALYSIS
# =============================================================================

# Get the last step (usually the load step)
step_name = list(odb.steps.keys())[-1]
step = odb.steps[step_name]
frame = step.frames[-1]

print(f"\n  Analyzing: Step '{step_name}', Frame {frame.frameId}")

# =============================================================================
# DISPLACEMENT ANALYSIS
# =============================================================================

print("\n" + "-"*60)
print("DISPLACEMENT ANALYSIS")
print("-"*60)

if 'U' in frame.fieldOutputs:
    disp_field = frame.fieldOutputs['U']
    
    # Initialize statistics
    max_ux = max_uy = max_uz = max_mag = float('-inf')
    min_ux = min_uy = min_uz = float('inf')
    max_mag_node = None
    
    # Process all values
    for value in disp_field.values:
        ux, uy, uz = value.data[0], value.data[1], value.data[2]
        mag = value.magnitude
        
        max_ux = max(max_ux, ux)
        max_uy = max(max_uy, uy)
        max_uz = max(max_uz, uz)
        min_ux = min(min_ux, ux)
        min_uy = min(min_uy, uy)
        min_uz = min(min_uz, uz)
        
        if mag > max_mag:
            max_mag = mag
            max_mag_node = value.nodeLabel
    
    print(f"\n  Displacement components:")
    print(f"    U1 (X): {min_ux:.6e} to {max_ux:.6e} mm")
    print(f"    U2 (Y): {min_uy:.6e} to {max_uy:.6e} mm")
    print(f"    U3 (Z): {min_uz:.6e} to {max_uz:.6e} mm")
    print(f"")
    print(f"  Maximum displacement magnitude: {max_mag:.6e} mm")
    print(f"  Location: Node {max_mag_node}")
    
else:
    print("  WARNING: No displacement field (U) found in ODB")

# =============================================================================
# STRESS ANALYSIS
# =============================================================================

print("\n" + "-"*60)
print("STRESS ANALYSIS")
print("-"*60)

if 'S' in frame.fieldOutputs:
    stress_field = frame.fieldOutputs['S']
    
    # Initialize statistics
    max_mises = 0.0
    max_mises_elem = None
    max_s11 = max_s22 = max_s33 = float('-inf')
    min_s11 = min_s22 = min_s33 = float('inf')
    
    # Process all values
    for value in stress_field.values:
        # Get Mises stress if available
        if hasattr(value, 'mises'):
            if value.mises > max_mises:
                max_mises = value.mises
                max_mises_elem = value.elementLabel
        
        # Get stress components
        s11 = value.data[0]  # S11
        s22 = value.data[1]  # S22
        s33 = value.data[2]  # S33
        
        max_s11 = max(max_s11, s11)
        max_s22 = max(max_s22, s22)
        max_s33 = max(max_s33, s33)
        min_s11 = min(min_s11, s11)
        min_s22 = min(min_s22, s22)
        min_s33 = min(min_s33, s33)
    
    print(f"\n  Stress components (normal):")
    print(f"    S11 (X): {min_s11:.2f} to {max_s11:.2f} MPa")
    print(f"    S22 (Y): {min_s22:.2f} to {max_s22:.2f} MPa")
    print(f"    S33 (Z): {min_s33:.2f} to {max_s33:.2f} MPa")
    print(f"")
    print(f"  Maximum von Mises stress: {max_mises:.2f} MPa")
    print(f"  Location: Element {max_mises_elem}")
    
else:
    print("  WARNING: No stress field (S) found in ODB")

# =============================================================================
# REACTION FORCE ANALYSIS
# =============================================================================

print("\n" + "-"*60)
print("REACTION FORCE ANALYSIS")
print("-"*60)

if 'RF' in frame.fieldOutputs:
    rf_field = frame.fieldOutputs['RF']
    
    # Sum reaction forces
    total_rf = [0.0, 0.0, 0.0]
    num_nodes_with_rf = 0
    
    for value in rf_field.values:
        rf1, rf2, rf3 = value.data[0], value.data[1], value.data[2]
        if abs(rf1) > 1e-10 or abs(rf2) > 1e-10 or abs(rf3) > 1e-10:
            total_rf[0] += rf1
            total_rf[1] += rf2
            total_rf[2] += rf3
            num_nodes_with_rf += 1
    
    print(f"\n  Nodes with reactions: {num_nodes_with_rf}")
    print(f"")
    print(f"  Total reaction forces:")
    print(f"    RF1 (X): {total_rf[0]:.2f} N")
    print(f"    RF2 (Y): {total_rf[1]:.2f} N")
    print(f"    RF3 (Z): {total_rf[2]:.2f} N")
    print(f"")
    print(f"  Resultant: {(total_rf[0]**2 + total_rf[1]**2 + total_rf[2]**2)**0.5:.2f} N")
    
else:
    print("  WARNING: No reaction force field (RF) found in ODB")

# =============================================================================
# STRAIN ENERGY (if available)
# =============================================================================

print("\n" + "-"*60)
print("ENERGY ANALYSIS")
print("-"*60)

if 'ELSE' in frame.fieldOutputs:
    energy_field = frame.fieldOutputs['ELSE']  # Element strain energy
    total_energy = 0.0
    for value in energy_field.values:
        total_energy += value.data
    print(f"\n  Total strain energy: {total_energy:.6e} mJ")
elif 'ENER' in frame.fieldOutputs:
    print("\n  Energy density available in 'ENER' field")
else:
    print("\n  No strain energy output found")

# =============================================================================
# MESH INFORMATION
# =============================================================================

print("\n" + "-"*60)
print("MESH INFORMATION")
print("-"*60)

# Get instance info
instance = odb.rootAssembly.instances[list(odb.rootAssembly.instances.keys())[0]]

num_nodes = len(instance.nodes)
num_elements = len(instance.elements)

print(f"\n  Instance: {instance.name}")
print(f"  Nodes: {num_nodes}")
print(f"  Elements: {num_elements}")

# Element types
elem_types = {}
for elem in instance.elements:
    etype = elem.type
    elem_types[etype] = elem_types.get(etype, 0) + 1

print(f"\n  Element types:")
for etype, count in elem_types.items():
    print(f"    {etype}: {count}")

# =============================================================================
# CLOSE ODB
# =============================================================================

odb.close()

# =============================================================================
# SUMMARY REPORT
# =============================================================================

print("\n" + "="*60)
print("ANALYSIS SUMMARY")
print("="*60)

print(f"""
File: {odb_path}

RESULTS:
  Max displacement: {max_mag:.6e} mm (Node {max_mag_node})
  Max von Mises stress: {max_mises:.2f} MPa (Element {max_mises_elem})
  Reaction force (Y): {total_rf[1]:.2f} N

MESH:
  Nodes: {num_nodes}
  Elements: {num_elements}
""")

# =============================================================================
# OPTIONAL: WRITE RESULTS TO FILE
# =============================================================================

report_file = odb_path.replace('.odb', '_report.txt')

with open(report_file, 'w') as f:
    f.write("="*60 + "\n")
    f.write("FEA RESULTS REPORT\n")
    f.write("="*60 + "\n\n")
    f.write(f"Source: {odb_path}\n\n")
    f.write("DISPLACEMENTS\n")
    f.write(f"  Max magnitude: {max_mag:.6e} mm\n")
    f.write(f"  Location: Node {max_mag_node}\n\n")
    f.write("STRESSES\n")
    f.write(f"  Max von Mises: {max_mises:.2f} MPa\n")
    f.write(f"  Location: Element {max_mises_elem}\n\n")
    f.write("REACTIONS\n")
    f.write(f"  RF1 (X): {total_rf[0]:.2f} N\n")
    f.write(f"  RF2 (Y): {total_rf[1]:.2f} N\n")
    f.write(f"  RF3 (Z): {total_rf[2]:.2f} N\n\n")
    f.write("MESH\n")
    f.write(f"  Nodes: {num_nodes}\n")
    f.write(f"  Elements: {num_elements}\n")

print(f"Report written to: {report_file}")

print("\n" + "="*60)
print("STEP 4 COMPLETE")
print("="*60)
