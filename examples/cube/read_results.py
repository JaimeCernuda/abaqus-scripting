# read_results.py
# Read results from Abaqus ODB file
# Run with: abaqus python read_results.py
# Note: This uses 'abaqus python', not 'abaqus cae'

from odbAccess import *
from abaqusConstants import *
import json

def read_odb_results(odb_path):
    """
    Read and print results from an Abaqus ODB file.
    """
    print("\n" + "="*60)
    print(f"Reading results from: {odb_path}")
    print("="*60 + "\n")
    
    # Open the ODB
    try:
        odb = openOdb(path=odb_path, readOnly=True)
    except Exception as e:
        print(f"ERROR: Could not open ODB file: {e}")
        print("Make sure you've run the analysis first:")
        print("  abaqus job=CubeAnalysis interactive")
        return
    
    # Print basic info
    print("ODB Info:")
    print(f"  Analysis Title: {odb.analysisTitle}")
    print(f"  Description: {odb.description}")
    print(f"  Path: {odb.path}")
    
    # List steps
    print(f"\nSteps ({len(odb.steps)}):")
    for step_name, step in odb.steps.items():
        print(f"  - {step_name}")
        print(f"      Frames: {len(step.frames)}")
        print(f"      Time period: {step.timePeriod}")
    
    # Get the last frame of the last step
    last_step = odb.steps[odb.steps.keys()[-1]]
    last_frame = last_step.frames[-1]
    
    print(f"\nLast frame info:")
    print(f"  Step: {last_step.name}")
    print(f"  Frame: {last_frame.frameId}")
    print(f"  Time: {last_frame.frameValue}")
    
    # List available field outputs
    print(f"\nAvailable Field Outputs:")
    for fo_name in last_frame.fieldOutputs.keys():
        fo = last_frame.fieldOutputs[fo_name]
        print(f"  - {fo_name}: {fo.description}")
    
    # Extract stress data if available
    if 'S' in last_frame.fieldOutputs:
        print("\n" + "-"*60)
        print("STRESS RESULTS (S)")
        print("-"*60)
        
        stress_field = last_frame.fieldOutputs['S']
        
        # Get max Mises stress
        max_mises = 0.0
        max_mises_element = None
        
        for value in stress_field.values:
            if hasattr(value, 'mises') and value.mises is not None:
                if value.mises > max_mises:
                    max_mises = value.mises
                    max_mises_element = value.elementLabel
        
        print(f"  Maximum von Mises stress: {max_mises:.4f}")
        if max_mises_element:
            print(f"  At element: {max_mises_element}")
    
    # Extract displacement data if available
    if 'U' in last_frame.fieldOutputs:
        print("\n" + "-"*60)
        print("DISPLACEMENT RESULTS (U)")
        print("-"*60)
        
        disp_field = last_frame.fieldOutputs['U']
        
        # Get max displacement magnitude
        max_disp = 0.0
        max_disp_node = None
        
        for value in disp_field.values:
            if hasattr(value, 'magnitude') and value.magnitude is not None:
                if value.magnitude > max_disp:
                    max_disp = value.magnitude
                    max_disp_node = value.nodeLabel
        
        print(f"  Maximum displacement magnitude: {max_disp:.6f}")
        if max_disp_node:
            print(f"  At node: {max_disp_node}")
    
    # Extract history output if available
    print("\n" + "-"*60)
    print("HISTORY OUTPUT")
    print("-"*60)
    
    for step_name, step in odb.steps.items():
        for region_name, history_region in step.historyRegions.items():
            print(f"\n  Region: {region_name}")
            for output_name in history_region.historyOutputs.keys():
                ho = history_region.historyOutputs[output_name]
                if len(ho.data) > 0:
                    last_value = ho.data[-1][1]
                    print(f"    {output_name}: {last_value:.6e} (final)")
    
    # Close ODB
    odb.close()
    
    print("\n" + "="*60)
    print("Results extraction complete!")
    print("="*60 + "\n")


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        odb_file = sys.argv[1]
    else:
        odb_file = 'files/CubeAnalysis.odb'
    
    read_odb_results(odb_file)
