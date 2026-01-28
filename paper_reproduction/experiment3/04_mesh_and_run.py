# 04_mesh_and_run.py - EXPERIMENT 3
#
# Meshes the bracket and runs Job 1 (vertical load only)
#
# Run with: abaqus cae noGUI=paper_reproduction/scripts/experiment3/04_mesh_and_run.py

from abaqus import *
from abaqusConstants import *
from caeModules import *
import os

print("\n" + "=" * 70)
print("EXPERIMENT 3 - STEP 4: MESH AND RUN (JOB 1)")
print("=" * 70)

MESH_SIZE = 12.0  # mm (adequate for this geometry)
NODE_LIMIT = 1000  # Learning Edition limit
JOB_NAME = 'Exp3_Job1_Vertical'
MODEL_NAME = 'TO_Bracket_Exp3'
PART_NAME = 'Bracket'

print(f"\nMesh size: {MESH_SIZE} mm")
print(f"Node limit: {NODE_LIMIT}")
print(f"Job name: {JOB_NAME}")

# Load model
print("\n[1/4] Loading analysis model...")
openMdb(pathName='paper_reproduction/outputs/experiment3/models/TO_Bracket_Analysis.cae')
model = mdb.models[MODEL_NAME]
part = model.parts[PART_NAME]
print(f"       Model loaded")

# Seed and mesh
print("\n[2/4] Generating mesh...")
part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)

# Use tetrahedral elements (C3D4) for complex geometry
elemType = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setMeshControls(regions=part.cells, elemShape=TET, technique=FREE)
part.setElementType(regions=(part.cells,), elemTypes=(elemType,))
part.generateMesh()

num_nodes = len(part.nodes)
num_elements = len(part.elements)
print(f"       Nodes: {num_nodes}")
print(f"       Elements: {num_elements}")

if num_nodes > NODE_LIMIT:
    print(f"       WARNING: Exceeds {NODE_LIMIT} node limit!")

# Save meshed model
mdb.saveAs(pathName='paper_reproduction/outputs/experiment3/models/TO_Bracket_Meshed.cae')

# Change to job output directory
os.chdir('paper_reproduction/outputs/experiment3/job1')

# Create and run job
print("\n[3/4] Creating and running job...")
job = mdb.Job(name=JOB_NAME, model=MODEL_NAME,
              description='Experiment 3 Job 1: Vertical load only (20 kN in -Z)',
              type=ANALYSIS, memory=90, memoryUnits=PERCENTAGE,
              getMemoryFromAnalysis=True, numCpus=1, numDomains=1)

job.writeInput(consistencyChecking=OFF)
print(f"       Input file: {JOB_NAME}.inp")

if num_nodes <= NODE_LIMIT:
    job.submit(consistencyChecking=OFF)
    job.waitForCompletion()
    print(f"       Job status: {job.status}")
else:
    print("       Job NOT submitted (node limit exceeded)")
    print(f"       Increase MESH_SIZE or use full Abaqus license")

# Return to original directory
os.chdir('../../../..')

print("\n[4/4] Saving final model...")
mdb.saveAs(pathName='paper_reproduction/outputs/experiment3/models/TO_Bracket_Meshed.cae')

print("\n" + "=" * 70)
print("EXPERIMENT 3 - STEP 4 COMPLETE")
print("=" * 70)
print(f"""
Job 1 Results:
  - Mesh: {num_nodes} nodes, {num_elements} elements
  - Output: paper_reproduction/outputs/experiment3/job1/{JOB_NAME}.odb
""")
