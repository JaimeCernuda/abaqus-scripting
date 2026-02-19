# -*- coding: utf-8 -*-
"""
Experiment 5: Setup Tosca topology optimization.

Loads the design space CAE, applies boundary conditions and 20 kN primary
load case, configures SIMP topology optimization with volume constraint.
"""

import os
from abaqus import *
from abaqusConstants import *
from caeModules import *

try:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    SCRIPT_DIR = os.path.join(os.getcwd(), 'scripts')
PROJECT_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, os.pardir))
os.chdir(PROJECT_DIR)

NUM_CPUS = int(os.environ.get('ABAQUS_NUM_CPUS', '1'))
MESH_SIZE = float(os.environ.get('ABAQUS_MESH_SIZE', '3.0'))
MAX_DESIGN_CYCLES = int(os.environ.get('ABAQUS_MAX_CYCLES', '50'))

print("\n" + "=" * 70)
print("EXPERIMENT 5: TOPOLOGY OPTIMIZATION SETUP")
print("=" * 70)

# =============================================================================
# LOAD DESIGN SPACE
# =============================================================================
print("\n[1/7] Loading design space...")

openMdb(os.path.join(PROJECT_DIR, 'Experiment5_TO.cae'))

model = mdb.models['Experiment5_TO']
part = model.parts['TO_Specimen']
assembly = model.rootAssembly
instance = assembly.instances['TO_Specimen-1']

# =============================================================================
# DIMENSIONS
# =============================================================================
TOTAL_HEIGHT = 146.17
BLOCK_HEIGHT_Y = 28.0
BLOCK_WIDTH_X = 18.0
PIN_RADIUS = 6.35
HALF_WIDTH = 32.3
HALF_THICK = 12.5

UPPER_PIN_Y = TOTAL_HEIGHT - BLOCK_HEIGHT_Y / 2.0
LOWER_PIN_Y = BLOCK_HEIGHT_Y / 2.0
UB_LEFT = -BLOCK_WIDTH_X / 2.0
UB_RIGHT = BLOCK_WIDTH_X / 2.0
LB_LEFT_XMIN = -HALF_WIDTH
LB_LEFT_XMAX = -HALF_WIDTH + BLOCK_WIDTH_X
LB_RIGHT_XMIN = HALF_WIDTH - BLOCK_WIDTH_X
LB_RIGHT_XMAX = HALF_WIDTH

# =============================================================================
# STEP
# =============================================================================
print("[2/7] Creating analysis step...")

model.StaticStep(name='LoadStep', previous='Initial',
                 initialInc=1.0, maxInc=1.0, minInc=1e-6)

model.FieldOutputRequest(name='F-Output-1', createStepName='LoadStep',
                         variables=('S', 'U', 'RF', 'ENER'))

# =============================================================================
# BOUNDARY CONDITIONS AND LOADS
# =============================================================================
print("[3/7] Applying boundary conditions and loads...")

# Find pin hole surfaces
lower_left_faces = instance.faces.getByBoundingCylinder(
    center1=(LB_LEFT_XMIN - 1, LOWER_PIN_Y, HALF_THICK),
    center2=(LB_LEFT_XMAX + 1, LOWER_PIN_Y, HALF_THICK),
    radius=PIN_RADIUS + 0.5)
lower_right_faces = instance.faces.getByBoundingCylinder(
    center1=(LB_RIGHT_XMIN - 1, LOWER_PIN_Y, HALF_THICK),
    center2=(LB_RIGHT_XMAX + 1, LOWER_PIN_Y, HALF_THICK),
    radius=PIN_RADIUS + 0.5)
upper_faces = instance.faces.getByBoundingCylinder(
    center1=(UB_LEFT - 1, UPPER_PIN_Y, HALF_THICK),
    center2=(UB_RIGHT + 1, UPPER_PIN_Y, HALF_THICK),
    radius=PIN_RADIUS + 0.5)

print("  Lower left pin faces: {}".format(len(lower_left_faces)))
print("  Lower right pin faces: {}".format(len(lower_right_faces)))
print("  Upper pin faces: {}".format(len(upper_faces)))

# Lower pins: fix U2 and U3 (allow sliding in X)
if len(lower_left_faces) > 0:
    assembly.Set(faces=lower_left_faces, name='LowerLeftPinHole')
    model.DisplacementBC(name='LowerLeftPin_BC', createStepName='Initial',
        region=assembly.sets['LowerLeftPinHole'], u1=UNSET, u2=0.0, u3=0.0)

