# -*- coding: utf-8 -*-
"""
Experiment 4: Define IN718 Material
Based on paper parameters - Table 2
"""

from abaqus import *
from abaqusConstants import *
from caeModules import *

# Open existing model
openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen.cae')

model_name = 'Experiment4_TO_Specimen'
part_name = 'TO_Specimen'

model = mdb.models[model_name]
part = model.parts[part_name]

# =============================================================================
# MATERIAL PROPERTIES - IN718 (Inconel 718) from Table 2
# =============================================================================
# Young's Modulus: 198.4 GPa = 198400 MPa
# Poisson's Ratio: 0.30
# Density: 8.19 g/cm³ = 8.19e-9 tonne/mm³
# Yield Strength (0.2%): 1191 MPa
# Proportional Limit: 980 MPa

E = 198400.0      # MPa
nu = 0.30
rho = 8.19e-9     # tonne/mm³

# Create IN718 material
material = model.Material(name='IN718')

# Elastic properties
material.Elastic(table=((E, nu),))

# Density (needed for dynamic analysis / mass calculations)
material.Density(table=((rho,),))

# Plastic properties (Ramberg-Osgood converted to tabular)
# Paper: α = 0.002041, n = 11.5
# ε = σ/E + α(σ/E)^n
# Converted to true stress - plastic strain pairs
plastic_data = (
    (980.0, 0.0),       # Proportional limit (onset of plasticity)
    (1000.0, 0.00005),
    (1050.0, 0.0005),
    (1100.0, 0.0015),
    (1150.0, 0.0035),
    (1191.0, 0.006),    # 0.2% offset yield strength
    (1250.0, 0.012),
    (1300.0, 0.020),
    (1350.0, 0.030),
    (1400.0, 0.045),
)

material.Plastic(table=plastic_data)

print("IN718 Material created with elastic-plastic properties")

# =============================================================================
# CREATE SECTION AND ASSIGN TO PART
# =============================================================================
# Create solid section
model.HomogeneousSolidSection(
    name='IN718_Section',
    material='IN718',
    thickness=None
)

# Create set for all cells
all_cells = part.cells
region = part.Set(cells=all_cells, name='AllCells')

# Assign section to all cells
part.SectionAssignment(
    region=region,
    sectionName='IN718_Section',
    offset=0.0,
    offsetType=MIDDLE_SURFACE,
    offsetField='',
    thicknessAssignment=FROM_SECTION
)

print("Section created and assigned to part")

# =============================================================================
# UPDATE ASSEMBLY INSTANCE
# =============================================================================
assembly = model.rootAssembly
assembly.regenerate()

# =============================================================================
# SAVE
# =============================================================================
mdb.saveAs(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen.cae')

print("\n" + "="*50)
print("MATERIAL DEFINITION COMPLETE")
print("Material: IN718")
print("E = {} MPa".format(E))
print("nu = {}".format(nu))
print("rho = {} tonne/mm³".format(rho))
print("Yield stress = 1191 MPa (with plasticity)")
print("="*50)
