# extract_optimized_geometry.py
#
# Extract the optimized topology from an Abaqus optimization run
# Exports to STL format for use in CAD or 3D printing
#
# Run with: abaqus cae script=extract_optimized_geometry.py
# (Needs GUI for extraction dialog, or use noGUI with modifications)

from abaqus import *
from abaqusConstants import *
from caeModules import *
from odbAccess import *
import os

print("\n" + "="*70)
print("EXTRACT OPTIMIZED GEOMETRY")
print("="*70)

# =============================================================================
# CONFIGURATION
# =============================================================================

# Path to optimization output directory
OPT_PROCESS_NAME = 'OptProcess'
OPT_DIR = OPT_PROCESS_NAME + '/TOSCA_POST'

# Threshold for keeping elements (density > threshold = solid)
DENSITY_THRESHOLD = 0.5  # Elements with density > 50% are kept

# Output filename
OUTPUT_STL = 'optimized_bracket.stl'
OUTPUT_INP = 'optimized_bracket.inp'

# =============================================================================
# FIND OPTIMIZATION RESULTS
# =============================================================================

print("\n[1/4] Locating optimization results...")

# Check if optimization directory exists
if not os.path.exists(OPT_DIR):
    print("ERROR: Optimization directory not found: {}".format(OPT_DIR))
    print("Make sure you've run the optimization first!")
    print("\nLooking for available directories...")
    for item in os.listdir('.'):
        if os.path.isdir(item):
            print("  - {}/".format(item))
    raise SystemExit(1)

# Find the final ODB file
odb_files = [f for f in os.listdir(OPT_DIR) if f.endswith('.odb')]
if not odb_files:
    print("ERROR: No ODB files found in {}".format(OPT_DIR))
    raise SystemExit(1)

# The final design is typically the last ODB or one named specifically
# Sort to get the last iteration
odb_files.sort()
final_odb = os.path.join(OPT_DIR, odb_files[-1])
print("  Found {} ODB files".format(len(odb_files)))
print("  Using: {}".format(final_odb))

# =============================================================================
# READ OPTIMIZATION RESULTS
# =============================================================================

print("\n[2/4] Reading optimization results...")

odb = openOdb(path=final_odb, readOnly=True)

# Get the last frame
step = odb.steps[odb.steps.keys()[-1]]
frame = step.frames[-1]

print("  Step: {}".format(step.name))
print("  Frame: {} (time: {})".format(frame.frameId, frame.frameValue))

# Get element densities (this is the optimization result)
# The field is typically named 'DENSITY' or 'MAT_PROP_NORMALIZED'
density_field = None
for field_name in frame.fieldOutputs.keys():
    if 'DENSITY' in field_name.upper() or 'MAT_PROP' in field_name.upper():
        density_field = frame.fieldOutputs[field_name]
        print("  Found density field: {}".format(field_name))
        break

if density_field is None:
    print("  Available fields:")
    for name in frame.fieldOutputs.keys():
        print("    - {}".format(name))
    print("\n  Warning: Could not find density field automatically")

# =============================================================================
# ANALYZE DENSITY DISTRIBUTION
# =============================================================================

print("\n[3/4] Analyzing density distribution...")

if density_field:
    densities = []
    for value in density_field.values:
        if hasattr(value, 'data'):
            densities.append(value.data)
        else:
            densities.append(value.magnitude if hasattr(value, 'magnitude') else 0)

    import math

    min_density = min(densities)
    max_density = max(densities)
    avg_density = sum(densities) / len(densities)

    solid_elements = sum(1 for d in densities if d >= DENSITY_THRESHOLD)
    void_elements = len(densities) - solid_elements

    print("  Total elements: {}".format(len(densities)))
    print("  Density range: {:.3f} - {:.3f}".format(min_density, max_density))
    print("  Average density: {:.3f}".format(avg_density))
    print("  Solid elements (>= {}): {} ({:.1f}%)".format(
        DENSITY_THRESHOLD, solid_elements, 100.0 * solid_elements / len(densities)))
    print("  Void elements (< {}): {} ({:.1f}%)".format(
        DENSITY_THRESHOLD, void_elements, 100.0 * void_elements / len(densities)))

