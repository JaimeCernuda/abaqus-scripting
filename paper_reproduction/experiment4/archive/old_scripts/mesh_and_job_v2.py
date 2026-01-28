# -*- coding: utf-8 -*-
"""
Experiment 4: Mesh and Job - Simplified
"""

from abaqus import *
from abaqusConstants import *
from caeModules import *
import mesh
import os

# Open existing model
openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen.cae')

model_name = 'Experiment4_TO_Specimen'
part_name = 'TO_Specimen'

model = mdb.models[model_name]
part = model.parts[part_name]
assembly = model.rootAssembly

# =============================================================================
# CLEAR EXISTING MESH
# =============================================================================
part.deleteMesh()

# =============================================================================
# MESH CONFIGURATION
# =============================================================================
MESH_SIZE = 10.0  # mm

part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)

# Use C3D4 (linear tetrahedral) for fewer nodes
elem_type = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elem_type, elem_type, elem_type))
part.setMeshControls(regions=part.cells, technique=FREE, elemShape=TET)

part.generateMesh()

num_nodes = len(part.nodes)
num_elements = len(part.elements)
print("Mesh: {} nodes, {} elements".format(num_nodes, num_elements))

if num_nodes > 1000:
    print("WARNING: Exceeds 1000 node limit!")
else:
    print("OK: Within node limit")

assembly.regenerate()

# =============================================================================
# CREATE JOB
# =============================================================================
job_name = 'Experiment4_Job1'
work_dir = r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4'

if job_name in mdb.jobs.keys():
    del mdb.jobs[job_name]

job = mdb.Job(
    name=job_name,
    model=model_name,
    description='Experiment 4: FatigueTest - 20kN vertical load',
    type=ANALYSIS,
    memory=90,
    memoryUnits=PERCENTAGE,
    numCpus=1,
)

# Change to work directory and write input
os.chdir(work_dir)
job.writeInput(consistencyChecking=OFF)
print("Input file written to: {}".format(work_dir))

# =============================================================================
# SAVE
# =============================================================================
mdb.saveAs(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen.cae')

print("\n" + "="*50)
print("MESH AND JOB READY")
print("Nodes: {}, Elements: {}".format(num_nodes, num_elements))
print("Job: {}".format(job_name))
print("="*50)
