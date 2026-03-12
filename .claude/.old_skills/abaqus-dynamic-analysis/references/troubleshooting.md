# Dynamic Analysis Troubleshooting

## Common Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| "Excessive element distortion" | Large deformation | Reduce time step or use ALE |
| "Stable time increment = 0" | Zero stiffness element | Check material/element type |
| "Kinetic energy exceeds internal energy" | Instability | Add damping or reduce step |
| "Missing density" | No mass defined | Add `material.Density()` |
| "Time increment too small" | Very small elements | Use mass scaling or coarsen mesh |
| "Convergence failure" (implicit) | Severe nonlinearity | Switch to explicit or smaller increments |
| "Zero pivot" | Unconstrained rigid body | Add boundary conditions |
| "Negative eigenvalue" | Material instability | Check material properties |

## Explicit vs Implicit Comparison

| Factor | Explicit | Implicit |
|--------|----------|----------|
| **Duration** | Short (ms) | Longer (s) |
| **Time step** | Automatic (very small) | User-controlled |
| **Convergence** | No iterations needed | May not converge |
| **Memory** | Lower | Higher |
| **Contact** | Handles naturally | More difficult |
| **Best for** | Impact, crash, blast | Vibration, slow transient |
| **Cost per step** | Cheap | Expensive |
| **Total steps** | Many | Few |

### When to Use Explicit

- Event duration < 10 ms
- Impact or crash loading
- Severe contact/sliding
- Material failure/fracture
- Large deformations
- Complex nonlinearity

### When to Use Implicit

- Event duration > 100 ms
- Vibration response
- Linear or mildly nonlinear
- Fewer output frames needed
- Better energy conservation needed

## Time Step Guidelines

### Explicit (Automatic)

The stable time increment is computed automatically:
```
dt_stable ≈ L_min / c
```
Where:
- `L_min` = smallest element dimension
- `c` = wave speed = sqrt(E/ρ)

**Tips:**
- Smaller elements = smaller time step = longer analysis
- Mass scaling artificially increases dt_stable
- Check `*.sta` file for stable time increment

### Implicit (User-Controlled)

```python
model.ImplicitDynamicsStep(
    name='Step',
    previous='Initial',
    timePeriod=T_total,
    initialInc=T_total / 100,   # Start with 100 increments
    minInc=1e-8,                 # Very small minimum
    maxInc=T_total / 10,         # At most 10 increments
    maxNumInc=10000              # Allow many increments
)
```

**Guidelines:**
- `initialInc = timePeriod / 100` (good starting point)
- `maxInc = timePeriod / 10` (capture dynamics)
- For vibration: `maxInc < 1 / (20 * frequency)` (20 points per cycle)

## Energy Balance Diagnostics

### Checking Energy Conservation

```python
# Request energy history output
model.HistoryOutputRequest(
    name='Energies',
    createStepName='Impact',
    variables=('ALLKE', 'ALLIE', 'ALLWK', 'ALLPD', 'ALLAE', 'ETOTAL'),
    frequency=1
)
```

### Interpreting Energy Results

| Variable | Meaning | Check |
|----------|---------|-------|
| ETOTAL | Total energy | Should be ~constant |
| ALLKE | Kinetic energy | Transfer during impact |
| ALLIE | Internal energy | Stored strain energy |
| ALLPD | Plastic dissipation | Energy absorbed by plasticity |
| ALLAE | Artificial energy | < 5% of ALLIE (hourglass) |

### Energy Problems

| Symptom | Cause | Solution |
|---------|-------|----------|
| ETOTAL increasing | External work or instability | Check loads, contact |
| ETOTAL decreasing | Numerical dissipation | Expected with damping |
| ALLAE > 5% of ALLIE | Hourglass modes | Use `hourglassControl=ENHANCED` |
| ALLKE >> ALLIE | Rigid body motion | Check BCs |

## Mass Scaling Issues

### When Mass Scaling Causes Problems

- Inertia-dominated problems (drop tests)
- Wave propagation analysis
- Natural frequency estimation

