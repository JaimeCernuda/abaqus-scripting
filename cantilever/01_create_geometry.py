# 02_define_model.py
#
# STEP 2: Create Geometry + Define Model
#
# This script creates the geometry AND defines:
# - Material properties
# - Section assignment
# - Assembly
# - Boundary conditions (fixed end)
# - Loads (force at free end)
# - Mesh
# - Analysis step
# - Job definition
#
# It does NOT submit/run the job.
#
# Purpose: Demonstrate complete model setup without execution.
#
# Run with: abaqus cae noGUI=02_define_model.py
#
# Output: CantileverBeam_Defined.cae (complete model, ready to run)
#         CantileverBeam.inp (input file for manual submission)

from abaqus import *
from abaqusConstants import *
from caeModules import *

print("\n" + "="*60)
print("STEP 2: CREATE GEOMETRY + DEFINE MODEL")
print("="*60)

# =============================================================================
# PARAMETERS
# =============================================================================

# Beam dimensions (mm)
BEAM_LENGTH = 100.0
BEAM_HEIGHT = 10.0
BEAM_WIDTH = 10.0

# Material properties (Steel)
YOUNGS_MODULUS = 210000.0  # MPa
POISSONS_RATIO = 0.3
DENSITY = 7.85e-9          # tonne/mm³

# Loading
APPLIED_FORCE = -1000.0    # N (negative = downward in Y)

# Mesh
MESH_SIZE = 5.0            # mm

# =============================================================================
# STEP 2.1: CREATE MODEL AND GEOMETRY
# =============================================================================

print("\n[1/8] Creating model and geometry...")

model = mdb.Model(name='CantileverBeam')
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']

# Create part
part = model.Part(name='Beam', dimensionality=THREE_D, type=DEFORMABLE_BODY)

# Create sketch and extrude
sketch = model.ConstrainedSketch(name='BeamSketch', sheetSize=200.0)
sketch.rectangle(point1=(0.0, 0.0), point2=(BEAM_LENGTH, BEAM_HEIGHT))
part.BaseSolidExtrude(sketch=sketch, depth=BEAM_WIDTH)

print(f"       Geometry: {BEAM_LENGTH} x {BEAM_HEIGHT} x {BEAM_WIDTH} mm beam")

# =============================================================================
# STEP 2.2: DEFINE MATERIAL
# =============================================================================

print("\n[2/8] Defining material properties...")

material = model.Material(name='Steel')
material.Elastic(table=((YOUNGS_MODULUS, POISSONS_RATIO),))
material.Density(table=((DENSITY,),))

print(f"       Material: Steel")
print(f"       E = {YOUNGS_MODULUS} MPa, ν = {POISSONS_RATIO}")

# =============================================================================
# STEP 2.3: CREATE SECTION AND ASSIGN
# =============================================================================

print("\n[3/8] Creating section and assigning to part...")

# Create solid section
model.HomogeneousSolidSection(
    name='BeamSection',
    material='Steel',
    thickness=None
)

# Assign section to entire part
cells = part.cells
region = part.Set(cells=cells, name='AllCells')
part.SectionAssignment(
    region=region,
    sectionName='BeamSection',
    offset=0.0,
    offsetType=MIDDLE_SURFACE,
    offsetField='',
    thicknessAssignment=FROM_SECTION
)

print("       Section 'BeamSection' assigned to all cells")

# =============================================================================
# STEP 2.4: CREATE ASSEMBLY
# =============================================================================

print("\n[4/8] Creating assembly...")

assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)

# Create instance of the part
instance = assembly.Instance(name='Beam-1', part=part, dependent=ON)

print("       Instance 'Beam-1' created")

# =============================================================================
# STEP 2.5: DEFINE ANALYSIS STEP
# =============================================================================

print("\n[5/8] Creating analysis step...")

model.StaticStep(
    name='LoadStep',
    previous='Initial',
    description='Apply load to cantilever beam',
    initialInc=1.0,
    maxInc=1.0,
    minInc=1e-6,
    maxNumInc=100
)

# Request field outputs
model.FieldOutputRequest(
    name='F-Output-1',
    createStepName='LoadStep',
    variables=('S', 'U', 'RF', 'CF')
)

print("       Step 'LoadStep' created (Static)")

# =============================================================================
# STEP 2.6: DEFINE BOUNDARY CONDITIONS
# =============================================================================

print("\n[6/8] Defining boundary conditions...")

# Find the face at x=0 (fixed end)
# The face normal is (-1, 0, 0) and contains point (0, HEIGHT/2, WIDTH/2)
fixed_face = instance.faces.findAt(((0.0, BEAM_HEIGHT/2, BEAM_WIDTH/2),))

# Create a set for the fixed face
fixed_region = assembly.Set(faces=fixed_face, name='FixedEnd')

