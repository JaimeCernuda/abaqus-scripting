# -*- coding: utf-8 -*-
"""
Experiment 5: Plot optimization convergence history.

Reads convergence_history.csv and generates convergence_plot.png.
Standard Python 3 script — run locally, not through Abaqus.

Run with: uv run python scripts/plot_convergence.py
"""

import csv
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, os.pardir))

csv_path = os.path.join(PROJECT_DIR, 'convergence_history.csv')
if not os.path.exists(csv_path):
    print("ERROR: convergence_history.csv not found")
    print("Run monitor_convergence.py first (via abaqus python)")
    sys.exit(1)

# Read CSV
cycles: list[int] = []
strain_energies: list[float] = []
avg_densities: list[float] = []
solid_fractions: list[float] = []

with open(csv_path, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cycles.append(int(row['cycle']))
        strain_energies.append(float(row['strain_energy']))
        avg_densities.append(float(row['avg_density']))
        solid_fractions.append(float(row.get('solid_fraction', '0')))

print("Read {} data points from convergence_history.csv".format(len(cycles)))

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(3, 1, figsize=(10, 10), sharex=True)

    # Strain energy
    axes[0].plot(cycles, strain_energies, 'b-o', markersize=4)
    axes[0].set_ylabel('Strain Energy (mJ)')
    axes[0].set_title('Experiment 5: Topology Optimization Convergence')
    axes[0].grid(True, alpha=0.3)

    # Average density
    axes[1].plot(cycles, avg_densities, 'r-o', markersize=4)
    axes[1].set_ylabel('Average Density')
    axes[1].set_ylim(0, 1)
    axes[1].axhline(y=0.4, color='gray', linestyle='--', alpha=0.7, label='Target (40%)')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    # Solid fraction
    axes[2].plot(cycles, [sf * 100 for sf in solid_fractions], 'g-o', markersize=4)
    axes[2].set_xlabel('Design Cycle')
    axes[2].set_ylabel('Solid Fraction (%)')
    axes[2].set_ylim(0, 100)
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plot_path = os.path.join(PROJECT_DIR, 'convergence_plot.png')
    plt.savefig(plot_path, dpi=150)
    print("Plot saved to: convergence_plot.png")

except ImportError:
    print("matplotlib not available. Text summary:")
    print("")
    print("{:>5} | {:>15} | {:>12} | {:>12}".format(
        "Cycle", "Strain Energy", "Avg Density", "Solid %"))
    print("-" * 52)
    for c, se, ad, sf in zip(cycles, strain_energies, avg_densities, solid_fractions):
        print("{:5d} | {:15.2f} | {:12.4f} | {:11.1f}%".format(c, se, ad, sf * 100))
