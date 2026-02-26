# -*- coding: utf-8 -*-
"""
Experiment 7c: Import airbeam_vol.inp + setup TO via CAE Python API + writeParAndInputFiles()

Run 4 fixes:
  - Displacement DRESP: U2 rejects all operations (SUM/MAX/MIN/default). Skip displacement
    constraint entirely; use experiment 6 pattern: minimize strain energy + volume constraint.
  - writeParAndInputFiles() KeyError 'airbeam_FEA': try writeInput() on the job first.
  - Diagnostic print of opt.name crashes (no 'name' attr) — remove it.
"""

from abaqus import *
from abaqusConstants import *
from caeModules import *
import os, sys, traceback

SEPARATOR = "=" * 70

def phase_header(num, title):
    print("")
    print(SEPARATOR)
    print("  Phase {}: {}".format(num, title))
    print(SEPARATOR)
    sys.stdout.flush()

def safe_run(label, func):
    try:
        result = func()
        print("  [OK] {}".format(label))
        sys.stdout.flush()
        return True, result
    except Exception as e:
        print("  [FAIL] {}: {} - {}".format(label, type(e).__name__, e))
        traceback.print_exc()
        sys.stdout.flush()
        return False, None

def find_set_caseless(container, target_name):
    target_lower = target_name.lower()
    for name in container.keys():
        if name.lower() == target_lower:
            return name, container[name]
    return None, None

# ============================================================================
# Phase 1: Import the .inp
# ============================================================================
phase_header(1, "Import airbeam_vol.inp into CAE")

ok, model = safe_run("ModelFromInputFile",
    lambda: mdb.ModelFromInputFile(name='airbeam', inputFileName='airbeam_vol.inp'))

if not ok:
    print("FATAL: Cannot import .inp. Aborting.")
    sys.exit(1)

model = mdb.models['airbeam']
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']

# ============================================================================
# Phase 2: Discovery
# ============================================================================
phase_header(2, "Discovery")

assembly = model.rootAssembly
inst_name = list(assembly.instances.keys())[0]
inst = assembly.instances[inst_name]

print("  Parts: {}".format(sorted(model.parts.keys())))
print("  Instance: '{}'".format(inst_name))
print("  Assembly sets: {}".format(sorted(assembly.sets.keys())))
print("  Steps: {}".format(sorted(model.steps.keys())))

frozen_name, frozen_set = find_set_caseless(assembly.sets, 'frozen_elements')
print("  frozen_elements: '{}' ({} elements)".format(
    frozen_name, len(frozen_set.elements) if frozen_set else 0))

sys.stdout.flush()

# ============================================================================
# Phase 3: Create TopologyTask
# ============================================================================
phase_header(3, "Create TopologyTask")

ok3, _ = safe_run("TopologyTask",
    lambda: model.TopologyTask(
        name='topology_optimization',
        region=MODEL,
    ))

if not ok3:
    print("FATAL: Cannot create TopologyTask. Aborting.")
    sys.exit(1)

task = model.optimizationTasks['topology_optimization']

# ============================================================================
# Phase 4: Design Responses (strain energy + volume only)
# ============================================================================
phase_header(4, "Design Responses")

ok4a, _ = safe_run("DRESP strain_energy",
    lambda: task.SingleTermDesignResponse(
        name='strain_energy',
        identifier='STRAIN_ENERGY',
        region=MODEL,
        operation=SUM))

ok4b, _ = safe_run("DRESP volume",
    lambda: task.SingleTermDesignResponse(
        name='volume',
        identifier='VOLUME',
        region=MODEL,
        operation=SUM))

print("  Design responses: {}".format(sorted(task.designResponses.keys())))

# ============================================================================
# Phase 5: Objective Function — minimize strain energy
# ============================================================================
phase_header(5, "Objective Function (minimize strain energy)")

ok5, _ = safe_run("ObjectiveFunction",
    lambda: task.ObjectiveFunction(
        name='min_SE',
        objectives=((OFF, 'strain_energy', 1.0, 0.0, ''),),
        target=MINIMIZE))

# ============================================================================
# Phase 6: Constraint — volume <= 50%
# ============================================================================
phase_header(6, "Volume Constraint (<= 50%)")

ok6, _ = safe_run("OptimizationConstraint vol_limit",
    lambda: task.OptimizationConstraint(
        name='vol_limit',
        designResponse='volume',
        restrictionValue=0.5,
        restrictionMethod=RELATIVE_LESS_THAN_EQUAL))

# ============================================================================
# Phase 7: Frozen Area
# ============================================================================
phase_header(7, "Frozen Area")

frozen_ok = False
if frozen_set:
    ok7, _ = safe_run("FrozenArea (set '{}')".format(frozen_name),
        lambda: task.FrozenArea(
            name='dvcon_frozen',
            region=frozen_set))
    if ok7:
        frozen_ok = True

