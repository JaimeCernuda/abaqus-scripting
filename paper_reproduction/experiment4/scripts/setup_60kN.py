import os
from abaqus import *
from abaqusConstants import *

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, os.pardir))
os.chdir(PROJECT_DIR)

NUM_CPUS = int(os.environ.get('ABAQUS_NUM_CPUS', '1'))

openMdb(os.path.join(PROJECT_DIR, 'Experiment4_TO_Specimen.cae'))

model = mdb.models['Experiment4_TO_Specimen']

# Delete old load
if 'VerticalLoad_20kN' in model.loads.keys():
    del model.loads['VerticalLoad_20kN']

# Create new load with 60 kN
assembly = model.rootAssembly
upper_rp_region = assembly.sets['UpperRP']
model.ConcentratedForce(name='VerticalLoad_60kN', createStepName='FatigueTest',
    region=upper_rp_region, cf2=60000.0)

# Create new job
job_name = 'Job_60kN'
if job_name in mdb.jobs.keys():
    del mdb.jobs[job_name]
mdb.Job(name=job_name, model='Experiment4_TO_Specimen', type=ANALYSIS, numCpus=NUM_CPUS)

mdb.saveAs(os.path.join(PROJECT_DIR, 'Experiment4_TO_Specimen_60kN.cae'))
mdb.jobs[job_name].writeInput()
print('60kN job created')
