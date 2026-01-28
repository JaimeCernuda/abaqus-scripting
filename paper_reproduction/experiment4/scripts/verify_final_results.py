# -*- coding: utf-8 -*-
"""
Verify final results from all three job files.
"""
import os
from odbAccess import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')

output = []
output.append("=" * 70)
output.append("EXPERIMENT 4 - FINAL RESULTS VERIFICATION")
output.append("=" * 70)
output.append("")

jobs = [
    ('Job_20kN.odb', '20 kN'),
    ('Job_60kN.odb', '60 kN'),
    ('Job_100kN.odb', '100 kN'),
]

for odb_name, load in jobs:
    try:
        odb = openOdb(odb_name, readOnly=True)

        # Get the last frame of the last step
        step = odb.steps.values()[-1]
        frame = step.frames[-1]

        # Get stress
        stress_field = frame.fieldOutputs['S']
        stress_vals = [v.mises for v in stress_field.values]
        max_stress = max(stress_vals)

        # Get displacement
        disp_field = frame.fieldOutputs['U']
        disp_vals = [((v.data[0]**2 + v.data[1]**2 + v.data[2]**2)**0.5) for v in disp_field.values]
        max_disp = max(disp_vals)

        # Get plastic strain if available
        peeq = 0.0
        if 'PEEQ' in frame.fieldOutputs:
            peeq_field = frame.fieldOutputs['PEEQ']
            peeq_vals = [v.data for v in peeq_field.values]
            peeq = max(peeq_vals)

        output.append("{}: {} load".format(odb_name, load))
        output.append("  Max Stress: {:.2f} MPa".format(max_stress))
        output.append("  Max Displacement: {:.4f} mm".format(max_disp))
        output.append("  Max PEEQ: {:.4f}".format(peeq))
        output.append("")

        odb.close()
    except Exception as e:
        output.append("{}: Error - {}".format(odb_name, str(e)))
        output.append("")

output.append("=" * 70)
output.append("VERIFICATION COMPLETE")
output.append("=" * 70)

result_text = '\n'.join(output)
print(result_text)

with open('final_verification.txt', 'w') as f:
    f.write(result_text)
