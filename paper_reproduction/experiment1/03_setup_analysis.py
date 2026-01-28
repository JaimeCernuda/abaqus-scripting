# 03_setup_analysis.py
#
# Sets up the complete analysis for the TO bracket:
# - Creates assembly instance
# - Defines analysis step with NLGEOM
# - Creates reference points for pin loading
# - Applies boundary conditions at lower pins
# - Applies loads at upper pin
#
# Two load cases per paper:
# 1. Fatigue test: 20 kN vertical only
# 2. TO design loads: 20 kN vertical + ±5 kN horizontal
#
# Run with: abaqus cae noGUI=paper_reproduction/scripts/03_setup_analysis.py
#
# Prerequisites: Run 01 and 02 scripts first

from abaqus import *
from abaqusConstants import *
from caeModules import *

print("\n" + "=" * 70)
print("PAPER REPRODUCTION - STEP 3: SETUP ANALYSIS")
print("=" * 70)

# =============================================================================
# LOADING PARAMETERS (from paper Table 1)
# =============================================================================

# Vertical load at upper pin (both load cases)
F_VERTICAL = 20000.0  # N (20 kN, negative = downward in Y)

# Horizontal loads at lower pins (TO design case only)
F_HORIZONTAL = 5000.0  # N (5 kN, ±X direction)

# Geometry parameters (must match 01_create_to_geometry.py)
TOTAL_HEIGHT = 146.17
TOTAL_WIDTH = 64.60
THICKNESS = 12.0
UPPER_TAB_HEIGHT = 25.0
LOWER_BLOCK_HEIGHT = 25.0
UPPER_PIN_DIAMETER = 10.0
LOWER_PIN_DIAMETER = 10.0
UPPER_PIN_CENTER_Y = TOTAL_HEIGHT - UPPER_TAB_HEIGHT / 2
LOWER_PIN_CENTER_Y = LOWER_BLOCK_HEIGHT / 2
LOWER_LEFT_CENTER_X = -TOTAL_WIDTH / 2
LOWER_RIGHT_CENTER_X = TOTAL_WIDTH / 2

# Model and part names
MODEL_NAME = 'TO_Bracket'
PART_NAME = 'Bracket'

print("\nLoad Parameters:")
print(f"  Vertical load (F1):   {F_VERTICAL/1000:.0f} kN (downward at upper pin)")
print(f"  Horizontal load (F2): ±{F_HORIZONTAL/1000:.0f} kN (at lower pins, TO case only)")

# =============================================================================
# LOAD EXISTING MODEL
# =============================================================================

print("\n[1/7] Loading material model...")

openMdb(pathName='paper_reproduction/outputs/experiment1/TO_Bracket_Material.cae')

model = mdb.models[MODEL_NAME]
part = model.parts[PART_NAME]

print(f"       Model '{MODEL_NAME}' loaded")

# =============================================================================
# CREATE ASSEMBLY
# =============================================================================

print("\n[2/7] Creating assembly...")

assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)

# Create instance of the bracket part
instance = assembly.Instance(name='Bracket-1', part=part, dependent=ON)

print("       Instance 'Bracket-1' created")

# =============================================================================
# CREATE REFERENCE POINTS FOR COUPLING
# =============================================================================

print("\n[3/7] Creating reference points for pin couplings...")

# Reference point at center of upper pin hole
rp_upper = assembly.ReferencePoint(point=(0.0, UPPER_PIN_CENTER_Y, THICKNESS / 2))
rp_upper_id = rp_upper.id
assembly.Set(referencePoints=(assembly.referencePoints[rp_upper_id],), name='RP_UpperPin')
print(f"       RP_UpperPin at (0, {UPPER_PIN_CENTER_Y:.1f}, {THICKNESS/2})")

# Reference point at center of lower left pin hole
rp_ll = assembly.ReferencePoint(
    point=(LOWER_LEFT_CENTER_X, LOWER_PIN_CENTER_Y, THICKNESS / 2)
)
rp_ll_id = rp_ll.id
assembly.Set(
    referencePoints=(assembly.referencePoints[rp_ll_id],), name='RP_LowerLeftPin'
)
print(
    f"       RP_LowerLeftPin at ({LOWER_LEFT_CENTER_X:.1f}, {LOWER_PIN_CENTER_Y:.1f}, {THICKNESS/2})"
)

