# Topology Optimization Workflow Checklist

## Pre-Optimization

- [ ] Working static analysis (converges without optimization)
- [ ] Design space defined (region to optimize)
- [ ] Frozen regions identified (BCs, loads, connections)
- [ ] Volume fraction target set (e.g., 30%)
- [ ] Manufacturing constraints considered (min member size)

## Setup

- [ ] TopologyTask created
- [ ] Design responses defined (volume, strain energy)
- [ ] Objective function set (minimize energy = maximize stiffness)
- [ ] Volume constraint set
- [ ] Frozen regions applied

## Post-Optimization

- [ ] Optimization converged
- [ ] Result is manufacturable
- [ ] Export optimized geometry (STL or smooth)

## Validation Steps

| Stage | What to Check |
|-------|---------------|
| Base model | Static analysis runs, results are sensible |
| Optimization setup | No errors in task definition |
| After iteration 5 | Objective decreasing, no disconnection |
| Convergence | Objective stable (< 0.1% change) |
| Final design | Load path intact, no floating regions |

## Common Volume Fraction Targets

| Volume Fraction | Result | Use Case |
|-----------------|--------|----------|
| 20-30% | Aggressive lightweighting | Aerospace, weight-critical |
| 30-40% | Balanced | General structural |
| 40-50% | Conservative | Safety-critical, fatigue |
