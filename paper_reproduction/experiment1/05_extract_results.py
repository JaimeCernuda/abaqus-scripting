# 05_extract_results.py
#
# Extracts and analyzes results from the TO bracket simulation:
# - Reads ODB file
# - Extracts von Mises stress distribution
# - Finds maximum stress location (compare to paper's Location 3)
# - Extracts displacement field
# - Generates stress report
#
# Run with: abaqus python paper_reproduction/scripts/05_extract_results.py
#
# Prerequisites: Run 04_mesh_and_run.py and wait for job completion

from odbAccess import *
from abaqusConstants import *
import os

print("\n" + "=" * 70)
print("PAPER REPRODUCTION - STEP 5: EXTRACT RESULTS")
print("=" * 70)

# =============================================================================
# PARAMETERS
# =============================================================================

JOB_NAME = 'TO_Bracket_Fatigue'
ODB_PATH = JOB_NAME + '.odb'  # ODB is created in current working directory
STEP_NAME = 'FatigueLoad'

# Load value for stress normalization
APPLIED_LOAD = 20000.0  # N (20 kN)

# Paper reference values
PAPER_DESIGN_STRESS = 800.0  # MPa (TO design constraint)

print("\nAnalysis Parameters:")
print(f"  ODB file: {ODB_PATH}")
print(f"  Step: {STEP_NAME}")
print(f"  Applied load: {APPLIED_LOAD/1000:.0f} kN")

# =============================================================================
# CHECK ODB EXISTS
# =============================================================================

print("\n[1/6] Checking for ODB file...")

if not os.path.exists(ODB_PATH):
    print(f"       ERROR: ODB file not found: {ODB_PATH}")
    print(f"       Make sure 04_mesh_and_run.py completed successfully")
    print(f"       Or run manually: abaqus job={JOB_NAME} interactive")
    raise FileNotFoundError(f"ODB file not found: {ODB_PATH}")

print(f"       ODB file found")

# =============================================================================
# OPEN ODB
# =============================================================================

print("\n[2/6] Opening ODB file...")

odb = openOdb(path=ODB_PATH, readOnly=True)

# Get step and frame
step = odb.steps[STEP_NAME]
last_frame = step.frames[-1]

print(f"       Step: {STEP_NAME}")
print(f"       Frame: {last_frame.frameId} (increment {last_frame.incrementNumber})")
print(f"       Time: {last_frame.frameValue}")

# =============================================================================
# EXTRACT STRESS FIELD
# =============================================================================

print("\n[3/6] Extracting stress field...")

stress_field = last_frame.fieldOutputs['S']

# Get von Mises stress values
max_mises = 0.0
max_mises_element = None
max_mises_position = None
min_mises = float('inf')

# Statistics
mises_values = []

for value in stress_field.values:
    if hasattr(value, 'mises'):
        mises = value.mises
        mises_values.append(mises)

        if mises > max_mises:
            max_mises = mises
            max_mises_element = value.elementLabel
            if hasattr(value, 'position'):
                max_mises_position = value.position

        if mises < min_mises:
            min_mises = mises

