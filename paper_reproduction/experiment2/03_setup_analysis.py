# 03_setup_analysis.py - EXPERIMENT 2
#
# Sets up Job 1: Vertical load only (20 kN in -Y direction)
#
# Coordinate system for Experiment 2 (revised geometry):
# - X = width (horizontal, HOLES GO THROUGH HERE)
# - Y = height (vertical, LOADING DIRECTION)
# - Z = depth (thickness = 35mm)
#
# Run with: abaqus cae noGUI=paper_reproduction/scripts/experiment2/03_setup_analysis.py

from abaqus import *
from abaqusConstants import *
from caeModules import *

print("\n" + "=" * 70)
print("EXPERIMENT 2 - STEP 3: SETUP ANALYSIS (JOB 1)")
print("=" * 70)

# Load parameters
F_VERTICAL = 20000.0  # N (20 kN downward in -Y)

# Geometry parameters (must match 01_create_geometry_rotated.py)
TOTAL_HEIGHT = 146.17
TOTAL_WIDTH = 64.60
THICKNESS = 35.0  # Z depth

LOWER_BLOCK_SIZE = 35.0
UPPER_TAB_HEIGHT = 30.0

UPPER_PIN_CENTER_Y = TOTAL_HEIGHT - UPPER_TAB_HEIGHT / 2  # 131.17
LOWER_PIN_CENTER_Y = LOWER_BLOCK_SIZE / 2  # 17.5

LOWER_LEFT_X = -TOTAL_WIDTH / 2   # -32.3
LOWER_RIGHT_X = TOTAL_WIDTH / 2   # +32.3

MODEL_NAME = 'TO_Bracket_Exp2'
PART_NAME = 'Bracket'

print("\nLoad Case: Job 1 (Vertical Only)")
print(f"  F1 = {F_VERTICAL/1000:.0f} kN in -Y direction")

# Load model
print("\n[1/6] Loading material model...")
openMdb(pathName='paper_reproduction/outputs/experiment2/TO_Bracket_Material.cae')
model = mdb.models[MODEL_NAME]
part = model.parts[PART_NAME]
assembly = model.rootAssembly

# Get instance
if 'BracketInstance' in assembly.instances:
    instance = assembly.instances['BracketInstance']
    print("       Using existing instance")
else:
    assembly.DatumCsysByDefault(CARTESIAN)
    instance = assembly.Instance(name='BracketInstance', part=part, dependent=ON)
    print("       Created new instance")

# Create reference points at pin centers
print("\n[2/6] Creating reference points...")

# Pin centers are at (X, Y, Z) = (x_pos, y_pos, THICKNESS/2)
# Upper pin at center of upper tab
rp_upper = assembly.ReferencePoint(point=(0.0, UPPER_PIN_CENTER_Y, THICKNESS / 2))
assembly.Set(referencePoints=(assembly.referencePoints[rp_upper.id],), name='RP_UpperPin')
print(f"       RP_UpperPin at (0, {UPPER_PIN_CENTER_Y:.1f}, {THICKNESS/2:.1f})")

# Lower left pin
rp_ll = assembly.ReferencePoint(point=(LOWER_LEFT_X, LOWER_PIN_CENTER_Y, THICKNESS / 2))
assembly.Set(referencePoints=(assembly.referencePoints[rp_ll.id],), name='RP_LowerLeftPin')
print(f"       RP_LowerLeftPin at ({LOWER_LEFT_X:.1f}, {LOWER_PIN_CENTER_Y:.1f}, {THICKNESS/2:.1f})")

# Lower right pin
rp_lr = assembly.ReferencePoint(point=(LOWER_RIGHT_X, LOWER_PIN_CENTER_Y, THICKNESS / 2))
assembly.Set(referencePoints=(assembly.referencePoints[rp_lr.id],), name='RP_LowerRightPin')
print(f"       RP_LowerRightPin at ({LOWER_RIGHT_X:.1f}, {LOWER_PIN_CENTER_Y:.1f}, {THICKNESS/2:.1f})")

# Create coupling constraints
print("\n[3/6] Creating couplings...")

# Get faces from instance
upper_faces = instance.sets['UpperPinSurface'].faces
ll_faces = instance.sets['LowerLeftPinSurface'].faces
lr_faces = instance.sets['LowerRightPinSurface'].faces

assembly.Surface(name='Surf-UpperPin', side1Faces=upper_faces)
assembly.Surface(name='Surf-LowerLeftPin', side1Faces=ll_faces)
assembly.Surface(name='Surf-LowerRightPin', side1Faces=lr_faces)

# Upper pin - distributing coupling for load
model.Coupling(name='Coupling-UpperPin', controlPoint=assembly.sets['RP_UpperPin'],
               surface=assembly.surfaces['Surf-UpperPin'], influenceRadius=WHOLE_SURFACE,
               couplingType=DISTRIBUTING, weightingMethod=UNIFORM, localCsys=None,
               u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
print("       Coupling-UpperPin")

# Lower pins - kinematic for BC
model.Coupling(name='Coupling-LowerLeftPin', controlPoint=assembly.sets['RP_LowerLeftPin'],
               surface=assembly.surfaces['Surf-LowerLeftPin'], influenceRadius=WHOLE_SURFACE,
               couplingType=KINEMATIC, localCsys=None,
               u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
model.Coupling(name='Coupling-LowerRightPin', controlPoint=assembly.sets['RP_LowerRightPin'],
               surface=assembly.surfaces['Surf-LowerRightPin'], influenceRadius=WHOLE_SURFACE,
               couplingType=KINEMATIC, localCsys=None,
               u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
print("       Lower pin couplings")

# Create analysis step
print("\n[4/6] Creating analysis step...")
model.StaticStep(name='LoadStep', previous='Initial',
                 description='Experiment 2 Job 1: 20 kN vertical',
                 nlgeom=ON, initialInc=0.1, maxInc=0.1, minInc=1e-8, maxNumInc=100)

model.FieldOutputRequest(name='F-Output-1', createStepName='LoadStep',
                         variables=('S', 'E', 'PE', 'PEEQ', 'U', 'RF', 'CF'))

# Apply BCs and loads
print("\n[5/6] Applying BCs and loads...")

# Lower pins: Fixed in X, Y, Z (allow rotation around pin axis = X)
model.DisplacementBC(name='BC-LowerLeftPin', createStepName='Initial',
                     region=assembly.sets['RP_LowerLeftPin'],
                     u1=SET, u2=SET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET)
model.DisplacementBC(name='BC-LowerRightPin', createStepName='Initial',
                     region=assembly.sets['RP_LowerRightPin'],
                     u1=SET, u2=SET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET)
print("       BCs: lower pins fixed")

# Upper pin: Vertical load in -Y direction (downward)
model.ConcentratedForce(name='Load-Vertical', createStepName='LoadStep',
                        region=assembly.sets['RP_UpperPin'],
                        cf1=0.0, cf2=-F_VERTICAL, cf3=0.0)
print(f"       Load: {F_VERTICAL/1000:.0f} kN in -Y")

# Save
print("\n[6/6] Saving...")
mdb.saveAs(pathName='paper_reproduction/outputs/experiment2/TO_Bracket_Analysis.cae')

print("\n" + "=" * 70)
print("STEP 3 COMPLETE")
print("=" * 70)
