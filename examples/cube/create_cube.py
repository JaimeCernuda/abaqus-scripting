# create_cube.py
# Abaqus Python script to create a simple cube
# Run with: abaqus cae script=create_cube.py
# Or headless: abaqus cae noGUI=create_cube.py

from abaqus import *
from abaqusConstants import *
from caeModules import *

# Create a new model
model = mdb.Model(name='CubeModel')

# Delete the default model if it exists
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']

# --- Create Part ---
# Create a 3D deformable part
part = model.Part(name='Cube', dimensionality=THREE_D, type=DEFORMABLE_BODY)

# Create a sketch on the XY plane
sketch = model.ConstrainedSketch(name='CubeSketch', sheetSize=200.0)

# Draw a 10x10 square (this will be the base of the cube)
sketch.rectangle(point1=(0.0, 0.0), point2=(10.0, 10.0))

# Extrude the sketch to create a cube (10x10x10)
part.BaseSolidExtrude(sketch=sketch, depth=10.0)

# --- Create Material ---
material = model.Material(name='Steel')
material.Elastic(table=((210000.0, 0.3),))  # E = 210 GPa, nu = 0.3
material.Density(table=((7.85e-9,),))  # density in tonne/mm^3

# --- Create Section ---
model.HomogeneousSolidSection(name='SolidSection', material='Steel', thickness=None)

# --- Assign Section to Part ---
# First, we need to select the cells (the solid region)
cells = part.cells
region = part.Set(cells=cells, name='AllCells')
part.SectionAssignment(region=region, sectionName='SolidSection')

# --- Create Assembly ---
assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
instance = assembly.Instance(name='Cube-1', part=part, dependent=ON)

# --- Create Step ---
model.StaticStep(name='LoadStep', previous='Initial', 
                 initialInc=0.1, maxInc=1.0, minInc=1e-6)

# --- Create Boundary Conditions ---
# Fix the bottom face (z=0)
# Find the bottom face
bottom_face = instance.faces.findAt(((5.0, 5.0, 0.0),))
bottom_region = assembly.Set(faces=bottom_face, name='BottomFace')
model.EncastreBC(name='FixBottom', createStepName='Initial', region=bottom_region)

# --- Apply Load ---
# Apply pressure on the top face (z=10)
top_face = instance.faces.findAt(((5.0, 5.0, 10.0),))
top_region = assembly.Surface(side1Faces=top_face, name='TopSurface')
model.Pressure(name='TopPressure', createStepName='LoadStep',
               region=top_region, magnitude=100.0)

# --- Mesh the Part ---
# Seed the part
part.seedPart(size=2.5, deviationFactor=0.1, minSizeFactor=0.1)

# Assign element type (C3D8R - 8-node linear brick, reduced integration)
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType1, elemType2, elemType3))

# Generate mesh
part.generateMesh()

# --- Create Job ---
job = mdb.Job(name='CubeAnalysis', model='CubeModel', 
              description='Simple cube compression analysis')

# --- Save the model ---
mdb.saveAs(pathName='CubeModel.cae')

print("="*50)
print("Cube model created successfully!")
print("Model saved as: CubeModel.cae")
print("="*50)
print("\nTo run the analysis, use one of these methods:")
print("1. In Abaqus CAE: Job -> Submit")
print("2. Command line: abaqus job=CubeAnalysis")
print("="*50)
