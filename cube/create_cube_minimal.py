# create_cube_minimal.py
# Minimal Abaqus script - just creates a cube part, no analysis
# Good for testing your setup
# Run with: abaqus cae noGUI=create_cube_minimal.py

from abaqus import *
from abaqusConstants import *
from caeModules import *

print("\n" + "="*50)
print("Starting minimal cube creation...")
print("="*50 + "\n")

# Create model
model = mdb.Model(name='MinimalCube')
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']

# Create part
part = model.Part(name='Cube', dimensionality=THREE_D, type=DEFORMABLE_BODY)

# Sketch and extrude
sketch = model.ConstrainedSketch(name='CubeSketch', sheetSize=200.0)
sketch.rectangle(point1=(0.0, 0.0), point2=(10.0, 10.0))
part.BaseSolidExtrude(sketch=sketch, depth=10.0)

# Save
mdb.saveAs(pathName='MinimalCube.cae')

print("\n" + "="*50)
print("SUCCESS! Cube created and saved to MinimalCube.cae")
print("="*50 + "\n")