if not frozen_ok:
    for iname, i in assembly.instances.items():
        fname, fset = find_set_caseless(i.sets, 'frozen_elements')
        if fset:
            ok7, _ = safe_run("FrozenArea (instance '{}')".format(fname),
                lambda: task.FrozenArea(
                    name='dvcon_frozen',
                    region=fset))
            if ok7:
                frozen_ok = True
                break

if not frozen_ok:
    print("  [WARN] FrozenArea could not be created")

# ============================================================================
# Phase 8: Prototype Job + write input + OptimizationProcess
# ============================================================================
phase_header(8, "Prototype Job + OptimizationProcess")

ok8a, _ = safe_run("Prototype Job",
    lambda: mdb.Job(name='airbeam_FEA', model='airbeam', numCpus=1, numDomains=1))

print("  mdb.jobs: {}".format(sorted(mdb.jobs.keys())))

# Try writing input file first — might be needed for writeParAndInputFiles()
ok8_inp, _ = safe_run("Job.writeInput()",
    lambda: mdb.jobs['airbeam_FEA'].writeInput())

# Check if .inp was generated
if os.path.exists('airbeam_FEA.inp'):
    print("  airbeam_FEA.inp generated ({} bytes)".format(os.path.getsize('airbeam_FEA.inp')))
else:
    print("  airbeam_FEA.inp NOT generated")

ok8b, _ = safe_run("OptimizationProcess",
    lambda: mdb.OptimizationProcess(
        name='airbeam_Opt',
        model='airbeam',
        task='topology_optimization',
        prototypeJob='airbeam_FEA',
        maxDesignCycle=80))

print("  mdb.optimizationProcesses: {}".format(sorted(mdb.optimizationProcesses.keys())))

# ============================================================================
# Phase 9: Save CAE
# ============================================================================
phase_header(9, "Save CAE")

safe_run("saveAs", lambda: mdb.saveAs('airbeam_7c.cae'))

# ============================================================================
# Phase 10: writeParAndInputFiles()
# ============================================================================
phase_header(10, "writeParAndInputFiles()")

ok9 = False
ok_sub = False
if ok8b:
    # Re-obtain reference after save
    opt = mdb.optimizationProcesses['airbeam_Opt']

    # NOTE: do NOT call dir(opt) — it segfaults in GetLicenseType (run 4 finding)

    ok9, _ = safe_run("writeParAndInputFiles()",
        lambda: opt.writeParAndInputFiles())

    if not ok9:
        print("\n  writeParAndInputFiles failed.")
        print("  Trying submit() directly (bypassing writeParAndInputFiles)...")
        sys.stdout.flush()
        ok_sub, _ = safe_run("submit(validate=False)",
            lambda: opt.submit(validate=False))
        if ok_sub:
            print("  submit() succeeded! Waiting...")
            sys.stdout.flush()
            safe_run("waitForCompletion()", lambda: opt.waitForCompletion())

if ok9:
    print("\n  Looking for generated .par file...")
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.par'):
                parpath = os.path.join(root, f)
                print("  Found: {}".format(parpath))
                try:
                    with open(parpath, 'r') as pf:
                        print(pf.read())
                except:
                    pass

# ============================================================================
# Summary
# ============================================================================
print("")
print(SEPARATOR)
print("  EXPERIMENT 7c SUMMARY (run 4)")
print(SEPARATOR)
print("  Import .inp:         OK")
print("  TopologyTask:        {}".format("OK" if ok3 else "FAIL"))
print("  DRESP (energy):      {}".format("OK" if ok4a else "FAIL"))
print("  DRESP (volume):      {}".format("OK" if ok4b else "FAIL"))
print("  ObjectiveFunction:   {}".format("OK" if ok5 else "FAIL"))
print("  VolConstraint:       {}".format("OK" if ok6 else "FAIL"))
print("  FrozenArea:          {}".format("OK" if frozen_ok else "FAIL"))
print("  Job+writeInput:      {}".format("OK" if ok8_inp else "FAIL"))
print("  OptProcess:          {}".format("OK" if ok8b else "FAIL"))
print("  writeParAndInput:    {}".format("OK" if ok9 else "FAIL"))
print("  submit (fallback):   {}".format("OK" if ok_sub else "N/A" if ok9 else "FAIL"))
print(SEPARATOR)

print("\n  Files in CWD:")
for f in sorted(os.listdir('.')):
    if os.path.isdir(f):
        print("    {}/ (dir)".format(f))
    else:
        print("    {} ({} bytes)".format(f, os.path.getsize(f)))

# Check for subdirectories (optimization output)
for d in sorted(os.listdir('.')):
    if os.path.isdir(d):
        print("\n  Contents of {}/".format(d))
        try:
            contents = sorted(os.listdir(d))
            for f2 in contents[:20]:
                print("    {}".format(f2))
            if len(contents) > 20:
                print("    ... and {} more files".format(len(contents) - 20))
        except:
            pass

print("\nExperiment 7c finished.")
sys.stdout.flush()
