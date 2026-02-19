# -*- coding: utf-8 -*-
"""
Experiment 5: Create and run validation analysis jobs on optimized topology.

After topology optimization completes, this script:
1. Reads the final density field from the last TOSCA_POST ODB
2. Assigns near-zero stiffness to void elements (density < threshold)
3. Creates and runs validation jobs at 20/60/100 kN

The resulting Validation_*.odb files are read by run_validation.py for
comparison against the Experiment 4 baseline.

Run with: abaqus cae noGUI=scripts/setup_validation_jobs.py
"""

import os
from odbAccess import openOdb
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
DENSITY_THRESHOLD = float(os.environ.get('DENSITY_THRESHOLD', '0.5'))

# Which loads to validate (default: all three; set VALIDATION_LOADS=20 for quick test)
VALIDATION_LOADS_STR = os.environ.get('VALIDATION_LOADS', '20,60,100')
VALIDATION_LOADS = [int(x.strip()) for x in VALIDATION_LOADS_STR.split(',')]

# Material properties
E_SOLID = 200000.0   # IN718 Young's modulus (MPa)
NU = 0.3             # Poisson's ratio
E_VOID = 0.001       # Near-zero stiffness for void elements (MPa)

print("\n" + "=" * 70)
print("EXPERIMENT 5: VALIDATION JOB SETUP")
print("=" * 70)
print("  Density threshold: {}".format(DENSITY_THRESHOLD))
print("  Loads to validate: {} kN".format(VALIDATION_LOADS))
print("  CPUs per job: {}".format(NUM_CPUS))

# =========================================================================
# STEP 1: Read density field from final optimization ODB
# =========================================================================
print("\n[1/4] Reading density field from optimization results...")

opt_dir = os.path.join(PROJECT_DIR, 'Experiment5_TO', 'TOSCA_POST')
if not os.path.exists(opt_dir):
    opt_dir = os.path.join(PROJECT_DIR, 'TOSCA_POST')

if not os.path.exists(opt_dir):
    print("ERROR: TOSCA_POST directory not found")
    print("  Run topology optimization first")
    raise SystemExit(1)

odb_files = sorted([f for f in os.listdir(opt_dir) if f.endswith('.odb')])
if not odb_files:
    print("ERROR: No ODB files in {}".format(opt_dir))
    raise SystemExit(1)

final_odb_path = os.path.join(opt_dir, odb_files[-1])
print("  Final ODB: {}".format(odb_files[-1]))

odb = openOdb(path=final_odb_path, readOnly=True)
step = odb.steps[odb.steps.keys()[-1]]
frame = step.frames[-1]

# Find density field
density_field = None
for field_name in frame.fieldOutputs.keys():
    upper_name = field_name.upper()
    if 'DENSITY' in upper_name or 'MAT_PROP' in upper_name:
        density_field = frame.fieldOutputs[field_name]
        print("  Density field: {}".format(field_name))
        break

if density_field is None:
    print("ERROR: No density field found in optimization ODB")
    print("  Available fields: {}".format(list(frame.fieldOutputs.keys())))
    odb.close()
    raise SystemExit(1)

# Build element-to-density mapping
element_densities = {}
for value in density_field.values:
    elem_label = value.elementLabel
    if hasattr(value, 'data'):
        d = value.data
    elif hasattr(value, 'magnitude'):
        d = value.magnitude
    else:
        d = 0.0
    # For elements with multiple integration points, take the average
    if elem_label in element_densities:
        existing = element_densities[elem_label]
        element_densities[elem_label] = (existing[0] + d, existing[1] + 1)
    else:
        element_densities[elem_label] = (d, 1)

odb.close()

# Average densities across integration points
for label in element_densities:
    total, count = element_densities[label]
    element_densities[label] = total / count

solid_count = sum(1 for d in element_densities.values() if d >= DENSITY_THRESHOLD)
void_count = len(element_densities) - solid_count
print("  Total elements: {}".format(len(element_densities)))
print("  Solid (>= {}): {} ({:.1f}%)".format(
    DENSITY_THRESHOLD, solid_count,
    100.0 * solid_count / len(element_densities) if element_densities else 0))
print("  Void  (<  {}): {} ({:.1f}%)".format(
    DENSITY_THRESHOLD, void_count,
    100.0 * void_count / len(element_densities) if element_densities else 0))

# =========================================================================
# STEP 2: Open model and create density-based element sets
# =========================================================================
print("\n[2/4] Creating density-based element sets and materials...")

