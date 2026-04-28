"""Generate IN718 fatigue specimen Exodus mesh using Gmsh + netCDF4.

Rectangular envelope (146.17 x 64.60 x 25 mm) with 3 pin holes (dia 12.7mm).
Writes proper Exodus II with side sets for Plato Analyze BCs/loads.

Pin locations (from experiment 10):
  Upper:      (0,     132.17, 12.5)
  Lower left: (-23.30, 14.00, 12.5)
  Lower right:(+23.30, 14.00, 12.5)

Side sets:
  1: fixed_left_yz   — inner face of lower left block (X = -14.3, Y=[0,28])
  2: fixed_right_yz  — inner face of lower right block (X = +14.3, Y=[0,28])
  3: load_upper      — top face of upper block (Y = 146.17, |X| < 9)
  4: load_left_x     — outer face of lower left block (X = -32.3, Y=[0,28])
  5: load_right_x    — outer face of lower right block (X = +32.3, Y=[0,28])
"""
import gmsh
import numpy as np
import netCDF4
import os
from collections import defaultdict

# ============================================================
# Geometry parameters (from experiment 10)
# ============================================================
TOTAL_HEIGHT = 146.17
TOTAL_WIDTH = 64.60
THICKNESS = 25.0
HALF_WIDTH = TOTAL_WIDTH / 2.0    # 32.30
HALF_THICK = THICKNESS / 2.0      # 12.50

# Block dimensions
BLOCK_WIDTH_X = 18.0
BLOCK_HEIGHT_Y = 28.0
UB_HALF = BLOCK_WIDTH_X / 2.0     # 9.0
UB_BOTTOM = 118.17

# Pin parameters
PIN_DIAMETER = 12.7
PIN_RADIUS = PIN_DIAMETER / 2.0   # 6.35

# Pin centers
UPPER_PIN_X = 0.0
UPPER_PIN_Y = TOTAL_HEIGHT - BLOCK_HEIGHT_Y / 2.0  # 132.17
LOWER_PIN_Y = BLOCK_HEIGHT_Y / 2.0                 # 14.0
LL_PIN_X = -HALF_WIDTH + BLOCK_WIDTH_X / 2.0       # -23.30
LR_PIN_X = HALF_WIDTH - BLOCK_WIDTH_X / 2.0        # +23.30

# Lower block boundaries
LB_LEFT_XMIN = -HALF_WIDTH        # -32.30
LB_LEFT_XMAX = -HALF_WIDTH + BLOCK_WIDTH_X  # -14.30
LB_RIGHT_XMIN = HALF_WIDTH - BLOCK_WIDTH_X  # +14.30
LB_RIGHT_XMAX = HALF_WIDTH        # +32.30

MESH_SIZE = 3.0

# ============================================================
# Build geometry in Gmsh
# ============================================================
gmsh.initialize()
gmsh.option.setNumber("General.Terminal", 1)
gmsh.model.add("in718_specimen")

# Create full rectangular envelope
box = gmsh.model.occ.addBox(
    -HALF_WIDTH, 0, 0,
    TOTAL_WIDTH, TOTAL_HEIGHT, THICKNESS
)

# Create 3 pin hole cylinders (through-thickness in Z)
cyl_upper = gmsh.model.occ.addCylinder(
    UPPER_PIN_X, UPPER_PIN_Y, -1,
    0, 0, THICKNESS + 2,
    PIN_RADIUS
)
cyl_ll = gmsh.model.occ.addCylinder(
    LL_PIN_X, LOWER_PIN_Y, -1,
    0, 0, THICKNESS + 2,
    PIN_RADIUS
)
cyl_lr = gmsh.model.occ.addCylinder(
    LR_PIN_X, LOWER_PIN_Y, -1,
    0, 0, THICKNESS + 2,
    PIN_RADIUS
)

# Boolean cut: box minus 3 cylinders
result, result_map = gmsh.model.occ.cut(
    [(3, box)],
    [(3, cyl_upper), (3, cyl_ll), (3, cyl_lr)]
)
gmsh.model.occ.synchronize()