if len(lower_right_faces) > 0:
    assembly.Set(faces=lower_right_faces, name='LowerRightPinHole')
    model.DisplacementBC(name='LowerRightPin_BC', createStepName='Initial',
        region=assembly.sets['LowerRightPinHole'], u1=UNSET, u2=0.0, u3=0.0)

# Upper pin: load via coupling to reference point
if len(upper_faces) > 0:
    assembly.Set(faces=upper_faces, name='UpperPinHole')
    assembly.Surface(side1Faces=upper_faces, name='UpperPinSurface')

upper_rp = assembly.ReferencePoint(point=(0.0, UPPER_PIN_Y, HALF_THICK))
upper_rp_region = assembly.Set(
    referencePoints=(assembly.referencePoints[upper_rp.id],), name='UpperRP')

if len(upper_faces) > 0:
    model.Coupling(name='UpperPinCoupling', controlPoint=upper_rp_region,
        surface=assembly.surfaces['UpperPinSurface'], influenceRadius=WHOLE_SURFACE,
        couplingType=KINEMATIC, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)

# Apply 20 kN primary design load
model.ConcentratedForce(name='VerticalLoad_20kN', createStepName='LoadStep',
    region=upper_rp_region, cf2=20000.0)

print("  BCs and 20 kN load applied")

# =============================================================================
# TOPOLOGY OPTIMIZATION TASK
# =============================================================================
print("[4/7] Setting up topology optimization...")

opt_task = model.TopologyTask(
    name='TopoTask',
    region=MODEL,
    materialInterpolationTechnique=SIMP,
    materialInterpolationPenalty=3.0,
    freezeBoundaryConditionRegions=ON,
    freezeLoadRegions=ON,
    objectiveFunctionDeltaStopCriteria=0.001
)
print("  Created topology task (SIMP, penalty=3.0)")

# =============================================================================
# DESIGN RESPONSES
# =============================================================================
print("[5/7] Defining design responses and constraints...")

# Strain energy (minimize = maximize stiffness)
model.optimizationTasks['TopoTask'].SingleTermDesignResponse(
    name='strain_energy',
    region=MODEL,
    identifier='STRAIN_ENERGY'
)

# Volume (constrain)
model.optimizationTasks['TopoTask'].SingleTermDesignResponse(
    name='volume',
    region=MODEL,
    identifier='VOLUME'
)

# Objective: minimize strain energy
# Abaqus 2025 tuple format: (suppress, designResponse, weight, referenceValue, stepName)
model.optimizationTasks['TopoTask'].ObjectiveFunction(
    name='MinStrainEnergy',
    objectives=((OFF, 'strain_energy', 1.0, 0.0, ''),),
    target=MINIMIZE
)

# Constraint: volume <= 40%
model.optimizationTasks['TopoTask'].OptimizationConstraint(
    name='VolumeConstraint',
    designResponse='volume',
    restrictionMethod=RELATIVE_LESS_THAN_EQUAL,
    restrictionValue=0.4
)
print("  Objective: minimize strain energy")
print("  Constraint: volume <= 40%")

# =============================================================================
# FROZEN AREAS
# =============================================================================

# Freeze pin hole regions using assembly-level sets
frozen_sets = {
    'FrozenUpperPin': 'FreezeUpperPin',
    'FrozenLowerLeftPin': 'FreezeLowerLeft',
    'FrozenLowerRightPin': 'FreezeLowerRight',
}

