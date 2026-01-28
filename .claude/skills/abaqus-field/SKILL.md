---
name: abaqus-field
description: Define initial conditions and predefined fields in Abaqus - initial temperature, stress, velocity, and imported fields.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
---

# Abaqus Field Skill

## When to Use This Skill

**USE when you need to:**
- Set initial temperature distribution
- Apply pre-stress or residual stress
- Define initial velocity (explicit dynamics)
- Import temperature from thermal analysis to structural
- Define custom field variables
- Set up geostatic stress (soils)
- Apply bolt pre-tension

**Do NOT use for:**
- Temperature boundary conditions (fixed T) → use `/abaqus-bc`
- Heat flux or convection loads → use `/abaqus-load`
- Time-varying amplitudes → use `/abaqus-amplitude`

## Key Decisions

### 1. Field Type Selection

| Need | Field Type | Typical Use |
|------|------------|-------------|
| Starting temperature | Initial Temperature | Thermal stress from uniform T |
| Residual stress | Initial Stress | Pre-stressed members |
| Impact velocity | Initial Velocity | Explicit dynamics |
| Temperature from other analysis | Predefined Temperature | Sequential thermal-structural |
| Custom variable | Predefined Field | User-defined behaviors |

### 2. Distribution Type

| Type | When |
|------|------|
| UNIFORM | Same value everywhere |
| FROM_FILE | Import from ODB or FIL |
| ANALYTICAL_FIELD | Expression-based (X, Y, Z) |
| USER_DEFINED | Via user subroutine |

## Required Inputs

| Input | Required | Guidance |
|-------|----------|----------|
| Field type | YES | Temperature, Stress, Velocity, etc. |
| Region | YES | Where to apply |
| Distribution | YES | Uniform, from file, analytical |
| Value(s) | YES | Magnitude or file path |

## Common Patterns

### Initial Temperature (Uniform)
```python
model.Temperature(
    name='InitialTemp',
    createStepName='Initial',
    region=region,
    distributionType=UNIFORM,
    magnitude=25.0  # Starting temperature
)
```

### Initial Stress (Pre-tension)
```python
model.Stress(
    name='InitialStress',
    createStepName='Initial',
    region=region,
    distributionType=UNIFORM,
    sigma11=100.0,  # Pre-stress in X direction
    sigma22=0.0,
    sigma33=0.0,
    sigma12=0.0, sigma13=0.0, sigma23=0.0
)
```

### Initial Velocity (Impact)
```python
model.Velocity(
    name='InitialVelocity',
    createStepName='Initial',
    region=region,
    velocity1=0.0,
    velocity2=-5000.0,  # 5 m/s downward (mm/s)
    velocity3=0.0
)
```

### Temperature from Thermal Analysis ODB
```python
# Import temperature results from previous thermal analysis
model.Temperature(
    name='TempFromODB',
    createStepName='Step-1',
    region=region,
    distributionType=FROM_FILE,
    fileName='thermal_analysis.odb',
    beginStep=1,
    beginIncrement=1,
    endStep=1,
    endIncrement=LAST_INCREMENT
)
```

### Analytical Temperature Field
```python
# Temperature varies with position
model.ExpressionField(
    name='TempGradient',
    expression='20 + 80*X/100'  # Linear gradient
)

model.Temperature(
    name='AnalyticalTemp',
    createStepName='Initial',
    region=region,
    distributionType=ANALYTICAL_FIELD,
    field='TempGradient'
)
```

### Bolt Pre-Tension
```python
# Apply bolt pre-load
model.BoltLoad(
    name='BoltPretension',
    createStepName='Pretension',
    region=bolt_cross_section,
    magnitude=10000.0,  # N
    boltMethod=APPLY_FORCE
)

# Fix bolt length in subsequent step
model.loads['BoltPretension'].setValuesInStep(
    stepName='LoadStep',
    boltMethod=FIX_LENGTH
)
```

### Predefined Field Variable
```python
# Custom field variable (e.g., moisture)
model.Field(
    name='Moisture',
    createStepName='Step-1',
    region=region,
    distributionType=UNIFORM,
    fieldVariableNum=1,
    magnitude=0.5
)
```

## Sequential Thermal-Structural Workflow

1. Run thermal analysis, save ODB
2. In structural model, import temperature as predefined field
3. Temperature causes thermal strain via expansion coefficient

```python
# In structural model
model.Temperature(
    name='FromThermal',
    createStepName='StructuralStep',
    region=region,
    distributionType=FROM_FILE,
    fileName='thermal_model.odb',
    beginStep=1,
    endIncrement=LAST_INCREMENT
)
```

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Field not applied" | Wrong region or step | Verify region covers elements |
| "Cannot read from ODB" | ODB locked or wrong path | Close other sessions, check path |
| "Temperature mismatch" | Mesh incompatibility | Use mapping tolerance options |
| "Initial stress equilibrium" | Stress not self-equilibrating | Review stress field consistency |

## API Reference

For detailed parameters: [Field API](../../docs/abaqus-api/modules/field.md)
