# topology_optimization_bracket.py
# 
# Topology Optimization Example: Generate optimal structure connecting two regions
# 
# This script creates a design space (block) with:
# - Fixed mounting holes on one end
# - Load application point on the other end
# - The optimizer will "grow" the optimal connecting structure
#
# Run with: abaqus cae noGUI=topology_optimization_bracket.py
# 
# NOTE: Requires full Abaqus license with Optimization module (not Learning Edition)

from abaqus import *
from abaqusConstants import *
from caeModules import *

print("\n" + "="*70)
print("TOPOLOGY OPTIMIZATION: Bracket Design")
print("="*70)

# ============================================================================
# PARAMETERS - Easy to modify for different designs
# ============================================================================

# Design space dimensions (the "block" where material can exist)
LENGTH = 100.0      # mm - distance between mounting and load
WIDTH = 40.0        # mm
HEIGHT = 20.0       # mm

# Optimization parameters
VOLUME_FRACTION = 0.3    # Target: use only 30% of original volume
MAX_ITERATIONS = 50      # Maximum optimization cycles

# Mesh size
MESH_SIZE = 2.5          # mm - smaller = finer mesh, more accurate but slower

# Material properties (Steel)
YOUNGS_MODULUS = 210000.0  # MPa
POISSONS_RATIO = 0.3
DENSITY = 7.85e-9          # tonne/mm^3

# Load
APPLIED_FORCE = 1000.0     # N

# ============================================================================
# CREATE MODEL
# ============================================================================

print("\n[1/8] Creating model...")

model = mdb.Model(name='BracketOptimization')
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']

# ============================================================================
# CREATE PART - The Design Space
# ============================================================================

print("[2/8] Creating design space geometry...")

part = model.Part(name='DesignSpace', dimensionality=THREE_D, type=DEFORMABLE_BODY)

# Create sketch for the design space block
sketch = model.ConstrainedSketch(name='BlockSketch', sheetSize=200.0)
sketch.rectangle(point1=(0.0, 0.0), point2=(LENGTH, WIDTH))

# Extrude to create the block
part.BaseSolidExtrude(sketch=sketch, depth=HEIGHT)

# ============================================================================
# PARTITION THE PART - Define frozen regions (mounting & load areas)
# ============================================================================

print("[3/8] Creating partitions for frozen regions...")

# We'll create partitions to define:
# 1. Mounting region (left side) - will be frozen
# 2. Load region (right side) - will be frozen  
# 3. Design region (middle) - optimizer will work here

# Create datum planes for partitioning
# Partition at x = 10 (mounting region boundary)
datumPlane1 = part.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=10.0)
# Partition at x = LENGTH-10 (load region boundary)
datumPlane2 = part.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=LENGTH-10.0)

# Partition the cells
cells = part.cells
part.PartitionCellByDatumPlane(datumPlane=part.datums[datumPlane1.id], cells=cells)
cells = part.cells
part.PartitionCellByDatumPlane(datumPlane=part.datums[datumPlane2.id], cells=cells)

# ============================================================================
# CREATE SETS FOR REGIONS
# ============================================================================

print("[4/8] Creating region sets...")

# Find cells by location
# Mounting region (left, x < 10)
mounting_cell = part.cells.findAt(((5.0, WIDTH/2, HEIGHT/2),))
part.Set(cells=mounting_cell, name='MountingRegion')

# Load region (right, x > LENGTH-10)  
load_cell = part.cells.findAt(((LENGTH-5.0, WIDTH/2, HEIGHT/2),))
part.Set(cells=load_cell, name='LoadRegion')

# Design region (middle)
design_cell = part.cells.findAt(((LENGTH/2, WIDTH/2, HEIGHT/2),))
part.Set(cells=design_cell, name='DesignRegion')

# All cells for section assignment
all_cells = part.cells
part.Set(cells=all_cells, name='AllCells')

# ============================================================================
# MATERIAL AND SECTION
# ============================================================================

print("[5/8] Defining material and section...")

material = model.Material(name='Steel')
material.Elastic(table=((YOUNGS_MODULUS, POISSONS_RATIO),))
material.Density(table=((DENSITY,),))

model.HomogeneousSolidSection(name='SolidSection', material='Steel', thickness=None)

# Assign section to all cells
region = part.sets['AllCells']
part.SectionAssignment(region=region, sectionName='SolidSection')

