"""Generate cantilever beam Exodus mesh using Gmsh + netCDF4.

Writes proper Exodus II with side sets (not just node sets).
Side sets are required by Plato for BC and load application.
"""
import gmsh
import numpy as np
import netCDF4
import os
from collections import defaultdict

# ============================================================
# Geometry and mesh
# ============================================================
L, H, D = 100.0, 20.0, 10.0
MESH_SIZE = 5.0

gmsh.initialize()
gmsh.option.setNumber("General.Terminal", 1)
gmsh.model.add("cantilever")

box = gmsh.model.occ.addBox(0, 0, 0, L, H, D)
gmsh.model.occ.synchronize()

def find_surface(tx, ty, tz, tol=1.0):
    for dim, tag in gmsh.model.getEntities(2):
        com = gmsh.model.occ.getCenterOfMass(dim, tag)
        if abs(com[0]-tx)<tol and abs(com[1]-ty)<tol and abs(com[2]-tz)<tol:
            return tag
    raise ValueError(f"Surface not found near ({tx},{ty},{tz})")

fixed_face = find_surface(0, H/2, D/2)
load_face = find_surface(L, H/2, D/2)
print(f"Fixed face: {fixed_face}, Load face: {load_face}")

gmsh.model.addPhysicalGroup(2, [fixed_face], tag=1, name="fixed_support")
gmsh.model.addPhysicalGroup(2, [load_face], tag=2, name="load_surface")
gmsh.model.addPhysicalGroup(3, [box], tag=1, name="design_domain")

gmsh.option.setNumber("Mesh.MeshSizeMax", MESH_SIZE)
gmsh.option.setNumber("Mesh.MeshSizeMin", MESH_SIZE * 0.5)
gmsh.option.setNumber("Mesh.ElementOrder", 1)
gmsh.option.setNumber("Mesh.Algorithm3D", 1)
gmsh.option.setNumber("Mesh.Optimize", 1)
gmsh.model.mesh.generate(3)

# Extract nodes
node_tags, node_coords, _ = gmsh.model.mesh.getNodes()
coords = node_coords.reshape(-1, 3)
n_nodes = len(node_tags)
tag_to_idx = {int(t): i for i, t in enumerate(node_tags)}

# Extract tet4 elements
_, tet_tags_list, tet_conn_list = gmsh.model.mesh.getElements(dim=3)
tet_conn = tet_conn_list[0].reshape(-1, 4)
n_tets = len(tet_conn)
# Convert to 0-based indices
tet_conn_0 = np.array([[tag_to_idx[int(n)] for n in elem] for elem in tet_conn])

# Extract sideset triangles
ss_tris = {}
for phys_tag, phys_name in [(1, "fixed_support"), (2, "load_surface")]:
    entities = gmsh.model.getEntitiesForPhysicalGroup(2, phys_tag)
    tris = []
    for ent in entities:
        _, tri_tags, tri_conns = gmsh.model.mesh.getElements(dim=2, tag=ent)
        if tri_conns:
            for tri in tri_conns[0].reshape(-1, 3):
                tris.append(frozenset(tag_to_idx[int(n)] for n in tri))
    ss_tris[phys_name] = tris
    print(f"  Sideset '{phys_name}': {len(tris)} triangles")

print(f"Mesh: {n_nodes} nodes, {n_tets} tet4 elements")
gmsh.finalize()

# ============================================================
# Build side set data: (element_id, local_face) pairs
# ============================================================
# TETRA4 face definitions (0-based node indices within element):
# Exodus convention for TETRA4:
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

# Build a lookup: frozenset of global node indices -> (elem_idx, local_face)
face_to_elem = {}
for ei in range(n_tets):
    enodes = tet_conn_0[ei]
    for fi, local_face in enumerate(TET4_FACES):
        global_face = frozenset(enodes[li] for li in local_face)
        face_to_elem[global_face] = (ei + 1, fi + 1)  # 1-based

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
if os.path.exists("mesh.exo"):
    os.remove("mesh.exo")

ds = netCDF4.Dataset("mesh.exo", "w", format="NETCDF4")

# Global attributes
ds.api_version = np.float32(8.25)
ds.version = np.float32(8.25)
ds.floating_point_word_size = 8
ds.file_size = 1
ds.title = "Cantilever beam"

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
print(f"Written: mesh.exo ({n_nodes} nodes, {n_tets} tets, {num_ss} side sets)")
print("Done.")
