# 05_job2_horizontal.py - EXPERIMENT 3
#
# Job 2: Adds horizontal spreading forces (F2) at lower pins
#
# Paper-aligned coordinate system:
# - X = horizontal spreading direction (SPREADING FORCE APPLIED HERE)
# - Y = pin axis / thickness
# - Z = vertical loading direction
#
# Load case from paper:
# - F1: 20 kN vertical (-Z) at upper pin
# - F2: 5 kN outward at each lower pin (spreading in +/-X)
#
# Run with: abaqus cae noGUI=paper_reproduction/scripts/experiment3/05_job2_horizontal.py

from abaqus import *
from abaqusConstants import *
from caeModules import *
import os

print("\n" + "=" * 70)
print("EXPERIMENT 3 - JOB 2: WITH HORIZONTAL LOADS")
print("=" * 70)

F_VERTICAL = 20000.0    # N (20 kN)
F_HORIZONTAL = 5000.0   # N (5 kN)

MODEL_NAME = 'TO_Bracket_Exp3'
JOB_NAME = 'Exp3_Job2_Horizontal'

print(f"\nLoad Case: Job 2 (Vertical + Horizontal Spreading)")
print(f"  F1 = {F_VERTICAL/1000:.0f} kN vertical (-Z)")
print(f"  F2 = {F_HORIZONTAL/1000:.0f} kN horizontal (+/-X spreading)")

# Load meshed model
print("\n[1/3] Loading meshed model...")
openMdb(pathName='paper_reproduction/outputs/experiment3/models/TO_Bracket_Meshed.cae')
model = mdb.models[MODEL_NAME]
assembly = model.rootAssembly
print("       Model loaded")

# Modify BCs to allow horizontal motion and add horizontal loads
print("\n[2/3] Modifying BCs and adding horizontal loads...")

# Delete existing fixed BCs for lower pins
if 'BC-LowerLeftPin' in model.boundaryConditions:
    del model.boundaryConditions['BC-LowerLeftPin']
if 'BC-LowerRightPin' in model.boundaryConditions:
    del model.boundaryConditions['BC-LowerRightPin']
print("       Deleted fixed BCs for lower pins")

# Create new BCs: Fix Y and Z, Allow X (spreading)
# u1=X (UNSET = free), u2=Y (SET = fixed), u3=Z (SET = fixed)
model.DisplacementBC(name='BC-LowerLeftPin', createStepName='Initial',
                     region=assembly.sets['RP_LowerLeftPin'],
                     u1=UNSET, u2=SET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET)
model.DisplacementBC(name='BC-LowerRightPin', createStepName='Initial',
                     region=assembly.sets['RP_LowerRightPin'],
                     u1=UNSET, u2=SET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET)
print("       Lower pins: Y,Z fixed; X free (allows spreading)")

# Add horizontal loads at lower pins
# Lower left: Force in -X direction (outward to the left)
# cf1=X, cf2=Y, cf3=Z
model.ConcentratedForce(name='Load-HorizLeft', createStepName='LoadStep',
                        region=assembly.sets['RP_LowerLeftPin'],
                        cf1=-F_HORIZONTAL, cf2=0.0, cf3=0.0)
print(f"       Lower left: {F_HORIZONTAL/1000:.0f} kN in -X (outward)")

# Lower right: Force in +X direction (outward to the right)
model.ConcentratedForce(name='Load-HorizRight', createStepName='LoadStep',
                        region=assembly.sets['RP_LowerRightPin'],
                        cf1=F_HORIZONTAL, cf2=0.0, cf3=0.0)
print(f"       Lower right: {F_HORIZONTAL/1000:.0f} kN in +X (outward)")

# Save modified model
mdb.saveAs(pathName='paper_reproduction/outputs/experiment3/models/TO_Bracket_Job2.cae')

# Change to job output directory
os.chdir('paper_reproduction/outputs/experiment3/job2')

# Create and run job
print("\n[3/3] Running Job 2...")
job = mdb.Job(name=JOB_NAME, model=MODEL_NAME,
              description='Experiment 3 Job 2: Vertical + Horizontal loads',
              type=ANALYSIS, memory=90, memoryUnits=PERCENTAGE,
              getMemoryFromAnalysis=True, numCpus=1, numDomains=1)

job.writeInput(consistencyChecking=OFF)
job.submit(consistencyChecking=OFF)
job.waitForCompletion()

print(f"       Job status: {job.status}")

# Return to original directory
os.chdir('../../../..')

print("\n" + "=" * 70)
print("EXPERIMENT 3 - JOB 2 COMPLETE")
print("=" * 70)
print(f"""
Total loads applied (Paper-aligned coordinates):
  - Upper pin (RP-1): {F_VERTICAL/1000:.0f} kN downward (-Z)
  - Lower left (RP-2): {F_HORIZONTAL/1000:.0f} kN outward (-X)
  - Lower right (RP-3): {F_HORIZONTAL/1000:.0f} kN outward (+X)

Output: paper_reproduction/outputs/experiment3/job2/{JOB_NAME}.odb
""")
