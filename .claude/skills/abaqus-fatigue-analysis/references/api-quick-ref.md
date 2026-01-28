# Fatigue Analysis Quick Reference

## Abaqus Native Fatigue (Limited)

Abaqus/Standard has limited fatigue capabilities. For full fatigue analysis:
1. Run structural analysis in Abaqus
2. Export stress results
3. Use fe-safe, nCode, or custom scripts

## Stress History Extraction

```python
from odbAccess import openOdb

odb = openOdb('Model.odb', readOnly=True)
step = odb.steps['CyclicLoad']

# Get stress at critical node
region = odb.rootAssembly.nodeSets['CRITICAL_POINT']
stress_history = []

for frame in step.frames:
    stress = frame.fieldOutputs['S'].getSubset(region=region)
    for v in stress.values:
        stress_history.append(v.mises)

odb.close()
```

## Extract Stress at Specific Location

```python
from odbAccess import openOdb

odb = openOdb('Model.odb', readOnly=True)
step = odb.steps['LoadStep']
frame = step.frames[-1]

# Get stress field
stress = frame.fieldOutputs['S']

# Find max von Mises location
max_mises = 0
critical_node = None
for v in stress.values:
    if hasattr(v, 'mises') and v.mises > max_mises:
        max_mises = v.mises
        critical_node = v.nodeLabel

print(f"Critical location: Node {critical_node}, Stress {max_mises:.2f} MPa")
odb.close()
```

## Basquin Equation (High-Cycle Fatigue)

```python
# N = (S_a / Sf')^(-1/b)
# Where:
#   N = cycles to failure
#   S_a = alternating stress amplitude
#   Sf' = fatigue strength coefficient
#   b = fatigue strength exponent (negative, typically -0.05 to -0.12)

Sf_prime = 1000  # Fatigue strength coefficient (MPa)
b = -0.1         # Fatigue strength exponent
S_a = 200        # Alternating stress (MPa)

N = (S_a / Sf_prime) ** (1/b)
print(f"Predicted life: {N:.0f} cycles")
```

## Coffin-Manson (Low-Cycle Fatigue)

```python
# Total strain amplitude:
# epsilon_a = (Sf'/E) * (2*Nf)^b + ef' * (2*Nf)^c
# Where:
#   epsilon_a = total strain amplitude
#   Sf' = fatigue strength coefficient
#   E = elastic modulus
#   ef' = fatigue ductility coefficient
#   b = fatigue strength exponent
#   c = fatigue ductility exponent
#   Nf = cycles to failure (reversals = 2*Nf)

E = 210000       # Elastic modulus (MPa)
Sf_prime = 1000  # Fatigue strength coefficient (MPa)
ef_prime = 0.5   # Fatigue ductility coefficient
b = -0.1         # Fatigue strength exponent
c = -0.6         # Fatigue ductility exponent

def strain_amplitude(Nf):
    elastic = (Sf_prime / E) * (2 * Nf) ** b
    plastic = ef_prime * (2 * Nf) ** c
    return elastic + plastic
```

## Stress Ratio (R-ratio)

```python
# R = S_min / S_max
# Common cases:
#   R = 0:   zero-to-tension (pulsating)
#   R = -1:  fully reversed (symmetric)
#   R = 0.1: mostly tensile
#   R < 0:   tension-compression

S_max = 200  # MPa
S_min = 0    # MPa

R = S_min / S_max
S_amplitude = (S_max - S_min) / 2
S_mean = (S_max + S_min) / 2

print(f"R-ratio: {R}")
print(f"Amplitude: {S_amplitude} MPa")
print(f"Mean stress: {S_mean} MPa")
```

## History Output Request for Fatigue

```python
# Request stress history at critical point for fatigue analysis
model.HistoryOutputRequest(
    name='FatigueHistory',
    createStepName='CyclicStep',
    region=region,
    variables=('S11', 'S22', 'S33', 'S12', 'S13', 'S23', 'MISES'),
    frequency=1
)
```
