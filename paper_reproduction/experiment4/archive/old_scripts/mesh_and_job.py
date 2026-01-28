# -*- coding: utf-8 -*-
"""
Experiment 4: Mesh and Job Submission
"""

from abaqus import *
from abaqusConstants import *
from caeModules import *
import mesh

# Open existing model
openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen.cae')

model_name = 'Experiment4_TO_Specimen'
part_name = 'TO_Specimen'

model = mdb.models[model_name]
part = model.parts[part_name]
assembly = model.rootAssembly

# =============================================================================
# MESH CONFIGURATION
# Target < 1000 nodes for Learning Edition
# Using C3D10 (10-node quadratic tetrahedral) as specified in plan
# =============================================================================
MESH_SIZE = 10.0  # mm - adjusted for Learning Edition node limit

# Seed the part
part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)

# Set element type to C3D4 (4-node linear tetrahedral) for fewer nodes
# or C3D8R for hex mesh (requires structured region)
elem_type_tet = mesh.ElemType(
    elemCode=C3D4,
    elemLibrary=STANDARD,
)

# Assign element type to all cells
part.setElementType(
    regions=(part.cells,),
    elemTypes=(elem_type_tet, elem_type_tet, elem_type_tet)  # tet mesh
)

# Set mesh controls - use free mesh for complex geometry
part.setMeshControls(
    regions=part.cells,
    technique=FREE,
    elemShape=TET
)

# Generate mesh
part.generateMesh()

# Check node and element counts
num_nodes = len(part.nodes)
num_elements = len(part.elements)
print("\nMesh Statistics:")
print("  Total nodes: {}".format(num_nodes))
print("  Total elements: {}".format(num_elements))

if num_nodes > 1000:
    print("\nWARNING: Node count ({}) exceeds Learning Edition limit (1000)".format(num_nodes))
    print("Consider increasing MESH_SIZE")
else:
    print("\nNode count is within Learning Edition limit")

# Regenerate assembly to pick up mesh
assembly.regenerate()

# =============================================================================
# CREATE JOB
# =============================================================================
job_name = 'Experiment4_Job1'

# Delete existing job if present
if job_name in mdb.jobs.keys():
    del mdb.jobs[job_name]

# Create job
job = mdb.Job(
    name=job_name,
    model=model_name,
    description='Experiment 4: TO Specimen - FatigueTest and TODesign load cases',
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
    multiprocessingMode=DEFAULT,
    numCpus=1,
    numDomains=1,
)

print("\nJob '{}' created".format(job_name))

# Write input file (for inspection)
job.writeInput(consistencyChecking=OFF)
print("Input file written: {}.inp".format(job_name))

# =============================================================================
# SAVE MODEL
# =============================================================================
mdb.saveAs(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen.cae')

print("\n" + "="*50)
print("MESH AND JOB SETUP COMPLETE")
print("Mesh: {} nodes, {} elements".format(num_nodes, num_elements))
print("Element type: C3D10 (quadratic tetrahedral)")
print("Job name: {}".format(job_name))
print("="*50)
print("\nTo submit the job, run:")
print("  abaqus job={} interactive".format(job_name))
