# -*- coding: utf-8 -*-
"""
Experiment 4: Extract Results from All ODB Files
"""

from odbAccess import *
import os

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')

print("="*70)
print("EXPERIMENT 4 - COMPREHENSIVE RESULTS EXTRACTION")
print("="*70)

# List of jobs to analyze
job_files = [
    ('Experiment4_Job1.odb', 'Job 1: FatigueTest 20kN'),
    ('Experiment4_Job2.odb', 'Job 2: FatigueTest + TODesign'),
    ('Experiment4_Job3.odb', 'Job 3: PlasticityTest 100kN'),
]

for odb_file, job_desc in job_files:
    if not os.path.exists(odb_file):
        print("\n{}: File not found".format(job_desc))
        continue

    odb = openOdb(path=odb_file, readOnly=True)

    print("\n" + "="*70)
    print(job_desc)
    print("File: {}".format(odb_file))
    print("="*70)

    for step_name in odb.steps.keys():
        step = odb.steps[step_name]

        if len(step.frames) > 0:
            frame = step.frames[-1]

            print("\n  Step: {} (Frame {}, Time {})".format(
                step_name, frame.frameId, frame.frameValue))
            print("  " + "-"*60)

            # Stress
            if 'S' in frame.fieldOutputs.keys():
                stress_field = frame.fieldOutputs['S']

                max_mises = 0.0
                max_principal = 0.0
                min_principal = 0.0

                for v in stress_field.values:
                    if hasattr(v, 'mises') and v.mises is not None:
                        max_mises = max(max_mises, v.mises)
                    if hasattr(v, 'maxPrincipal') and v.maxPrincipal is not None:
                        max_principal = max(max_principal, v.maxPrincipal)
                    if hasattr(v, 'minPrincipal') and v.minPrincipal is not None:
                        min_principal = min(min_principal, v.minPrincipal)

                print("    Max von Mises stress: {:.1f} MPa".format(max_mises))
                print("    Max principal stress: {:.1f} MPa".format(max_principal))
                print("    Min principal stress: {:.1f} MPa".format(min_principal))

                # Check against material limits
                proportional_limit = 980.0
                yield_strength = 1191.0

                if max_mises < proportional_limit:
                    print("    Status: ELASTIC (below proportional limit)")
                elif max_mises < yield_strength:
                    print("    Status: EARLY PLASTIC (above proportional limit)")
                else:
                    print("    Status: SIGNIFICANT YIELDING (above 0.2% yield)")

            # Displacement
            if 'U' in frame.fieldOutputs.keys():
                disp_field = frame.fieldOutputs['U']

                max_disp = 0.0
                for v in disp_field.values:
                    if hasattr(v, 'magnitude') and v.magnitude is not None:
                        max_disp = max(max_disp, v.magnitude)

                print("    Max displacement: {:.4f} mm".format(max_disp))

            # Plastic strain (PEEQ)
            if 'PEEQ' in frame.fieldOutputs.keys():
                peeq_field = frame.fieldOutputs['PEEQ']

                max_peeq = 0.0
                for v in peeq_field.values:
                    if v.data is not None:
                        max_peeq = max(max_peeq, v.data)

                print("    Max plastic strain (PEEQ): {:.6f}".format(max_peeq))
                if max_peeq > 0:
                    print("    ** PLASTIC DEFORMATION DETECTED **")

    odb.close()

print("\n" + "="*70)
print("ANALYSIS COMPLETE")
print("="*70)
