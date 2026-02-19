# -*- coding: utf-8 -*-
"""
Generate .par file from saved OptimizationProcess.

Opens the CAE (with OptimizationProcess already defined) and calls
writeParAndInputFiles() to generate the .par file needed by the
abaqus optimization CLI.
"""

import os
import sys
sys.stdout.flush()

from abaqus import *
from abaqusConstants import *
from caeModules import *

try:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    SCRIPT_DIR = os.path.join(os.getcwd(), 'scripts')
PROJECT_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, os.pardir))
os.chdir(PROJECT_DIR)

print("=" * 70)
print("WRITE PAR FILE")
print("=" * 70)
sys.stdout.flush()

# Open saved CAE
print("[1/3] Loading saved CAE...")
sys.stdout.flush()
openMdb(os.path.join(PROJECT_DIR, 'Experiment5_TO.cae'))

print("  Models: {}".format(list(mdb.models.keys())))
print("  Jobs: {}".format(list(mdb.jobs.keys())))
print("  OptimizationProcesses: {}".format(list(mdb.optimizationProcesses.keys())))
sys.stdout.flush()

# Get the optimization process — do NOT print/stringify the object (crashes kernel)
print("[2/3] Calling writeParAndInputFiles()...")
sys.stdout.flush()
opt_process = mdb.optimizationProcesses['Experiment5_Optimization']

import traceback
try:
    opt_process.writeParAndInputFiles()
    print("  SUCCESS: writeParAndInputFiles() completed")
except Exception as e:
    print("  ERROR: {} - {}".format(type(e).__name__, e))
    traceback.print_exc()
sys.stdout.flush()

# Check for .par files
print("[3/3] Checking for .par files...")
import glob
par_files = glob.glob(os.path.join(PROJECT_DIR, '*.par'))
par_files += glob.glob(os.path.join(PROJECT_DIR, '**', '*.par'))
if par_files:
    for pf in par_files:
        size = os.path.getsize(pf)
        print("  Found: {} ({} bytes)".format(pf, size))
else:
    print("  No .par files found anywhere")
    # List working directory to see what was generated
    print("  Working dir contents:")
    for f in sorted(os.listdir(PROJECT_DIR)):
        print("    {}".format(f))

print("=" * 70)
sys.stdout.flush()
