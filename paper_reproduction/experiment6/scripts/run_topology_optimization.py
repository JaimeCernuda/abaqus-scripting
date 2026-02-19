# -*- coding: utf-8 -*-
"""
Experiment 6: Simplest possible topology optimization.

A rectangular block, fixed on one end, pressure on the other.
Minimize strain energy, volume <= 50%.
Calls OptimizationProcess.submit() directly.
"""

from abaqus import *
from abaqusConstants import *
from caeModules import *

import os

NUM_CPUS = int(os.environ.get('ABAQUS_NUM_CPUS', '1'))
MAX_CYCLES = int(os.environ.get('ABAQUS_MAX_CYCLES', '10'))

print("=" * 60)
print("EXPERIMENT 6: Simple Topology Optimization")
print("  CPUs: {}".format(NUM_CPUS))
print("  Max cycles: {}".format(MAX_CYCLES))
print("=" * 60)

# --- Model ---
model = mdb.Model(name='SimpleTO')
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']

# --- Part: 100x40x20 block ---
print("[1/8] Creating part...")
part = model.Part(name='Block', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='BlockSketch', sheetSize=200.0)
sketch.rectangle(point1=(0.0, 0.0), point2=(100.0, 40.0))
part.BaseSolidExtrude(sketch=sketch, depth=20.0)

# --- Material ---
print("[2/8] Defining material...")
mat = model.Material(name='Steel')
mat.Elastic(table=((210000.0, 0.3),))
mat.Density(table=((7.85e-9,),))

model.HomogeneousSolidSection(name='Section', material='Steel', thickness=None)
part.SectionAssignment(region=part.Set(cells=part.cells, name='AllCells'),
                       sectionName='Section')

# --- Assembly ---
print("[3/8] Creating assembly...")
assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
instance = assembly.Instance(name='Block-1', part=part, dependent=ON)

# --- Sets for BCs ---
fixed_face = instance.faces.findAt(((0.0, 20.0, 10.0),))
assembly.Set(faces=fixed_face, name='FixedFace')

load_face = instance.faces.findAt(((100.0, 20.0, 10.0),))
assembly.Surface(side1Faces=load_face, name='LoadSurface')

# --- Step ---
print("[4/8] Creating step...")
model.StaticStep(name='LoadStep', previous='Initial',
                 initialInc=1.0, maxInc=1.0, minInc=1e-6)
model.FieldOutputRequest(name='F-Output-1', createStepName='LoadStep',
                         variables=('S', 'U', 'RF', 'ENER'))

# --- BCs and Load ---
print("[5/8] Applying BCs and load...")
model.EncastreBC(name='Fixed', createStepName='Initial',
                 region=assembly.sets['FixedFace'])
model.Pressure(name='Load', createStepName='LoadStep',
               region=assembly.surfaces['LoadSurface'],
               magnitude=1.0)

# --- Mesh ---
print("[6/8] Meshing...")
part.seedPart(size=5.0, deviationFactor=0.1, minSizeFactor=0.1)
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType1, elemType2, elemType3))
part.generateMesh()
print("  Nodes: {}, Elements: {}".format(len(part.nodes), len(part.elements)))

# --- Optimization Task ---
print("[7/8] Setting up optimization...")
model.TopologyTask(
    name='TopoTask',
    region=MODEL,
    materialInterpolationTechnique=SIMP,
    materialInterpolationPenalty=3.0,
    objectiveFunctionDeltaStopCriteria=0.001
)

model.optimizationTasks['TopoTask'].SingleTermDesignResponse(
    name='strain_energy', region=MODEL, identifier='STRAIN_ENERGY')

model.optimizationTasks['TopoTask'].SingleTermDesignResponse(
    name='volume', region=MODEL, identifier='VOLUME')

model.optimizationTasks['TopoTask'].ObjectiveFunction(
    name='MinSE',
    objectives=((OFF, 'strain_energy', 1.0, 0.0, ''),),
    target=MINIMIZE)

model.optimizationTasks['TopoTask'].OptimizationConstraint(
    name='VolConstraint',
    designResponse='volume',
    restrictionMethod=RELATIVE_LESS_THAN_EQUAL,
    restrictionValue=0.5)

# --- Prototype Job + OptimizationProcess ---
print("[8/8] Creating optimization process and submitting...")
mdb.Job(name='SimpleTO_FEA', model='SimpleTO',
        numCpus=NUM_CPUS, numDomains=NUM_CPUS)

opt_process = mdb.OptimizationProcess(
    name='SimpleTO_Opt',
    model='SimpleTO',
    task='TopoTask',
    prototypeJob='SimpleTO_FEA',
    maxDesignCycle=MAX_CYCLES)

mdb.saveAs('SimpleTO.cae')
print("  Model saved: SimpleTO.cae")

print("\nSubmitting optimization...")
import sys
sys.stdout.flush()

opt_process.submit(validate=False)
opt_process.waitForCompletion()

print("\nOptimization complete!")
print("=" * 60)
