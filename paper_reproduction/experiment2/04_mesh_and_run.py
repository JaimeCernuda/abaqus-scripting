# 04_mesh_and_run.py - EXPERIMENT 2
#
# Meshes and runs Job 1 for Experiment 2
#
# Run with: abaqus cae noGUI=paper_reproduction/scripts/experiment2/04_mesh_and_run.py

from abaqus import *
from abaqusConstants import *
from caeModules import *

print("\n" + "=" * 70)
print("EXPERIMENT 2 - STEP 4: MESH AND RUN (JOB 1)")
print("=" * 70)

MESH_SIZE = 12.0  # Larger geometry needs adequate mesh
NODE_LIMIT = 1000
JOB_NAME = 'Exp2_Job1_Vertical'
MODEL_NAME = 'TO_Bracket_Exp2'
PART_NAME = 'Bracket'

print(f"\nMesh size: {MESH_SIZE} mm")
print(f"Job name: {JOB_NAME}")

# Load model
print("\n[1/4] Loading analysis model...")
openMdb(pathName='paper_reproduction/outputs/experiment2/TO_Bracket_Analysis.cae')
model = mdb.models[MODEL_NAME]
part = model.parts[PART_NAME]
print(f"       Model loaded")

# Seed and mesh
print("\n[2/4] Generating mesh...")
part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)

elemType = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setMeshControls(regions=part.cells, elemShape=TET, technique=FREE)
part.setElementType(regions=(part.cells,), elemTypes=(elemType,))
part.generateMesh()

num_nodes = len(part.nodes)
num_elements = len(part.elements)
print(f"       Nodes: {num_nodes}, Elements: {num_elements}")

if num_nodes > NODE_LIMIT:
    print(f"       WARNING: Exceeds {NODE_LIMIT} node limit!")

# Save meshed model
mdb.saveAs(pathName='paper_reproduction/outputs/experiment2/TO_Bracket_Meshed.cae')

# Create and run job
print("\n[3/4] Running job...")
job = mdb.Job(name=JOB_NAME, model=MODEL_NAME,
              description='Experiment 2 Job 1: Vertical load only',
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

print("\n" + "=" * 70)
print("EXPERIMENT 2 - STEP 4 COMPLETE")
print("=" * 70)