# ============================================================================
# ASSEMBLY
# ============================================================================

print("[6/8] Creating assembly...")

assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
instance = assembly.Instance(name='DesignSpace-1', part=part, dependent=ON)

# Create assembly-level sets for BCs and loads
# Fixed face (left end, x=0)
fixed_face = instance.faces.findAt(((0.0, WIDTH/2, HEIGHT/2),))
assembly.Set(faces=fixed_face, name='FixedFace')

# Load face (right end, x=LENGTH)
load_face = instance.faces.findAt(((LENGTH, WIDTH/2, HEIGHT/2),))
assembly.Surface(side1Faces=load_face, name='LoadSurface')

# Frozen regions (assembly level)
mounting_cells = instance.cells.findAt(((5.0, WIDTH/2, HEIGHT/2),))
assembly.Set(cells=mounting_cells, name='FrozenMounting')

load_cells = instance.cells.findAt(((LENGTH-5.0, WIDTH/2, HEIGHT/2),))
assembly.Set(cells=load_cells, name='FrozenLoad')

# ============================================================================
# STEP
# ============================================================================

model.StaticStep(name='LoadStep', previous='Initial',
                 initialInc=1.0, maxInc=1.0, minInc=1e-6)

# Request outputs
model.FieldOutputRequest(name='F-Output-1', createStepName='LoadStep',
                         variables=('S', 'U', 'RF', 'ENER'))

# ============================================================================
# BOUNDARY CONDITIONS AND LOADS
# ============================================================================

print("[7/8] Applying boundary conditions and loads...")

# Fix the left face (encastre - all DOFs fixed)
model.EncastreBC(name='FixedSupport', createStepName='Initial',
                 region=assembly.sets['FixedFace'])

# Apply distributed load on right face (pressure = force/area)
# Negative because pressure acts inward, we want downward (-Y direction)
# We'll use a surface traction instead for more control
load_region = assembly.surfaces['LoadSurface']
model.SurfaceTraction(name='AppliedLoad', createStepName='LoadStep',
                      region=load_region, magnitude=APPLIED_FORCE/(WIDTH*HEIGHT),
                      directionVector=((0.0, 0.0, 0.0), (0.0, -1.0, 0.0)),
                      distributionType=UNIFORM, traction=GENERAL)

# ============================================================================
# MESH
# ============================================================================

print("[8/8] Meshing...")

# Seed and mesh
part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)

# Use hex elements (C3D8R)
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD,
                          kinematicSplit=AVERAGE_STRAIN, 
                          secondOrderAccuracy=OFF,
                          hourglassControl=DEFAULT,
                          distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)

part.setElementType(regions=(part.cells,), elemTypes=(elemType1, elemType2, elemType3))
part.generateMesh()

# ============================================================================
# OPTIMIZATION TASK SETUP
# ============================================================================

print("\n" + "-"*70)
print("SETTING UP TOPOLOGY OPTIMIZATION")
print("-"*70)

# Create topology optimization task
# The design region is the WHOLE MODEL, but we'll freeze the end regions
opt_task = model.TopologyTask(
    name='TopoTask',
    region=MODEL,
    materialInterpolationTechnique=SIMP,  # Solid Isotropic Material with Penalization
    materialInterpolationPenalty=3.0,
    freezeBoundaryConditionRegions=ON,    # Keep BC regions solid
    freezeLoadRegions=ON,                 # Keep load regions solid
    objectiveFunctionDeltaStopCriteria=0.001
)

print("  - Created topology task with SIMP method")

# ============================================================================
# DESIGN RESPONSES
# ============================================================================

# Volume design response (what we'll constrain)
model.optimizationTasks['TopoTask'].SingleTermDesignResponse(
    name='volume',
    region=MODEL,
    identifier=VOLUME
)
print("  - Created volume design response")

# Strain energy design response (what we'll minimize = maximize stiffness)
model.optimizationTasks['TopoTask'].SingleTermDesignResponse(
    name='strain_energy', 
    region=MODEL,
    identifier=STRAIN_ENERGY,
    stepOptions=LAST_STEP  # Use results from final step
)
print("  - Created strain energy design response")

# ============================================================================
# OBJECTIVE FUNCTION
# ============================================================================

