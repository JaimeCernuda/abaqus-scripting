---
name: abaqus-amplitude
description: Define time-varying amplitudes in Abaqus for loads, BCs, and other time-dependent quantities.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
---

# Abaqus Amplitude Skill

## When to Use This Skill

**USE when you need to:**
- Ramp a load up/down over time
- Apply sinusoidal or cyclic loading
- Define impulse or impact loading
- Create smooth transitions (avoid sudden load application)
- Apply earthquake or vibration excitation
- Define temperature history for transient thermal

**Do NOT use for:**
- Constant loads (no amplitude needed)
- Initial conditions → use `/abaqus-field`
- Step transitions (use step sequence instead)

## Key Decisions

### 1. Amplitude Type Selection

| Load Profile | Amplitude Type | Use Case |
|--------------|----------------|----------|
| Custom time-value | TabularAmplitude | General purpose |
| Smooth ramp | SmoothStepAmplitude | Avoid sudden jumps |
| Sinusoidal | PeriodicAmplitude | Harmonic loading |
| Exponential decay | DecayAmplitude | Damped response |
| Modulated wave | ModulatedAmplitude | Complex vibration |

### 2. Time Reference

| Option | Meaning | When |
|--------|---------|------|
| STEP | Time relative to step start | Most common |
| TOTAL | Time from analysis start | Multi-step |

## Required Inputs

| Input | Required | Guidance |
|-------|----------|----------|
| Amplitude type | YES | Based on load profile needed |
| Time-value data | YES | (time, factor) pairs |
| Name | YES | Referenced by load/BC |

## Common Patterns

### Linear Ramp
```python
model.TabularAmplitude(
    name='Ramp',
    data=(
        (0.0, 0.0),   # Start at zero
        (1.0, 1.0),   # Full load at t=1
    ),
    timeSpan=STEP
)
```

### Ramp Up and Down
```python
model.TabularAmplitude(
    name='RampUpDown',
    data=(
        (0.0, 0.0),
        (0.5, 1.0),   # Peak at midpoint
        (1.0, 0.0),   # Back to zero
    )
)
```

### Step Function (Sudden)
```python
model.TabularAmplitude(
    name='Step',
    data=(
        (0.0, 0.0),
        (0.0, 1.0),   # Instant jump
        (1.0, 1.0),   # Hold
    )
)
```

### Smooth Ramp (No Shock)
```python
model.SmoothStepAmplitude(
    name='SmoothRamp',
    data=(
        (0.0, 0.0),
        (1.0, 1.0),
    )
)
```

### Sinusoidal
```python
# A * sin(2*pi*f*t)
model.PeriodicAmplitude(
    name='Sine',
    frequency=10.0,      # 10 Hz
    start=0.0,
    a_0=0.0,             # No DC offset
    data=((0.0, 1.0),)   # (cosine, sine) coefficients
)
```

### Impulse
```python
model.TabularAmplitude(
    name='Impulse',
    data=(
        (0.0, 0.0),
        (0.001, 1.0),
        (0.002, 0.0),
    )
)
```

### Exponential Decay
```python
model.DecayAmplitude(
    name='Decay',
    initial=1.0,
    maximum=1.0,
    start=0.0,
    decayTime=0.5  # Time constant
)
```

### Apply Amplitude to Load
```python
model.ConcentratedForce(
    name='VaryingLoad',
    createStepName='LoadStep',
    region=region,
    cf2=-1000.0,
    amplitude='Ramp'  # Reference amplitude by name
)
```

### Apply Amplitude to BC
```python
model.DisplacementBC(
    name='Prescribed',
    createStepName='LoadStep',
    region=region,
    u1=10.0,
    amplitude='Sine'
)
```

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Amplitude not monotonic in time" | Time values not increasing | Fix time sequence |
| "Sudden load causes convergence issues" | No smooth transition | Use SmoothStepAmplitude |
| "Amplitude exceeds 1.0" | Misunderstanding purpose | Amplitude is multiplier; adjust magnitude in load |

## API Reference

For detailed parameters: [Amplitude API](../../docs/abaqus-api/modules/amplitude.md)