# Get the resulting solid
solid_tag = result[0][1]
print(f"Solid volume tag: {solid_tag}")

# ============================================================
# Identify surfaces by center-of-mass
# ============================================================
def find_surface(tx, ty, tz, tol=2.0):
    """Find surface whose center of mass is near (tx, ty, tz)."""
    for dim, tag in gmsh.model.getEntities(2):
        com = gmsh.model.occ.getCenterOfMass(dim, tag)
        if abs(com[0]-tx)<tol and abs(com[1]-ty)<tol and abs(com[2]-tz)<tol:
            return tag
    return None

def find_surfaces_in_box(xmin, xmax, ymin, ymax, zmin, zmax, tol=1.0):
    """Find all surfaces whose center of mass is within the given box."""
    matches = []
    for dim, tag in gmsh.model.getEntities(2):
        com = gmsh.model.occ.getCenterOfMass(dim, tag)
        if (xmin-tol <= com[0] <= xmax+tol and
            ymin-tol <= com[1] <= ymax+tol and
            zmin-tol <= com[2] <= zmax+tol):
            matches.append(tag)
    return matches

# Print all surfaces for debugging
print("\nAll surfaces:")
for dim, tag in gmsh.model.getEntities(2):
    com = gmsh.model.occ.getCenterOfMass(dim, tag)
    area = gmsh.model.occ.getMass(dim, tag)
    print(f"  Surface {tag}: CoM=({com[0]:.2f}, {com[1]:.2f}, {com[2]:.2f}), area={area:.1f}")

# --- Load surface: top face of entire block (Y = TOTAL_HEIGHT) ---
# The top face at Y=146.17; for the simplified rectangular block this is the
# full width face. We want only the region near the upper pin (|X| < 9).
# Since we have a simple rectangular block, the top face spans the full width.
# We apply load to the entire top face but scale traction accordingly.
# Actually, for a rectangular block the top face CoM is at (0, 146.17, 12.5).
load_upper = find_surface(0.0, TOTAL_HEIGHT, HALF_THICK)
if load_upper is None:
    # Fallback: search with wider tolerance
    load_upper = find_surface(0.0, TOTAL_HEIGHT, HALF_THICK, tol=5.0)
print(f"\nload_upper (top face Y=146.17): {load_upper}")

# --- Fixed/load faces on lower blocks ---
# Lower left inner face: X = LB_LEFT_XMAX = -14.30, Y center ~ 14, Z center ~ 12.5
# But this is a flat face only if we had partitioned. For the simple rectangular block,
# there is no face at X = -14.3. Instead, we use the bottom face for BC and outer
# side faces for loads.

# For BCs: bottom face Y=0 of the block
# CoM of bottom face at Y=0: (0, 0, 12.5)
fixed_bottom = find_surface(0.0, 0.0, HALF_THICK)
print(f"Bottom face (Y=0): {fixed_bottom}")

# For loads on the side faces:
# Left face: X = -32.30, CoM at (-32.3, ~73, 12.5)
face_left = find_surface(-HALF_WIDTH, TOTAL_HEIGHT/2, HALF_THICK, tol=5.0)
print(f"Left face (X=-32.3): {face_left}")

# Right face: X = +32.30
face_right = find_surface(HALF_WIDTH, TOTAL_HEIGHT/2, HALF_THICK, tol=5.0)
print(f"Right face (X=+32.3): {face_right}")

# --- Cylindrical pin hole surfaces ---
# Upper pin hole: cylindrical surface near (0, 132.17, 12.5)
# Lower left pin hole: cylindrical surface near (-23.3, 14, 12.5)
# Lower right pin hole: cylindrical surface near (23.3, 14, 12.5)
# These are curved surfaces; their CoM should be at the pin center

