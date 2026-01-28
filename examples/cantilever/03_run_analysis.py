# 04_analyze_results.py
#
# STEP 4: Analyze Results from ODB
#
# This script reads the output database (ODB) and extracts:
# - Displacement field
# - Stress field
# - Reaction forces
# - Creates a summary report
#
# Purpose: Demonstrate post-processing of FEA results.
#
# Run with: abaqus python 04_analyze_results.py
#   or:     abaqus python 04_analyze_results.py path/to/results.odb
#
# Note: This uses 'abaqus python', not 'abaqus cae', since it only
#       accesses the ODB API and doesn't need the CAE GUI.

# 03_run_analysis.py
# Cantilever beam with SurfaceTraction - fixed for GUI mode

from abaqus import *
from abaqusConstants import *
from caeModules import *

print("\n" + "="*60)
print("CANTILEVER BEAM ANALYSIS")
print("="*60)

# Parameters
BEAM_LENGTH = 100.0
BEAM_HEIGHT = 10.0
BEAM_WIDTH = 10.0
YOUNGS_MODULUS = 210000.0
POISSONS_RATIO = 0.3
DENSITY = 7.85e-9
APPLIED_FORCE = -1000.0
MESH_SIZE = 5.0

# Create model
model = mdb.Model(name='CantileverBeam')
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']

# --- Create Part ---
part = model.Part(name='Beam', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='BeamSketch', sheetSize=200.0)
sketch.rectangle(point1=(0.0, 0.0), point2=(BEAM_LENGTH, BEAM_HEIGHT))
part.BaseSolidExtrude(sketch=sketch, depth=BEAM_WIDTH)
print("Part created")

# --- Create Material ---
material = model.Material(name='Steel')
material.Elastic(table=((YOUNGS_MODULUS, POISSONS_RATIO),))
material.Density(table=((DENSITY,),))
print("Material defined")

# --- Create Section ---
model.HomogeneousSolidSection(name='BeamSection', material='Steel', thickness=None)
cells = part.cells
region = part.Set(cells=cells, name='AllCells')
part.SectionAssignment(region=region, sectionName='BeamSection')
print("Section assigned")

# --- Create Assembly ---
assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
instance = assembly.Instance(name='Beam-1', part=part, dependent=ON)
print("Assembly created")

# --- Create Step ---
model.StaticStep(name='LoadStep', previous='Initial',
                 initialInc=0.1, maxInc=1.0, minInc=1e-6)
model.FieldOutputRequest(name='F-Output-1', createStepName='LoadStep',
                         variables=('S', 'U', 'RF', 'CF', 'E'))
print("Step created")

# --- Boundary Conditions (fixed at x=0) ---
fixed_face = instance.faces.findAt(((0.0, BEAM_HEIGHT/2, BEAM_WIDTH/2),))
fixed_region = assembly.Set(faces=fixed_face, name='FixedEnd')
model.EncastreBC(name='FixedSupport', createStepName='Initial', region=fixed_region)
print("BC applied: Fixed at x=0")

# --- Apply Load (SurfaceTraction at x=100) ---
load_face = instance.faces.findAt(((BEAM_LENGTH, BEAM_HEIGHT/2, BEAM_WIDTH/2),))
load_surface = assembly.Surface(side1Faces=load_face, name='LoadSurface')
traction_magnitude = APPLIED_FORCE / (BEAM_HEIGHT * BEAM_WIDTH)
model.SurfaceTraction(
    name='AppliedForce',
    createStepName='LoadStep',
    region=load_surface,
    magnitude=traction_magnitude,
    directionVector=((0.0, 0.0, 0.0), (0.0, 1.0, 0.0)),
    distributionType=UNIFORM,
    traction=GENERAL
)
print(f"Load applied: {APPLIED_FORCE} N as SurfaceTraction")

# --- Mesh ---
part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType1, elemType2, elemType3))
part.generateMesh()
print(f"Mesh generated: {len(part.nodes)} nodes, {len(part.elements)} elements")

# --- Create Job ---
job = mdb.Job(name='CantileverBeam', model='CantileverBeam',
              description='Cantilever beam analysis',
              type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0,
              queue=None, memory=90, memoryUnits=PERCENTAGE,
              getMemoryFromAnalysis=True, explicitPrecision=SINGLE,
              nodalOutputPrecision=SINGLE, echoPrint=OFF,
              modelPrint=OFF, contactPrint=OFF, historyPrint=OFF,
              userSubroutine='', scratch='', resultsFormat=ODB)

# --- Save ---
mdb.saveAs(pathName='CantileverBeam.cae')
print("Model saved: CantileverBeam.cae")

# --- Write input file ---
job.writeInput(consistencyChecking=OFF)
print("Input file: CantileverBeam.inp")

# --- Submit and wait ---
print("\nSubmitting job...")
job.submit(consistencyChecking=OFF)
job.waitForCompletion()

print("\n" + "="*60)
print("DONE!")
print("="*60)
print("Results file: CantileverBeam.odb")
print("To analyze: abaqus python 04_analyze_results.py")
print("="*60 + "\n")