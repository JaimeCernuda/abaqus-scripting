# 03_setup_analysis.py - EXPERIMENT 3
#
# Sets up Job 1: Vertical load only (20 kN in -Z direction)
#
# Paper-aligned coordinate system:
# - X = horizontal spreading direction
# - Y = pin axis / thickness
# - Z = vertical loading direction (LOAD APPLIED HERE)
#
# Run with: abaqus cae noGUI=paper_reproduction/scripts/experiment3/03_setup_analysis.py

from abaqus import *
from abaqusConstants import *
from caeModules import *

print("\n" + "=" * 70)
print("EXPERIMENT 3 - STEP 3: SETUP ANALYSIS (JOB 1)")
print("=" * 70)

# Load parameters
F_VERTICAL = 20000.0  # N (20 kN downward in -Z)

# Geometry parameters (must match 01_create_geometry.py)
TOTAL_HEIGHT = 146.17       # Z extent
TOTAL_WIDTH = 64.60         # X extent
THICKNESS = 35.0            # Y extent

LOWER_BLOCK_SIZE = 35.0
UPPER_TAB_HEIGHT = 30.0

# Pin center Z coordinates (vertical positions)
UPPER_PIN_CENTER_Z = TOTAL_HEIGHT - UPPER_TAB_HEIGHT / 2  # 131.17
LOWER_PIN_CENTER_Z = LOWER_BLOCK_SIZE / 2  # 17.5

# Pin center X coordinates
LOWER_LEFT_X = -TOTAL_WIDTH / 2   # -32.3
LOWER_RIGHT_X = TOTAL_WIDTH / 2   # +32.3

# All pins at Y = THICKNESS / 2 (center of thickness)
PIN_Y = THICKNESS / 2  # 17.5

MODEL_NAME = 'TO_Bracket_Exp3'
PART_NAME = 'Bracket'

print("\nLoad Case: Job 1 (Vertical Only)")
print(f"  F1 = {F_VERTICAL/1000:.0f} kN in -Z direction (downward)")
print("\nReference Point Locations:")
print(f"  RP_UpperPin:      (0, {PIN_Y:.1f}, {UPPER_PIN_CENTER_Z:.2f})")
print(f"  RP_LowerLeftPin:  ({LOWER_LEFT_X:.1f}, {PIN_Y:.1f}, {LOWER_PIN_CENTER_Z:.1f})")
print(f"  RP_LowerRightPin: ({LOWER_RIGHT_X:.1f}, {PIN_Y:.1f}, {LOWER_PIN_CENTER_Z:.1f})")

# Load model
print("\n[1/6] Loading material model...")
openMdb(pathName='paper_reproduction/outputs/experiment3/models/TO_Bracket_Material.cae')
model = mdb.models[MODEL_NAME]
part = model.parts[PART_NAME]
assembly = model.rootAssembly

# Get or create instance
if 'BracketInstance' in assembly.instances:
    instance = assembly.instances['BracketInstance']
    print("       Using existing instance")
else:
    assembly.DatumCsysByDefault(CARTESIAN)
    instance = assembly.Instance(name='BracketInstance', part=part, dependent=ON)
    print("       Created new instance")

# Create reference points at pin centers
print("\n[2/6] Creating reference points...")

# Upper pin at (0, Y_center, Z_upper)
rp_upper = assembly.ReferencePoint(point=(0.0, PIN_Y, UPPER_PIN_CENTER_Z))
assembly.Set(referencePoints=(assembly.referencePoints[rp_upper.id],), name='RP_UpperPin')
print(f"       RP_UpperPin at (0, {PIN_Y:.1f}, {UPPER_PIN_CENTER_Z:.2f})")

# Lower left pin
rp_ll = assembly.ReferencePoint(point=(LOWER_LEFT_X, PIN_Y, LOWER_PIN_CENTER_Z))
assembly.Set(referencePoints=(assembly.referencePoints[rp_ll.id],), name='RP_LowerLeftPin')
print(f"       RP_LowerLeftPin at ({LOWER_LEFT_X:.1f}, {PIN_Y:.1f}, {LOWER_PIN_CENTER_Z:.1f})")

