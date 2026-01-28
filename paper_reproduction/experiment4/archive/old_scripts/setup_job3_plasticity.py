# -*- coding: utf-8 -*-
"""
Experiment 4: Setup Job 3 - High Load for Plasticity
Explore elastic-plastic response by increasing load to induce yielding
"""

from abaqus import *
from abaqusConstants import *
from caeModules import *
import os

# Open existing model
openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen.cae')

model_name = 'Experiment4_TO_Specimen'
part_name = 'TO_Specimen'
instance_name = part_name + '-1'

model = mdb.models[model_name]
assembly = model.rootAssembly

# =============================================================================
# ANALYSIS PARAMETERS
# =============================================================================
# Job 1 with 20 kN gave max stress of ~236 MPa
# To reach proportional limit of 980 MPa, need ~4.15x more load
# To exceed yield (1191 MPa), need ~5x more load
# Let's use 100 kN to definitely induce plasticity

HIGH_LOAD = 100000.0  # 100 kN - should induce significant plasticity

# =============================================================================
# CREATE NEW STEP FOR HIGH LOAD (or modify existing)
# =============================================================================
# Add a PlasticityTest step after TODesign
if 'PlasticityTest' not in model.steps.keys():
    model.StaticStep(
        name='PlasticityTest',
        previous='TODesign',
        nlgeom=ON,
        initialInc=0.05,  # Smaller increments for plasticity
        maxNumInc=200,
        minInc=1e-10,
        maxInc=0.1,
    )
    print("Step 'PlasticityTest' created")

# =============================================================================
# MODIFY LOAD IN PLASTICITY STEP
# The vertical load propagates from FatigueTest.
# We'll modify it in the PlasticityTest step.
# =============================================================================
# Get the upper RP region
upper_rp_region = assembly.sets['UpperRP']

# Modify the existing load in PlasticityTest step
# First, deactivate in FatigueTest propagation if needed
model.loads['VerticalLoad_20kN'].setValuesInStep(
    stepName='PlasticityTest',
    cf2=HIGH_LOAD  # Increase to 100 kN
)
print("Load increased to {} kN in PlasticityTest step".format(HIGH_LOAD/1000))

# =============================================================================
# CREATE JOB 3
# =============================================================================
job_name = 'Experiment4_Job3'
work_dir = r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4'

if job_name in mdb.jobs.keys():
    del mdb.jobs[job_name]

job = mdb.Job(
    name=job_name,
    model=model_name,
    description='Experiment 4: PlasticityTest - 100kN vertical load (plasticity)',
    type=ANALYSIS,
    memory=90,
    memoryUnits=PERCENTAGE,
    numCpus=1,
)

os.chdir(work_dir)
job.writeInput(consistencyChecking=OFF)
print("\nJob '{}' input file written".format(job_name))

# =============================================================================
# SAVE
# =============================================================================
mdb.saveAs(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen.cae')

print("\n" + "="*50)
print("JOB 3 SETUP COMPLETE - PLASTICITY TEST")
print("Load: {} kN".format(HIGH_LOAD/1000))
print("Expected: Significant plasticity (stress > 980 MPa)")
print("="*50)
