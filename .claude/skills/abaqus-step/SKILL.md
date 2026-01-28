---
name: abaqus-step
description: Define analysis steps in Abaqus - static, dynamic, frequency, thermal, coupled. Use for configuring analysis procedures.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
---

# Abaqus Step Skill

## When to Use This Skill

**USE when you need to:**
- Create a static analysis step (linear or nonlinear)
- Set up a frequency/modal extraction step
- Configure dynamic (implicit or explicit) analysis
- Define heat transfer steps (steady-state or transient)
- Configure coupled thermomechanical analysis
- Control increment size and convergence settings

**Do NOT use for:**
- Applying BCs or loads (use in step, but define with `/abaqus-bc`, `/abaqus-load`)
- Setting up optimization tasks → use `/abaqus-optimization`
- Configuring output requests → use `/abaqus-output`

## Key Decisions

### 1. Which Step Type?

| Analysis Goal | Step Type | Key Parameter |
|---------------|-----------|---------------|
| Stress under constant load | StaticStep | nlgeom=OFF/ON |
| Natural frequencies | FrequencyStep | numEigen |
| Buckling modes | BuckleStep | numEigen |
| Transient dynamics (smooth) | ImplicitDynamicsStep | timePeriod |
| Impact/crash | ExplicitDynamicsStep | timePeriod |
| Heat conduction | HeatTransferStep | response |
| Thermal + structural | CoupledTempDisplacementStep | timePeriod |
| Harmonic response | SteadyStateDynamicsStep | frequencyRange |

### 2. Linear vs Nonlinear Static?

| Condition | Setting | When |
|-----------|---------|------|
| Small deformation, linear material | nlgeom=OFF | Default |
| Large rotation/displacement | nlgeom=ON | Thin structures, cables |
| Plasticity | nlgeom=ON | Material yields |
| Contact | nlgeom=ON | Parts touching |

### 3. Increment Control

| Convergence | initialInc | minInc | maxInc |
|-------------|------------|--------|--------|
| Easy (linear) | 1.0 | 1e-6 | 1.0 |
| Moderate | 0.1 | 1e-8 | 0.2 |
| Difficult (contact, plasticity) | 0.01 | 1e-12 | 0.05 |

## Required Inputs

| Input | Required | Default | Guidance |
|-------|----------|---------|----------|
| Step type | YES | StaticStep | Match analysis physics |
| Step name | NO | 'Step-1' | Descriptive name |
| Previous step | NO | 'Initial' | Chain from previous |
| Time period | For transient | 1.0 | Duration of step |

## Common Patterns

### Static Step (Linear)
```python
model.StaticStep(
    name='LoadStep',
    previous='Initial',
    timePeriod=1.0,
    initialInc=1.0,
    nlgeom=OFF  # Linear geometry
)
```

### Static Step (Nonlinear)
```python
model.StaticStep(
    name='NonlinearStep',
    previous='Initial',
    nlgeom=ON,           # Large deformation
    initialInc=0.1,      # Start smaller
    maxNumInc=100,
    minInc=1e-8,
    maxInc=0.1
)
```

### Frequency Step
```python
model.FrequencyStep(
    name='Frequency',
    previous='Initial',
    numEigen=10,         # Number of modes to extract
    eigensolver=LANCZOS,
    normalization=DISPLACEMENT
)
```

### Buckling Step
```python
model.BuckleStep(
    name='Buckling',
    previous='LoadStep',  # After load application
    numEigen=5,
    eigensolver=SUBSPACE
)
```

### Dynamic Implicit
```python
model.ImplicitDynamicsStep(
    name='Dynamic',
    previous='Initial',
    timePeriod=0.1,      # 100 ms
    initialInc=0.001,
    maxNumInc=10000,
    nlgeom=ON
)
```

### Dynamic Explicit
```python
model.ExplicitDynamicsStep(
    name='Impact',
    previous='Initial',
    timePeriod=0.001     # 1 ms (explicit uses very small increments)
)
```

### Heat Transfer
```python
# Steady-state
model.HeatTransferStep(
    name='SteadyHeat',
    previous='Initial',
    response=STEADY_STATE
)

# Transient
model.HeatTransferStep(
    name='TransientHeat',
    previous='Initial',
    response=TRANSIENT,
    timePeriod=100.0,
    deltmx=5.0  # Max temperature change per increment
)
```

### Coupled Thermomechanical
```python
model.CoupledTempDisplacementStep(
    name='ThermoMech',
    previous='Initial',
    response=TRANSIENT,
    timePeriod=10.0,
    deltmx=10.0,
    nlgeom=ON
)
```

### Step Sequence
```python
# Multiple sequential steps
model.StaticStep(name='Step-1', previous='Initial')
model.StaticStep(name='Step-2', previous='Step-1')
model.StaticStep(name='Step-3', previous='Step-2')
```

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Too many increments" | Convergence difficulty | Reduce maxInc, increase maxNumInc |
| "Negative eigenvalues" | Unconstrained or unstable | Check BCs, add stabilization |
| "Time increment too small" | Severe nonlinearity | Add stabilization, check material |
| "Explicit time increment" | Very small elements | Use mass scaling or coarsen mesh |

## API Reference

For detailed parameters: [Step API](../../docs/abaqus-api/modules/step.md)
