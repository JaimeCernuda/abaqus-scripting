"""Extract and analyze results from Plato cantilever smoke test.
Reads result.exo, extracts density field, writes summary + ASCII visualization.
"""
import netCDF4
import numpy as np
import sys

def read_exodus_results(filename):
    """Read density and coordinate data from Plato result Exodus file."""
    ds = netCDF4.Dataset(filename, "r")

    print(f"=== {filename} ===")
    print(f"Dimensions: {dict((k, len(v)) for k,v in ds.dimensions.items())}")

    # Coordinates
    x = ds.variables["coordx"][:]
    y = ds.variables["coordy"][:]
    z = ds.variables["coordz"][:]
    n_nodes = len(x)
    print(f"Nodes: {n_nodes}")
    print(f"  X range: [{x.min():.1f}, {x.max():.1f}]")
    print(f"  Y range: [{y.min():.1f}, {y.max():.1f}]")
    print(f"  Z range: [{z.min():.1f}, {z.max():.1f}]")

    # Time steps
    if "time_whole" in ds.variables:
        times = ds.variables["time_whole"][:]
        print(f"Time steps: {len(times)}")

    # Node variables
    print("\nNode variables:")
    nvar = 0
    for v in ds.variables:
        if v.startswith("vals_nod_var"):
            nvar += 1
    print(f"  Count: {nvar}")

    # Try to find variable names
    if "name_nod_var" in ds.variables:
        raw = ds.variables["name_nod_var"][:]
        names = []
        for row in raw:
            chars = []
            for c in row:
                if isinstance(c, bytes):
                    chars.append(c.decode())
                elif hasattr(c, 'item'):
                    chars.append(str(c.item()) if c is not np.ma.masked else '')
                elif c is not np.ma.masked:
                    chars.append(str(c))
            names.append(''.join(chars).strip())
        print(f"  Names: {names}")

    # Read density/topology field
    density = None
    for i in range(1, nvar + 1):
        varname = f"vals_nod_var{i}"
        if varname in ds.variables:
            data = ds.variables[varname][:]
            if data.ndim == 2:
                # Last time step
                vals = data[-1, :]
            else:
                vals = data[:]
            print(f"\n  Variable {i}: min={vals.min():.6f}, max={vals.max():.6f}, mean={vals.mean():.6f}")

            # Check if this looks like a density field (values between 0 and 1)
            if vals.min() >= -0.1 and vals.max() <= 1.1:
                density = vals
                print(f"    → Likely density field")
                solid = np.sum(vals > 0.5)
                void = np.sum(vals <= 0.5)
                print(f"    → Solid nodes (>0.5): {solid} ({100*solid/len(vals):.1f}%)")
                print(f"    → Void nodes (≤0.5): {void} ({100*void/len(vals):.1f}%)")

    # ASCII visualization: project density onto XY plane
    if density is not None:
        print("\n=== ASCII Topology (XY projection, Z-averaged) ===")
        print("  Legend: ██=solid(>0.7) ▓▓=medium(0.3-0.7) ░░=void(<0.3) .=empty")

        nx, ny = 50, 12
        x_bins = np.linspace(x.min(), x.max(), nx + 1)
        y_bins = np.linspace(y.min(), y.max(), ny + 1)

        grid = np.full((ny, nx), -1.0)
        for xi in range(nx):
            for yi in range(ny):
                mask = ((x >= x_bins[xi]) & (x < x_bins[xi+1]) &
                        (y >= y_bins[yi]) & (y < y_bins[yi+1]))
                if mask.any():
                    grid[yi, xi] = density[mask].mean()

        # Print top to bottom (Y descending)
        for yi in range(ny - 1, -1, -1):
            row = ""
            for xi in range(nx):
                v = grid[yi, xi]
                if v < 0:
                    row += "  "
                elif v > 0.7:
                    row += "██"
                elif v > 0.3:
                    row += "▓▓"
                else:
                    row += "░░"
            print(f"  {row}")
        print(f"  {'──' * nx}")
        print(f"  Fixed←                                                              →Load")

    ds.close()
    return density

# Read both result files
for f in ["result.exo", "restart_result.exo", "mesh.exo"]:
    try:
        read_exodus_results(f)
    except Exception as e:
        print(f"\n{f}: Error - {e}")
    print()
