# visualize_forces_diagram.py - EXPERIMENT 2
#
# Shows the geometry with load/BC symbols to visualize applied forces
#
# Run with: abaqus cae noGUI=paper_reproduction/scripts/experiment2/visualize_forces_diagram.py

from abaqus import *
from abaqusConstants import *
from caeModules import *

OUTPUT_DIR = 'paper_reproduction/outputs/experiment2/'

print("\n" + "=" * 70)
print("EXPERIMENT 2 - FORCE DIAGRAM")
print("=" * 70)

# Load the Job 2 model (has all loads)
print("\nLoading Job 2 model...")
openMdb(pathName=OUTPUT_DIR + 'TO_Bracket_Job2.cae')

model = mdb.models['TO_Bracket_Exp2']
assembly = model.rootAssembly

# Get viewport
vp = session.viewports['Viewport: 1']
vp.setValues(displayedObject=assembly)

# Set white background
session.graphicsOptions.setValues(backgroundStyle=SOLID, backgroundColor='#FFFFFF')

# Enable symbols for BCs and loads
vp.assemblyDisplay.setValues(
    loads=ON,
    bcs=ON,
    predefinedFields=OFF,
    connectors=OFF,
    optimizationTasks=OFF,
    geometricRestrictions=OFF,
    stopConditions=OFF
)

# Set mesh off to show clean geometry
vp.assemblyDisplay.setValues(mesh=OFF)
vp.assemblyDisplay.meshOptions.setValues(meshTechnique=OFF)

# Symbol options are using defaults

# Set isometric view
vp.view.setValues(session.views['Iso'])
vp.view.fitView()

# Save diagram
img_path = OUTPUT_DIR + 'screenshots/Forces_Diagram_Iso.png'
session.printToFile(fileName=img_path, format=PNG, canvasObjects=(vp,))
print(f"Saved: {img_path}")

# Front view
vp.view.setValues(session.views['Front'])
vp.view.fitView()
img_path2 = OUTPUT_DIR + 'screenshots/Forces_Diagram_Front.png'
session.printToFile(fileName=img_path2, format=PNG, canvasObjects=(vp,))
print(f"Saved: {img_path2}")

# Top view (to show horizontal spreading forces)
vp.view.setValues(session.views['Top'])
vp.view.fitView()
img_path3 = OUTPUT_DIR + 'screenshots/Forces_Diagram_Top.png'
session.printToFile(fileName=img_path3, format=PNG, canvasObjects=(vp,))
print(f"Saved: {img_path3}")

print("\n" + "=" * 70)
print("FORCE DIAGRAM COMPLETE")
print("=" * 70)
print("""
Applied Forces (Job 2):
  - Upper pin: 20 kN vertical (-Y direction, downward)
  - Lower left pin: 5 kN horizontal (-X direction, outward left)
  - Lower right pin: 5 kN horizontal (+X direction, outward right)

Boundary Conditions:
  - Lower pins: Fixed in Y (vertical) and Z (out-of-plane)
  - Lower pins: FREE in X (allows spreading motion)
""")
