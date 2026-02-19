# -*- coding: utf-8 -*-
"""
Experiment 5: Validate optimized design against all 3 load cases.

After topology optimization, re-runs the optimized geometry under
20/60/100 kN loads and compares stress/displacement vs Experiment 4 baseline.
"""

import os
from odbAccess import *
from abaqusConstants import *

try:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    SCRIPT_DIR = os.path.join(os.getcwd(), 'scripts')
PROJECT_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, os.pardir))
os.chdir(PROJECT_DIR)

# Experiment 4 directory for baseline comparison
EXP4_DIR = os.path.normpath(os.path.join(PROJECT_DIR, os.pardir, 'experiment4'))

print("\n" + "=" * 70)
print("EXPERIMENT 5: VALIDATION - OPTIMIZED vs BASELINE")
print("=" * 70)

output = []
output.append("=" * 70)
output.append("EXPERIMENT 5 - VALIDATION RESULTS")
output.append("=" * 70)
output.append("")

# =============================================================================
# EXTRACT BASELINE RESULTS (Experiment 4)
# =============================================================================
print("\n[1/3] Reading Experiment 4 baseline results...")

baseline = {}
exp4_jobs = [
    ('Job_20kN.odb', '20 kN'),
    ('Job_60kN.odb', '60 kN'),
    ('Job_100kN.odb', '100 kN'),
]

for odb_name, load_label in exp4_jobs:
    odb_path = os.path.join(EXP4_DIR, odb_name)
    if not os.path.exists(odb_path):
        print("  WARNING: {} not found, skipping baseline".format(odb_name))
        baseline[load_label] = None
        continue

    odb = openOdb(odb_path, readOnly=True)
    step = odb.steps.values()[-1]
    frame = step.frames[-1]

    max_mises = 0.0
    for value in frame.fieldOutputs['S'].values:
        if value.mises > max_mises:
            max_mises = value.mises

    max_disp = 0.0
    for value in frame.fieldOutputs['U'].values:
        mag = (value.data[0]**2 + value.data[1]**2 + value.data[2]**2)**0.5
        if mag > max_disp:
            max_disp = mag

    max_peeq = 0.0
    if 'PEEQ' in frame.fieldOutputs:
        for value in frame.fieldOutputs['PEEQ'].values:
            if value.data > max_peeq:
                max_peeq = value.data

    baseline[load_label] = {
        'stress': max_mises,
        'disp': max_disp,
        'peeq': max_peeq,
    }
    odb.close()
    print("  {} baseline: {:.1f} MPa, {:.4f} mm disp".format(
        load_label, max_mises, max_disp))

output.append("BASELINE (Experiment 4 - full geometry):")
for load_label in ['20 kN', '60 kN', '100 kN']:
    if baseline.get(load_label):
        b = baseline[load_label]
        output.append("  {}: Stress={:.1f} MPa, Disp={:.4f} mm, PEEQ={:.6f}".format(
            load_label, b['stress'], b['disp'], b['peeq']))
    else:
        output.append("  {}: Not available".format(load_label))
output.append("")

# =============================================================================
# EXTRACT OPTIMIZED RESULTS (Experiment 5 validation jobs)
# =============================================================================
print("\n[2/3] Reading optimized validation results...")

optimized = {}
exp5_jobs = [
    ('Validation_20kN.odb', '20 kN'),
    ('Validation_60kN.odb', '60 kN'),
    ('Validation_100kN.odb', '100 kN'),
]

for odb_name, load_label in exp5_jobs:
    odb_path = os.path.join(PROJECT_DIR, odb_name)
    if not os.path.exists(odb_path):
        print("  WARNING: {} not found, skipping".format(odb_name))
        optimized[load_label] = None
        continue

    odb = openOdb(odb_path, readOnly=True)
    step = odb.steps.values()[-1]
    frame = step.frames[-1]

    max_mises = 0.0
    for value in frame.fieldOutputs['S'].values:
        if value.mises > max_mises:
            max_mises = value.mises

    max_disp = 0.0
    for value in frame.fieldOutputs['U'].values:
        mag = (value.data[0]**2 + value.data[1]**2 + value.data[2]**2)**0.5
        if mag > max_disp:
            max_disp = mag

    max_peeq = 0.0
    if 'PEEQ' in frame.fieldOutputs:
        for value in frame.fieldOutputs['PEEQ'].values:
            if value.data > max_peeq:
                max_peeq = value.data

    optimized[load_label] = {
        'stress': max_mises,
        'disp': max_disp,
        'peeq': max_peeq,
    }
    odb.close()
    print("  {} optimized: {:.1f} MPa, {:.4f} mm disp".format(
        load_label, max_mises, max_disp))

output.append("OPTIMIZED (Experiment 5 - TO result):")
for load_label in ['20 kN', '60 kN', '100 kN']:
    if optimized.get(load_label):
        o = optimized[load_label]
        output.append("  {}: Stress={:.1f} MPa, Disp={:.4f} mm, PEEQ={:.6f}".format(
            load_label, o['stress'], o['disp'], o['peeq']))
    else:
        output.append("  {}: Not available".format(load_label))
output.append("")

# =============================================================================
# COMPARISON
# =============================================================================
print("\n[3/3] Comparing results...")

output.append("=" * 70)
output.append("COMPARISON (Optimized vs Baseline):")
output.append("=" * 70)
output.append("")
output.append("{:<10} {:<20} {:<20} {:<15}".format(
    "Load", "Stress (MPa)", "Displacement (mm)", "PEEQ"))
output.append("{:<10} {:<10} {:<10} {:<10} {:<10} {:<15}".format(
    "", "Base", "Opt", "Base", "Opt", "Change"))
output.append("-" * 70)

for load_label in ['20 kN', '60 kN', '100 kN']:
    b = baseline.get(load_label)
    o = optimized.get(load_label)
    if b and o:
        stress_change = ((o['stress'] - b['stress']) / b['stress'] * 100) if b['stress'] > 0 else 0
        disp_change = ((o['disp'] - b['disp']) / b['disp'] * 100) if b['disp'] > 0 else 0
        output.append("{:<10} {:<10.1f} {:<10.1f} {:<10.4f} {:<10.4f} S:{:+.1f}% D:{:+.1f}%".format(
            load_label, b['stress'], o['stress'], b['disp'], o['disp'],
            stress_change, disp_change))
    else:
        output.append("{:<10} Incomplete data".format(load_label))

output.append("")
output.append("=" * 70)
output.append("VALIDATION COMPLETE")
output.append("=" * 70)

result_text = '\n'.join(output)
print(result_text)

with open(os.path.join(PROJECT_DIR, 'validation_results.txt'), 'w') as f:
    f.write(result_text)

# Write CSV
with open(os.path.join(PROJECT_DIR, 'validation_comparison.csv'), 'w') as f:
    f.write('load_kn,baseline_stress_mpa,optimized_stress_mpa,stress_change_pct,')
    f.write('baseline_disp_mm,optimized_disp_mm,disp_change_pct\n')
    for load_label, load_kn in [('20 kN', 20), ('60 kN', 60), ('100 kN', 100)]:
        b = baseline.get(load_label)
        o = optimized.get(load_label)
        if b and o:
            sc = ((o['stress'] - b['stress']) / b['stress'] * 100) if b['stress'] > 0 else 0
            dc = ((o['disp'] - b['disp']) / b['disp'] * 100) if b['disp'] > 0 else 0
            f.write('{},{:.2f},{:.2f},{:.2f},{:.4f},{:.4f},{:.2f}\n'.format(
                load_kn, b['stress'], o['stress'], sc, b['disp'], o['disp'], dc))
