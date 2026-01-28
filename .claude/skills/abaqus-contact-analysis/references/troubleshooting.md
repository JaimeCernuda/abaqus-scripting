# Contact Analysis Troubleshooting

## Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "Contact not detected" | Gap too large | Check initial geometry, use adjust |
| "Overclosure too large" | Initial penetration | Use adjustment=OVERCLOSED |
| "Convergence failure" | Contact instability | Use stabilization, smaller increments |
| "Chattering" | Contact oscillation | Add damping, refine mesh |
| "Severe discontinuity" | Contact state change | Smaller time increments |
| "Too much penetration" | Wrong master/slave | Swap roles, refine slave mesh |
| "Negative eigenvalue" | Unstable contact | Add stabilization |
| "Zero pivot" | Rigid body motion | Check constraints, add BCs |

## Master/Slave Selection Rules

- **Master**: stiffer material, coarser mesh, larger surface area
- **Slave**: softer material, finer mesh, smaller surface area

**If both are similar:**
- Choose the analytically rigid surface as master
- Choose the surface with coarser mesh as master
- Choose the larger surface as master

## Convergence Tips

### Step 1: Start Simple
- Begin with frictionless contact
- Add friction after contact works

### Step 2: Control Increments
```python
model.StaticStep(
    name='Load',
    previous='Initial',
    nlgeom=ON,
    initialInc=0.01,    # Start small
    minInc=1e-10,       # Allow very small increments
    maxInc=0.1,         # Limit maximum increment
    maxNumInc=500       # Allow many increments
)
```

### Step 3: Add Stabilization
```python
# Automatic stabilization
model.StaticStep(..., stabilizationMagnitude=0.0002,
                 stabilizationMethod=DAMPING_FACTOR)

# Or contact-specific stabilization
model.SurfaceToSurfaceContactStd(...,
    contactStabilization=ON,
    stabilizationMagnitude=0.001)
```

### Step 4: Refine Contact Mesh
- Use finer mesh on slave surface
- Ensure element size is similar across contact

## Initial Gap/Overclosure Issues

### Too Much Gap
```python
# Adjust surfaces to be in contact initially
model.SurfaceToSurfaceContactStd(..., adjustment=ON)
```

### Overclosure (Penetration)
```python
# Resolve interference gradually
model.SurfaceToSurfaceContactStd(..., adjustment=OVERCLOSED)
```

## Contact Output Verification

Check these outputs to verify contact:

| Output | What to Check |
|--------|---------------|
| CPRESS | Contact pressure (should be non-zero where contact occurs) |
| COPEN | Opening distance (should be zero where in contact) |
| CSLIP | Slip distance (verify friction is working) |
| CSTATUS | Contact status (1=closed, 0=open) |

## Friction Issues

### Friction Causing Convergence Problems
1. Try frictionless first
2. Use penalty method (more stable)
3. Reduce friction coefficient
4. Use smaller increments

### No Friction Effect Visible
1. Check CSHEAR output
2. Verify tangential behavior is defined
3. Check if surfaces are actually sliding

## Mesh Quality at Contact

- Avoid distorted elements at contact surfaces
- Match mesh density across contact pair
- Use structured mesh if possible
- Second-order elements may help accuracy

## Explicit vs Implicit

| Issue | Try Explicit If |
|-------|-----------------|
| Many contact pairs | >10 interacting bodies |
| Impact/crash | High-speed events |
| Convergence failure | Implicit won't converge |
| Complex sliding | Large relative motion |

```python
# Switch to explicit dynamics
model.ExplicitDynamicsStep(name='Impact', previous='Initial',
                           timePeriod=0.01)
```

## Debugging Workflow

1. **Verify geometry**: Check initial positions in CAE
2. **Check surfaces**: Visualize contact surfaces
3. **Test without contact**: Does model work without contact?
4. **Simple contact first**: Start with tie, then add sliding
5. **Check outputs**: CSTRESS, CDISP should show contact
6. **Review .sta file**: Check for warnings about contact
