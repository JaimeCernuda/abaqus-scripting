============================================================
STEP 4: ANALYZE RESULTS
============================================================

  Opening: files/CantileverBeam.odb
  ✓ ODB opened successfully

  Model: D:/Libraries/Documents/projects/Abaqus/cantilever/files/CantileverBeam.odb
  Description: DDB object

------------------------------------------------------------
AVAILABLE DATA IN ODB
------------------------------------------------------------

  Steps: ['LoadStep']

  Step 'LoadStep':
    - Frames: 7
    - Time: 0.0
    - Field outputs: ['E', 'RF', 'S', 'U']
    - History regions: 1

  Analyzing: Step 'LoadStep', Frame 6

------------------------------------------------------------
DISPLACEMENT ANALYSIS
------------------------------------------------------------

  Displacement components:
    U1 (X): -1.894262e-01 to 1.894262e-01 mm
    U2 (Y): -2.532815e+00 to 4.819114e-38 mm
    U3 (Z): -7.691433e-03 to 7.691433e-03 mm

  Maximum displacement magnitude: 2.539161e+00 mm
  Location: Node 4

------------------------------------------------------------
STRESS ANALYSIS
------------------------------------------------------------

  Stress components (normal):
    S11 (X): -388.64 to 388.64 MPa
    S22 (Y): -9.02 to 9.02 MPa
    S33 (Z): -38.54 to 38.54 MPa

  Maximum von Mises stress: 384.35 MPa
  Location: Element 73

------------------------------------------------------------
REACTION FORCE ANALYSIS
------------------------------------------------------------

  Nodes with reactions: 9

  Total reaction forces:
    RF1 (X): 0.00 N
    RF2 (Y): 1000.00 N
    RF3 (Z): 0.00 N

  Resultant: 1000.00 N

------------------------------------------------------------
ENERGY ANALYSIS
------------------------------------------------------------

  No strain energy output found

------------------------------------------------------------
MESH INFORMATION
------------------------------------------------------------

  Instance: BEAM-1
  Nodes: 189
  Elements: 80

  Element types:
    C3D8R: 80

============================================================
ANALYSIS SUMMARY
============================================================

File: files/CantileverBeam.odb

RESULTS:
  Max displacement: 2.539161e+00 mm (Node 4)
  Max von Mises stress: 384.35 MPa (Element 73)
  Reaction force (Y): 1000.00 N

MESH:
  Nodes: 189
  Elements: 80

Report written to: files/CantileverBeam_report.txt

============================================================
STEP 4 COMPLETE
============================================================