# Calculate statistics
if len(mises_values) > 0:
    # Manual sum to avoid type issues with Abaqus arrays
    total = 0.0
    for v in mises_values:
        total += float(v)
    avg_mises = total / len(mises_values)
    mises_values_sorted = sorted([float(v) for v in mises_values])
    median_mises = mises_values_sorted[len(mises_values_sorted) // 2]
else:
    avg_mises = 0.0
    median_mises = 0.0

print(f"       Von Mises stress statistics:")
print(f"         Maximum: {max_mises:.2f} MPa (Element {max_mises_element})")
print(f"         Minimum: {min_mises:.2f} MPa")
print(f"         Average: {avg_mises:.2f} MPa")
print(f"         Median:  {median_mises:.2f} MPa")

# =============================================================================
# EXTRACT PRINCIPAL STRESSES
# =============================================================================

print("\n[4/6] Extracting principal stresses...")

# Get max principal stress at the location of max von Mises
max_principal = 0.0
min_principal = 0.0

for value in stress_field.values:
    if value.elementLabel == max_mises_element:
        if hasattr(value, 'maxPrincipal'):
            max_principal = value.maxPrincipal
        if hasattr(value, 'minPrincipal'):
            min_principal = value.minPrincipal
        break

print(f"       At max von Mises location (Element {max_mises_element}):")
print(f"         Max principal: {max_principal:.2f} MPa")
print(f"         Min principal: {min_principal:.2f} MPa")

# =============================================================================
# EXTRACT DISPLACEMENT FIELD
# =============================================================================

print("\n[5/6] Extracting displacement field...")

disp_field = last_frame.fieldOutputs['U']

max_disp_magnitude = 0.0
max_disp_node = None
max_disp_components = (0.0, 0.0, 0.0)

for value in disp_field.values:
    if value.magnitude > max_disp_magnitude:
        max_disp_magnitude = value.magnitude
        max_disp_node = value.nodeLabel
        max_disp_components = tuple(value.data)

print(f"       Maximum displacement: {max_disp_magnitude:.4f} mm")
print(f"         Node: {max_disp_node}")
print(f"         Components: U1={max_disp_components[0]:.4f}, U2={max_disp_components[1]:.4f}, U3={max_disp_components[2]:.4f} mm")

# =============================================================================
# EXTRACT REACTION FORCES
# =============================================================================

print("\n[6/6] Extracting reaction forces...")

rf_field = last_frame.fieldOutputs['RF']

total_rf = [0.0, 0.0, 0.0]

for value in rf_field.values:
    for i in range(3):
        if abs(value.data[i]) > 1e-10:
            total_rf[i] += value.data[i]

print(f"       Total reaction forces:")
print(f"         RF1 (X): {total_rf[0]:.2f} N")
print(f"         RF2 (Y): {total_rf[1]:.2f} N")
print(f"         RF3 (Z): {total_rf[2]:.2f} N")

# Check equilibrium
equilibrium_error = abs(total_rf[1] + APPLIED_LOAD) / APPLIED_LOAD * 100
print(f"       Equilibrium check (Y): {equilibrium_error:.2f}% error")

# =============================================================================
# COMPARISON WITH PAPER
# =============================================================================

print("\n" + "-" * 70)
print("COMPARISON WITH PAPER")
print("-" * 70)

print(f"""
Paper Design Criteria:
  - TO stress constraint: {PAPER_DESIGN_STRESS} MPa (von Mises)
  - Failure location: Inner face of lower legs (Location 3)

Simulation Results:
  - Maximum von Mises: {max_mises:.2f} MPa
  - At element: {max_mises_element}
  - Ratio to design stress: {max_mises/PAPER_DESIGN_STRESS:.2f}x

Interpretation:
""")

if max_mises < PAPER_DESIGN_STRESS:
    print(f"  - Stress is BELOW design constraint")
    print(f"  - Structure has margin: {(PAPER_DESIGN_STRESS - max_mises)/PAPER_DESIGN_STRESS*100:.1f}% reserve")
elif max_mises < 1.2 * PAPER_DESIGN_STRESS:
    print(f"  - Stress is NEAR design constraint")
    print(f"  - Exceeds constraint by: {(max_mises - PAPER_DESIGN_STRESS)/PAPER_DESIGN_STRESS*100:.1f}%")
else:
    print(f"  - Stress EXCEEDS design constraint significantly")
    print(f"  - May indicate high stress concentration")

# =============================================================================
# WRITE REPORT FILE
# =============================================================================

report_path = 'paper_reproduction/outputs/experiment1/job1_results.txt'

with open(report_path, 'w') as f:
    f.write("=" * 70 + "\n")
    f.write("TO BRACKET ANALYSIS RESULTS REPORT\n")
    f.write("=" * 70 + "\n\n")

    f.write("Job: {}\n".format(JOB_NAME))
    f.write("Applied Load: {:.0f} kN (vertical)\n\n".format(APPLIED_LOAD / 1000))

    f.write("-" * 70 + "\n")
    f.write("STRESS RESULTS\n")
    f.write("-" * 70 + "\n")
    f.write("Von Mises Stress:\n")
    f.write("  Maximum: {:.2f} MPa (Element {})\n".format(max_mises, max_mises_element))
    f.write("  Minimum: {:.2f} MPa\n".format(min_mises))
    f.write("  Average: {:.2f} MPa\n".format(avg_mises))
    f.write("  Median:  {:.2f} MPa\n\n".format(median_mises))

    f.write("Principal Stresses at Max Von Mises Location:\n")
    f.write("  Max Principal: {:.2f} MPa\n".format(max_principal))
    f.write("  Min Principal: {:.2f} MPa\n\n".format(min_principal))

    f.write("-" * 70 + "\n")
    f.write("DISPLACEMENT RESULTS\n")
    f.write("-" * 70 + "\n")
    f.write("Maximum Displacement: {:.4f} mm (Node {})\n".format(max_disp_magnitude, max_disp_node))
    f.write("  U1: {:.4f} mm\n".format(max_disp_components[0]))
    f.write("  U2: {:.4f} mm\n".format(max_disp_components[1]))
    f.write("  U3: {:.4f} mm\n\n".format(max_disp_components[2]))

    f.write("-" * 70 + "\n")
    f.write("REACTION FORCES\n")
    f.write("-" * 70 + "\n")
    f.write("Total Reactions:\n")
    f.write("  RF1 (X): {:.2f} N\n".format(total_rf[0]))
    f.write("  RF2 (Y): {:.2f} N\n".format(total_rf[1]))
    f.write("  RF3 (Z): {:.2f} N\n".format(total_rf[2]))
    f.write("Equilibrium Error (Y): {:.2f}%\n\n".format(equilibrium_error))

    f.write("-" * 70 + "\n")
    f.write("COMPARISON WITH PAPER\n")
    f.write("-" * 70 + "\n")
    f.write("Paper Design Constraint: {:.0f} MPa\n".format(PAPER_DESIGN_STRESS))
    f.write("Simulation Max Stress:   {:.2f} MPa\n".format(max_mises))
    f.write("Ratio: {:.2f}x\n".format(max_mises / PAPER_DESIGN_STRESS))

print(f"\nReport written to: {report_path}")

# =============================================================================
# CLOSE ODB
# =============================================================================

odb.close()

# =============================================================================
# SUMMARY
# =============================================================================

print("\n" + "=" * 70)
print("STEP 5 COMPLETE - RESULTS EXTRACTED")
print("=" * 70)
print(
    f"""
Output files:
  - paper_reproduction/outputs/experiment1/job1_results.txt

Key Results:
  - Max von Mises stress: {max_mises:.2f} MPa (Element {max_mises_element})
  - Max displacement: {max_disp_magnitude:.4f} mm (Node {max_disp_node})
  - Reaction force (Y): {total_rf[1]:.2f} N
  - Equilibrium error: {equilibrium_error:.2f}%

Comparison with Paper:
  - Design constraint: {PAPER_DESIGN_STRESS} MPa
  - Ratio: {max_mises/PAPER_DESIGN_STRESS:.2f}x

To visualize results in Abaqus/CAE:
  abaqus cae database={ODB_PATH}

Workflow complete!
"""
)
