# Common Modal Analysis Patterns

## Free Vibration (No BCs)

```python
# Free-free analysis - no boundary conditions
# Expect minimum 6 rigid body modes at ~0 Hz
# Elastic/flexible modes start at mode 7

model.FrequencyStep(name='Free', previous='Initial', numEigen=15)

# Tip: Request 15+ modes to get meaningful elastic modes
# Modes 1-6: Translation (3) + Rotation (3) at ~0 Hz
# Modes 7+: Actual structural modes
```

**Use case:** Unconstrained components, test correlation, free vibration study.

## Fixed-Free (Cantilever)

```python
# Classic cantilever configuration
# First mode is typically first bending mode
# Frequency depends on: length, E, I, density

# Fix one end
fixed_face = instance.faces.findAt(((0, HEIGHT/2, WIDTH/2),))
assembly.Set(faces=fixed_face, name='Fixed')
model.EncastreBC(name='Fixed', createStepName='Initial',
                  region=assembly.sets['Fixed'])

# Frequency extraction
model.FrequencyStep(name='Modes', previous='Initial', numEigen=10)
```

**Use case:** Mounted brackets, cantilever beams, fixed-base structures.

## Simply Supported Beam

```python
# Pinned at both ends - rotations free

# End 1: Pinned (all translations fixed)
end1 = instance.faces.findAt(((0, HEIGHT/2, WIDTH/2),))
assembly.Set(faces=end1, name='End1')
model.DisplacementBC(name='Pin1', createStepName='Initial',
                      region=assembly.sets['End1'],
                      u1=0.0, u2=0.0, u3=0.0)

# End 2: Roller (only vertical fixed)
end2 = instance.faces.findAt(((LENGTH, HEIGHT/2, WIDTH/2),))
assembly.Set(faces=end2, name='End2')
model.DisplacementBC(name='Roller', createStepName='Initial',
                      region=assembly.sets['End2'],
                      u2=0.0)  # Only vertical constrained

model.FrequencyStep(name='Modes', previous='Initial', numEigen=10)
```

**Use case:** Bridge-like structures, simply supported plates.

## Fixed-Fixed Beam

```python
# Both ends fully constrained

for i, x_pos in enumerate([0, LENGTH]):
    face = instance.faces.findAt(((x_pos, HEIGHT/2, WIDTH/2),))
    assembly.Set(faces=face, name=f'Fixed{i+1}')
    model.EncastreBC(name=f'Fixed{i+1}', createStepName='Initial',
                      region=assembly.sets[f'Fixed{i+1}'])

model.FrequencyStep(name='Modes', previous='Initial', numEigen=10)
```

**Use case:** Clamped beams, pipes between supports.

## Prestressed Modal Analysis

```python
# Modal analysis with preload (e.g., bolted joint, tensioned cable)

# Step 1: Static preload
model.StaticStep(name='Preload', previous='Initial')
model.ConcentratedForce(name='Tension', createStepName='Preload',
                         region=tip_set, cf1=1000.0)  # Preload force

# Step 2: Frequency extraction AFTER preload
model.FrequencyStep(name='Modes', previous='Preload', numEigen=10)

# Note: Prestress affects frequencies
# Tension increases frequency (stiffening)
# Compression decreases frequency (softening)
```

**Use case:** Prestressed structures, bolted assemblies, tensioned cables.

## Frequency Range Search

```python
# Extract all modes within a specific frequency range
# Useful when you need modes near an excitation frequency

model.FrequencyStep(
    name='Modes',
    previous='Initial',
    numEigen=20,           # Max modes to find
    minEigen=100.0,        # Minimum frequency (Hz)
    maxEigen=500.0         # Maximum frequency (Hz)
)

# Only modes between 100-500 Hz will be extracted
```

**Use case:** Resonance avoidance, when excitation frequency is known.

## Shift-Invert for Target Frequency

```python
# Find modes near a specific frequency
# More efficient than extracting all modes up to that frequency

model.FrequencyStep(
    name='Modes',
    previous='Initial',
    numEigen=10,
    shift=500.0  # Extract modes near 500 Hz
)

# Modes closest to 500 Hz will be found first
```

**Use case:** High-frequency modes, modes near operating speed.

## Symmetric Model (Half/Quarter)

```python
# Use symmetry to reduce model size

# Apply symmetry BC
sym_face = instance.faces.findAt(((LENGTH/2, HEIGHT/2, 0),))
assembly.Set(faces=sym_face, name='SymPlane')
model.ZsymmBC(name='Symmetry', createStepName='Initial',
               region=assembly.sets['SymPlane'])

model.FrequencyStep(name='Modes', previous='Initial', numEigen=10)

# Note: Only symmetric modes will be captured
# Anti-symmetric modes require separate analysis
```

**Use case:** Large models with geometric symmetry.

## Plate/Shell Modal Analysis

```python
# For thin structures, use shell elements

part = model.Part(name='Plate', dimensionality=THREE_D, type=DEFORMABLE_BODY)
# ... create shell geometry ...

# Shell section
model.HomogeneousShellSection(name='ShellSec', material='Steel',
                               thickness=2.0)  # mm

# Shell element type
elemType = mesh.ElemType(elemCode=S4R, elemLibrary=STANDARD)
part.setElementType(regions=(part.faces,), elemTypes=(elemType,))

model.FrequencyStep(name='Modes', previous='Initial', numEigen=20)

# Shell modes: bending, membrane, and coupled
```

**Use case:** Thin plates, panels, sheet metal.
