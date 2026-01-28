import os
from abaqus import *
from abaqusConstants import *
os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')
openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v17.cae')
job = mdb.jobs['Job_FatigueTest_v16']
job.writeInput()
print('Input file written to: {}'.format(os.getcwd()))
job.submit()
job.waitForCompletion()
print('Job completed')
