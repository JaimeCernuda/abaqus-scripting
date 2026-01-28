# 03_run_analysis.py
#
# STEP 3: Create Geometry + Define Model + Run Analysis
#
# This script does EVERYTHING:
# - Creates geometry
# - Defines material, sections, BCs, loads
# - Creates mesh
# - Submits the job
# - Waits for completion
#
# Purpose: Complete automated workflow from start to finish.
#
# Run with: abaqus cae noGUI=03_run_analysis.py
#
# Output: CantileverBeam.cae (model)
#         CantileverBeam.inp (input file)
#         CantileverBeam.odb (results)
#         CantileverBeam.dat, .msg, .sta (log files)

from abaqus import *
from abaqusConstants import *
from caeModules import *

print("\n" + "="*60)
print("STEP 3: COMPLETE WORKFLOW - BUILD AND RUN")
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

# Job name
JOB_NAME = 'CantileverBeam'

# =============================================================================
# PHASE 1: CREATE GEOMETRY
# =============================================================================

print("\n" + "-"*60)
print("PHASE 1: GEOMETRY")
print("-"*60)

model = mdb.Model(name='CantileverBeam')
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']

part = model.Part(name='Beam', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='BeamSketch', sheetSize=200.0)
sketch.rectangle(point1=(0.0, 0.0), point2=(BEAM_LENGTH, BEAM_HEIGHT))
part.BaseSolidExtrude(sketch=sketch, depth=BEAM_WIDTH)

print(f"  ✓ Created beam: {BEAM_LENGTH} x {BEAM_HEIGHT} x {BEAM_WIDTH} mm")

# =============================================================================
# PHASE 2: MATERIAL AND SECTION
# =============================================================================

print("\n" + "-"*60)
print("PHASE 2: MATERIAL AND SECTION")
print("-"*60)

material = model.Material(name='Steel')
material.Elastic(table=((YOUNGS_MODULUS, POISSONS_RATIO),))
material.Density(table=((DENSITY,),))

model.HomogeneousSolidSection(name='BeamSection', material='Steel', thickness=None)

cells = part.cells
region = part.Set(cells=cells, name='AllCells')
part.SectionAssignment(region=region, sectionName='BeamSection')

print(f"  ✓ Material: Steel (E={YOUNGS_MODULUS} MPa, ν={POISSONS_RATIO})")
print(f"  ✓ Section assigned to beam")

# =============================================================================
# PHASE 3: ASSEMBLY
# =============================================================================

print("\n" + "-"*60)
print("PHASE 3: ASSEMBLY")
print("-"*60)

assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
instance = assembly.Instance(name='Beam-1', part=part, dependent=ON)

print(f"  ✓ Instance 'Beam-1' created in assembly")

# =============================================================================
# PHASE 4: ANALYSIS STEP
# =============================================================================

print("\n" + "-"*60)
print("PHASE 4: ANALYSIS STEP")
print("-"*60)

model.StaticStep(name='LoadStep', previous='Initial')

model.FieldOutputRequest(name='F-Output-1', createStepName='LoadStep',
                         variables=('S', 'U', 'RF', 'CF', 'E'))

print(f"  ✓ Static step 'LoadStep' created")
print(f"  ✓ Field outputs: Stress, Displacement, Reactions")

# =============================================================================
# PHASE 5: BOUNDARY CONDITIONS
# =============================================================================

print("\n" + "-"*60)
print("PHASE 5: BOUNDARY CONDITIONS")
print("-"*60)

# Fixed end at x=0
fixed_face = instance.faces.findAt(((0.0, BEAM_HEIGHT/2, BEAM_WIDTH/2),))
fixed_region = assembly.Set(faces=fixed_face, name='FixedEnd')
model.EncastreBC(name='FixedSupport', createStepName='Initial', region=fixed_region)

print(f"  ✓ Encastre BC at x=0 (fixed end)")
print(f"    - All displacements = 0")
print(f"    - All rotations = 0")

# =============================================================================
# PHASE 6: LOADS
# =============================================================================

print("\n" + "-"*60)
print("PHASE 6: LOADS")
print("-"*60)

# Load at x=LENGTH
load_face = instance.faces.findAt(((BEAM_LENGTH, BEAM_HEIGHT/2, BEAM_WIDTH/2),))
load_surface = assembly.Surface(side1Faces=load_face, name='LoadSurface')

# Convert force to traction (force/area)
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

print(f"  ✓ Surface traction at x={BEAM_LENGTH} (free end)")
print(f"    - Total force: {APPLIED_FORCE} N")
print(f"    - Direction: Y (vertical)")
print(f"    - Traction: {traction_magnitude:.2f} MPa")

# =============================================================================
# PHASE 7: MESH
# =============================================================================

print("\n" + "-"*60)
print("PHASE 7: MESH")
print("-"*60)

part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)

elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType1, elemType2, elemType3))

part.generateMesh()

num_nodes = len(part.nodes)
num_elements = len(part.elements)

