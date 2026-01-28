# 02_define_in718_material.py
#
# Defines IN718 (Inconel 718) material properties from the paper
# "Fatigue Response of a Topology Optimized Feature-based Component"
#
# Material data from Table 2:
# - Elastic: E = 198.4 GPa, nu = 0.30
# - Plastic: Converted from Ramberg-Osgood (alpha=0.002041, n=11.5)
# - Density: 8.19e-9 tonne/mm³
#
# Run with: abaqus cae noGUI=paper_reproduction/scripts/02_define_in718_material.py
#
# Prerequisites: Run 01_create_to_geometry.py first

from abaqus import *
from abaqusConstants import *
from caeModules import *
import math

print("\n" + "=" * 70)
print("PAPER REPRODUCTION - STEP 2: DEFINE IN718 MATERIAL")
print("=" * 70)

# =============================================================================
# MATERIAL PROPERTIES (from paper Table 2)
# =============================================================================

# Elastic properties
YOUNGS_MODULUS = 198400.0  # MPa (198.4 GPa from paper)
POISSONS_RATIO = 0.30

# Density (tonne/mm³ for mm-N-MPa-tonne unit system)
DENSITY = 8.19e-9  # IN718 standard density

# Ramberg-Osgood parameters (from paper Table 2)
# Strain equation: eps = sigma/E + alpha * (sigma/E)^n
RO_ALPHA = 0.002041
RO_N = 11.5

# Key stress values from paper
PROPORTIONAL_LIMIT = 980.0  # MPa
YIELD_STRENGTH_02 = 1191.0  # MPa (0.2% offset yield)

# Model and part names (must match geometry script)
MODEL_NAME = 'TO_Bracket'
PART_NAME = 'Bracket'

print("\nMaterial: IN718 (Inconel 718)")
print(f"  Young's Modulus:    {YOUNGS_MODULUS/1000:.1f} GPa")
print(f"  Poisson's Ratio:    {POISSONS_RATIO}")
print(f"  Density:            {DENSITY:.2e} tonne/mm³")
print(f"  Proportional Limit: {PROPORTIONAL_LIMIT} MPa")
print(f"  Yield Strength:     {YIELD_STRENGTH_02} MPa (0.2% offset)")

# =============================================================================
# LOAD EXISTING MODEL
# =============================================================================

print("\n[1/4] Loading geometry model...")

# Open the model from previous step
openMdb(pathName='paper_reproduction/outputs/experiment1/TO_Bracket_Geometry.cae')

# Get model and part references
model = mdb.models[MODEL_NAME]
part = model.parts[PART_NAME]

print(f"       Model '{MODEL_NAME}' loaded")

# =============================================================================
# CONVERT RAMBERG-OSGOOD TO PLASTIC STRAIN TABLE
# =============================================================================

print("\n[2/4] Converting Ramberg-Osgood to plastic strain table...")


def ramberg_osgood_to_plastic(sigma, E, alpha, n):
    """
    Convert true stress to plastic strain using Ramberg-Osgood equation.

    Total strain: eps_total = sigma/E + alpha * (sigma/E)^n
    Elastic strain: eps_elastic = sigma/E
    Plastic strain: eps_plastic = alpha * (sigma/E)^n

    Parameters:
        sigma: True stress (MPa)
        E: Young's modulus (MPa)
        alpha: Ramberg-Osgood coefficient
        n: Strain hardening exponent

    Returns:
        eps_plastic: Plastic strain
    """
    eps_plastic = alpha * (sigma / E) ** n
    return eps_plastic


# Generate plastic strain data points
# Abaqus requires (yield_stress, plastic_strain) pairs
# Start from proportional limit (where plastic strain begins)

stress_points = [
    PROPORTIONAL_LIMIT,  # First yield point
    1000.0,
    1050.0,
    1100.0,
    1150.0,
    YIELD_STRENGTH_02,  # 0.2% offset yield
    1250.0,
    1300.0,
    1350.0,
    1400.0,
    1450.0,
    1500.0,  # Beyond yield for ductile response
]

plastic_data = []
for sigma in stress_points:
    eps_p = ramberg_osgood_to_plastic(sigma, YOUNGS_MODULUS, RO_ALPHA, RO_N)
    # First point should have zero plastic strain (or very small)
    if sigma == PROPORTIONAL_LIMIT:
        eps_p = 0.0
    plastic_data.append((sigma, eps_p))

print("       Stress (MPa)  |  Plastic Strain")
print("       " + "-" * 35)
for stress, strain in plastic_data:
    print(f"       {stress:10.1f}   |  {strain:.6f}")

# Convert to tuple of tuples for Abaqus
plastic_table = tuple(plastic_data)

# =============================================================================
# CREATE MATERIAL
# =============================================================================

print("\n[3/4] Creating IN718 material definition...")

# Create material
material = model.Material(name='IN718')

# Define elastic behavior
material.Elastic(table=((YOUNGS_MODULUS, POISSONS_RATIO),))
print("       Elastic properties defined")

# Define plastic behavior
material.Plastic(table=plastic_table)
print("       Plastic properties defined (Ramberg-Osgood converted)")

# Define density
material.Density(table=((DENSITY,),))
print("       Density defined")

# =============================================================================
# CREATE SECTION AND ASSIGN TO PART
# =============================================================================

print("\n[4/4] Creating section and assigning to part...")

# Create solid section
model.HomogeneousSolidSection(
    name='BracketSection',
    material='IN718',
    thickness=None
)

# Get the AllCells set created in geometry script
region = part.sets['AllCells']

# Assign section to all cells
part.SectionAssignment(
    region=region,
    sectionName='BracketSection',
    offset=0.0,
    offsetType=MIDDLE_SURFACE,
    offsetField='',
    thicknessAssignment=FROM_SECTION
)

print("       Section 'BracketSection' created with IN718 material")
print("       Section assigned to all cells")

# =============================================================================
# SAVE MODEL
# =============================================================================

mdb.saveAs(pathName='paper_reproduction/outputs/experiment1/TO_Bracket_Material.cae')

print("\n" + "=" * 70)
print("STEP 2 COMPLETE - MATERIAL DEFINED")
print("=" * 70)
print(f"""
Output files:
  - paper_reproduction/outputs/experiment1/TO_Bracket_Material.cae

Material summary (IN718):
  - Elastic: E = {YOUNGS_MODULUS/1000:.1f} GPa, nu = {POISSONS_RATIO}
  - Plastic: {len(plastic_data)} data points from Ramberg-Osgood
  - Density: {DENSITY:.2e} tonne/mm³

Section:
  - 'BracketSection' assigned to entire part

Note on unit system (mm-tonne-s-N-MPa):
  - Length: mm
  - Force: N
  - Stress/Modulus: MPa
  - Density: tonne/mm³
  - Time: s

Next: Run 03_setup_analysis.py to create assembly and apply loads
""")