# Apply Encastre BC (all DOFs = 0)
model.EncastreBC(
    name='FixedSupport',
    createStepName='Initial',
    region=fixed_region,
    localCsys=None
)

print("       Encastre BC applied at x=0 (fixed end)")

# =============================================================================
# STEP 2.7: DEFINE LOADS
# =============================================================================

print("\n[7/8] Defining loads...")

# Find the face at x=LENGTH (free end where load is applied)
load_face = instance.faces.findAt(((BEAM_LENGTH, BEAM_HEIGHT/2, BEAM_WIDTH/2),))

# Create a set for the load face
load_region = assembly.Set(faces=load_face, name='LoadFace')

# Apply concentrated force at the face centroid
# For a surface load, we'll use a concentrated force at the centroid
# Alternatively, we could use pressure or surface traction

# Get vertices at the free end to apply concentrated force
# Let's apply at the center of the free end face
# Using surface traction for distributed load
load_surface = assembly.Surface(side1Faces=load_face, name='LoadSurface')

# Apply as surface traction (distributed force)
model.SurfaceTraction(
    name='AppliedForce',
    createStepName='LoadStep',
    region=load_surface,
    magnitude=APPLIED_FORCE / (BEAM_HEIGHT * BEAM_WIDTH),  # Force / Area
    directionVector=((0.0, 0.0, 0.0), (0.0, 1.0, 0.0)),   # Y direction
    distributionType=UNIFORM,
    traction=GENERAL,
    follower=OFF
)

print(f"       Traction load applied at x={BEAM_LENGTH} (free end)")
print(f"       Total force: {APPLIED_FORCE} N in Y direction")

# =============================================================================
# STEP 2.8: CREATE MESH
# =============================================================================

print("\n[8/8] Creating mesh...")

# Seed the part
part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)

# Set element type (C3D8R - 8-node linear brick, reduced integration)
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD,
                          kinematicSplit=AVERAGE_STRAIN,
                          secondOrderAccuracy=OFF,
                          hourglassControl=DEFAULT,
                          distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)

part.setElementType(
    regions=(part.cells,),
    elemTypes=(elemType1, elemType2, elemType3)
)

# Generate mesh
part.generateMesh()

num_nodes = len(part.nodes)
num_elements = len(part.elements)

print(f"       Mesh size: {MESH_SIZE} mm")
print(f"       Elements: {num_elements}")
print(f"       Nodes: {num_nodes}")

if num_nodes > 1000:
    print(f"       ⚠️ WARNING: {num_nodes} nodes exceeds Learning Edition limit of 1000!")
    print(f"       Increase MESH_SIZE to reduce node count.")

# =============================================================================
# CREATE JOB (but don't submit)
# =============================================================================

print("\n[Bonus] Creating job definition...")

job = mdb.Job(
    name='CantileverBeam',
    model='CantileverBeam',
    description='Cantilever beam static analysis',
    type=ANALYSIS,
    atTime=None,
    waitMinutes=0,
    waitHours=0,
    queue=None,
    memory=90,
    memoryUnits=PERCENTAGE,
    getMemoryFromAnalysis=True,
    explicitPrecision=SINGLE,
    nodalOutputPrecision=SINGLE,
    echoPrint=OFF,
    modelPrint=OFF,
    contactPrint=OFF,
    historyPrint=OFF,
    userSubroutine='',
    scratch='',
    resultsFormat=ODB
)

# Write input file (but don't run)
job.writeInput(consistencyChecking=OFF)

print("       Job 'CantileverBeam' created")
print("       Input file written: CantileverBeam.inp")

# =============================================================================
# SAVE MODEL
# =============================================================================

mdb.saveAs(pathName='CantileverBeam_Defined.cae')

print("\n" + "="*60)
print("STEP 2 COMPLETE")
print("="*60)
print(f"""
Output files:
  ✓ CantileverBeam_Defined.cae (complete model database)
  ✓ CantileverBeam.inp (input file for solver)

What was created:
  ✓ Geometry (beam)
  ✓ Material (Steel: E={YOUNGS_MODULUS} MPa)
  ✓ Section assignment
  ✓ Assembly with instance
  ✓ Analysis step (Static)
  ✓ Boundary condition (Fixed at x=0)
  ✓ Load ({APPLIED_FORCE} N at x={BEAM_LENGTH})
  ✓ Mesh ({num_elements} elements, {num_nodes} nodes)
  ✓ Job definition

What was NOT done:
  ✗ Job submission (analysis not run)
  ✗ Results extraction

To run the analysis manually:
  Option 1: abaqus job=CantileverBeam interactive
  Option 2: In Abaqus/CAE: Job > Submit

Next: Run 03_run_analysis.py to execute the analysis
""")
