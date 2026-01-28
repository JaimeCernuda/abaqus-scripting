# 05_job2_horizontal.py - EXPERIMENT 2
#
# Job 2: Adds horizontal spreading forces (F2) at lower pins
#
# Coordinate system:
# - X = width (HORIZONTAL SPREADING DIRECTION, pin axis)
# - Y = height (vertical, F1 load direction)
# - Z = depth
#
# Load case from paper:
# - F1: 20 kN vertical (-Y) at upper pin
# - F2: 5 kN outward at each lower pin (spreading in ±X)
#
# Run with: abaqus cae noGUI=paper_reproduction/scripts/experiment2/05_job2_horizontal.py

from abaqus import *
from abaqusConstants import *
from caeModules import *

print("\n" + "=" * 70)
print("EXPERIMENT 2 - JOB 2: WITH HORIZONTAL LOADS")
print("=" * 70)

F_VERTICAL = 20000.0    # N (20 kN)
F_HORIZONTAL = 5000.0   # N (5 kN)

MODEL_NAME = 'TO_Bracket_Exp2'
JOB_NAME = 'Exp2_Job2_Horizontal'

print(f"\nLoad Case: Job 2 (Vertical + Horizontal)")
print(f"  F1 = {F_VERTICAL/1000:.0f} kN vertical (-Y)")
print(f"  F2 = {F_HORIZONTAL/1000:.0f} kN horizontal (±X spreading)")

# Load meshed model
print("\n[1/3] Loading meshed model...")
openMdb(pathName='paper_reproduction/outputs/experiment2/TO_Bracket_Meshed.cae')
model = mdb.models[MODEL_NAME]
assembly = model.rootAssembly
print("       Model loaded")

# For Job 2, we need to modify the BCs to allow horizontal motion
# The lower pins were fixed in all directions for Job 1
# For Job 2, we release the X constraint and apply horizontal loads

print("\n[2/3] Modifying BCs and adding horizontal loads...")

# First, modify the BCs to allow X motion (spreading)
# Delete the existing fixed BCs and create new ones that only fix Y, Z
if 'BC-LowerLeftPin' in model.boundaryConditions:
    del model.boundaryConditions['BC-LowerLeftPin']
if 'BC-LowerRightPin' in model.boundaryConditions:
    del model.boundaryConditions['BC-LowerRightPin']
print("       Deleted fixed BCs for lower pins")

# Create new BCs: Fix Y (vertical support), Fix Z (out of plane), Allow X (spreading)
model.DisplacementBC(name='BC-LowerLeftPin', createStepName='Initial',
                     region=assembly.sets['RP_LowerLeftPin'],
                     u1=UNSET, u2=SET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET)
model.DisplacementBC(name='BC-LowerRightPin', createStepName='Initial',
                     region=assembly.sets['RP_LowerRightPin'],
                     u1=UNSET, u2=SET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET)
print("       Lower pins: Y fixed, X free (allow spreading)")

# Lower left: Force in -X direction (outward to the left)
model.ConcentratedForce(name='Load-HorizLeft', createStepName='LoadStep',
                        region=assembly.sets['RP_LowerLeftPin'],
                        cf1=-F_HORIZONTAL, cf2=0.0, cf3=0.0)
print(f"       Lower left: {F_HORIZONTAL/1000:.0f} kN in -X")

# Lower right: Force in +X direction (outward to the right)
model.ConcentratedForce(name='Load-HorizRight', createStepName='LoadStep',
                        region=assembly.sets['RP_LowerRightPin'],
                        cf1=F_HORIZONTAL, cf2=0.0, cf3=0.0)
print(f"       Lower right: {F_HORIZONTAL/1000:.0f} kN in +X")

# Save and run
print("\n[3/3] Running Job 2...")
mdb.saveAs(pathName='paper_reproduction/outputs/experiment2/TO_Bracket_Job2.cae')

job = mdb.Job(name=JOB_NAME, model=MODEL_NAME,
              description='Experiment 2 Job 2: Vertical + Horizontal loads',
              type=ANALYSIS, memory=90, memoryUnits=PERCENTAGE,
              getMemoryFromAnalysis=True, numCpus=1, numDomains=1)

job.writeInput(consistencyChecking=OFF)
job.submit(consistencyChecking=OFF)
job.waitForCompletion()

print(f"       Job status: {job.status}")

print("\n" + "=" * 70)
print("EXPERIMENT 2 - JOB 2 COMPLETE")
print("=" * 70)
print(f"""
Total loads applied:
  - Upper pin: {F_VERTICAL/1000:.0f} kN down (-Y)
  - Lower left: {F_HORIZONTAL/1000:.0f} kN outward (-X)
  - Lower right: {F_HORIZONTAL/1000:.0f} kN outward (+X)

Output: {JOB_NAME}.odb
""")