cyl_surfs = {}
for dim, tag in gmsh.model.getEntities(2):
    com = gmsh.model.occ.getCenterOfMass(dim, tag)
    area = gmsh.model.occ.getMass(dim, tag)
    # Cylindrical surface has area ~ pi * d * thickness = pi * 12.7 * 25 ~ 998
    if 900 < area < 1100:  # cylindrical pin hole surface
        # Match to pin by Y coordinate
        if abs(com[1] - UPPER_PIN_Y) < 2:
            cyl_surfs['upper_pin'] = tag
        elif abs(com[1] - LOWER_PIN_Y) < 2 and com[0] < 0:
            cyl_surfs['ll_pin'] = tag
        elif abs(com[1] - LOWER_PIN_Y) < 2 and com[0] > 0:
            cyl_surfs['lr_pin'] = tag

print(f"\nCylindrical pin surfaces: {cyl_surfs}")

# ============================================================
# Define side sets using physical groups
# For Plato, we need faces where BCs and loads are applied.
#
# Strategy: Use bottom face for Y,Z fixed BCs (both lower pins).
# Use top face for vertical load.
# Use left/right outer faces for horizontal loads.
# ============================================================

ss_id = 1
sideset_names = {}

# Sideset 1: fixed_left_yz — bottom face (Y=0) for Y,Z fixity
# Actually we need separate sidesets for left and right BCs.
# Since it's a rectangular block, we can't isolate left/right on the bottom face.
# Instead: use the cylindrical pin hole surfaces for BCs.
# Lower left pin hole surface: fix Y, Z
# Lower right pin hole surface: fix Y, Z

if 'll_pin' in cyl_surfs:
    gmsh.model.addPhysicalGroup(2, [cyl_surfs['ll_pin']], tag=ss_id, name="fixed_left_yz")
    sideset_names[ss_id] = "fixed_left_yz"
    print(f"Sideset {ss_id}: fixed_left_yz (lower left pin hole)")
    ss_id += 1

if 'lr_pin' in cyl_surfs:
    gmsh.model.addPhysicalGroup(2, [cyl_surfs['lr_pin']], tag=ss_id, name="fixed_right_yz")
    sideset_names[ss_id] = "fixed_right_yz"
    print(f"Sideset {ss_id}: fixed_right_yz (lower right pin hole)")
    ss_id += 1

# Sideset 3: load_upper — top face for vertical load
if load_upper is not None:
    gmsh.model.addPhysicalGroup(2, [load_upper], tag=ss_id, name="load_upper")
    sideset_names[ss_id] = "load_upper"
    print(f"Sideset {ss_id}: load_upper (top face Y={TOTAL_HEIGHT})")
    ss_id += 1

# Sideset 4: load_left_x — left outer face for horizontal load
if face_left is not None:
    gmsh.model.addPhysicalGroup(2, [face_left], tag=ss_id, name="load_left_x")
    sideset_names[ss_id] = "load_left_x"
    print(f"Sideset {ss_id}: load_left_x (left face X={-HALF_WIDTH})")
    ss_id += 1

# Sideset 5: load_right_x — right outer face for horizontal load
if face_right is not None:
    gmsh.model.addPhysicalGroup(2, [face_right], tag=ss_id, name="load_right_x")
    sideset_names[ss_id] = "load_right_x"
    print(f"Sideset {ss_id}: load_right_x (right face X={+HALF_WIDTH})")
    ss_id += 1

# Volume block
gmsh.model.addPhysicalGroup(3, [solid_tag], tag=1, name="design_domain")
print(f"\nVolume block 1: design_domain")

# ============================================================
# Mesh
# ============================================================
gmsh.option.setNumber("Mesh.MeshSizeMax", MESH_SIZE)
gmsh.option.setNumber("Mesh.MeshSizeMin", MESH_SIZE * 0.5)
gmsh.option.setNumber("Mesh.ElementOrder", 1)
gmsh.option.setNumber("Mesh.Algorithm3D", 1)  # Delaunay
gmsh.option.setNumber("Mesh.Optimize", 1)
gmsh.model.mesh.generate(3)

