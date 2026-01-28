# 06_extract_results.py - EXPERIMENT 3
#
# Extracts results from Job 1 and Job 2, creates summary report.
#
# Run with: abaqus python paper_reproduction/scripts/experiment3/06_extract_results.py

from odbAccess import *
from abaqusConstants import *
import os

print("\n" + "=" * 70)
print("EXPERIMENT 3 - EXTRACT RESULTS")
print("=" * 70)

jobs = [
    ('job1/Exp3_Job1_Vertical', 'Job 1: Vertical Only (20 kN in -Z)'),
    ('job2/Exp3_Job2_Horizontal', 'Job 2: Vertical + Horizontal (20 kN -Z, 5 kN +/-X)'),
]

results = {}

OUTPUT_DIR = 'paper_reproduction/outputs/experiment3/'

for job_path, description in jobs:
    odb_path = OUTPUT_DIR + job_path + '.odb'
    job_name = job_path.split('/')[-1]

    print(f"\n--- {description} ---")

    if not os.path.exists(odb_path):
        print(f"    ODB not found: {odb_path}")
        continue

    odb = openOdb(path=odb_path, readOnly=True)
    step = odb.steps['LoadStep']
    frame = step.frames[-1]

    # Extract stress
    stress_field = frame.fieldOutputs['S']
    max_mises = 0.0
    max_mises_location = None
    for value in stress_field.values:
        if hasattr(value, 'mises') and value.mises > max_mises:
            max_mises = value.mises
            try:
                if value.instance is not None:
                    max_mises_location = (value.instance.name, value.elementLabel)
            except Exception:
                pass

    # Extract displacement
    disp_field = frame.fieldOutputs['U']
    max_disp = 0.0
    max_disp_location = None
    for value in disp_field.values:
        if value.magnitude > max_disp:
            max_disp = value.magnitude
            try:
                if value.instance is not None:
                    max_disp_location = (value.instance.name, value.nodeLabel)
            except Exception:
                pass

    results[job_name] = {
        'mises': max_mises,
        'disp': max_disp,
        'mises_loc': max_mises_location,
        'disp_loc': max_disp_location
    }

    print(f"    Max von Mises stress: {max_mises:.2f} MPa")
    print(f"    Max displacement: {max_disp:.6f} mm")

    odb.close()

# Write individual job results
for job_name in ['Exp3_Job1_Vertical', 'Exp3_Job2_Horizontal']:
    if job_name not in results:
        continue
    r = results[job_name]
    job_num = '1' if 'Job1' in job_name else '2'
    result_file = OUTPUT_DIR + f'job{job_num}_results.txt'
    with open(result_file, 'w') as f:
        f.write(f"EXPERIMENT 3 - JOB {job_num} RESULTS\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Max von Mises stress: {r['mises']:.2f} MPa\n")
        f.write(f"Max displacement: {r['disp']:.6f} mm\n")
    print(f"    Written: {result_file}")

# Write combined summary
summary_path = OUTPUT_DIR + 'SUMMARY.md'
with open(summary_path, 'w') as f:
    f.write("# Experiment 3 Results Summary\n\n")
    f.write("## Coordinate System (Paper-Aligned)\n\n")
    f.write("| Axis | Direction | Usage |\n")
    f.write("|------|-----------|-------|\n")
    f.write("| X | Horizontal | Spreading direction |\n")
    f.write("| Y | Perpendicular | Pin axis / thickness |\n")
    f.write("| Z | Vertical | Loading direction |\n\n")

    f.write("## Load Cases\n\n")
    f.write("### Job 1: Vertical Only\n\n")
    f.write("| Reference Point | Force (N) | Direction |\n")
    f.write("|-----------------|-----------|----------|\n")
    f.write("| RP-1 (Upper) | 20,000 | -Z (down) |\n")
    f.write("| RP-2 (Lower Left) | Fixed | X, Y, Z |\n")
    f.write("| RP-3 (Lower Right) | Fixed | X, Y, Z |\n\n")

    f.write("### Job 2: Vertical + Horizontal Spreading\n\n")
    f.write("| Reference Point | Force (N) | Direction |\n")
    f.write("|-----------------|-----------|----------|\n")
    f.write("| RP-1 (Upper) | 20,000 | -Z (down) |\n")
    f.write("| RP-2 (Lower Left) | 5,000 | -X (outward) |\n")
    f.write("| RP-3 (Lower Right) | 5,000 | +X (outward) |\n\n")

    f.write("## Results\n\n")
    f.write("| Metric | Job 1 (Vertical) | Job 2 (V+H) | Change |\n")
    f.write("|--------|------------------|-------------|--------|\n")

    if 'Exp3_Job1_Vertical' in results and 'Exp3_Job2_Horizontal' in results:
        j1 = results['Exp3_Job1_Vertical']
        j2 = results['Exp3_Job2_Horizontal']

        stress_change = (j2['mises'] - j1['mises']) / j1['mises'] * 100 if j1['mises'] > 0 else 0
        disp_change = (j2['disp'] - j1['disp']) / j1['disp'] * 100 if j1['disp'] > 0 else 0

        f.write(f"| Max von Mises (MPa) | {j1['mises']:.2f} | {j2['mises']:.2f} | {stress_change:+.1f}% |\n")
        f.write(f"| Max Displacement (mm) | {j1['disp']:.6f} | {j2['disp']:.6f} | {disp_change:+.1f}% |\n\n")

        f.write("## Analysis\n\n")
        f.write(f"- **Stress change**: The horizontal spreading forces {'increase' if stress_change > 0 else 'decrease'} ")
        f.write(f"max stress by {abs(stress_change):.1f}%\n")
        f.write(f"- **Displacement change**: Adding horizontal loads {'increases' if disp_change > 0 else 'decreases'} ")
        f.write(f"max displacement by {abs(disp_change):.1f}%\n")
        f.write("- Stress concentration expected at upper pin hole where vertical load is applied\n")
    else:
        f.write("| Max von Mises (MPa) | - | - | - |\n")
        f.write("| Max Displacement (mm) | - | - | - |\n\n")
        f.write("*Some job results not available*\n")

print(f"\nSummary written: {summary_path}")

print("\n" + "=" * 70)
print("EXPERIMENT 3 - RESULTS EXTRACTED")
print("=" * 70)
