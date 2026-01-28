# 06_extract_results.py - EXPERIMENT 2
#
# Extracts results from both Job 1 and Job 2
#
# Run with: abaqus python paper_reproduction/scripts/experiment2/06_extract_results.py

from odbAccess import *
from abaqusConstants import *
import os

print("\n" + "=" * 70)
print("EXPERIMENT 2 - EXTRACT RESULTS")
print("=" * 70)

jobs = [
    ('Exp2_Job1_Vertical', 'Job 1: Vertical Only'),
    ('Exp2_Job2_Horizontal', 'Job 2: Vertical + Horizontal'),
]

results = {}

OUTPUT_DIR = 'paper_reproduction/outputs/experiment2/'

for job_name, description in jobs:
    odb_path = OUTPUT_DIR + job_name + '.odb'

    print(f"\n--- {description} ---")

    if not os.path.exists(odb_path):
        print(f"    ODB not found: {odb_path}")
        continue

    odb = openOdb(path=odb_path, readOnly=True)
    step = odb.steps['LoadStep']
    frame = step.frames[-1]

    # Stress
    stress_field = frame.fieldOutputs['S']
    max_mises = 0.0
    for value in stress_field.values:
        if hasattr(value, 'mises') and value.mises > max_mises:
            max_mises = value.mises

    # Displacement
    disp_field = frame.fieldOutputs['U']
    max_disp = 0.0
    for value in disp_field.values:
        if value.magnitude > max_disp:
            max_disp = value.magnitude

    results[job_name] = {'mises': max_mises, 'disp': max_disp}

    print(f"    Max von Mises: {max_mises:.2f} MPa")
    print(f"    Max displacement: {max_disp:.4f} mm")

    odb.close()

# Write summary
report_path = 'paper_reproduction/outputs/experiment2/results_summary.txt'
with open(report_path, 'w') as f:
    f.write("=" * 70 + "\n")
    f.write("EXPERIMENT 2 RESULTS SUMMARY\n")
    f.write("(Correct hole orientation - pins through Y axis)\n")
    f.write("=" * 70 + "\n\n")

    for job_name, desc in jobs:
        if job_name in results:
            r = results[job_name]
            f.write(f"{desc}\n")
            f.write(f"  Max von Mises: {r['mises']:.2f} MPa\n")
            f.write(f"  Max displacement: {r['disp']:.4f} mm\n\n")

    if len(results) == 2:
        j1 = results['Exp2_Job1_Vertical']
        j2 = results['Exp2_Job2_Horizontal']
        stress_increase = (j2['mises'] - j1['mises']) / j1['mises'] * 100
        disp_increase = (j2['disp'] - j1['disp']) / j1['disp'] * 100

        f.write("-" * 70 + "\n")
        f.write("COMPARISON\n")
        f.write("-" * 70 + "\n")
        f.write(f"Stress increase (Job1 to Job2): {stress_increase:.1f}%\n")
        f.write(f"Displacement increase: {disp_increase:.1f}%\n")

print(f"\nReport written: {report_path}")
print("\n" + "=" * 70)
print("EXPERIMENT 2 - RESULTS EXTRACTED")
print("=" * 70)