# Reference point at center of lower right pin hole
rp_lr = assembly.ReferencePoint(
    point=(LOWER_RIGHT_CENTER_X, LOWER_PIN_CENTER_Y, THICKNESS / 2)
)
rp_lr_id = rp_lr.id
assembly.Set(
    referencePoints=(assembly.referencePoints[rp_lr_id],), name='RP_LowerRightPin'
)
print(
    f"       RP_LowerRightPin at ({LOWER_RIGHT_CENTER_X:.1f}, {LOWER_PIN_CENTER_Y:.1f}, {THICKNESS/2})"
)

# =============================================================================
# CREATE COUPLING CONSTRAINTS
# =============================================================================

print("\n[4/7] Creating coupling constraints...")

# Get the faces from the instance sets and create assembly-level surfaces
# This ensures the surfaces are written to the INP file

# Get face sequences from the instance
upper_faces = instance.sets['UpperPinSurface'].faces
ll_faces = instance.sets['LowerLeftPinSurface'].faces
lr_faces = instance.sets['LowerRightPinSurface'].faces

# Create assembly-level surfaces
assembly.Surface(name='Surf-UpperPin', side1Faces=upper_faces)
assembly.Surface(name='Surf-LowerLeftPin', side1Faces=ll_faces)
assembly.Surface(name='Surf-LowerRightPin', side1Faces=lr_faces)
print("       Assembly surfaces created from instance face sets")

# Upper pin coupling (distributing coupling for load application)
model.Coupling(
    name='Coupling-UpperPin',
    controlPoint=assembly.sets['RP_UpperPin'],
    surface=assembly.surfaces['Surf-UpperPin'],
    influenceRadius=WHOLE_SURFACE,
    couplingType=DISTRIBUTING,
    weightingMethod=UNIFORM,
    localCsys=None,
    u1=ON,
    u2=ON,
    u3=ON,
    ur1=ON,
    ur2=ON,
    ur3=ON,
)
print("       Coupling-UpperPin (distributing) created")

# Lower left pin coupling (kinematic for BC application)
model.Coupling(
    name='Coupling-LowerLeftPin',
    controlPoint=assembly.sets['RP_LowerLeftPin'],
    surface=assembly.surfaces['Surf-LowerLeftPin'],
    influenceRadius=WHOLE_SURFACE,
    couplingType=KINEMATIC,
    localCsys=None,
    u1=ON,
    u2=ON,
    u3=ON,
    ur1=ON,
    ur2=ON,
    ur3=ON,
)
print("       Coupling-LowerLeftPin (kinematic) created")

# Lower right pin coupling (kinematic for BC application)
model.Coupling(
    name='Coupling-LowerRightPin',
    controlPoint=assembly.sets['RP_LowerRightPin'],
    surface=assembly.surfaces['Surf-LowerRightPin'],
    influenceRadius=WHOLE_SURFACE,
    couplingType=KINEMATIC,
    localCsys=None,
    u1=ON,
    u2=ON,
    u3=ON,
    ur1=ON,
    ur2=ON,
    ur3=ON,
)
print("       Coupling-LowerRightPin (kinematic) created")

# =============================================================================
# CREATE ANALYSIS STEP
# =============================================================================

print("\n[5/7] Creating analysis step...")

# Static step with nonlinear geometry (NLGEOM) for plastic behavior
model.StaticStep(
    name='FatigueLoad',
    previous='Initial',
    description='20 kN vertical load at upper pin (fatigue test condition)',
    nlgeom=ON,  # Nonlinear geometry for large strain effects
    initialInc=0.1,
    maxInc=0.1,
    minInc=1e-8,
    maxNumInc=100,
)
print("       Step 'FatigueLoad' created (Static, NLGEOM=ON)")

# Request field outputs
model.FieldOutputRequest(
    name='F-Output-1',
    createStepName='FatigueLoad',
    variables=(
        'S',  # Stress
        'E',  # Strain
        'PE',  # Plastic strain
        'PEEQ',  # Equivalent plastic strain
        'U',  # Displacement
        'RF',  # Reaction forces
        'CF',  # Concentrated forces
    ),
)
print("       Field outputs requested: S, E, PE, PEEQ, U, RF, CF")

# Request history output at reference points
model.HistoryOutputRequest(
    name='H-Output-Pins',
    createStepName='FatigueLoad',
    variables=('U1', 'U2', 'U3', 'RF1', 'RF2', 'RF3'),
    region=assembly.sets['RP_UpperPin'],
)
print("       History outputs requested at upper pin RP")

# =============================================================================
# APPLY BOUNDARY CONDITIONS
# =============================================================================

