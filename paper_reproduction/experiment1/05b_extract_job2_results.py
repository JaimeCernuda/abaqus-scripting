# 05b_extract_job2_results.py
#
# Extracts results from Job 2 (TO design loads with horizontal forces)
#
# Run with: abaqus python paper_reproduction/scripts/05b_extract_job2_results.py
#
# Prerequisites: Run 03b_setup_job2_horizontal.py first

from odbAccess import *
from abaqusConstants import *
import os

print("\n" + "=" * 70)
print("EXPERIMENT 1 - JOB 2: EXTRACT RESULTS")
print("=" * 70)

# =============================================================================
# PARAMETERS
# =============================================================================

JOB_NAME = 'TO_Bracket_Job2_Horizontal'
ODB_PATH = JOB_NAME + '.odb'
STEP_NAME = 'FatigueLoad'

# Load values
F_VERTICAL = 20000.0    # N
F_HORIZONTAL = 5000.0   # N

# Paper reference
PAPER_DESIGN_STRESS = 800.0  # MPa

print("\nJob 2 Parameters:")
print(f"  ODB file: {ODB_PATH}")
print(f"  Loads: {F_VERTICAL/1000:.0f} kN vertical + {F_HORIZONTAL/1000:.0f} kN horizontal")

# =============================================================================
# CHECK ODB EXISTS
# =============================================================================

print("\n[1/5] Checking for ODB file...")

if not os.path.exists(ODB_PATH):
    print(f"       ERROR: ODB file not found: {ODB_PATH}")
    print(f"       Run 03b_setup_job2_horizontal.py first")
    raise FileNotFoundError(f"ODB file not found: {ODB_PATH}")

print(f"       ODB file found")

# =============================================================================
# OPEN ODB
# =============================================================================

print("\n[2/5] Opening ODB file...")

odb = openOdb(path=ODB_PATH, readOnly=True)
step = odb.steps[STEP_NAME]
last_frame = step.frames[-1]

print(f"       Step: {STEP_NAME}")
print(f"       Frame: {last_frame.frameId}")

# =============================================================================
# EXTRACT STRESS
# =============================================================================

print("\n[3/5] Extracting stress field...")

stress_field = last_frame.fieldOutputs['S']

max_mises = 0.0
max_mises_element = None
min_mises = float('inf')
mises_values = []

for value in stress_field.values:
    if hasattr(value, 'mises'):
        mises = value.mises
        mises_values.append(mises)
        if mises > max_mises:
            max_mises = mises
            max_mises_element = value.elementLabel
        if mises < min_mises:
            min_mises = mises

if len(mises_values) > 0:
    total = 0.0
    for v in mises_values:
        total += float(v)
    avg_mises = total / len(mises_values)
else:
    avg_mises = 0.0

print(f"       Von Mises stress:")
print(f"         Maximum: {max_mises:.2f} MPa (Element {max_mises_element})")
print(f"         Minimum: {min_mises:.2f} MPa")
print(f"         Average: {avg_mises:.2f} MPa")

# =============================================================================
# EXTRACT DISPLACEMENT
# =============================================================================

print("\n[4/5] Extracting displacement field...")

disp_field = last_frame.fieldOutputs['U']

max_disp = 0.0
max_disp_node = None
max_disp_components = (0.0, 0.0, 0.0)

for value in disp_field.values:
    if value.magnitude > max_disp:
        max_disp = value.magnitude
        max_disp_node = value.nodeLabel
        max_disp_components = tuple(value.data)

print(f"       Maximum displacement: {max_disp:.4f} mm (Node {max_disp_node})")
print(f"         U1={max_disp_components[0]:.4f}, U2={max_disp_components[1]:.4f}, U3={max_disp_components[2]:.4f}")

# =============================================================================
# EXTRACT REACTIONS
# =============================================================================

print("\n[5/5] Extracting reaction forces...")

rf_field = last_frame.fieldOutputs['RF']
total_rf = [0.0, 0.0, 0.0]

for value in rf_field.values:
    for i in range(3):
        if abs(value.data[i]) > 1e-10:
            total_rf[i] += value.data[i]

print(f"       Total reactions:")
print(f"         RF1 (X): {total_rf[0]:.2f} N")
print(f"         RF2 (Y): {total_rf[1]:.2f} N")
print(f"         RF3 (Z): {total_rf[2]:.2f} N")

# =============================================================================
# WRITE REPORT
# =============================================================================

report_path = 'paper_reproduction/outputs/experiment1/job2_results.txt'

with open(report_path, 'w') as f:
    f.write("=" * 70 + "\n")
    f.write("EXPERIMENT 1 - JOB 2 RESULTS\n")
    f.write("TO Design Load Case (with horizontal forces)\n")
    f.write("=" * 70 + "\n\n")

    f.write("LOAD CASE\n")
    f.write("-" * 70 + "\n")
    f.write(f"Vertical (upper pin): {F_VERTICAL/1000:.0f} kN downward\n")
    f.write(f"Horizontal (lower left): {F_HORIZONTAL/1000:.0f} kN in -X\n")
    f.write(f"Horizontal (lower right): {F_HORIZONTAL/1000:.0f} kN in +X\n\n")

    f.write("STRESS RESULTS\n")
    f.write("-" * 70 + "\n")
    f.write(f"Max von Mises: {max_mises:.2f} MPa (Element {max_mises_element})\n")
    f.write(f"Min von Mises: {min_mises:.2f} MPa\n")
    f.write(f"Avg von Mises: {avg_mises:.2f} MPa\n\n")

    f.write("DISPLACEMENT RESULTS\n")
    f.write("-" * 70 + "\n")
    f.write(f"Max displacement: {max_disp:.4f} mm (Node {max_disp_node})\n")
    f.write(f"  U1: {max_disp_components[0]:.4f} mm\n")
    f.write(f"  U2: {max_disp_components[1]:.4f} mm\n")
    f.write(f"  U3: {max_disp_components[2]:.4f} mm\n\n")

    f.write("REACTION FORCES\n")
    f.write("-" * 70 + "\n")
    f.write(f"RF1 (X): {total_rf[0]:.2f} N\n")
    f.write(f"RF2 (Y): {total_rf[1]:.2f} N\n")
    f.write(f"RF3 (Z): {total_rf[2]:.2f} N\n\n")

    f.write("COMPARISON WITH JOB 1 (vertical only)\n")
    f.write("-" * 70 + "\n")
    f.write("Job 1 had only vertical load (20 kN)\n")
    f.write("Job 2 adds horizontal spreading forces (±5 kN)\n")
    f.write("Expected: Higher stress due to combined loading\n")

print(f"\nReport written to: {report_path}")

odb.close()

# =============================================================================
# SUMMARY
# =============================================================================

print("\n" + "=" * 70)
print("JOB 2 RESULTS EXTRACTED")
print("=" * 70)
print(f"""
Key Results:
  - Max von Mises: {max_mises:.2f} MPa
  - Max displacement: {max_disp:.4f} mm
  - Design constraint: {PAPER_DESIGN_STRESS} MPa
  - Ratio: {max_mises/PAPER_DESIGN_STRESS:.2f}x

Output: {report_path}
""")