# Lower right pin
rp_lr = assembly.ReferencePoint(point=(LOWER_RIGHT_X, PIN_Y, LOWER_PIN_CENTER_Z))
assembly.Set(referencePoints=(assembly.referencePoints[rp_lr.id],), name='RP_LowerRightPin')
print(f"       RP_LowerRightPin at ({LOWER_RIGHT_X:.1f}, {PIN_Y:.1f}, {LOWER_PIN_CENTER_Z:.1f})")

# Create coupling constraints
print("\n[3/6] Creating couplings...")

# Get pin surfaces from instance
upper_faces = instance.sets['UpperPinSurface'].faces
ll_faces = instance.sets['LowerLeftPinSurface'].faces
lr_faces = instance.sets['LowerRightPinSurface'].faces

assembly.Surface(name='Surf-UpperPin', side1Faces=upper_faces)
assembly.Surface(name='Surf-LowerLeftPin', side1Faces=ll_faces)
assembly.Surface(name='Surf-LowerRightPin', side1Faces=lr_faces)

# Upper pin - distributing coupling for load application
model.Coupling(name='Coupling-UpperPin', controlPoint=assembly.sets['RP_UpperPin'],
               surface=assembly.surfaces['Surf-UpperPin'], influenceRadius=WHOLE_SURFACE,
               couplingType=DISTRIBUTING, weightingMethod=UNIFORM, localCsys=None,
               u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
print("       Coupling-UpperPin (DISTRIBUTING)")

# Lower pins - kinematic coupling for BC
model.Coupling(name='Coupling-LowerLeftPin', controlPoint=assembly.sets['RP_LowerLeftPin'],
               surface=assembly.surfaces['Surf-LowerLeftPin'], influenceRadius=WHOLE_SURFACE,
               couplingType=KINEMATIC, localCsys=None,
               u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
model.Coupling(name='Coupling-LowerRightPin', controlPoint=assembly.sets['RP_LowerRightPin'],
               surface=assembly.surfaces['Surf-LowerRightPin'], influenceRadius=WHOLE_SURFACE,
               couplingType=KINEMATIC, localCsys=None,
               u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
print("       Coupling-LowerLeftPin, Coupling-LowerRightPin (KINEMATIC)")

# Create analysis step
print("\n[4/6] Creating analysis step...")
model.StaticStep(name='LoadStep', previous='Initial',
                 description='Experiment 3 Job 1: 20 kN vertical (-Z)',
                 nlgeom=ON, initialInc=0.1, maxInc=0.1, minInc=1e-8, maxNumInc=100)

model.FieldOutputRequest(name='F-Output-1', createStepName='LoadStep',
                         variables=('S', 'E', 'PE', 'PEEQ', 'U', 'RF', 'CF'))

# Apply BCs and loads
print("\n[5/6] Applying BCs and loads...")

# Lower pins: Fixed in X, Y, Z (allow rotation around pin axis = Y)
# u1=X, u2=Y, u3=Z
model.DisplacementBC(name='BC-LowerLeftPin', createStepName='Initial',
                     region=assembly.sets['RP_LowerLeftPin'],
                     u1=SET, u2=SET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET)
model.DisplacementBC(name='BC-LowerRightPin', createStepName='Initial',
                     region=assembly.sets['RP_LowerRightPin'],
                     u1=SET, u2=SET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET)
print("       BCs: lower pins fixed in X, Y, Z (rotations free)")

# Upper pin: Vertical load in -Z direction (downward)
# cf1=X, cf2=Y, cf3=Z
model.ConcentratedForce(name='Load-Vertical', createStepName='LoadStep',
                        region=assembly.sets['RP_UpperPin'],
                        cf1=0.0, cf2=0.0, cf3=-F_VERTICAL)
print(f"       Load: {F_VERTICAL/1000:.0f} kN in -Z (downward)")

# Save
print("\n[6/6] Saving...")
mdb.saveAs(pathName='paper_reproduction/outputs/experiment3/models/TO_Bracket_Analysis.cae')

print("\n" + "=" * 70)
print("EXPERIMENT 3 - STEP 3 COMPLETE")
print("=" * 70)
print(f"""
Summary:
  - Reference points created at pin centers
  - Couplings link RPs to pin hole surfaces
  - Lower pins: Fixed (X, Y, Z)
  - Upper pin: Load {F_VERTICAL/1000:.0f} kN in -Z direction
""")