# ============================================================
# Extract mesh data
# ============================================================
node_tags, node_coords, _ = gmsh.model.mesh.getNodes()
coords = node_coords.reshape(-1, 3)
n_nodes = len(node_tags)
tag_to_idx = {int(t): i for i, t in enumerate(node_tags)}

# Extract tet4 elements
_, tet_tags_list, tet_conn_list = gmsh.model.mesh.getElements(dim=3)
tet_conn = tet_conn_list[0].reshape(-1, 4)
n_tets = len(tet_conn)
tet_conn_0 = np.array([[tag_to_idx[int(n)] for n in elem] for elem in tet_conn])

print(f"\nMesh: {n_nodes} nodes, {n_tets} tet4 elements")

# Extract sideset triangles
ss_tris = {}
for phys_tag in sorted(sideset_names.keys()):
    phys_name = sideset_names[phys_tag]
    entities = gmsh.model.getEntitiesForPhysicalGroup(2, phys_tag)
    tris = []
    for ent in entities:
        _, tri_tags, tri_conns = gmsh.model.mesh.getElements(dim=2, tag=ent)
        if tri_conns:
            for tri in tri_conns[0].reshape(-1, 3):
                tris.append(frozenset(tag_to_idx[int(n)] for n in tri))
    ss_tris[phys_name] = tris
    print(f"  Sideset '{phys_name}': {len(tris)} triangles")

gmsh.finalize()

# ============================================================
# Build side set data: (element_id, local_face) pairs
# ============================================================
# TETRA4 face definitions (0-based node indices within element):
#   Face 1: nodes 0,1,3
#   Face 2: nodes 1,2,3
#   Face 3: nodes 0,3,2
#   Face 4: nodes 0,2,1
TET4_FACES = [
    frozenset([0, 1, 3]),  # face 1
    frozenset([1, 2, 3]),  # face 2
    frozenset([0, 3, 2]),  # face 3
    frozenset([0, 2, 1]),  # face 4
]

# Build lookup: frozenset of global node indices -> (elem_idx_1based, local_face_1based)
face_to_elem = {}
for ei in range(n_tets):
    enodes = tet_conn_0[ei]
    for fi, local_face in enumerate(TET4_FACES):
        global_face = frozenset(enodes[li] for li in local_face)
        face_to_elem[global_face] = (ei + 1, fi + 1)

ss_data = {}
for ss_name, tris in ss_tris.items():
    elems = []
    sides = []
    for tri_nodes in tris:
        if tri_nodes in face_to_elem:
            e, s = face_to_elem[tri_nodes]
            elems.append(e)
            sides.append(s)
    ss_data[ss_name] = (elems, sides)
    print(f"  Side set '{ss_name}': {len(elems)} faces matched")

# ============================================================
# Write Exodus II (netCDF-4)
# ============================================================
exo_file = "mesh.exo"
if os.path.exists(exo_file):
    os.remove(exo_file)

ds = netCDF4.Dataset(exo_file, "w", format="NETCDF4")

# Global attributes
ds.api_version = np.float32(8.25)
ds.version = np.float32(8.25)
ds.floating_point_word_size = 8
ds.file_size = 1
ds.title = "IN718 fatigue specimen - topology optimization"

num_ss = len(ss_data)

# Dimensions
ds.createDimension("len_string", 33)
ds.createDimension("len_name", 33)
ds.createDimension("num_dim", 3)
ds.createDimension("num_nodes", n_nodes)
ds.createDimension("num_elem", n_tets)
ds.createDimension("num_el_blk", 1)
ds.createDimension("num_side_sets", num_ss)
ds.createDimension("time_step", None)
ds.createDimension("num_el_in_blk1", n_tets)
ds.createDimension("num_nod_per_el1", 4)

for i, (ss_name, (elems, sides)) in enumerate(ss_data.items(), 1):
    ds.createDimension(f"num_side_ss{i}", len(elems))

