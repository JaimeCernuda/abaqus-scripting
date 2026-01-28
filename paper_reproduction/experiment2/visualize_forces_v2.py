# visualize_forces_v2.py - EXPERIMENT 2
#
# Shows the geometry with load/BC symbols
#
# Run with: abaqus cae noGUI=paper_reproduction/scripts/experiment2/visualize_forces_v2.py

from abaqus import *
from abaqusConstants import *
from caeModules import *

OUTPUT_DIR = 'paper_reproduction/outputs/experiment2/'

print("\n" + "=" * 70)
print("EXPERIMENT 2 - FORCE DIAGRAM V2")
print("=" * 70)

# Load the Job 2 model (has all loads)
print("\nLoading Job 2 model...")
openMdb(pathName=OUTPUT_DIR + 'TO_Bracket_Job2.cae')

model = mdb.models['TO_Bracket_Exp2']
assembly = model.rootAssembly

# Regenerate the assembly to ensure geometry is visible
assembly.regenerate()

# Get viewport
vp = session.viewports['Viewport: 1']
vp.setValues(displayedObject=assembly)

# Set white background
session.graphicsOptions.setValues(backgroundStyle=SOLID, backgroundColor='#FFFFFF')

# Turn on rendering
vp.assemblyDisplay.setValues(
    loads=ON,
    bcs=ON,
    constraints=ON
)

# Set step to LoadStep to see the loads
vp.assemblyDisplay.setValues(step='LoadStep')

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