print("\n[6/7] Applying boundary conditions...")

# Lower pins: Fix Y and Z (vertical and thickness), allow X (width) and all rotations
# This matches the paper's description: "fixed Y, Z at lower pins; free X translation/rotation"

# Lower left pin BC
model.DisplacementBC(
    name='BC-LowerLeftPin',
    createStepName='Initial',
    region=assembly.sets['RP_LowerLeftPin'],
    u1=UNSET,  # X free (allows horizontal displacement)
    u2=SET,  # Y fixed (vertical)
    u3=SET,  # Z fixed (thickness direction)
    ur1=UNSET,  # Rotation about X free
    ur2=UNSET,  # Rotation about Y free
    ur3=UNSET,  # Rotation about Z free
    amplitude=UNSET,
    distributionType=UNIFORM,
    fieldName='',
    localCsys=None,
)
print("       BC-LowerLeftPin: u2=0, u3=0 (Y,Z fixed; X,rotations free)")

# Lower right pin BC
model.DisplacementBC(
    name='BC-LowerRightPin',
    createStepName='Initial',
    region=assembly.sets['RP_LowerRightPin'],
    u1=UNSET,  # X free
    u2=SET,  # Y fixed
    u3=SET,  # Z fixed
    ur1=UNSET,
    ur2=UNSET,
    ur3=UNSET,
    amplitude=UNSET,
    distributionType=UNIFORM,
    fieldName='',
    localCsys=None,
)
print("       BC-LowerRightPin: u2=0, u3=0 (Y,Z fixed; X,rotations free)")

# Need to constrain at least one X DOF to prevent rigid body motion
# Fix X at one of the lower pins (left) to prevent horizontal drift
model.DisplacementBC(
    name='BC-LowerLeftPin-X',
    createStepName='Initial',
    region=assembly.sets['RP_LowerLeftPin'],
    u1=SET,  # Also fix X to prevent rigid body motion
    u2=UNSET,
    u3=UNSET,
    ur1=UNSET,
    ur2=UNSET,
    ur3=UNSET,
    amplitude=UNSET,
    distributionType=UNIFORM,
    fieldName='',
    localCsys=None,
)
print("       BC-LowerLeftPin-X: u1=0 (prevent rigid body motion)")

# =============================================================================
# APPLY LOADS
# =============================================================================

print("\n[7/7] Applying loads...")

# Vertical load at upper pin: -F_VERTICAL in Y direction (downward)
model.ConcentratedForce(
    name='Load-VerticalUpper',
    createStepName='FatigueLoad',
    region=assembly.sets['RP_UpperPin'],
    cf1=0.0,  # No X force
    cf2=-F_VERTICAL,  # Negative Y = downward
    cf3=0.0,  # No Z force
    distributionType=UNIFORM,
    field='',
    localCsys=None,
)
print(f"       Load-VerticalUpper: {F_VERTICAL/1000:.0f} kN downward at upper pin")

# Note: Horizontal loads (±5 kN) would be added for the TO design case
# For the fatigue test case (which we're simulating), only vertical load is applied
print("\n       Note: This is the FATIGUE TEST load case (vertical only)")
print("       For TO design loads, add ±5 kN horizontal at lower pins")

# =============================================================================
# SAVE MODEL
# =============================================================================

mdb.saveAs(pathName='paper_reproduction/outputs/experiment1/TO_Bracket_Analysis.cae')

print("\n" + "=" * 70)
print("STEP 3 COMPLETE - ANALYSIS SETUP")
print("=" * 70)
print(
    f"""
Output files:
  - paper_reproduction/outputs/experiment1/TO_Bracket_Analysis.cae

Analysis setup summary:
  - Instance: 'Bracket-1' in assembly
  - Reference points at all three pin centers
  - Coupling constraints: Distributing (upper), Kinematic (lower)
  - Step: 'FatigueLoad' (Static, NLGEOM=ON)
  - BCs: Lower pins fixed in Y, Z; left pin also fixed in X
  - Load: {F_VERTICAL/1000:.0f} kN downward at upper pin

Boundary condition details:
  - Lower left pin: u1=0, u2=0, u3=0 (fixed point)
  - Lower right pin: u2=0, u3=0, u1=free (roller in X)
  - This creates a simply-supported configuration

Load case:
  - Current: Fatigue test (vertical only)
  - Paper also used horizontal loads (±5 kN) for TO design

Next: Run 04_mesh_and_run.py to mesh the model and submit the job
"""
)
