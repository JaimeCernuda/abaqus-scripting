# 07_visualize_results.py - EXPERIMENT 3
#
# Creates screenshots of Job 1 and Job 2 stress results
#
# Run with: abaqus cae script=paper_reproduction/scripts/experiment3/07_visualize_results.py
# (Requires GUI - cannot use noGUI mode)

from abaqus import *
from abaqusConstants import *
from caeModules import *
from visualization import *

print("\n" + "=" * 70)
print("EXPERIMENT 3 - VISUALIZE RESULTS")
print("=" * 70)

OUTPUT_DIR = 'paper_reproduction/outputs/experiment3/'

jobs = [
    ('job1/Exp3_Job1_Vertical', 'Job1'),
    ('job2/Exp3_Job2_Horizontal', 'Job2'),
]

for job_path, job_label in jobs:
    odb_path = OUTPUT_DIR + job_path + '.odb'
    print(f"\nProcessing {job_label}...")

    # Open ODB
    odb = session.openOdb(name=odb_path)
    viewport = session.viewports['Viewport: 1']
    viewport.setValues(displayedObject=odb)

    # Display von Mises stress
    viewport.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))
    viewport.odbDisplay.setPrimaryVariable(
        variableLabel='S',
        outputPosition=INTEGRATION_POINT,
        refinement=(INVARIANT, 'Mises')
    )

    # Set deformation scale
    viewport.odbDisplay.commonOptions.setValues(deformationScaling=UNIFORM, uniformScaleFactor=100)

    # Isometric view
    viewport.view.setValues(session.views['Iso'])
    viewport.view.fitView()

    # Save isometric screenshot
    session.printToFile(
        fileName=OUTPUT_DIR + f'screenshots/Exp3_{job_label}_VonMises_Iso',
        format=PNG,
        canvasObjects=(viewport,)
    )
    print(f"  Saved: Exp3_{job_label}_VonMises_Iso.png")

    # Front view (looking at X-Z plane, Y into page)
    viewport.view.setValues(nearPlane=200, farPlane=400,
                            cameraPosition=(0, 200, 73),
                            cameraUpVector=(0, 0, 1),
                            cameraTarget=(0, 17.5, 73))
    viewport.view.fitView()

    session.printToFile(
        fileName=OUTPUT_DIR + f'screenshots/Exp3_{job_label}_VonMises_Front',
        format=PNG,
        canvasObjects=(viewport,)
    )
    print(f"  Saved: Exp3_{job_label}_VonMises_Front.png")

    # Close ODB
    odb.close()

print("\n" + "=" * 70)
print("EXPERIMENT 3 - VISUALIZATION COMPLETE")
print("=" * 70)
print(f"\nScreenshots saved to: {OUTPUT_DIR}screenshots/")
