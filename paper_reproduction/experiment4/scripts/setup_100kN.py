import os
from abaqus import *
from abaqusConstants import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')
openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v19_60kN.cae')

model = mdb.models['Experiment4_TO_Specimen']

# Delete old load
for name in list(model.loads.keys()):
    del model.loads[name]

# Create new load with 100 kN
assembly = model.rootAssembly
upper_rp_region = assembly.sets['UpperRP']
model.ConcentratedForce(name='VerticalLoad_100kN', createStepName='FatigueTest',
    region=upper_rp_region, cf2=100000.0)

# Create new job
job_name = 'Job_v19_100kN'
if job_name in mdb.jobs.keys():
    del mdb.jobs[job_name]
mdb.Job(name=job_name, model='Experiment4_TO_Specimen', type=ANALYSIS, numCpus=1)

mdb.saveAs(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v19_100kN.cae')
mdb.jobs[job_name].writeInput()
print('100kN job created')
