# 02_define_material.py - EXPERIMENT 3
#
# Defines IN718 material properties for the bracket.
# Same material as Experiments 1 and 2.
#
# Run with: abaqus cae noGUI=paper_reproduction/scripts/experiment3/02_define_material.py

from abaqus import *
from abaqusConstants import *
from caeModules import *

print("\n" + "=" * 70)
print("EXPERIMENT 3 - STEP 2: DEFINE IN718 MATERIAL")
print("=" * 70)

# Material properties (from paper - IN718 nickel superalloy)
YOUNGS_MODULUS = 198400.0  # MPa
POISSONS_RATIO = 0.30
DENSITY = 8.19e-9  # tonne/mm^3
PROPORTIONAL_LIMIT = 980.0  # MPa (yield strength)

MODEL_NAME = 'TO_Bracket_Exp3'
PART_NAME = 'Bracket'

print(f"\nMaterial: IN718 (Nickel Superalloy)")
print(f"  Young's modulus: {YOUNGS_MODULUS:.0f} MPa")
print(f"  Poisson's ratio: {POISSONS_RATIO}")
print(f"  Density: {DENSITY:.2e} tonne/mm^3")
print(f"  Yield strength: {PROPORTIONAL_LIMIT:.0f} MPa")

# Load geometry
print("\n[1/3] Loading geometry model...")
openMdb(pathName='paper_reproduction/outputs/experiment3/models/TO_Bracket_Geometry.cae')
model = mdb.models[MODEL_NAME]
part = model.parts[PART_NAME]
print(f"       Model '{MODEL_NAME}' loaded")

# Create material
print("\n[2/3] Creating IN718 material...")
material = model.Material(name='IN718')
material.Elastic(table=((YOUNGS_MODULUS, POISSONS_RATIO),))
material.Density(table=((DENSITY,),))
# Simplified plasticity with yield point
material.Plastic(table=((PROPORTIONAL_LIMIT, 0.0),))
print("       IN718 material created")

# Create section and assign
print("\n[3/3] Creating section and assigning...")
model.HomogeneousSolidSection(name='BracketSection', material='IN718', thickness=None)
region = part.sets['AllCells']
part.SectionAssignment(region=region, sectionName='BracketSection', offset=0.0,
                       offsetType=MIDDLE_SURFACE, offsetField='',
                       thicknessAssignment=FROM_SECTION)
print("       Section assigned to all cells")

# Save
mdb.saveAs(pathName='paper_reproduction/outputs/experiment3/models/TO_Bracket_Material.cae')

print("\n" + "=" * 70)
print("EXPERIMENT 3 - STEP 2 COMPLETE")
print("=" * 70)
