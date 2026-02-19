# -*- coding: utf-8 -*-
"""
Experiment 5: Capture topology optimization result screenshots.

Captures density contour images from the final optimization ODB and
stress contour images from validation ODBs (if they exist).

Run with: xvfb-run -a abaqus cae script=scripts/capture_to_results.py
"""
import os
from abaqus import *
from abaqusConstants import *
from visualization import *

try:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    SCRIPT_DIR = os.path.join(os.getcwd(), 'scripts')
PROJECT_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, os.pardir))
os.chdir(PROJECT_DIR)

# Create screenshots directory
screenshots_dir = os.path.join(PROJECT_DIR, 'screenshots')
if not os.path.exists(screenshots_dir):
    os.makedirs(screenshots_dir)

vp = session.viewports['Viewport: 1']

# =========================================================================
# DENSITY CONTOURS — final optimization ODB
# =========================================================================
print("\n--- Density contour screenshots ---")

opt_dir = os.path.join(PROJECT_DIR, 'Experiment5_TO', 'TOSCA_POST')
if not os.path.exists(opt_dir):
    opt_dir = os.path.join(PROJECT_DIR, 'TOSCA_POST')

if os.path.exists(opt_dir):
    odb_files = sorted([f for f in os.listdir(opt_dir) if f.endswith('.odb')])
    if odb_files:
        final_odb_path = os.path.join(opt_dir, odb_files[-1])
        print("Opening: {}".format(odb_files[-1]))

        odb = session.openOdb(final_odb_path)
        vp.setValues(displayedObject=odb)

        # Show contours on undeformed shape
        vp.odbDisplay.display.setValues(plotState=(CONTOURS_ON_UNDEF,))

        # Find density field
        step = odb.steps[odb.steps.keys()[-1]]
        frame = step.frames[-1]
        density_field_name = None
        for name in frame.fieldOutputs.keys():
            upper_name = name.upper()
            if 'DENSITY' in upper_name or 'MAT_PROP' in upper_name:
                density_field_name = name
                break

        if density_field_name:
            vp.odbDisplay.setPrimaryVariable(
                variableLabel=density_field_name,
                outputPosition=INTEGRATION_POINT)

            # Set contour range 0 to 1
            vp.odbDisplay.contourOptions.setValues(
                numIntervals=10,
                minAutoCompute=OFF, minValue=0.0,
                maxAutoCompute=OFF, maxValue=1.0)
            print("  Density field: {}".format(density_field_name))
        else:
            print("  WARNING: No density field found, using default display")
            print("  Available fields: {}".format(list(frame.fieldOutputs.keys())))

        # Capture from multiple views
        for view_name in ['Iso', 'Front', 'Right', 'Top']:
            vp.view.setValues(session.views[view_name])
            vp.view.fitView()
            session.printToFile(
                fileName='screenshots/density_{}'.format(view_name.lower()),
                format=PNG,
                canvasObjects=(vp,))
            print("  Saved: density_{}.png".format(view_name.lower()))

        odb.close()
    else:
        print("No ODB files in TOSCA_POST — optimization may not have completed")
else:
    print("TOSCA_POST not found — optimization may not have run yet")

# =========================================================================
# VALIDATION STRESS CONTOURS — if validation ODBs exist
# =========================================================================
print("\n--- Validation stress contour screenshots ---")

val_jobs = [
    ('Validation_20kN.odb', 'val_20kN'),
    ('Validation_60kN.odb', 'val_60kN'),
    ('Validation_100kN.odb', 'val_100kN'),
]

for odb_name, prefix in val_jobs:
    odb_path = os.path.join(PROJECT_DIR, odb_name)
    if not os.path.exists(odb_path):
        print("Skipping {} (not found)".format(odb_name))
        continue

    print("Opening: {}".format(odb_name))
    odb = session.openOdb(odb_path)
    vp.setValues(displayedObject=odb)

    # Stress contours on deformed shape
    vp.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))
    vp.odbDisplay.setPrimaryVariable(
        variableLabel='S',
        outputPosition=INTEGRATION_POINT,
        refinement=(INVARIANT, 'Mises'))
    vp.odbDisplay.commonOptions.setValues(
        deformationScaling=UNIFORM, uniformScaleFactor=10)

    for view_name in ['Iso', 'Front', 'Right']:
        vp.view.setValues(session.views[view_name])
        vp.view.fitView()
        session.printToFile(
            fileName='screenshots/{}_{}'.format(prefix, view_name.lower()),
            format=PNG,
            canvasObjects=(vp,))
        print("  Saved: {}_{}.png".format(prefix, view_name.lower()))

    odb.close()

print("\nScreenshot capture complete")
