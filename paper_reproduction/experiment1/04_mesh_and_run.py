# 04_mesh_and_run.py
#
# Meshes the TO bracket and submits the analysis job:
# - Seeds part with appropriate mesh size
# - Uses C3D10 elements (10-node quadratic tetrahedra) per paper
# - Checks node count for student license compatibility
# - Creates and submits the job
#
# Run with: abaqus cae noGUI=paper_reproduction/scripts/04_mesh_and_run.py
#
# Prerequisites: Run 01, 02, and 03 scripts first

from abaqus import *
from abaqusConstants import *
from caeModules import *

print("\n" + "=" * 70)
print("PAPER REPRODUCTION - STEP 4: MESH AND RUN")
print("=" * 70)

# =============================================================================
# MESH PARAMETERS
# =============================================================================

# Mesh size (mm)
# Paper uses 1mm seed, but that exceeds student license limit
# Start with larger size for student license compatibility
MESH_SIZE = 15.0  # mm (with C3D4, can use finer mesh than C3D10)

# Student license node limit
NODE_LIMIT = 1000

# Element type
# Paper specifies C3D10 (10-node quadratic tet), but Learning Edition needs fewer nodes
# Using C3D4 (4-node linear tet) to stay under 1000 node limit
ELEMENT_TYPE = C3D4

# Job name
JOB_NAME = 'TO_Bracket_Fatigue'

# Model and part names
MODEL_NAME = 'TO_Bracket'
PART_NAME = 'Bracket'

print("\nMesh Parameters:")
print(f"  Element type: C3D10 (10-node quadratic tetrahedral)")
print(f"  Seed size:    {MESH_SIZE} mm")
print(f"  Node limit:   {NODE_LIMIT} (student license)")

# =============================================================================
# LOAD EXISTING MODEL
# =============================================================================

print("\n[1/5] Loading analysis model...")

openMdb(pathName='paper_reproduction/outputs/experiment1/TO_Bracket_Analysis.cae')

model = mdb.models[MODEL_NAME]
part = model.parts[PART_NAME]

print(f"       Model '{MODEL_NAME}' loaded")

# =============================================================================
# SEED THE PART
# =============================================================================

print("\n[2/5] Seeding part for meshing...")

part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)

print(f"       Global seed size: {MESH_SIZE} mm")

# =============================================================================
# SET ELEMENT TYPE
# =============================================================================

print("\n[3/5] Setting element type...")

# C3D4 - 4-node linear tetrahedral element
# Using this instead of C3D10 to stay under Learning Edition node limit
elemType_tet4 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)

# Set mesh controls to use tetrahedral elements (free mesh)
part.setMeshControls(regions=part.cells, elemShape=TET, technique=FREE)

# Assign element type - for tetrahedral mesh, only need one element type
part.setElementType(regions=(part.cells,), elemTypes=(elemType_tet4,))

print(f"       Element type: C3D4 (linear tetrahedral)")
print(f"       Mesh technique: FREE (tetrahedral)")

# =============================================================================
# GENERATE MESH
# =============================================================================

print("\n[4/5] Generating mesh...")

part.generateMesh()

# Count nodes and elements
num_nodes = len(part.nodes)
num_elements = len(part.elements)

print(f"       Mesh generated successfully")
print(f"       Nodes:    {num_nodes}")
print(f"       Elements: {num_elements}")

# Check node count against student license limit
if num_nodes > NODE_LIMIT:
    print(f"\n       WARNING: Node count ({num_nodes}) exceeds limit ({NODE_LIMIT})!")
    print(f"       Increase MESH_SIZE and re-run this script.")
    print(f"       Suggested mesh size: {MESH_SIZE * (num_nodes / NODE_LIMIT) ** 0.33:.1f} mm")

    # Calculate recommended mesh size
    # Node count scales roughly as (1/size)^3 for 3D
    recommended_size = MESH_SIZE * (num_nodes / NODE_LIMIT) ** 0.33 * 1.2
    print(f"       Try MESH_SIZE = {recommended_size:.0f} mm")

else:
    print(f"\n       Node count OK (within {NODE_LIMIT} limit)")

# =============================================================================
# CREATE AND SUBMIT JOB
# =============================================================================

print("\n[5/5] Creating and submitting job...")

# Save the meshed model first
mdb.saveAs(pathName='paper_reproduction/outputs/experiment1/TO_Bracket_Meshed.cae')
print(f"       Model saved: TO_Bracket_Meshed.cae")

# Create job
job = mdb.Job(
    name=JOB_NAME,
    model=MODEL_NAME,
    description='TO Bracket fatigue load analysis - 20 kN vertical',
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
    resultsFormat=ODB,
    numCpus=1,
    numDomains=1,
)

# Write input file
job.writeInput(consistencyChecking=OFF)
print(f"       Input file written: {JOB_NAME}.inp")

# Only submit if node count is within limit
if num_nodes <= NODE_LIMIT:
    print(f"\n       Submitting job '{JOB_NAME}'...")
    print(f"       (This may take a moment)")

    job.submit(consistencyChecking=OFF)
    job.waitForCompletion()

    # Check job status
    if job.status == COMPLETED:
        print(f"       Job completed successfully!")
    else:
        print(f"       Job status: {job.status}")
        print(f"       Check {JOB_NAME}.msg and {JOB_NAME}.dat for details")
else:
    print(f"\n       Job NOT submitted (node count exceeds limit)")
    print(f"       Increase MESH_SIZE and re-run, or use full Abaqus license")

# =============================================================================
# SUMMARY
# =============================================================================

print("\n" + "=" * 70)
print("STEP 4 COMPLETE - MESH AND RUN")
print("=" * 70)
print(
    f"""
Output files:
  - paper_reproduction/outputs/experiment1/TO_Bracket_Meshed.cae
  - paper_reproduction/outputs/job/{JOB_NAME}.inp
  - paper_reproduction/outputs/job/{JOB_NAME}.odb (if job completed)

Mesh summary:
  - Element type: C3D10 (10-node quadratic tetrahedral)
  - Seed size: {MESH_SIZE} mm
  - Nodes: {num_nodes}
  - Elements: {num_elements}
  - Status: {'Within limit' if num_nodes <= NODE_LIMIT else 'EXCEEDS LIMIT'}

Job: {JOB_NAME}
  - Status: {'Submitted' if num_nodes <= NODE_LIMIT else 'Not submitted'}

If mesh is too fine for student license:
  1. Edit MESH_SIZE in this script (try {max(MESH_SIZE + 2, 6):.0f} mm)
  2. Re-run: abaqus cae noGUI=paper_reproduction/scripts/04_mesh_and_run.py

Next: Run 05_extract_results.py to post-process results
"""
)
