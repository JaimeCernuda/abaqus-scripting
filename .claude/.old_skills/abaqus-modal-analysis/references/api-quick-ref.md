# Modal Analysis API Quick Reference

## FrequencyStep

```python
model.FrequencyStep(
    name='StepName',
    previous='Initial',
    numEigen=10,                 # Number of modes to extract
    eigensolver=LANCZOS,         # or SUBSPACE
    minEigen=0.0,                # Minimum frequency (Hz)
    maxEigen=1000.0,             # Maximum frequency (Hz)
    normalization=MASS           # or DISPLACEMENT
)
```

### Parameter Details

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | str | Required | Step name |
| `previous` | str | Required | Previous step (usually 'Initial') |
| `numEigen` | int | Required | Number of eigenvalues to extract |
| `eigensolver` | symbolic | LANCZOS | LANCZOS (recommended) or SUBSPACE |
| `minEigen` | float | None | Minimum frequency bound (Hz) |
| `maxEigen` | float | None | Maximum frequency bound (Hz) |
| `shift` | float | None | Shift point for shift-invert |
| `normalization` | symbolic | DISPLACEMENT | DISPLACEMENT or MASS |

### Eigensolver Selection

| Solver | Best For | Notes |
|--------|----------|-------|
| LANCZOS | Most problems | Default, robust, efficient |
| SUBSPACE | Many repeated eigenvalues | Less common |

## Extract Frequencies from ODB

```python
from odbAccess import openOdb

odb = openOdb('Modal.odb', readOnly=True)
step = odb.steps['Modes']

frequencies = []
for frame in step.frames[1:]:  # Skip initial frame (frame 0)
    frequencies.append(frame.frequency)
    print(f"Mode {frame.frameId}: {frame.frequency:.2f} Hz")

odb.close()
```

### Alternative: Parse Frame Description

```python
for i, frame in enumerate(step.frames):
    if i == 0:
        continue  # Skip initial frame
    # Description format: "Mode X: Eigenfrequency = Y"
    desc = frame.description
    freq = float(desc.split('=')[-1].strip())
    print(f"Mode {i}: {freq:.2f} Hz")
```

## Mode Shape Visualization (CAE)

```python
# In CAE script:
session.viewports['Viewport: 1'].odbDisplay.setFrame(step='Modes', frame=1)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=DEFORMED)

# Animate mode shape
session.viewports['Viewport: 1'].animationController.setValues(
    animationType=SCALE_FACTOR,
    viewports=('Viewport: 1',)
)
session.viewports['Viewport: 1'].animationController.play()
```

## Field Output Request

```python
# Request mode shapes (displacements)
model.FieldOutputRequest(
    name='F-Output',
    createStepName='Frequency',
    variables=('U',)  # Displacement (mode shapes)
)

# For stress modes (optional)
model.FieldOutputRequest(
    name='F-Output',
    createStepName='Frequency',
    variables=('U', 'S')  # Displacement and stress
)
```

## Material Density (REQUIRED)

```python
# Steel (tonne/mm^3)
material.Density(table=((7.85e-9,),))

# Aluminum
material.Density(table=((2.7e-9,),))

# Titanium
material.Density(table=((4.5e-9,),))
```

**Units reminder:** In mm-tonne-s system, density is tonne/mm^3 (very small numbers).

## Boundary Conditions for Modal

```python
# Fixed (Encastre)
model.EncastreBC(name='Fixed', createStepName='Initial', region=region)

# Pinned (displacements fixed, rotations free)
model.DisplacementBC(name='Pinned', createStepName='Initial', region=region,
                      u1=0.0, u2=0.0, u3=0.0)

# Symmetry plane
model.XssymmBC(name='SymX', createStepName='Initial', region=region)

# Free-free: No BCs (expect 6 rigid body modes at ~0 Hz)
```
