# -*- coding: utf-8 -*-
"""
Experiment 5: Extract optimization convergence history.

Reads per-iteration ODBs from TOSCA_POST and extracts strain energy
and average density at each design cycle. Writes convergence_history.csv.

Can be run at any time during or after optimization.
Run with: abaqus python scripts/monitor_convergence.py
"""

import os
from odbAccess import openOdb
from abaqusConstants import *

try:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    SCRIPT_DIR = os.path.join(os.getcwd(), 'scripts')
PROJECT_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, os.pardir))
os.chdir(PROJECT_DIR)

DENSITY_THRESHOLD = 0.5

print("\n" + "=" * 70)
print("EXPERIMENT 5: CONVERGENCE HISTORY")
print("=" * 70)

# Locate TOSCA_POST
opt_dir = os.path.join(PROJECT_DIR, 'Experiment5_TO', 'TOSCA_POST')
if not os.path.exists(opt_dir):
    opt_dir = os.path.join(PROJECT_DIR, 'TOSCA_POST')
if not os.path.exists(opt_dir):
    print("No TOSCA_POST directory found. Optimization may not have started.")
    raise SystemExit(1)

odb_files = sorted([f for f in os.listdir(opt_dir) if f.endswith('.odb')])
print("Found {} design cycle ODBs\n".format(len(odb_files)))

rows = []
for i, odb_name in enumerate(odb_files):
    odb_path = os.path.join(opt_dir, odb_name)
    try:
        odb = openOdb(path=odb_path, readOnly=True)
        step = odb.steps[odb.steps.keys()[-1]]
        frame = step.frames[-1]

        # Extract total strain energy from ENER field
        strain_energy = 0.0
        if 'ENER' in frame.fieldOutputs:
            for value in frame.fieldOutputs['ENER'].values:
                if hasattr(value, 'data'):
                    strain_energy += value.data
                elif hasattr(value, 'magnitude'):
                    strain_energy += value.magnitude

        # Extract density statistics
        avg_density = 0.0
        solid_fraction = 0.0
        density_field = None
        for field_name in frame.fieldOutputs.keys():
            if 'DENSITY' in field_name.upper() or 'MAT_PROP' in field_name.upper():
                density_field = frame.fieldOutputs[field_name]
                break

        if density_field:
            densities = []
            for value in density_field.values:
                d = value.data if hasattr(value, 'data') else (
                    value.magnitude if hasattr(value, 'magnitude') else 0.0)
                densities.append(d)
            if densities:
                avg_density = sum(densities) / len(densities)
                solid_fraction = sum(
                    1 for d in densities if d >= DENSITY_THRESHOLD) / float(len(densities))

        rows.append({
            'cycle': i + 1,
            'odb': odb_name,
            'strain_energy': strain_energy,
            'avg_density': avg_density,
            'solid_fraction': solid_fraction,
        })
        odb.close()
        print("  Cycle {:3d}: SE={:12.2f}  avg_density={:.4f}  solid={:.1f}%".format(
            i + 1, strain_energy, avg_density, solid_fraction * 100))
    except Exception as e:
        print("  Cycle {:3d}: Error - {}".format(i + 1, str(e)))

# Write convergence CSV
csv_path = os.path.join(PROJECT_DIR, 'convergence_history.csv')
with open(csv_path, 'w') as f:
    f.write('cycle,odb_file,strain_energy,avg_density,solid_fraction\n')
    for row in rows:
        f.write('{},{},{:.6f},{:.6f},{:.6f}\n'.format(
            row['cycle'], row['odb'], row['strain_energy'],
            row['avg_density'], row['solid_fraction']))

print("\nConvergence history written to: convergence_history.csv")

# Print summary
if len(rows) >= 2:
    first = rows[0]
    last = rows[-1]
    if first['strain_energy'] > 0:
        se_change = (last['strain_energy'] - first['strain_energy']) / first['strain_energy'] * 100
        print("Strain energy change: {:.2f} -> {:.2f} ({:+.1f}%)".format(
            first['strain_energy'], last['strain_energy'], se_change))
    print("Avg density change: {:.4f} -> {:.4f}".format(
        first['avg_density'], last['avg_density']))

print("\n" + "=" * 70)