### Checking Mass Scaling Effects

1. Run with and without mass scaling
2. Compare kinetic energies
3. If ALLKE differs significantly, reduce scaling

### Safe Mass Scaling Settings

```python
# Conservative: scale only at beginning
massScaling=((SEMI_AUTOMATIC, MODEL, AT_BEGINNING, 0.0, 1e-07, BELOW_MIN, 0, 0, 0.0, 0.0, 0, None),)

# More aggressive (use with caution)
massScaling=((SEMI_AUTOMATIC, MODEL, THROUGHOUT_STEP, 0.0, 1e-06, BELOW_MIN, 1, 0, 0.0, 0.0, 0, None),)
```

## Contact Problems in Dynamics

| Issue | Cause | Solution |
|-------|-------|----------|
| Penetration | Insufficient penalty | Increase contact stiffness |
| Bouncing | Overconstrained | Reduce penalty stiffness |
| Chattering | Friction + inertia | Add friction damping |
| Explosion | Initial penetration | Fix initial geometry |

### Contact Stabilization

```python
# Add damping to contact
model.interactionProperties['Contact'].NormalBehavior(
    pressureOverclosure=HARD,
    allowSeparation=ON,
    contactStiffnessScaleFactor=1.0  # Default
)

# For explicit: use default contact works well
# For implicit: may need soft contact
model.interactionProperties['Contact'].NormalBehavior(
    pressureOverclosure=LINEAR,
    contactStiffness=1e6
)
```

## Mesh Quality for Dynamics

### Element Quality Requirements

| Check | Requirement | Command |
|-------|-------------|---------|
| Aspect ratio | < 10:1 | `mesh.verifyMeshQuality()` |
| Warpage | < 15° | Check element warnings |
| Jacobian | > 0 | No inverted elements |

### Element Type Selection

| Problem Type | Recommended Elements |
|--------------|---------------------|
| General 3D | C3D8R (explicit), C3D8 (implicit) |
| Bending-dominated | C3D8I or C3D20R |
| Contact surfaces | C3D8R with fine mesh |
| Thin structures | S4R shells |

## Debugging Workflow

### 1. Check Model Setup

```python
# Verify material has density
for mat in model.materials.values():
    if not hasattr(mat, 'density'):
        print("WARNING: %s missing density" % mat.name)
```

### 2. Run Short Test

```python
# Run 1% of total time first
model.ExplicitDynamicsStep(
    name='Test',
    previous='Initial',
    timePeriod=TIME_PERIOD * 0.01
)
```

### 3. Check Stable Time Increment

Look in `.sta` file:
```
STEP    INC   ATT  SEVERE     TOTAL       KINETIC       TOTAL
                   DISCON     TIME        ENERGY        ENERGY
   1      1    1              0.000E+00   1.234E+03     1.234E+03
          STABLE TIME INCREMENT =   1.234E-07
```

### 4. Monitor Energy Balance

```bash
# Open ODB and check history
abaqus python check_energy.py
```

```python
# check_energy.py
from odbAccess import *
odb = openOdb('Analysis.odb')
step = odb.steps['Impact']
hr = step.historyRegions['Assembly ASSEMBLY']
etotal = hr.historyOutputs['ETOTAL'].data
print("Initial E:", etotal[0][1])
print("Final E:", etotal[-1][1])
print("Change:", (etotal[-1][1] - etotal[0][1]) / etotal[0][1] * 100, "%")
odb.close()
```

## Performance Optimization

| Issue | Solution |
|-------|----------|
| Too slow (explicit) | Use mass scaling, coarser mesh |
| Too slow (implicit) | Reduce output frequency, larger increments |
| Memory issues | Reduce output variables, use restart |
| Disk space | Compress ODB, reduce output |

### Parallel Execution

```bash
# Run explicit with multiple CPUs
abaqus job=Analysis cpus=4 mp_mode=threads

# Or in script
job = mdb.Job(name='Analysis', model='Model',
              numCpus=4, numDomains=4)
```
