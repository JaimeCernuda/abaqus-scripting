# -*- coding: utf-8 -*-
"""
Experiment 6 Diagnostic: Capture all generated files before submit().

Same model as run_topology_optimization.py but adds intermediate saves:
  - writeInput() -> .inp file
  - writeParAndInputFiles() -> .par + .inp files
  - saveAs() at every stage
  - submit() last (expected to segfault)
"""

from abaqus import *
from abaqusConstants import *
from caeModules import *

import os
import sys
import glob
import traceback

NUM_CPUS = int(os.environ.get('ABAQUS_NUM_CPUS', '1'))
MAX_CYCLES = int(os.environ.get('ABAQUS_MAX_CYCLES', '10'))

def flush():
    sys.stdout.flush()
    sys.stderr.flush()

def list_files(label):
    """Print all files in the working directory."""
    print("\n  --- {} ---".format(label))
    cwd = os.getcwd()
    for f in sorted(os.listdir(cwd)):
        full = os.path.join(cwd, f)
        if os.path.isfile(full):
            size = os.path.getsize(full)
            print("  {:>10} bytes  {}".format(size, f))
        elif os.path.isdir(full):
            print("  {:>10}       {}/".format('[dir]', f))
    flush()

print("=" * 60)
print("EXPERIMENT 6 DIAGNOSTIC")
print("  CPUs: {}".format(NUM_CPUS))
print("  Max cycles: {}".format(MAX_CYCLES))
print("  CWD: {}".format(os.getcwd()))
print("  Abaqus version: {}".format(session.journalOptions.recoverGeometry))
print("=" * 60)
flush()

# ===== STAGE 1: Model =====
print("\n[1/11] Creating model...")
model = mdb.Model(name='SimpleTO')
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']
print("  DONE")
flush()

# ===== STAGE 2: Part =====
print("[2/11] Creating part (100x40x20 block)...")
part = model.Part(name='Block', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='BlockSketch', sheetSize=200.0)
sketch.rectangle(point1=(0.0, 0.0), point2=(100.0, 40.0))
part.BaseSolidExtrude(sketch=sketch, depth=20.0)
print("  DONE")
flush()

# ===== STAGE 3: Material =====
print("[3/11] Defining material (Steel)...")
mat = model.Material(name='Steel')
mat.Elastic(table=((210000.0, 0.3),))
mat.Density(table=((7.85e-9,),))
model.HomogeneousSolidSection(name='Section', material='Steel', thickness=None)
part.SectionAssignment(region=part.Set(cells=part.cells, name='AllCells'),
                       sectionName='Section')
print("  DONE")
flush()

# ===== STAGE 4: Assembly =====
print("[4/11] Creating assembly...")
assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
instance = assembly.Instance(name='Block-1', part=part, dependent=ON)
print("  DONE")
flush()

# ===== STAGE 5: Step + BCs + Load =====
print("[5/11] Creating step, BCs, load...")
model.StaticStep(name='LoadStep', previous='Initial',
                 initialInc=1.0, maxInc=1.0, minInc=1e-6)
model.FieldOutputRequest(name='F-Output-1', createStepName='LoadStep',
                         variables=('S', 'U', 'RF', 'ENER'))

fixed_face = instance.faces.findAt(((0.0, 20.0, 10.0),))
assembly.Set(faces=fixed_face, name='FixedFace')
load_face = instance.faces.findAt(((100.0, 20.0, 10.0),))
assembly.Surface(side1Faces=load_face, name='LoadSurface')

model.EncastreBC(name='Fixed', createStepName='Initial',
                 region=assembly.sets['FixedFace'])
model.Pressure(name='Load', createStepName='LoadStep',
               region=assembly.surfaces['LoadSurface'],
               magnitude=1.0)
print("  DONE")
flush()

# ===== STAGE 6: Mesh =====
print("[6/11] Meshing...")
part.seedPart(size=5.0, deviationFactor=0.1, minSizeFactor=0.1)
elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType1, elemType2, elemType3))
part.generateMesh()
print("  Nodes: {}, Elements: {}".format(len(part.nodes), len(part.elements)))
flush()

# ===== STAGE 7: Save CAE (pre-optimization) =====
print("[7/11] Saving CAE (pre-optimization)...")
mdb.saveAs('SimpleTO.cae')
print("  Saved: SimpleTO.cae")
list_files("After model creation")

# ===== STAGE 8: Topology optimization setup =====
print("[8/11] Setting up topology optimization...")
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
print("  DONE — TopologyTask, 2 design responses, objective, constraint")
flush()

# ===== STAGE 9: Create prototype job + OptimizationProcess =====
print("[9/11] Creating prototype job and OptimizationProcess...")
mdb.Job(name='SimpleTO_FEA', model='SimpleTO',
        numCpus=NUM_CPUS, numDomains=NUM_CPUS)
print("  Created prototype job: SimpleTO_FEA")

opt_process = mdb.OptimizationProcess(
    name='SimpleTO_Opt',
    model='SimpleTO',
    task='TopoTask',
    prototypeJob='SimpleTO_FEA',
    maxDesignCycle=MAX_CYCLES)
print("  Created OptimizationProcess: SimpleTO_Opt (maxCycles={})".format(MAX_CYCLES))
flush()

# ===== STAGE 10: Generate all output files =====
print("[10/11] Generating output files...")

# 10a: Save CAE with optimization defined
mdb.saveAs('SimpleTO.cae')
print("  Saved: SimpleTO.cae (with optimization)")

# 10b: Write .inp from the prototype job
print("  Writing .inp from prototype job...")
try:
    mdb.jobs['SimpleTO_FEA'].writeInput()
    print("  DONE: SimpleTO_FEA.inp")
except Exception as e:
    print("  FAILED writeInput(): {} - {}".format(type(e).__name__, e))
    traceback.print_exc()
flush()

# 10c: Write .par + .inp from OptimizationProcess
print("  Writing .par + .inp from OptimizationProcess...")
try:
    opt_process.writeParAndInputFiles()
    print("  DONE: writeParAndInputFiles()")
except Exception as e:
    print("  FAILED writeParAndInputFiles(): {} - {}".format(type(e).__name__, e))
    traceback.print_exc()
flush()

# 10d: List everything generated
list_files("After writeInput + writeParAndInputFiles")

# Also list any subdirectories
for d in os.listdir(os.getcwd()):
    full = os.path.join(os.getcwd(), d)
    if os.path.isdir(full) and not d.startswith('.'):
        print("\n  --- Contents of {}/ ---".format(d))
        for f in sorted(os.listdir(full)):
            fp = os.path.join(full, f)
            if os.path.isfile(fp):
                print("  {:>10} bytes  {}/{}".format(os.path.getsize(fp), d, f))
            elif os.path.isdir(fp):
                print("  {:>10}       {}/{}/".format('[dir]', d, f))
flush()

# ===== STAGE 11: Attempt submit =====
print("\n[11/11] Attempting opt_process.submit(validate=False)...")
print("  If this segfaults, all files above are still captured.")
flush()

try:
    opt_process.submit(validate=False)
    print("  submit() returned successfully!")
    opt_process.waitForCompletion()
    print("  Optimization complete!")
except Exception as e:
    print("  submit() raised: {} - {}".format(type(e).__name__, e))
    traceback.print_exc()
flush()

list_files("Final state")
print("\n" + "=" * 60)
print("DIAGNOSTIC COMPLETE")
print("=" * 60)