# Minimize strain energy = Maximize stiffness
model.optimizationTasks['TopoTask'].ObjectiveFunction(
    name='MinStrainEnergy',
    objectives=((model.optimizationTasks['TopoTask'].designResponses['strain_energy'], 
                 MINIMIZE_MAXIMUM, 1.0, 0.0),)
)
print("  - Created objective function: minimize strain energy (maximize stiffness)")

# ============================================================================
# CONSTRAINTS
# ============================================================================

# Constrain volume to target fraction
model.optimizationTasks['TopoTask'].OptimizationConstraint(
    name='VolumeConstraint',
    designResponse='volume',
    restrictionMethod=RELATIVE_LESS_THAN_EQUAL,
    restrictionValue=VOLUME_FRACTION
)
print("  - Created volume constraint: <= {}% of original".format(VOLUME_FRACTION * 100))

# ============================================================================
# GEOMETRIC RESTRICTIONS (Manufacturing Constraints)
# ============================================================================

# Symmetry constraint (optional - makes part symmetric about XZ plane)
model.optimizationTasks['TopoTask'].GeometricRestriction(
    name='SymmetryXZ',
    cells=part.cells,
    csys=None,  
    presumeFeasibleRegionAtStart=ON,
    masterPointDetermination=MINIMUM,
    symmetric=SYMMETRIC,
    axis=AXIS_2  # Y-axis symmetry
)
print("  - Added symmetry constraint about XZ plane")

# Minimum member size (prevents checkerboard patterns)
model.optimizationTasks['TopoTask'].GeometricRestriction(
    name='MinMemberSize',
    cells=part.cells,
    technique=STAMP,
    region=MODEL,
    presumeFeasibleRegionAtStart=ON,
    stampDirection=((0.0, 0.0, 0.0), (0.0, 1.0, 0.0)),  # Stamp in Y direction
    overhangAngle=45.0,
    pointOnAxis=(0.0, 0.0, 0.0),
    pullDirection=((0.0, 0.0, 0.0), (0.0, -1.0, 0.0))
)
print("  - Added manufacturing constraint (stamping direction)")

# ============================================================================
# FREEZE REGIONS EXPLICITLY
# ============================================================================

# Freeze the mounting and load regions so they stay solid
model.optimizationTasks['TopoTask'].FrozenArea(
    name='FreezeMounting',
    region=assembly.sets['FrozenMounting']
)
model.optimizationTasks['TopoTask'].FrozenArea(
    name='FreezeLoad', 
    region=assembly.sets['FrozenLoad']
)
print("  - Frozen mounting and load regions")

# ============================================================================
# CREATE OPTIMIZATION PROCESS
# ============================================================================

print("\n" + "-"*70)
print("CREATING OPTIMIZATION PROCESS")
print("-"*70)

# Create the optimization process (this is like creating a Job)
opt_process = mdb.OptimizationProcess(
    name='BracketOptimization',
    model='BracketOptimization',
    task='TopoTask',
    description='Topology optimization of bracket connecting two regions',
    maxDesignCycle=MAX_ITERATIONS,
    dataSaveFrequency=OPT_DATASAVE_EVERY_CYCLE,
    saveInitial=True,
    saveFirst=True,
    saveLast=True,
    saveEvery=None
)

print("  - Created optimization process: {} max iterations".format(MAX_ITERATIONS))

# ============================================================================
# SAVE MODEL
# ============================================================================

mdb.saveAs(pathName='BracketOptimization.cae')
print("\n  - Model saved: BracketOptimization.cae")

# ============================================================================
# SUBMIT OPTIMIZATION (Comment out if you just want to create the model)
# ============================================================================

print("\n" + "="*70)
print("READY TO RUN OPTIMIZATION")
print("="*70)

print("""
To run the optimization:

Option 1 - From this script (uncomment the lines below):
    opt_process.submit()
    opt_process.waitForCompletion()

Option 2 - From Abaqus/CAE GUI:
    1. Open BracketOptimization.cae
    2. Go to Optimization module
    3. Select Optimization > Process > Submit

Option 3 - From command line:
    abaqus optimization job=BracketOptimization interactive

After optimization completes:
    - Results in: BracketOptimization/TOSCA_POST/
    - Open the .odb file to view optimization progression
    - Extract optimized geometry: Optimization > Extract > STL

""")

# Uncomment to actually run the optimization:
# print("Submitting optimization...")
# opt_process.submit()
# opt_process.waitForCompletion()
# print("Optimization complete!")

print("="*70)
print("Script completed successfully!")
print("="*70 + "\n")