# Coordinates
coor_names = ds.createVariable("coor_names", "S1", ("num_dim", "len_string"))
for i, name in enumerate(["coordx", "coordy", "coordz"]):
    coor_names[i] = list(name.ljust(33))

coordx = ds.createVariable("coordx", "f8", ("num_nodes",))
coordy = ds.createVariable("coordy", "f8", ("num_nodes",))
coordz = ds.createVariable("coordz", "f8", ("num_nodes",))
coordx[:] = coords[:, 0]
coordy[:] = coords[:, 1]
coordz[:] = coords[:, 2]

# Element block
eb_status = ds.createVariable("eb_status", "i4", ("num_el_blk",))
eb_status[:] = [1]
eb_prop1 = ds.createVariable("eb_prop1", "i4", ("num_el_blk",))
eb_prop1.setncattr("name", "ID")
eb_prop1[:] = [1]
eb_names = ds.createVariable("eb_names", "S1", ("num_el_blk", "len_name"))
eb_names[0] = list("design_domain".ljust(33))

# Connectivity (1-based)
connect1 = ds.createVariable("connect1", "i4", ("num_el_in_blk1", "num_nod_per_el1"))
connect1.elem_type = "TETRA4"
connect1[:] = tet_conn_0 + 1

# Element map
elem_map = ds.createVariable("elem_map", "i4", ("num_elem",))
elem_map[:] = np.arange(1, n_tets + 1)

# Side sets
ss_status = ds.createVariable("ss_status", "i4", ("num_side_sets",))
ss_status[:] = [1] * num_ss
ss_prop1 = ds.createVariable("ss_prop1", "i4", ("num_side_sets",))
ss_prop1.setncattr("name", "ID")
ss_prop1[:] = list(range(1, num_ss + 1))
ss_names = ds.createVariable("ss_names", "S1", ("num_side_sets", "len_name"))

for i, (ss_name, (elems, sides)) in enumerate(ss_data.items(), 1):
    ss_names[i-1] = list(ss_name.ljust(33))
    elem_var = ds.createVariable(f"elem_ss{i}", "i4", (f"num_side_ss{i}",))
    elem_var[:] = elems
    side_var = ds.createVariable(f"side_ss{i}", "i4", (f"num_side_ss{i}",))
    side_var[:] = sides

# Time
ds.createVariable("time_whole", "f8", ("time_step",))

ds.close()

# ============================================================
# Summary
# ============================================================
print(f"\nWritten: {exo_file}")
print(f"  Nodes: {n_nodes}")
print(f"  Elements: {n_tets} tet4")
print(f"  Side sets: {num_ss}")
for ss_name, (elems, sides) in ss_data.items():
    print(f"    {ss_name}: {len(elems)} faces")

# Compute domain volume for constraint
vol = TOTAL_WIDTH * TOTAL_HEIGHT * THICKNESS
pin_vol = 3 * np.pi * PIN_RADIUS**2 * THICKNESS
net_vol = vol - pin_vol
print(f"\n  Envelope volume: {vol:.1f} mm^3")
print(f"  Pin hole volume: {pin_vol:.1f} mm^3")
print(f"  Net design volume: {net_vol:.1f} mm^3")
print(f"  30% target: {0.3 * net_vol:.1f} mm^3")

# Compute traction values for reference
top_area = TOTAL_WIDTH * THICKNESS  # full top face
left_area = TOTAL_HEIGHT * THICKNESS  # full left face
right_area = TOTAL_HEIGHT * THICKNESS
print(f"\n  Top face area: {top_area:.1f} mm^2 -> 20kN traction: {20000/top_area:.2f} MPa")
print(f"  Left face area: {left_area:.1f} mm^2 -> 5kN traction: {5000/left_area:.2f} MPa")
print(f"  Right face area: {right_area:.1f} mm^2 -> 5kN traction: {5000/right_area:.2f} MPa")

print("\nDone.")
