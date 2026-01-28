# Step Troubleshooting

## Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "Too many increments" | Load too large or convergence difficulty | Reduce load magnitude, reduce maxInc, increase maxNumInc |
| "Convergence not achieved" | Severe nonlinearity | Reduce initialInc, check model for errors, add stabilization |
| "Time increment too small" | Automatic cutback hit minInc | Increase minInc, fix instability source, check for overconstrained model |
| "Negative eigenvalues" | Buckling, instability, or free body | Check BCs for rigid body motion, add stabilization |
| "Explicit time increment" | Very small elements | Use mass scaling, coarsen mesh, increase element size |
| "Zero pivot" | Singular stiffness matrix | Check BCs, look for unconnected nodes |

## Convergence Strategies

### For Nonlinear Problems

1. **Start with smaller increments:**
   ```python
   initialInc=0.01, maxInc=0.05
   ```

2. **Allow more iterations:**
   ```python
   maxNumInc=1000
   ```

3. **Enable automatic stabilization:**
   ```python
   model.StaticStep(name='Load', previous='Initial',
                    stabilizationMethod=DISSIPATED_ENERGY_FRACTION,
                    continueDampingFactors=False,
                    adaptiveDampingRatio=0.05)
   ```

### For Contact Problems

1. Use `nlgeom=ON` always
2. Start with very small increments: `initialInc=0.001`
3. Consider explicit dynamics if convergence is impossible

### For Large Deformation

1. Always use `nlgeom=ON`
2. Check for element distortion
3. Consider remeshing for extreme deformation

## Increment Size Guidelines

| Analysis Type | initialInc | minInc | maxInc |
|---------------|------------|--------|--------|
| Linear static | 1.0 | 1e-6 | 1.0 |
| Nonlinear static | 0.1 | 1e-8 | 0.2 |
| Contact | 0.01 | 1e-12 | 0.05 |
| Plasticity | 0.05 | 1e-10 | 0.1 |
| Dynamic implicit | 0.001 | 1e-10 | 0.01 |

## When to Use Each Step Type

| Scenario | Wrong Choice | Right Choice |
|----------|--------------|--------------|
| Slow quasi-static loading | ExplicitDynamicsStep | StaticStep with nlgeom=ON |
| High-speed impact (<10ms) | StaticStep | ExplicitDynamicsStep |
| Vibration at single frequency | FrequencyStep | SteadyStateDynamicsStep |
| Finding natural frequencies | SteadyStateDynamicsStep | FrequencyStep |
| Gradual temperature change | HeatTransferStep(STEADY_STATE) | HeatTransferStep(TRANSIENT) |

## Debugging Tips

1. **Run single increment first:**
   ```python
   maxNumInc=1, initialInc=0.01
   ```
   Check if model is set up correctly.

2. **Check for rigid body motion:**
   Ensure all 6 DOFs are constrained (3 translations + 3 rotations).

3. **Verify material properties:**
   Young's modulus and Poisson's ratio must be reasonable.

4. **Examine increment cutback pattern:**
   If solver keeps cutting back, look for instability or overconstrained regions.

5. **Check message file (.msg):**
   Contains detailed convergence information and warnings.
