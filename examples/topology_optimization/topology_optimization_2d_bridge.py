# topology_optimization_2d_bridge.py
#
# Classic Topology Optimization Example: MBB Beam (Messerschmitt-Bölkow-Blohm)
# 
# This is the "hello world" of topology optimization:
# - Rectangular design space
# - Fixed on left edge
# - Roller support on right bottom corner  
# - Load applied at top left
# - Goal: Find optimal truss-like structure
#
# Run with: abaqus cae noGUI=topology_optimization_2d_bridge.py
#
# NOTE: Requires full Abaqus license with Optimization module

from abaqus import *
from abaqusConstants import *
from caeModules import *

print("\n" + "="*70)
print("TOPOLOGY OPTIMIZATION: 2D MBB Beam (Classic Example)")
print("="*70)

# =============================================================================
# PARAMETERS
# =============================================================================

# Design space
LENGTH = 300.0      # mm
HEIGHT = 100.0      # mm
THICKNESS = 1.0     # mm (for 2D plane stress)

# Optimization
VOLUME_FRACTION = 0.5  # Keep 50% of material
MAX_CYCLES = 40

# Mesh
MESH_SIZE = 5.0  # mm

# Material
E = 210000.0   # MPa
NU = 0.3

# Load
LOAD = -1000.0  # N

# =============================================================================
# MODEL SETUP
# =============================================================================

print("\n[1/6] Creating model and geometry...")

model = mdb.Model(name='MBB_Beam')
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']

# Create 2D part (shell for plane stress)
sketch = model.ConstrainedSketch(name='BeamSketch', sheetSize=500.0)
sketch.rectangle(point1=(0.0, 0.0), point2=(LENGTH, HEIGHT))

part = model.Part(name='Beam', dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
part.BaseShell(sketch=sketch)

# =============================================================================
# MATERIAL AND SECTION
# =============================================================================

print("[2/6] Defining material...")

material = model.Material(name='Steel')
material.Elastic(table=((E, NU),))

# Plane stress section
model.HomogeneousShellSection(name='PlaneStress', 
                               preIntegrate=OFF,
                               material='Steel',
                               thickness=THICKNESS)

# Assign
faces = part.faces
region = part.Set(faces=faces, name='AllFaces')
part.SectionAssignment(region=region, sectionName='PlaneStress')

# =============================================================================
# ASSEMBLY AND STEP
# =============================================================================

print("[3/6] Creating assembly and step...")

assembly = model.rootAssembly
instance = assembly.Instance(name='Beam-1', part=part, dependent=ON)

model.StaticStep(name='Load', previous='Initial')

# =============================================================================
# BOUNDARY CONDITIONS AND LOADS
# =============================================================================

print("[4/6] Applying BCs and loads...")

# BC 1: Fix left edge (all DOFs)
left_edge = instance.edges.findAt(((0.0, HEIGHT/2, 0.0),))
left_region = assembly.Set(edges=left_edge, name='LeftEdge')
model.DisplacementBC(name='FixLeft', createStepName='Initial',
                     region=left_region, u1=0.0, u2=0.0, ur3=0.0)

# BC 2: Roller on bottom right corner (only vertical fixed)
# This creates the classic half-MBB beam setup
right_bottom_vertex = instance.vertices.findAt(((LENGTH, 0.0, 0.0),))
right_region = assembly.Set(vertices=right_bottom_vertex, name='RightBottom')
model.DisplacementBC(name='RollerRight', createStepName='Initial',
                     region=right_region, u2=0.0)

# Load: Concentrated force at top-left corner
top_left_vertex = instance.vertices.findAt(((0.0, HEIGHT, 0.0),))
load_region = assembly.Set(vertices=top_left_vertex, name='LoadPoint')
model.ConcentratedForce(name='TopLoad', createStepName='Load',
                        region=load_region, cf2=LOAD)

# =============================================================================
# MESH
# =============================================================================

print("[5/6] Meshing...")

part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)