for part_set_name, frozen_name in frozen_sets.items():
    if part_set_name in part.sets.keys():
        # Create assembly-level set from part set
        inst_cells = instance.cells.getByBoundingBox(
            xMin=-HALF_WIDTH - 1, yMin=-1, zMin=-1,
            xMax=HALF_WIDTH + 1, yMax=TOTAL_HEIGHT + 1, zMax=30)
        # Use the part set coordinates to find matching instance cells
        if part_set_name == 'FrozenUpperPin':
            cells = instance.cells.getByBoundingBox(
                xMin=UB_LEFT - 1, yMin=TOTAL_HEIGHT - BLOCK_HEIGHT_Y - 0.1, zMin=-1,
                xMax=UB_RIGHT + 1, yMax=TOTAL_HEIGHT + 1, zMax=30)
        elif part_set_name == 'FrozenLowerLeftPin':
            cells = instance.cells.getByBoundingBox(
                xMin=LB_LEFT_XMIN - 1, yMin=-1, zMin=-1,
                xMax=LB_LEFT_XMAX + 1, yMax=BLOCK_HEIGHT_Y + 0.1, zMax=30)
        elif part_set_name == 'FrozenLowerRightPin':
            cells = instance.cells.getByBoundingBox(
                xMin=LB_RIGHT_XMIN - 1, yMin=-1, zMin=-1,
                xMax=LB_RIGHT_XMAX + 1, yMax=BLOCK_HEIGHT_Y + 0.1, zMax=30)
        else:
            continue

        if len(cells) > 0:
            asm_set = assembly.Set(cells=cells, name=frozen_name)
            model.optimizationTasks['TopoTask'].FrozenArea(
                name=frozen_name, region=asm_set)
            print("  Frozen: {} ({} cells)".format(frozen_name, len(cells)))

# =============================================================================
# MANUFACTURING CONSTRAINT
# =============================================================================

# Minimum member size to prevent checkerboard
model.optimizationTasks['TopoTask'].TopologyMemberSize(
    name='MinSize',
    region=MODEL,
    minThickness=MESH_SIZE * 2.0,
    sizeRestriction=MINIMUM
)
print("  Minimum member size: {} mm".format(MESH_SIZE * 2.0))

# =============================================================================
# SAVE
# =============================================================================
print("[6/7] Saving model...")

mdb.saveAs(os.path.join(PROJECT_DIR, 'Experiment5_TO.cae'))

print("\n" + "=" * 70)
print("Optimization setup complete")
print("  Volume fraction: 40%")
print("  Frozen regions: 3 pin areas")
print("  CAE saved: Experiment5_TO.cae")
print("=" * 70)

# =============================================================================
# CREATE OPTIMIZATION PROCESS
# =============================================================================
print("\n[7/7] Creating optimization process...")

# Prototype job (required by OptimizationProcess as the FEA template)
mdb.Job(name='Experiment5_FEA', model='Experiment5_TO',
        numCpus=NUM_CPUS, numDomains=NUM_CPUS)
print("  Created prototype job: Experiment5_FEA")

# Create OptimizationProcess
try:
    opt_process = mdb.OptimizationProcess(
        name='Experiment5_Optimization',
        model='Experiment5_TO',
        task='TopoTask',
        prototypeJob='Experiment5_FEA',
        maxDesignCycle=MAX_DESIGN_CYCLES)
except TypeError:
    # Fallback if prototypeJob not accepted in this Abaqus version
    print("  WARNING: prototypeJob not accepted, trying without it...")
    opt_process = mdb.OptimizationProcess(
        name='Experiment5_Optimization',
        model='Experiment5_TO',
        task='TopoTask',
        maxDesignCycle=MAX_DESIGN_CYCLES)

print("  Max design cycles: {}".format(MAX_DESIGN_CYCLES))

# Generate .par + input files for CLI submission (avoids submit() segfault)
import sys
import traceback
print("  Calling writeParAndInputFiles()...")
sys.stdout.flush()
try:
    opt_process.writeParAndInputFiles()
    print("  writeParAndInputFiles() succeeded")
except KeyError as e:
    print("  KeyError from writeParAndInputFiles(): {}".format(e))
    traceback.print_exc()
    print("  Falling back: writing .inp manually...")
    sys.stdout.flush()
    mdb.jobs['Experiment5_FEA'].writeInput()
    print("  Written: Experiment5_FEA.inp")
except Exception as e:
    print("  ERROR: {} - {}".format(type(e).__name__, e))
    traceback.print_exc()
sys.stdout.flush()

# Save CAE with everything defined
mdb.saveAs(os.path.join(PROJECT_DIR, 'Experiment5_TO.cae'))

# List what was generated
import glob
par_files = glob.glob(os.path.join(PROJECT_DIR, '*.par'))
for d in os.listdir(PROJECT_DIR):
    sub = os.path.join(PROJECT_DIR, d)
    if os.path.isdir(sub):
        par_files += glob.glob(os.path.join(sub, '*.par'))
if par_files:
    for pf in par_files:
        print("  Generated: {}".format(pf))
else:
    print("  No .par files found — .inp file available for manual Tosca setup")

print("\n" + "=" * 70)
print("Optimization setup complete")
print("=" * 70)
