---
name: abaqus-fatigue-analysis
description: Workflow for fatigue and durability analysis - cycle counting, damage accumulation, and fatigue life prediction.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
  - Skill
---

# Abaqus Fatigue Analysis Workflow

## When to Use This Skill

**USE for:**
- Predicting component fatigue life
- Identifying critical locations for fatigue
- Comparing designs for durability
- Evaluating S-N curve data against FEA stress
- Cycle counting for variable amplitude loading

**Do NOT use for:**
- Just stress analysis → use `/abaqus-static-analysis`
- Crack propagation (fracture mechanics) → specialized tools
- Simple static strength check → use static analysis

**Note:** Full fatigue analysis typically requires post-processors like fe-safe. Abaqus provides stress/strain results for fatigue calculations.

## Key Decisions

### 1. Fatigue Approach

| Approach | When | Data Needed |
|----------|------|-------------|
| Stress-life (S-N) | High-cycle fatigue (N > 10⁴) | S-N curve |
| Strain-life (ε-N) | Low-cycle fatigue (N < 10⁴) | Coffin-Manson parameters |
| Fracture mechanics | Crack growth | da/dN curve |

### 2. Loading Type

| Loading | Analysis Method |
|---------|-----------------|
| Constant amplitude | Single static analysis |
| Variable amplitude | Multiple loads + rainflow counting |
| Proportional | Single load case |
| Non-proportional | Critical plane methods |

### 3. Mean Stress Correction

| Method | Use Case |
|--------|----------|
| Goodman | Conservative, tensile mean stress |
| Gerber | Less conservative |
| Soderberg | Very conservative |
| SWT | Strain-life with mean stress |

## Workflow Steps

1. **Static Analysis** for stress extraction
2. **Identify critical location** (max stress)
3. **Extract stress/strain** at critical points
4. **Apply fatigue method** (S-N, ε-N)
5. **Calculate life** using appropriate correction

## Step 1: Static Analysis Setup

```python
from abaqus import *
from abaqusConstants import *
from caeModules import *

# Standard static analysis with detailed output
model.FieldOutputRequest(
    name='F-Output',
    createStepName='LoadStep',
    variables=('S', 'E', 'PEEQ', 'PEMAG'),
    frequency=1
)
```

## Step 2: Extract Stress Results

```python
from odbAccess import openOdb

odb = openOdb('Analysis.odb', readOnly=True)
frame = odb.steps['LoadStep'].frames[-1]
stress = frame.fieldOutputs['S']

# Find maximum stress location
max_mises = 0
max_location = None
for v in stress.values:
    if hasattr(v, 'mises') and v.mises > max_mises:
        max_mises = v.mises
        max_location = (v.elementLabel, v.integrationPoint)

print(f"Max stress: {max_mises:.2f} MPa at element {max_location}")
odb.close()
```

## Step 3: S-N Fatigue Life Calculation

```python
import math

def sn_fatigue_life(stress_amplitude, material='steel'):
    """Calculate fatigue life using Basquin equation.

    N = (S_a / A)^(-1/b)

    Args:
        stress_amplitude: Alternating stress (MPa)
        material: Material for S-N parameters

    Returns:
        Cycles to failure
    """
    # S-N parameters (example values)
    params = {
        'steel': {'A': 1000, 'b': 0.1},
        'aluminum': {'A': 500, 'b': 0.12},
    }

    A = params[material]['A']
    b = params[material]['b']

    if stress_amplitude <= 0:
        return float('inf')

    N = (stress_amplitude / A) ** (-1/b)
    return N


# Example: R = 0 loading (zero to max)
stress_max = 200.0  # MPa (from FEA)
stress_min = 0.0
stress_amplitude = (stress_max - stress_min) / 2
stress_mean = (stress_max + stress_min) / 2

N = sn_fatigue_life(stress_amplitude)
print(f"Fatigue life: {N:.0f} cycles")
```

## Step 4: Mean Stress Correction (Goodman)

```python
def goodman_correction(stress_amp, stress_mean, ultimate_strength):
    """Goodman mean stress correction.

    S_a / S_f + S_m / S_u = 1
    S_f = S_a / (1 - S_m/S_u)
    """
    if stress_mean >= ultimate_strength:
        return float('inf')  # Static failure

    equivalent_amplitude = stress_amp / (1 - stress_mean / ultimate_strength)
    return equivalent_amplitude


S_u = 500.0  # Ultimate strength (MPa)
corrected_amp = goodman_correction(stress_amplitude, stress_mean, S_u)
N_corrected = sn_fatigue_life(corrected_amp)
print(f"Corrected fatigue life: {N_corrected:.0f} cycles")
```

## Variable Amplitude: Miner's Rule

```python
def miners_damage(cycle_counts, sn_func):
    """Calculate Miner's cumulative damage.

    D = Σ(n_i / N_i)
    Failure when D >= 1.0

    Args:
        cycle_counts: List of (stress_amplitude, count) tuples
        sn_func: Function that returns N for given stress amplitude

    Returns:
        Cumulative damage (failure at D >= 1)
    """
    damage = 0.0
    for stress_amp, count in cycle_counts:
        N = sn_func(stress_amp)
        if N != float('inf'):
            damage += count / N

    return damage


# Example
cycles = [
    (150.0, 1000),   # 1000 cycles at 150 MPa amplitude
    (100.0, 10000),  # 10000 cycles at 100 MPa amplitude
    (50.0, 100000),  # 100000 cycles at 50 MPa amplitude
]

D = miners_damage(cycles, sn_fatigue_life)
print(f"Cumulative damage: {D:.4f}")
print(f"Safe: {'Yes' if D < 1.0 else 'No'}")
```

## Direct Cyclic Step (Low-Cycle Fatigue)

For problems with plastic straining:

```python
model.DirectCyclicStep(
    name='Cyclic',
    previous='Initial',
    timePeriod=1.0,
    fatigue=ON,
    maxNumCycles=100,
    minCycleInc=100,
    maxCycleInc=1000
)
```

## Stress Concentration Factor

```python
def fatigue_notch_factor(Kt, q):
    """Calculate fatigue notch factor.

    Kf = 1 + q*(Kt - 1)

    Args:
        Kt: Stress concentration factor (from FEA)
        q: Notch sensitivity (0-1, typically 0.7-0.95 for steel)
    """
    return 1 + q * (Kt - 1)


Kt = 2.5  # From FEA (peak/nominal stress)
q = 0.9   # Notch sensitivity
Kf = fatigue_notch_factor(Kt, q)

effective_stress = nominal_stress * Kf
```

## Output Requests for Fatigue

```python
model.FieldOutputRequest(
    name='FatigueOutputs',
    createStepName='LoadStep',
    variables=(
        'S',      # Stress (principal, Mises)
        'E',      # Strain
        'PEEQ',   # Equivalent plastic strain
        'COORD',  # Node coordinates (for locating critical points)
    ),
    frequency=1
)
```

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Unrealistically short life | Stress singularity | Use Kt/Kf correction or refine mesh |
| Wrong units | MPa vs Pa | Verify stress units match S-N data |
| Unconservative prediction | Missing mean stress | Apply Goodman/Gerber correction |

## For Full Fatigue Analysis

Consider external tools:
- **fe-safe**: Comprehensive fatigue from Abaqus ODB
- **nCode**: Durability analysis
- **FEMFAT**: Fatigue life prediction

These integrate directly with Abaqus results for complete fatigue workflows.

## API Reference

For stress extraction: `/abaqus-odb`
For static analysis: `/abaqus-static-analysis`
