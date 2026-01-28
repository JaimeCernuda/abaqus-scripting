# 07_visualize_forces.py - EXPERIMENT 2
#
# Visualizes reaction forces and applied loads for both jobs
# Saves images showing force vectors
#
# Run with: abaqus cae noGUI=paper_reproduction/scripts/experiment2/07_visualize_forces.py

from abaqus import *
from abaqusConstants import *
from caeModules import *
import visualization

OUTPUT_DIR = 'paper_reproduction/outputs/experiment2/'

print("\n" + "=" * 70)
print("EXPERIMENT 2 - VISUALIZE FORCES")
print("=" * 70)

jobs = [
    ('Exp2_Job1_Vertical', 'Job 1: Vertical Only'),
    ('Exp2_Job2_Horizontal', 'Job 2: Vertical + Horizontal'),
]

for job_name, description in jobs:
    odb_path = OUTPUT_DIR + job_name + '.odb'
    print(f"\n--- {description} ---")

    # Open ODB
    odb = visualization.openOdb(path=odb_path)

    # Get viewport
    vp = session.viewports['Viewport: 1']
    vp.setValues(displayedObject=odb)

    # Set to last frame
    vp.odbDisplay.setFrame(step=0, frame=-1)

    # Display reaction forces as vectors
    vp.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))
    vp.odbDisplay.setPrimaryVariable(variableLabel='RF', outputPosition=NODAL,
                                      refinement=(INVARIANT, 'Magnitude'))

    # Set view
    vp.view.setValues(session.views['Iso'])
    vp.view.fitView()

    # Turn on symbols for BCs and loads
    vp.odbDisplay.basicOptions.setValues(
        renderBeamProfiles=OFF,
        renderShellThickness=OFF
    )

    # Display deformed shape with reaction force contours
    vp.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))

    # Save image
    img_path = OUTPUT_DIR + 'screenshots/' + job_name + '_forces.png'
    session.printToFile(fileName=img_path, format=PNG, canvasObjects=(vp,))
    print(f"    Saved: {img_path}")

    # Also show von Mises with deformation
    vp.odbDisplay.setPrimaryVariable(variableLabel='S', outputPosition=INTEGRATION_POINT,
                                      refinement=(INVARIANT, 'Mises'))
    vp.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))

    img_path2 = OUTPUT_DIR + 'screenshots/' + job_name + '_mises.png'
    session.printToFile(fileName=img_path2, format=PNG, canvasObjects=(vp,))
    print(f"    Saved: {img_path2}")

    odb.close()

print("\n" + "=" * 70)
print("FORCE VISUALIZATION COMPLETE")
print("=" * 70)