# Use CPS4R elements (4-node plane stress, reduced integration)
elemType = mesh.ElemType(elemCode=CPS4R, elemLibrary=STANDARD)
part.setElementType(regions=(part.faces,), elemTypes=(elemType,))
part.generateMesh()

num_elements = len(part.elements)
num_nodes = len(part.nodes)
print(f"  Mesh: {num_elements} elements, {num_nodes} nodes")

# =============================================================================
# TOPOLOGY OPTIMIZATION SETUP
# =============================================================================

print("[6/6] Setting up topology optimization...")

# Design region = entire model
part.Set(faces=part.faces, name='DesignRegion')

# Create optimization task
model.TopologyTask(
    name='TopoOpt',
    region=instance.sets['DesignRegion'],
    materialInterpolationTechnique=SIMP,
    materialInterpolationPenalty=3.0,
    freezeBoundaryConditionRegions=ON,
    freezeLoadRegions=ON,
    maxDesignCycle=MAX_CYCLES
)

# Design responses
model.optimizationTasks['TopoOpt'].SingleTermDesignResponse(
    name='StrainEnergy',
    region=MODEL,
    identifier='STRAIN_ENERGY',
    operation=SUM)

model.optimizationTasks['TopoOpt'].SingleTermDesignResponse(
    name='Volume', 
    region=MODEL,
    identifier='VOLUME',
    operation=SUM)

# Objective: Minimize compliance (strain energy)
model.optimizationTasks['TopoOpt'].ObjectiveFunction(
    name='MinCompliance',
    objectives=((model.optimizationTasks['TopoOpt'].designResponses['StrainEnergy'], 
                 MINIMIZE, 1.0),))

# Constraint: Volume <= 50%
model.optimizationTasks['TopoOpt'].OptimizationConstraint(
    name='VolumeFraction',
    designResponse='Volume',
    restrictionMethod=RELATIVE_LESS_THAN_EQUAL,
    restrictionValue=VOLUME_FRACTION)

# Create optimization process
mdb.OptimizationProcess(
    name='MBB_Optimization',
    model='MBB_Beam',
    task='TopoOpt',
    maxDesignCycle=MAX_CYCLES)

# Save
mdb.saveAs(pathName='MBB_Beam.cae')

print("\n" + "="*70)
print("MODEL CREATED SUCCESSFULLY")
print("="*70)
print(f"""
Summary:
  - Design space: {LENGTH} x {HEIGHT} mm
  - Elements: {num_elements}
  - Target volume: {VOLUME_FRACTION*100}% of original
  - Max iterations: {MAX_CYCLES}

Expected result:
  The optimizer will generate a truss-like structure that efficiently
  transfers the load from top-left to the supports, similar to:
  
     LOAD
       ↓
       ●━━━━━━━━━━━━━━━━━━━━━━━━━━●
       ┃╲                      ╱┃
       ┃  ╲                  ╱  ┃
       ┃    ╲              ╱    ┃
       ┃      ╲          ╱      ┃
       ┃        ╲      ╱        ┃
       ┃          ╲  ╱          ┃
       ┃            ╳            ┃
       ┃          ╱  ╲          ┃
       ┃        ╱      ╲        ┃
       ┃      ╱          ╲      ┃
       ┃    ╱              ╲    ┃
       ┃  ╱                  ╲  ┃
       ┃╱                      ╲┃
    ▓▓▓●━━━━━━━━━━━━━━━━━━━━━━━━━━●
    FIXED                      ROLLER

To run:
  1. Open MBB_Beam.cae in Abaqus/CAE
  2. Optimization > Process Manager > Submit
  
Or uncomment the submit lines at the end of this script.
""")

# Uncomment to run:
# mdb.optimizationProcesses['MBB_Optimization'].submit()
# mdb.optimizationProcesses['MBB_Optimization'].waitForCompletion()