odb.close()

# =============================================================================
# EXPORT GEOMETRY
# =============================================================================

print("\n[4/4] Exporting optimized geometry...")

print("""
To export the optimized geometry from Abaqus/CAE:

Method 1 - GUI (Recommended):
  1. Open your .cae file in Abaqus/CAE
  2. Go to Job module
  3. Select: Optimization > Extract
  4. Choose the optimization process
  5. Set the iso-surface value (typically 0.3-0.5)
  6. Choose output format:
     - STL: For 3D printing / CAD import
     - INP: For further Abaqus analysis
  7. Click OK

Method 2 - Python (in Abaqus/CAE):
  from abaqus import *
  from caeModules import *

  # Extract isosurface at threshold
  session.viewports['Viewport: 1'].odbDisplay.setFrame(step=-1, frame=-1)
  session.viewports['Viewport: 1'].odbDisplay.setValues(
      visibleOutputs=('DENSITY',))

  # Use the Optimization module extraction
  # (This requires GUI interaction)

Method 3 - Post-process with Python:
  Read the ODB, filter elements by density,
  write new INP with only solid elements
  (See advanced script below)
""")

print("\n" + "="*70)
print("EXTRACTION INFO COMPLETE")
print("="*70)

# =============================================================================
# ADVANCED: Manual extraction (creates filtered INP file)
# =============================================================================

def extract_solid_elements_to_inp(odb_path, output_inp, threshold=0.5):
    """
    Extract elements above density threshold and write to INP file.
    This is a simplified approach - production code would need more detail.
    """
    print("\nExtracting solid elements (density >= {}) to {}...".format(threshold, output_inp))

    odb = openOdb(path=odb_path, readOnly=True)

    # Get density field
    step = odb.steps[odb.steps.keys()[-1]]
    frame = step.frames[-1]

    density_field = None
    for name in frame.fieldOutputs.keys():
        if 'DENSITY' in name.upper():
            density_field = frame.fieldOutputs[name]
            break

    if not density_field:
        print("ERROR: No density field found")
        odb.close()
        return

    # Get solid element labels
    solid_elements = set()
    for value in density_field.values:
        density = value.data if hasattr(value, 'data') else value.magnitude
        if density >= threshold:
            solid_elements.add(value.elementLabel)

    print("  Found {} solid elements".format(len(solid_elements)))

    # Get instance
    instance = odb.rootAssembly.instances[odb.rootAssembly.instances.keys()[0]]

    # Write INP file
    with open(output_inp, 'w') as f:
        f.write("*HEADING\n")
        f.write("Extracted optimized geometry\n")
        f.write("** Elements with density >= {}\n".format(threshold))
        f.write("**\n")

        # Write nodes
        f.write("*NODE\n")
        used_nodes = set()
        for elem in instance.elements:
            if elem.label in solid_elements:
                for node_label in elem.connectivity:
                    used_nodes.add(node_label)

        for node in instance.nodes:
            if node.label in used_nodes:
                coords = node.coordinates
                if len(coords) == 3:
                    f.write("{}, {}, {}, {}\n".format(
                        node.label, coords[0], coords[1], coords[2]))
                else:
                    f.write("{}, {}, {}, 0.0\n".format(
                        node.label, coords[0], coords[1]))

        # Write elements
        f.write("*ELEMENT, TYPE=C3D8R\n")  # Adjust type as needed
        for elem in instance.elements:
            if elem.label in solid_elements:
                conn = ', '.join(str(n) for n in elem.connectivity)
                f.write("{}, {}\n".format(elem.label, conn))

    print("  Wrote {}".format(output_inp))
    odb.close()

# Uncomment to run extraction:
# extract_solid_elements_to_inp(final_odb, OUTPUT_INP, DENSITY_THRESHOLD)
