# -*- coding: utf-8 -*-
"""
Experiment 5: Extract topology optimization results.

Reads the optimization ODB, extracts density field at final iteration,
reports convergence history, and exports summary CSV.
"""

import os
from odbAccess import *
from abaqusConstants import *

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, os.pardir))
os.chdir(PROJECT_DIR)

DENSITY_THRESHOLD = 0.4

print("\n" + "=" * 70)
print("EXPERIMENT 5: EXTRACT OPTIMIZATION RESULTS")
print("=" * 70)

# =============================================================================
# FIND OPTIMIZATION OUTPUT
# =============================================================================
print("\n[1/4] Locating optimization results...")

opt_dir = os.path.join(PROJECT_DIR, 'Experiment5_TO', 'TOSCA_POST')
if not os.path.exists(opt_dir):
    # Try alternate location
    opt_dir = os.path.join(PROJECT_DIR, 'TOSCA_POST')

if not os.path.exists(opt_dir):
    print("ERROR: Optimization output directory not found")
    print("  Checked: Experiment5_TO/TOSCA_POST/")
    print("  Checked: TOSCA_POST/")
    print("  Make sure optimization has completed before running this script")
    raise SystemExit(1)

odb_files = sorted([f for f in os.listdir(opt_dir) if f.endswith('.odb')])
if not odb_files:
    print("ERROR: No ODB files found in {}".format(opt_dir))
    raise SystemExit(1)

final_odb_path = os.path.join(opt_dir, odb_files[-1])
print("  Found {} ODB files".format(len(odb_files)))
print("  Using final: {}".format(odb_files[-1]))

# =============================================================================
# READ DENSITY FIELD
# =============================================================================
print("\n[2/4] Reading density field...")

odb = openOdb(path=final_odb_path, readOnly=True)

step = odb.steps[odb.steps.keys()[-1]]
frame = step.frames[-1]

print("  Step: {}".format(step.name))
print("  Frame: {} (time: {})".format(frame.frameId, frame.frameValue))

# Find density field
density_field = None
for field_name in frame.fieldOutputs.keys():
    upper_name = field_name.upper()
    if 'DENSITY' in upper_name or 'MAT_PROP' in upper_name:
        density_field = frame.fieldOutputs[field_name]
        print("  Density field: {}".format(field_name))
        break

if density_field is None:
    print("  WARNING: No density field found")
    print("  Available fields: {}".format(list(frame.fieldOutputs.keys())))

# =============================================================================
# ANALYZE DENSITY DISTRIBUTION
# =============================================================================
print("\n[3/4] Analyzing density distribution...")

if density_field:
    densities = []
    for value in density_field.values:
        if hasattr(value, 'data'):
            densities.append(value.data)
        elif hasattr(value, 'magnitude'):
            densities.append(value.magnitude)
        else:
            densities.append(0.0)

    min_d = min(densities)
    max_d = max(densities)
    avg_d = sum(densities) / len(densities)
    solid_count = sum(1 for d in densities if d >= DENSITY_THRESHOLD)
    void_count = len(densities) - solid_count

    print("  Total elements: {}".format(len(densities)))
    print("  Density range: {:.3f} - {:.3f}".format(min_d, max_d))
    print("  Average density: {:.3f}".format(avg_d))
    print("  Solid (>= {:.1f}): {} ({:.1f}%)".format(
        DENSITY_THRESHOLD, solid_count, 100.0 * solid_count / len(densities)))
    print("  Void  (<  {:.1f}): {} ({:.1f}%)".format(
        DENSITY_THRESHOLD, void_count, 100.0 * void_count / len(densities)))

# =============================================================================
# CONVERGENCE HISTORY
# =============================================================================
print("\n[4/4] Writing summary...")

# Check for stress/displacement in final frame
max_mises = 0.0
max_disp = 0.0
if 'S' in frame.fieldOutputs:
    for value in frame.fieldOutputs['S'].values:
        if value.mises > max_mises:
            max_mises = value.mises
if 'U' in frame.fieldOutputs:
    for value in frame.fieldOutputs['U'].values:
        mag = (value.data[0]**2 + value.data[1]**2 + value.data[2]**2)**0.5
        if mag > max_disp:
            max_disp = mag

odb.close()

# Write summary CSV
csv_path = os.path.join(PROJECT_DIR, 'optimization_summary.csv')
with open(csv_path, 'w') as f:
    f.write('metric,value\n')
    if density_field:
        f.write('total_elements,{}\n'.format(len(densities)))
        f.write('density_threshold,{}\n'.format(DENSITY_THRESHOLD))
        f.write('solid_elements,{}\n'.format(solid_count))
        f.write('void_elements,{}\n'.format(void_count))
        f.write('solid_fraction,{:.4f}\n'.format(float(solid_count) / len(densities)))
        f.write('min_density,{:.4f}\n'.format(min_d))
        f.write('max_density,{:.4f}\n'.format(max_d))
        f.write('avg_density,{:.4f}\n'.format(avg_d))
    f.write('max_von_mises_mpa,{:.2f}\n'.format(max_mises))
    f.write('max_displacement_mm,{:.4f}\n'.format(max_disp))
    f.write('num_odb_files,{}\n'.format(len(odb_files)))

# Write text report
report_path = os.path.join(PROJECT_DIR, 'optimization_report.txt')
with open(report_path, 'w') as f:
    f.write("=" * 70 + "\n")
    f.write("EXPERIMENT 5 - TOPOLOGY OPTIMIZATION RESULTS\n")
    f.write("=" * 70 + "\n\n")
    f.write("Final ODB: {}\n".format(odb_files[-1]))
    f.write("Design cycles completed: {}\n\n".format(len(odb_files)))
    if density_field:
        f.write("Density Distribution:\n")
        f.write("  Elements: {}\n".format(len(densities)))
        f.write("  Density range: {:.3f} - {:.3f}\n".format(min_d, max_d))
        f.write("  Average: {:.3f}\n".format(avg_d))
        f.write("  Solid (>= {:.1f}): {} ({:.1f}%)\n".format(
            DENSITY_THRESHOLD, solid_count, 100.0 * solid_count / len(densities)))
        f.write("  Void:  {} ({:.1f}%)\n\n".format(
            void_count, 100.0 * void_count / len(densities)))
    f.write("Structural Response:\n")
    f.write("  Max von Mises: {:.2f} MPa\n".format(max_mises))
    f.write("  Max displacement: {:.4f} mm\n".format(max_disp))

print("\n  Summary written to: optimization_summary.csv")
print("  Report written to: optimization_report.txt")
print("\n" + "=" * 70)
print("Results extraction complete")
print("=" * 70)
