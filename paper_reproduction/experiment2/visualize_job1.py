# visualize_job1.py - EXPERIMENT 2
#
# Opens Job 1 ODB and saves von Mises stress contour screenshot
#
# Run with: abaqus cae noGUI=paper_reproduction/scripts/experiment2/visualize_job1.py

from abaqus import *
from abaqusConstants import *
from caeModules import *
import visualization

OUTPUT_DIR = 'paper_reproduction/outputs/experiment2/'

print("\n" + "=" * 70)
print("EXPERIMENT 2 - VISUALIZE JOB 1 RESULTS")
print("=" * 70)

# Open ODB
odb_path = OUTPUT_DIR + 'Exp2_Job1_Vertical.odb'
print(f"\nOpening: {odb_path}")
odb = visualization.openOdb(path=odb_path)

# Get viewport
vp = session.viewports['Viewport: 1']
vp.setValues(displayedObject=odb)

# Set to last frame
vp.odbDisplay.setFrame(step=0, frame=-1)

# Display von Mises stress on deformed shape
vp.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))
vp.odbDisplay.setPrimaryVariable(variableLabel='S', outputPosition=INTEGRATION_POINT,
                                  refinement=(INVARIANT, 'Mises'))

# Configure contour options
vp.odbDisplay.contourOptions.setValues(
    numIntervals=10,
    maxAutoCompute=ON,
    minAutoCompute=ON
)

# Set isometric view
vp.view.setValues(session.views['Iso'])
vp.view.fitView()

# Set white background for better screenshots
session.graphicsOptions.setValues(backgroundStyle=SOLID, backgroundColor='#FFFFFF')

# Save screenshot
img_path = OUTPUT_DIR + 'screenshots/Job1_VonMises.png'
session.printToFile(fileName=img_path, format=PNG, canvasObjects=(vp,))
print(f"Saved: {img_path}")

# Also save front view
vp.view.setValues(session.views['Front'])
vp.view.fitView()
img_path2 = OUTPUT_DIR + 'screenshots/Job1_VonMises_Front.png'
session.printToFile(fileName=img_path2, format=PNG, canvasObjects=(vp,))
print(f"Saved: {img_path2}")

# Extract max values
step = odb.steps['LoadStep']
frame = step.frames[-1]

stress_field = frame.fieldOutputs['S']
max_mises = 0.0
for value in stress_field.values:
    if hasattr(value, 'mises') and value.mises > max_mises:
        max_mises = value.mises

disp_field = frame.fieldOutputs['U']
max_disp = 0.0
for value in disp_field.values:
    if value.magnitude > max_disp:
        max_disp = value.magnitude

print(f"\nJob 1 Results:")
print(f"  Max von Mises stress: {max_mises:.2f} MPa")
print(f"  Max displacement: {max_disp:.4f} mm")

odb.close()

print("\n" + "=" * 70)
print("JOB 1 VISUALIZATION COMPLETE")
print("=" * 70)
