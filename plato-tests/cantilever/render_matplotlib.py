"""Render topology optimization results using matplotlib (no OpenGL needed).

Creates 2D projection plots of the density field.
Works on headless CPU nodes without GPU or display.
"""
import numpy as np
import netCDF4
import matplotlib
matplotlib.use('Agg')  # headless backend
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation
import os

def render_results(exo_file, output_dir="."):
    """Read Exodus result and create density visualization."""
    ds = netCDF4.Dataset(exo_file, "r")
    x = ds.variables["coordx"][:]
    y = ds.variables["coordy"][:]
    z = ds.variables["coordz"][:]
    conn = ds.variables["connect1"][:] - 1  # 0-based
    density = ds.variables["vals_nod_var1"][-1, :]  # last timestep
    ds.close()

    n_nodes = len(x)
    n_cells = len(conn)
    print(f"Loaded: {n_nodes} nodes, {n_cells} tets")
    print(f"Density range: [{density.min():.4f}, {density.max():.4f}]")
    print(f"Solid (>0.5): {np.sum(density > 0.5)} nodes ({100*np.mean(density > 0.5):.1f}%)")

    # ============================================================
    # Plot 1: XY projection (side view) — average Z
    # ============================================================
    fig, ax = plt.subplots(1, 1, figsize=(14, 4))

    # Project tet faces onto XY plane — find all boundary triangles
    # For simplicity, create a triangulation of all nodes projected to XY
    # and color by density
    tri = Triangulation(x, y)

    # Filter triangles where all vertices have non-zero mesh involvement
    tcf = ax.tripcolor(tri, density, cmap='RdYlBu_r', vmin=0, vmax=1,
                       shading='gouraud')
    ax.set_aspect('equal')
    ax.set_xlabel('X (mm)')
    ax.set_ylabel('Y (mm)')
    ax.set_title('Cantilever Beam — Topology Optimization (Side View)\n'
                 f'Volume fraction: 30%, {n_nodes} nodes, {n_cells} tets')
    plt.colorbar(tcf, ax=ax, label='Density (0=void, 1=solid)')

    # Mark BCs
    ax.annotate('FIXED', xy=(0, 10), fontsize=10, fontweight='bold',
                ha='center', color='red')
    ax.annotate('LOAD ↓', xy=(100, 10), fontsize=10, fontweight='bold',
                ha='center', color='blue')

    plt.tight_layout()
    fname = os.path.join(output_dir, 'topology_side_view.png')
    plt.savefig(fname, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {fname}")

    # ============================================================
    # Plot 2: Thresholded view (solid only)
    # ============================================================
    fig, ax = plt.subplots(1, 1, figsize=(14, 4))

    # Binary threshold at 0.3
    binary = np.where(density > 0.3, 1.0, 0.0)
    tcf2 = ax.tripcolor(tri, binary, cmap='gray_r', vmin=0, vmax=1,
                        shading='flat')
    ax.set_aspect('equal')
    ax.set_xlabel('X (mm)')
    ax.set_ylabel('Y (mm)')
    ax.set_title('Optimized Shape (density > 0.3)')
    ax.annotate('FIXED', xy=(0, 10), fontsize=10, fontweight='bold',
                ha='center', color='red')
    ax.annotate('LOAD ↓', xy=(100, 10), fontsize=10, fontweight='bold',
                ha='center', color='blue')
    plt.tight_layout()
    fname = os.path.join(output_dir, 'topology_thresholded.png')
    plt.savefig(fname, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {fname}")

    # ============================================================
    # Plot 3: Convergence (from log data if available)
    # ============================================================
    # Extract compliance values from the optimization log
    compliance_values = []
    log_file = None
    for f in os.listdir('.'):
        if f.startswith('plato-final') and f.endswith('.out'):
            log_file = f
            break

    if log_file:
        with open(log_file) as fh:
            for line in fh:
                if 'objective:compliance] Criterion evaluation complete' in line:
                    val = float(line.split('Result: ')[1].strip())
                    compliance_values.append(val)

    if compliance_values:
        fig, ax = plt.subplots(1, 1, figsize=(10, 5))
        ax.plot(compliance_values, 'b.-', markersize=3)
        ax.set_xlabel('Function Evaluation')
        ax.set_ylabel('Compliance')
        ax.set_title('Convergence History')
        ax.set_yscale('log')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        fname = os.path.join(output_dir, 'convergence.png')
        plt.savefig(fname, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"Saved: {fname}")
    else:
        print("No convergence data found in log files")


if __name__ == "__main__":
    if os.path.exists("result.exo"):
        render_results("result.exo", ".")
    else:
        print("result.exo not found in current directory")
