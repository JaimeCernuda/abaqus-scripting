# 03b_setup_job2_horizontal.py
#
# Creates Job 2: TO design load case with horizontal forces
# Adds ±5 kN horizontal loads at lower pins (in addition to 20 kN vertical)
#
# Load case from paper Table 1:
# - F1: 20 kN vertical at upper pin (downward)
# - F2: +5 kN at lower left pin (outward, -X direction)
# - F2: -5 kN at lower right pin (outward, +X direction)
#
# Run with: abaqus cae noGUI=paper_reproduction/scripts/03b_setup_job2_horizontal.py
#
# Prerequisites: Run 01, 02, and 03 scripts first (need TO_Bracket_Analysis.cae)

from abaqus import *
from abaqusConstants import *
from caeModules import *

print("\n" + "=" * 70)
print("EXPERIMENT 1 - JOB 2: TO DESIGN LOADS (WITH HORIZONTAL)")
print("=" * 70)

# =============================================================================
# PARAMETERS
# =============================================================================

# Loads from paper Table 1
F_VERTICAL = 20000.0    # N (20 kN downward at upper pin)
F_HORIZONTAL = 5000.0   # N (5 kN at each lower pin, opposing directions)

# Model names
MODEL_NAME = 'TO_Bracket'
PART_NAME = 'Bracket'
JOB_NAME = 'TO_Bracket_Job2_Horizontal'

print("\nLoad Case: TO Design (with horizontal)")
print(f"  Vertical (upper pin): {F_VERTICAL/1000:.0f} kN downward")
print(f"  Horizontal (lower left): {F_HORIZONTAL/1000:.0f} kN in -X direction")
print(f"  Horizontal (lower right): {F_HORIZONTAL/1000:.0f} kN in +X direction")

# =============================================================================
# LOAD MODEL
# =============================================================================

print("\n[1/4] Loading analysis model...")

openMdb(pathName='paper_reproduction/outputs/experiment1/TO_Bracket_Meshed.cae')

model = mdb.models[MODEL_NAME]
assembly = model.rootAssembly

print(f"       Model '{MODEL_NAME}' loaded")

# =============================================================================
# MODIFY STEP NAME FOR CLARITY
# =============================================================================

print("\n[2/4] Renaming step for Job 2...")

# Rename the existing step to indicate this is the TO design case
# Note: Can't rename steps in Abaqus, so we'll just add the horizontal loads
# to the existing FatigueLoad step

print("       Using existing 'FatigueLoad' step")
print("       (Adding horizontal loads to vertical load)")

# =============================================================================
# ADD HORIZONTAL LOADS
# =============================================================================

print("\n[3/4] Adding horizontal loads at lower pins...")

# Lower left pin: Force in -X direction (outward from center)
model.ConcentratedForce(
    name='Load-HorizontalLowerLeft',
    createStepName='FatigueLoad',
    region=assembly.sets['RP_LowerLeftPin'],
    cf1=-F_HORIZONTAL,  # -X direction (outward)
    cf2=0.0,
    cf3=0.0,
    distributionType=UNIFORM,
    field='',
    localCsys=None,
)
print(f"       Load-HorizontalLowerLeft: {F_HORIZONTAL/1000:.0f} kN in -X")

# Lower right pin: Force in +X direction (outward from center)
model.ConcentratedForce(
    name='Load-HorizontalLowerRight',
    createStepName='FatigueLoad',
    region=assembly.sets['RP_LowerRightPin'],
    cf1=F_HORIZONTAL,  # +X direction (outward)
    cf2=0.0,
    cf3=0.0,
    distributionType=UNIFORM,
    field='',
    localCsys=None,
)
print(f"       Load-HorizontalLowerRight: {F_HORIZONTAL/1000:.0f} kN in +X")

# =============================================================================
# SAVE AND CREATE JOB
# =============================================================================

print("\n[4/4] Creating and submitting Job 2...")

# Save model with new loads
mdb.saveAs(pathName='paper_reproduction/outputs/experiment1/TO_Bracket_Job2.cae')
print(f"       Model saved: TO_Bracket_Job2.cae")

# Create job
job = mdb.Job(
    name=JOB_NAME,
    model=MODEL_NAME,
    description='TO Bracket - Job 2: 20kN vertical + 5kN horizontal loads',
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

# Write input and submit
job.writeInput(consistencyChecking=OFF)
print(f"       Input file written: {JOB_NAME}.inp")

print(f"\n       Submitting job '{JOB_NAME}'...")
job.submit(consistencyChecking=OFF)
job.waitForCompletion()

if job.status == COMPLETED:
    print(f"       Job completed successfully!")
else:
    print(f"       Job status: {job.status}")

# =============================================================================
# SUMMARY
# =============================================================================

print("\n" + "=" * 70)
print("JOB 2 COMPLETE")
print("=" * 70)
print(f"""
Load case: TO Design (with horizontal forces)
  - Upper pin: {F_VERTICAL/1000:.0f} kN downward (Y)
  - Lower left pin: {F_HORIZONTAL/1000:.0f} kN outward (-X)
  - Lower right pin: {F_HORIZONTAL/1000:.0f} kN outward (+X)

Output files:
  - paper_reproduction/outputs/experiment1/TO_Bracket_Job2.cae
  - {JOB_NAME}.inp
  - {JOB_NAME}.odb

Next: Run 05b_extract_job2_results.py to extract results
""")
