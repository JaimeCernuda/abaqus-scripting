# -*- coding: utf-8 -*-
"""
Experiment 4: Extract Results from ODB
"""

from odbAccess import *
import os

# Change to experiment4 directory
os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')

# Open ODB file
odb_path = 'Experiment4_Job1.odb'
odb = openOdb(path=odb_path, readOnly=True)

print("="*60)
print("EXPERIMENT 4 - RESULTS EXTRACTION")
print("="*60)

# Get step names
print("\nSteps in model:")
for step_name in odb.steps.keys():
    print("  - {}".format(step_name))

# Extract results for each step
for step_name in odb.steps.keys():
    step = odb.steps[step_name]

    # Get last frame (final converged state)
    if len(step.frames) > 0:
        frame = step.frames[-1]

        print("\n" + "-"*60)
        print("Step: {}".format(step_name))
        print("Frame: {}, Time: {}".format(frame.frameId, frame.frameValue))
        print("-"*60)

        # Extract stress field (S)
        if 'S' in frame.fieldOutputs.keys():
            stress_field = frame.fieldOutputs['S']

            # Get max von Mises stress
            max_mises = 0.0
            max_mises_location = None
            for v in stress_field.values:
                if hasattr(v, 'mises') and v.mises is not None:
                    if v.mises > max_mises:
                        max_mises = v.mises
                        max_mises_location = v.elementLabel

            print("  Max von Mises stress: {:.1f} MPa".format(max_mises))
            if max_mises_location:
                print("  Location: Element {}".format(max_mises_location))

            # Get max principal stress
            max_principal = 0.0
            for v in stress_field.values:
                if hasattr(v, 'maxPrincipal') and v.maxPrincipal is not None:
                    if v.maxPrincipal > max_principal:
                        max_principal = v.maxPrincipal

            print("  Max principal stress: {:.1f} MPa".format(max_principal))

        # Extract displacement field (U)
        if 'U' in frame.fieldOutputs.keys():
            disp_field = frame.fieldOutputs['U']

            max_disp = 0.0
            for v in disp_field.values:
                if hasattr(v, 'magnitude') and v.magnitude is not None:
                    if v.magnitude > max_disp:
                        max_disp = v.magnitude

            print("  Max displacement: {:.4f} mm".format(max_disp))

# Close ODB
odb.close()

print("\n" + "="*60)
print("RESULTS EXTRACTION COMPLETE")
print("="*60)
