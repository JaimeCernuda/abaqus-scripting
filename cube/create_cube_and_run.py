# create_cube_and_run.py
# Creates cube model, writes input file, and submits job
# Run with: abaqus cae noGUI=create_cube_and_run.py

from abaqus import *
from abaqusConstants import *
from caeModules import *

# Create a new model
model = mdb.Model(name='CubeModel')

# Delete the default model if it exists
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']

# --- Create Part ---
part = model.Part(name='Cube', dimensionality=THREE_D, type=DEFORMABLE_BODY)

# Create a sketch on the XY plane
sketch = model.ConstrainedSketch(name='CubeSketch', sheetSize=200.0)
sketch.rectangle(point1=(0.0, 0.0), point2=(10.0, 10.0))

# Extrude to create cube (10x10x10)
part.BaseSolidExtrude(sketch=sketch, depth=10.0)

# --- Create Material ---
material = model.Material(name='Steel')
material.Elastic(table=((210000.0, 0.3),))  # E = 210 GPa, nu = 0.3
material.Density(table=((7.85e-9,),))

# --- Create Section ---
model.HomogeneousSolidSection(name='SolidSection', material='Steel', thickness=None)

# --- Assign Section ---
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

# --- Request Output ---
# Field output (for contour plots)
model.FieldOutputRequest(name='F-Output-1', createStepName='LoadStep',
                         variables=('S', 'U', 'RF'))

# --- Boundary Conditions ---
bottom_face = instance.faces.findAt(((5.0, 5.0, 0.0),))
bottom_region = assembly.Set(faces=bottom_face, name='BottomFace')
model.EncastreBC(name='FixBottom', createStepName='Initial', region=bottom_region)

# --- Apply Load ---
top_face = instance.faces.findAt(((5.0, 5.0, 10.0),))
top_region = assembly.Surface(side1Faces=top_face, name='TopSurface')
model.Pressure(name='TopPressure', createStepName='LoadStep',
               region=top_region, magnitude=100.0)

# --- Mesh ---
part.seedPart(size=2.5, deviationFactor=0.1, minSizeFactor=0.1)
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType1, elemType2, elemType3))
part.generateMesh()

# --- Create Job ---
job = mdb.Job(name='CubeAnalysis', model='CubeModel',
              description='Simple cube compression analysis',
              type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0,
              queue=None, memory=90, memoryUnits=PERCENTAGE,
              getMemoryFromAnalysis=True, explicitPrecision=SINGLE,
              nodalOutputPrecision=SINGLE, echoPrint=OFF,
              modelPrint=OFF, contactPrint=OFF, historyPrint=OFF,
              userSubroutine='', scratch='', resultsFormat=ODB)

# --- Save the CAE file ---
mdb.saveAs(pathName='CubeModel.cae')

print("\n" + "="*60)
print("Model created and saved!")
print("="*60)

# --- Write the input file ---
print("\nWriting input file...")
job.writeInput(consistencyChecking=OFF)
print("Input file written: CubeAnalysis.inp")

# --- Submit the job ---
print("\nSubmitting job...")
job.submit(consistencyChecking=OFF)

# --- Wait for job to complete ---
print("Waiting for job to complete...")
job.waitForCompletion()

print("\n" + "="*60)
print("Job completed!")
print("="*60)
print("\nGenerated files:")
print("  - CubeModel.cae      (model database)")
print("  - CubeAnalysis.inp   (input file)")
print("  - CubeAnalysis.odb   (results database)")
print("  - CubeAnalysis.dat   (printed output)")
print("  - CubeAnalysis.msg   (message file)")
print("  - CubeAnalysis.sta   (status file)")
print("\nTo view results, open CubeAnalysis.odb in Abaqus/Viewer")
print("Or run: abaqus python read_results.py")
print("="*60 + "\n")