openMdb(os.path.join(PROJECT_DIR, 'Experiment5_TO.cae'))
model = mdb.models['Experiment5_TO']
part = model.parts['TO_Specimen']
assembly = model.rootAssembly
instance = assembly.instances['TO_Specimen-1']

# Get all mesh elements
all_elements = part.elements

# Build solid and void element label lists
solid_labels = []
void_labels = []
for elem in all_elements:
    d = element_densities.get(elem.label, 0.0)
    if d >= DENSITY_THRESHOLD:
        solid_labels.append(elem.label)
    else:
        void_labels.append(elem.label)

print("  Solid element labels: {}".format(len(solid_labels)))
print("  Void element labels: {}".format(len(void_labels)))

# Create element sets on the part
if solid_labels:
    solid_elements = part.elements.sequenceFromLabels(solid_labels)
    part.Set(elements=solid_elements, name='SolidElements')

if void_labels:
    void_elements = part.elements.sequenceFromLabels(void_labels)
    part.Set(elements=void_elements, name='VoidElements')

# Create materials
if 'IN718_Solid' not in model.materials.keys():
    model.Material(name='IN718_Solid')
    model.materials['IN718_Solid'].Elastic(table=((E_SOLID, NU),))
    model.materials['IN718_Solid'].Density(table=((8.19e-9,),))

if 'IN718_Void' not in model.materials.keys():
    model.Material(name='IN718_Void')
    model.materials['IN718_Void'].Elastic(table=((E_VOID, NU),))
    model.materials['IN718_Void'].Density(table=((8.19e-12,),))

# Create sections
if 'SolidSection' not in model.sections.keys():
    model.HomogeneousSolidSection(name='SolidSection', material='IN718_Solid')

if 'VoidSection' not in model.sections.keys():
    model.HomogeneousSolidSection(name='VoidSection', material='IN718_Void')

# Assign sections to element sets
if solid_labels:
    part.SectionAssignment(
        region=part.sets['SolidElements'],
        sectionName='SolidSection',
        offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)

if void_labels:
    part.SectionAssignment(
        region=part.sets['VoidElements'],
        sectionName='VoidSection',
        offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)

print("  Materials and sections assigned")

# Regenerate assembly to pick up section changes
assembly.regenerate()

# =========================================================================
# STEP 3: Remove optimization task (run as standard analysis)
# =========================================================================
print("\n[3/4] Preparing model for standard analysis...")

# Delete optimization-related objects if they exist
if 'Experiment5_TO' in mdb.optimizationProcesses.keys():
    del mdb.optimizationProcesses['Experiment5_TO']
if 'TopoTask' in model.optimizationTasks.keys():
    del model.optimizationTasks['TopoTask']

# =========================================================================
# STEP 4: Create and run validation jobs for each load case
# =========================================================================
print("\n[4/4] Creating and running validation jobs...")

upper_rp_region = assembly.sets['UpperRP']

for load_kn in VALIDATION_LOADS:
    print("\n  --- {} kN ---".format(load_kn))

    # Delete existing loads
    for name in list(model.loads.keys()):
        del model.loads[name]

    # Apply new load
    load_name = 'VerticalLoad_{}kN'.format(load_kn)
    model.ConcentratedForce(
        name=load_name,
        createStepName='LoadStep',
        region=upper_rp_region,
        cf2=float(load_kn * 1000))
    print("  Applied: {} N".format(load_kn * 1000))

    # Create job
    job_name = 'Validation_{}kN'.format(load_kn)
    if job_name in mdb.jobs.keys():
        del mdb.jobs[job_name]

    mdb.Job(name=job_name, model='Experiment5_TO',
            type=ANALYSIS, numCpus=NUM_CPUS, numDomains=NUM_CPUS)

    # Save model state
    mdb.saveAs(os.path.join(PROJECT_DIR, 'Experiment5_Validation.cae'))

    # Write input file for debugging
    mdb.jobs[job_name].writeInput()
    print("  Input written: {}.inp".format(job_name))

    # Submit and wait
    print("  Submitting {}...".format(job_name))
    mdb.jobs[job_name].submit()
    mdb.jobs[job_name].waitForCompletion()

    # Check result
    if os.path.exists(os.path.join(PROJECT_DIR, '{}.odb'.format(job_name))):
        print("  PASSED: {}.odb created".format(job_name))
    else:
        print("  WARNING: {}.odb not found".format(job_name))

print("\n" + "=" * 70)
print("Validation job setup complete")
print("  Jobs created: {}".format(
    ['Validation_{}kN'.format(kn) for kn in VALIDATION_LOADS]))
print("=" * 70)
