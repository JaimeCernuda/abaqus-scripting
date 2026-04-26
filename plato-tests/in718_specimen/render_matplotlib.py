"""Render IN718 specimen topology optimization results using matplotlib.

Creates 2D projection plots of the density field (XY side view).
Works on headless CPU nodes without GPU or display.
"""
import numpy as np
import netCDF4
import matplotlib
matplotlib.use('Agg')  # headless backend
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation
from matplotlib.patches import Circle
import os

# Geometry constants (from experiment 10)
TOTAL_HEIGHT = 146.17
TOTAL_WIDTH = 64.60
THICKNESS = 25.0
HALF_WIDTH = TOTAL_WIDTH / 2.0
PIN_RADIUS = 12.7 / 2.0

# Pin centers
UPPER_PIN = (0.0, 132.17)
LL_PIN = (-23.30, 14.0)
LR_PIN = (23.30, 14.0)


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
    # Plot 1: XY projection (side view) — density field
    # ============================================================
    fig, ax = plt.subplots(1, 1, figsize=(6, 12))

    tri = Triangulation(x, y)
    tcf = ax.tripcolor(tri, density, cmap='RdYlBu_r', vmin=0, vmax=1,
                       shading='gouraud')
    ax.set_aspect('equal')
    ax.set_xlabel('X (mm)')
    ax.set_ylabel('Y (mm)')
    ax.set_title('IN718 Specimen — Topology Optimization (XY Side View)\n'
                 f'Volume fraction: 30%, {n_nodes} nodes, {n_cells} tets\n'
                 '3 load cases: 20kN vert + 5kN horiz (left) + 5kN horiz (right)')
    plt.colorbar(tcf, ax=ax, label='Density (0=void, 1=solid)', shrink=0.6)

    # Mark pin holes
    for (px, py), label in [(UPPER_PIN, 'Upper pin\n20kN'),
                             (LL_PIN, 'LL pin\nBC+5kN'),
                             (LR_PIN, 'LR pin\nBC+5kN')]:
        circle = Circle((px, py), PIN_RADIUS, fill=False, edgecolor='black',
                        linewidth=1.5, linestyle='--')
        ax.add_patch(circle)
        offset_y = 10 if py > 50 else -10
        ax.annotate(label, xy=(px, py), fontsize=7, fontweight='bold',
                    ha='center', va='center', color='black',
                    bbox=dict(boxstyle='round,pad=0.2', fc='white', alpha=0.7))

    # Mark BCs
    ax.annotate('FIXED Y,Z', xy=(-HALF_WIDTH + 9, 3), fontsize=8,
                fontweight='bold', ha='center', color='red')
    ax.annotate('FIXED Y,Z', xy=(HALF_WIDTH - 9, 3), fontsize=8,
                fontweight='bold', ha='center', color='red')
    ax.annotate('LOAD 20kN', xy=(0, TOTAL_HEIGHT + 3), fontsize=8,
                fontweight='bold', ha='center', color='blue')

    plt.tight_layout()
    fname = os.path.join(output_dir, 'topology_side_view.png')
    plt.savefig(fname, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {fname}")

    # ============================================================
    # Plot 2: Thresholded view (solid only)
    # ============================================================
    fig, ax = plt.subplots(1, 1, figsize=(6, 12))

    binary = np.where(density > 0.3, 1.0, 0.0)
    tcf2 = ax.tripcolor(tri, binary, cmap='gray_r', vmin=0, vmax=1,
                        shading='flat')
    ax.set_aspect('equal')
    ax.set_xlabel('X (mm)')
    ax.set_ylabel('Y (mm)')
    ax.set_title('Optimized Shape (density > 0.3)')

    # Mark pin holes
    for (px, py) in [UPPER_PIN, LL_PIN, LR_PIN]:
        circle = Circle((px, py), PIN_RADIUS, fill=True, facecolor='white',
                        edgecolor='red', linewidth=1.5)
        ax.add_patch(circle)

    plt.tight_layout()
    fname = os.path.join(output_dir, 'topology_thresholded.png')
    plt.savefig(fname, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {fname}")

    # ============================================================
    # Plot 3: Convergence (from log data if available)
    # ============================================================
    # Look for compliance values in SLURM output log
    compliance_lc1 = []
    compliance_lc2 = []
    compliance_lc3 = []
    log_file = None
    for f in os.listdir('.'):
        if f.startswith('in718-plato') and f.endswith('.out'):
            log_file = f
            break

    if log_file:
        with open(log_file) as fh:
            for line in fh:
                if 'objective:lc1] Criterion evaluation complete' in line:
                    try:
                        val = float(line.split('Result: ')[1].strip())
                        compliance_lc1.append(val)
                    except (IndexError, ValueError):
                        pass
                elif 'objective:lc2] Criterion evaluation complete' in line:
                    try:
                        val = float(line.split('Result: ')[1].strip())
                        compliance_lc2.append(val)
                    except (IndexError, ValueError):
                        pass
                elif 'objective:lc3] Criterion evaluation complete' in line:
                    try:
                        val = float(line.split('Result: ')[1].strip())
                        compliance_lc3.append(val)
                    except (IndexError, ValueError):
                        pass

    has_data = compliance_lc1 or compliance_lc2 or compliance_lc3
    if has_data:
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        # Individual load case convergence
        ax = axes[0]
        if compliance_lc1:
            ax.plot(compliance_lc1, 'b.-', markersize=3, label='LC1 (20kN vert)')
        if compliance_lc2:
            ax.plot(compliance_lc2, 'r.-', markersize=3, label='LC2 (5kN left)')
        if compliance_lc3:
            ax.plot(compliance_lc3, 'g.-', markersize=3, label='LC3 (5kN right)')
        ax.set_xlabel('Function Evaluation')
        ax.set_ylabel('Compliance')
        ax.set_title('Per-Load-Case Convergence')
        ax.set_yscale('log')
        ax.legend()
        ax.grid(True, alpha=0.3)

        # Weighted sum convergence
        ax = axes[1]
        n = min(len(compliance_lc1) if compliance_lc1 else 999,
                len(compliance_lc2) if compliance_lc2 else 999,
                len(compliance_lc3) if compliance_lc3 else 999)
        if n < 999 and n > 0:
            weighted = [0.5 * compliance_lc1[i] + 0.25 * compliance_lc2[i] +
                       0.25 * compliance_lc3[i] for i in range(n)]
            ax.plot(weighted, 'k.-', markersize=3)
            ax.set_xlabel('Iteration')
            ax.set_ylabel('Weighted Compliance')
            ax.set_title('Total Objective (0.5*LC1 + 0.25*LC2 + 0.25*LC3)')
            ax.set_yscale('log')
            ax.grid(True, alpha=0.3)

        plt.tight_layout()
        fname = os.path.join(output_dir, 'convergence.png')
        plt.savefig(fname, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"Saved: {fname}")
    else:
        print("No convergence data found in log files")

    # ============================================================
    # Plot 4: Cross-section at mid-thickness (XY slice at Z ~ 12.5)
    # ============================================================
    z_mid = THICKNESS / 2.0
    z_tol = THICKNESS * 0.15  # nodes within 15% of mid-plane
    mask = np.abs(z - z_mid) < z_tol

    if np.sum(mask) > 100:
        fig, ax = plt.subplots(1, 1, figsize=(6, 12))

        x_slice = x[mask]
        y_slice = y[mask]
        d_slice = density[mask]

        try:
            tri_slice = Triangulation(x_slice, y_slice)
            tcf3 = ax.tripcolor(tri_slice, d_slice, cmap='RdYlBu_r',
                               vmin=0, vmax=1, shading='gouraud')
            ax.set_aspect('equal')
            ax.set_xlabel('X (mm)')
            ax.set_ylabel('Y (mm)')
            ax.set_title(f'Mid-Thickness Cross Section (Z={z_mid:.1f}mm)')
            plt.colorbar(tcf3, ax=ax, label='Density', shrink=0.6)

            for (px, py) in [UPPER_PIN, LL_PIN, LR_PIN]:
                circle = Circle((px, py), PIN_RADIUS, fill=False,
                               edgecolor='black', linewidth=1.5, linestyle='--')
                ax.add_patch(circle)

            plt.tight_layout()
            fname = os.path.join(output_dir, 'topology_midplane.png')
            plt.savefig(fname, dpi=150, bbox_inches='tight')
            plt.close()
            print(f"Saved: {fname}")
        except Exception as e:
            print(f"Mid-plane plot failed: {e}")


if __name__ == "__main__":
    if os.path.exists("result.exo"):
        render_results("result.exo", ".")
    else:
        print("result.exo not found in current directory")
        # Try parent directory
        for candidate in ["../result.exo", "run/result.exo"]:
            if os.path.exists(candidate):
                print(f"Found: {candidate}")
                render_results(candidate, ".")
                break