print(f"  ✓ Mesh generated")
print(f"    - Element size: {MESH_SIZE} mm")
print(f"    - Element type: C3D8R (8-node hex)")
print(f"    - Elements: {num_elements}")
print(f"    - Nodes: {num_nodes}")

if num_nodes > 1000:
    print(f"\n  ⚠️ WARNING: Node count ({num_nodes}) exceeds Learning Edition limit!")

# =============================================================================
# PHASE 8: CREATE AND RUN JOB
# =============================================================================

print("\n" + "-"*60)
print("PHASE 8: RUN ANALYSIS")
print("-"*60)

# Save model first
mdb.saveAs(pathName='CantileverBeam.cae')
print(f"  ✓ Model saved: CantileverBeam.cae")

# Create job
job = mdb.Job(name=JOB_NAME, model='CantileverBeam',
              description='Cantilever beam analysis', type=ANALYSIS)

# Write input file
job.writeInput(consistencyChecking=OFF)
print(f"  ✓ Input file written: {JOB_NAME}.inp")

# Submit job
print(f"\n  Submitting job '{JOB_NAME}'...")
print(f"  (This may take a moment)")

job.submit(consistencyChecking=OFF)
job.waitForCompletion()

print(f"  ✓ Job completed!")

# =============================================================================
# PHASE 9: QUICK RESULTS CHECK
# =============================================================================

print("\n" + "-"*60)
print("PHASE 9: RESULTS SUMMARY")
print("-"*60)

# Read results from ODB
from odbAccess import openOdb

odb_path = JOB_NAME + '.odb'
odb = openOdb(path=odb_path, readOnly=True)

# Get the last frame of the load step
step = odb.steps['LoadStep']
frame = step.frames[-1]

# Get displacement field
disp_field = frame.fieldOutputs['U']

# Find maximum displacement
max_disp_magnitude = 0.0
max_disp_node = None
for value in disp_field.values:
    if value.magnitude > max_disp_magnitude:
        max_disp_magnitude = value.magnitude
        max_disp_node = value.nodeLabel

# Get stress field
stress_field = frame.fieldOutputs['S']

# Find maximum Mises stress
max_mises = 0.0
max_stress_element = None
for value in stress_field.values:
    if hasattr(value, 'mises') and value.mises > max_mises:
        max_mises = value.mises
        max_stress_element = value.elementLabel

# Get reaction forces
rf_field = frame.fieldOutputs['RF']
total_rf_y = 0.0
for value in rf_field.values:
    if value.data[1] != 0:  # RF2 (Y direction)
        total_rf_y += value.data[1]

odb.close()

print(f"  Maximum displacement: {max_disp_magnitude:.6f} mm (Node {max_disp_node})")
print(f"  Maximum von Mises stress: {max_mises:.2f} MPa (Element {max_stress_element})")
print(f"  Total Y reaction force: {total_rf_y:.2f} N")

# =============================================================================
# ANALYTICAL COMPARISON
# =============================================================================

print("\n" + "-"*60)
print("ANALYTICAL COMPARISON")
print("-"*60)

# Beam theory (Euler-Bernoulli)
I = (BEAM_WIDTH * BEAM_HEIGHT**3) / 12  # Second moment of area
c = BEAM_HEIGHT / 2                      # Distance to neutral axis

# Max deflection at free end: delta = P*L^3 / (3*E*I)
P = abs(APPLIED_FORCE)
L = BEAM_LENGTH
E = YOUNGS_MODULUS

analytical_deflection = (P * L**3) / (3 * E * I)

# Max stress at fixed end: sigma = M*c/I = P*L*c/I
analytical_stress = (P * L * c) / I

print(f"  Analytical max deflection: {analytical_deflection:.6f} mm")
print(f"  Analytical max stress: {analytical_stress:.2f} MPa")
print(f"")
print(f"  FEA vs Analytical:")
print(f"    Deflection error: {100*abs(max_disp_magnitude - analytical_deflection)/analytical_deflection:.1f}%")
print(f"    Stress error: {100*abs(max_mises - analytical_stress)/analytical_stress:.1f}%")

# =============================================================================
# SUMMARY
# =============================================================================

print("\n" + "="*60)
print("STEP 3 COMPLETE - ANALYSIS FINISHED")
print("="*60)
print(f"""
Output files:
  ✓ CantileverBeam.cae  - Model database
  ✓ CantileverBeam.inp  - Input file
  ✓ CantileverBeam.odb  - Results database
  ✓ CantileverBeam.dat  - Printed output
  ✓ CantileverBeam.msg  - Solver messages
  ✓ CantileverBeam.sta  - Status file

Key Results:
  ✓ Max displacement: {max_disp_magnitude:.6f} mm
  ✓ Max von Mises stress: {max_mises:.2f} MPa
  ✓ Reaction force: {total_rf_y:.2f} N

Next: Run 04_analyze_results.py for detailed post-processing
      Or open CantileverBeam.odb in Abaqus/CAE Visualization
""")
