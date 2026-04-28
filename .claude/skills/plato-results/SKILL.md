---
name: plato-results
description: Post-process Plato Exodus output files. Extract topology density, stress, displacement, convergence data.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
---

# Plato Results — Exodus Post-Processing

Read and analyze results from Plato optimization/analysis runs.

## When to Use

- User asks about maximum stress, displacement, or density field
- User wants convergence information
- User asks "did it converge?" or "what's the result?"
- After a Plato job completes

## Output Files

| File | Contents |
|---|---|
| `platomain.exo` | Main output with topology field over all iterations |
| `Iteration###.exo` | Per-iteration results (density, stress, displacement) |
| `plato-<jobid>.out` | Console output with convergence info |

## Reading Results with Python

**CRITICAL**: Run post-processing via SLURM, not on login nodes.

### Extract final topology (density field)

```python
import exodus

exo = exodus.exodus("platomain.exo", "r")
num_times = exo.num_times()
print(f"Number of iterations: {num_times}")

# Get nodal density at final iteration
node_var_names = exo.get_node_variable_names()
print(f"Node variables: {node_var_names}")

if "Topology" in node_var_names:
    topology = exo.get_node_variable_values("Topology", num_times)
    print(f"Density range: [{min(topology):.4f}, {max(topology):.4f}]")
    print(f"Solid fraction: {sum(1 for d in topology if d > 0.5) / len(topology):.1%}")

exo.close()
```

### Extract stress and displacement

```python
import exodus

exo = exodus.exodus("Iteration050.exo", "r")

# Element variables (stress)
elem_var_names = exo.get_element_variable_names()
print(f"Element variables: {elem_var_names}")

block_ids = exo.get_element_block_ids()
for bid in block_ids:
    if "vonmises" in elem_var_names:
        vonmises = exo.get_element_variable_values(bid, "vonmises", 1)
        print(f"Block {bid}: max von Mises = {max(vonmises):.2e}")

# Nodal variables (displacement)
node_var_names = exo.get_node_variable_names()
if "dispx" in node_var_names:
    ux = exo.get_node_variable_values("dispx", 1)
    uy = exo.get_node_variable_values("dispy", 1)
    uz = exo.get_node_variable_values("dispz", 1)
    import math
    max_disp = max(math.sqrt(x**2 + y**2 + z**2) for x, y, z in zip(ux, uy, uz))
    print(f"Max displacement magnitude: {max_disp:.6e}")

exo.close()
```

### Convergence from console output

```bash
grep "Objective\|objective\|iteration\|Iteration" plato-*.out
```

## SLURM Post-Processing Script

```bash
srun --account=bekn-delta-cpu --partition=cpu-interactive \
  --time=00:10:00 --mem=4g --pty bash -c '
  source /projects/bekn/jcernuda/plato/spack/share/spack/setup-env.sh
  spack env activate /projects/bekn/jcernuda/plato
  python3 extract_results.py
'
```

## Validation Checklist

- [ ] Final density field is mostly 0 or 1 (not stuck at gray 0.5)
- [ ] Volume fraction matches target (within 1-2%)
- [ ] Objective value decreased monotonically (convergence)
- [ ] Max stress is within allowable limit (if stress-constrained)
- [ ] Displacement is physically reasonable
- [ ] No floating disconnected material regions

## Troubleshooting

| Issue | Cause | Fix |
|---|---|---|
| "module exodus not found" | Spack env not loaded | Source spack setup first |
| All densities = 0.5 | Optimization didn't run | Check max_iterations > 0 |
| Gray densities (0.3-0.7) | Insufficient iterations or low penalty | Increase iterations or SIMP exponent |
| Volume fraction wrong | Constraint not applied | Check constraint block in .i file |
| No Exodus files | Job failed | Check plato-*.err for errors |
