# Abaqus Topology Optimization - Python Scripting Guide

## Overview

This folder contains Python scripts for running topology optimization in Abaqus. 
Topology optimization finds the optimal material distribution given:
- **Fixed regions** (mounting points, interfaces)
- **Loads** (forces, pressures)
- **Constraints** (max volume, stress limits)
- **Objective** (maximize stiffness, minimize weight)

```
INPUT:                          OUTPUT:
┌─────────────────────┐         ┌─────────────────────┐
│ █████████████████ │         │ █               █ │
│ █████████████████ │   →→→   │ █ ╲           ╱ █ │
│ █████████████████ │  TOPO   │ █   ╲   █   ╱   █ │
│ █████████████████ │  OPT    │ █     ╲ █ ╱     █ │
│ █████████████████ │         │ █       █       █ │
│ ▓▓▓           ▓▓▓ │         │ ▓▓▓           ▓▓▓ │
└─────────────────────┘         └─────────────────────┘
  Full design space              Optimized structure
  (100% volume)                  (e.g., 30% volume)
```

## Scripts Included

| Script | Description |
|--------|-------------|
| `topology_optimization_bracket.py` | 3D bracket with two holes - full example |
| `topology_optimization_2d_bridge.py` | Classic 2D MBB beam - simpler example |
| `extract_optimized_geometry.py` | Extract results and export to STL/INP |

## Requirements

- **Abaqus with Optimization Module** (Tosca integration)
- NOT available in Learning Edition
- Requires Academic Research/Teaching Suite or Commercial license

## Quick Start

```bash
# 1. Create the model and optimization setup
abaqus cae noGUI=topology_optimization_2d_bridge.py

# 2. Open CAE and submit optimization (or add submit to script)
abaqus cae database=MBB_Beam.cae

# 3. After optimization, extract results
abaqus cae script=extract_optimized_geometry.py
```

---

## API Reference for MCP Development

### Key Classes and Methods

```python
# 1. CREATE OPTIMIZATION TASK
model.TopologyTask(
    name='TaskName',
    region=<element_set>,              # Design region
    materialInterpolationTechnique=SIMP,  # or RAMP
    materialInterpolationPenalty=3.0,     # Penalization factor
    freezeBoundaryConditionRegions=ON,    # Keep BC regions solid
    freezeLoadRegions=ON,                 # Keep load regions solid
    maxDesignCycle=50                     # Max iterations
)

# 2. DEFINE DESIGN RESPONSES (what to measure)
model.optimizationTasks['TaskName'].SingleTermDesignResponse(
    name='ResponseName',
    region=MODEL,                      # or specific region
    identifier='STRAIN_ENERGY',        # See table below
    operation=SUM                      # or MAX, MIN
)

# 3. CREATE OBJECTIVE FUNCTION (what to optimize)
model.optimizationTasks['TaskName'].ObjectiveFunction(
    name='ObjName',
    objectives=(
        (designResponse, MINIMIZE, weight),  # or MAXIMIZE
    )
)

# 4. CREATE CONSTRAINTS (limits)
model.optimizationTasks['TaskName'].OptimizationConstraint(
    name='ConstraintName',
    designResponse='ResponseName',
    restrictionMethod=RELATIVE_LESS_THAN_EQUAL,  # or ABSOLUTE_*
    restrictionValue=0.3                          # e.g., 30% volume
)

# 5. CREATE AND RUN OPTIMIZATION PROCESS
mdb.OptimizationProcess(
    name='ProcessName',
    model='ModelName',
    task='TaskName',
    maxDesignCycle=50
)

# Submit and wait
mdb.optimizationProcesses['ProcessName'].submit()
mdb.optimizationProcesses['ProcessName'].waitForCompletion()
```

### Design Response Identifiers

| Identifier | Description | Typical Use |
|------------|-------------|-------------|
| `STRAIN_ENERGY` | Compliance (inverse of stiffness) | Minimize for max stiffness |
| `VOLUME` | Total volume | Constraint (e.g., ≤30%) |
| `MASS` | Total mass | Alternative to volume |
| `DISPLACEMENT` | Nodal displacement | Constraint on deflection |
| `EIGENFREQUENCY` | Natural frequency | Avoid resonance |
| `STRESS` | von Mises stress | Constraint on max stress |
| `REACTION_FORCE` | Support reactions | Monitoring |
| `MOMENT_OF_INERTIA` | Rotational inertia | Dynamic applications |

### Geometric Restrictions (Manufacturing Constraints)

```python
# Minimum member size (prevents checkerboard)
model.optimizationTasks['Task'].minMemberSize = 5.0  # mm

# Symmetry plane
model.optimizationTasks['Task'].GeometricRestriction(
    name='Symmetry',
    technique=SYMMETRY,
    axis=AXIS_1,           # X, Y, or Z
    csys=None              # Use global coordinates
)

# Planar symmetry
model.optimizationTasks['Task'].GeometricRestriction(
    name='PlanarSym',
    technique=PLANAR_SYMMETRY,
    masterPointDetermination=SPECIFY,
    masterPoint=(0, 0, 0),
    normal=(1, 0, 0)
)

# Demold (for casting)
model.optimizationTasks['Task'].GeometricRestriction(
    name='Demold',
    technique=DEMOLD,
    pullDirection=(0, 0, 1)
)

# Stamping direction
model.optimizationTasks['Task'].GeometricRestriction(
    name='Stamp',
    technique=STAMP,
    pullDirection=(0, 1, 0)
)
```

### Frozen Regions

```python
# Method 1: Automatic (freeze BC and load regions)
model.TopologyTask(
    ...
    freezeBoundaryConditionRegions=ON,
    freezeLoadRegions=ON
)

# Method 2: Explicit frozen region
model.optimizationTasks['Task'].FrozenRegion(
    name='KeepSolid',
    region=<element_set>
)
```

---

## MCP Architecture Suggestion

```python
# abaqus_mcp_server.py (conceptual)

class AbaqusMCP:
    """MCP Server for Abaqus/Tosca Topology Optimization"""
    
    def __init__(self, abaqus_path='abaqus'):
        self.abaqus = abaqus_path
        
    # === TOOLS ===
    
    def create_design_space(self, geometry: dict) -> str:
        """
        Create design space geometry.
        geometry: {type: 'box'|'cylinder'|'from_step', dimensions: {...}}
        Returns: path to .cae file
        """
        pass
    
    def add_boundary_condition(self, model_path: str, bc: dict) -> None:
        """
        Add BC to model.
        bc: {type: 'fixed'|'displacement'|'symmetry', region: {...}, values: {...}}
        """
        pass
    
    def add_load(self, model_path: str, load: dict) -> None:
        """
        Add load to model.
        load: {type: 'force'|'pressure'|'moment', region: {...}, magnitude: float}
        """
        pass
    
    def setup_optimization(self, model_path: str, config: dict) -> None:
        """
        Configure topology optimization.
        config: {
            objective: 'max_stiffness'|'min_mass',
            volume_fraction: 0.3,
            constraints: [...],
            manufacturing: {...}
        }
        """
        pass
    
    def run_optimization(self, model_path: str) -> dict:
        """
        Submit and monitor optimization.
        Returns: {status, iterations, final_volume, convergence_history}
        """
        pass
    
    def extract_result(self, model_path: str, format: str) -> str:
        """
        Extract optimized geometry.
        format: 'stl'|'step'|'inp'
        Returns: path to exported file
        """
        pass
    
    # === EXECUTION ===
    
    def _run_script(self, script_path: str, gui: bool = False) -> dict:
        """Execute Abaqus Python script"""
        cmd = f'{self.abaqus} cae {"script" if gui else "noGUI"}={script_path}'
        # subprocess.run(...)
        pass
```

---

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     TOPOLOGY OPTIMIZATION WORKFLOW               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  │
│  │  Define  │ →  │  Setup   │ →  │   Run    │ →  │ Extract  │  │
│  │  Design  │    │  Optim.  │    │  Optim.  │    │  Result  │  │
│  │  Space   │    │  Task    │    │  Process │    │          │  │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘  │
│       │               │               │               │         │
│       ▼               ▼               ▼               ▼         │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  │
│  │ Geometry │    │ Objective│    │ Iterate: │    │ STL/STEP │  │
│  │ Material │    │ Constrai-│    │ FEA →    │    │ for CAD  │  │
│  │ Mesh     │    │ nts      │    │ Density  │    │ or 3D    │  │
│  │ BCs/Load │    │ Frozen   │    │ Update   │    │ Print    │  │
│  └──────────┘    │ Regions  │    └──────────┘    └──────────┘  │
│                  └──────────┘                                   │
│                                                                  │
│  Python API:     Python API:      Python API:     Python API:   │
│  Part, Mesh,     TopologyTask,    OptProcess,     odbAccess,    │
│  Assembly,       DesignResponse   submit(),       extract()     │
│  Step, BC        Objective,       waitFor-                      │
│                  Constraint       Completion()                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Tips for Your MCP

1. **Parametric Templates**: Create base scripts with `{placeholders}` that your MCP fills in

2. **Status Monitoring**: Parse the `.sta` file for convergence info:
   ```
   ITERATION  OBJECTIVE  CONSTRAINT  STATUS
   1          1.234e+03  0.95        FEASIBLE
   2          9.876e+02  0.45        FEASIBLE
   ...
   ```

3. **Result Visualization**: The ODB contains `DENSITY` field - values 0-1 indicate void-solid

4. **STL Export**: Abaqus can export iso-surfaces at a threshold (e.g., density=0.3)

5. **Batch Processing**: Use `noGUI` mode for headless optimization runs

---

## Common Issues

| Issue | Solution |
|-------|----------|
| "Optimization module not available" | Need full Abaqus license with Tosca |
| "No convergence" | Relax constraints, increase iterations |
| "Checkerboard pattern" | Add minimum member size constraint |
| "Disconnected regions" | Add connectivity constraint or frozen regions |
| "Mesh too coarse" | Refine mesh (but increases compute time) |

---

## References

- Abaqus User's Guide: Chapter 18 "The Optimization Module"
- Abaqus Example Problems Guide: Section 11 "Structural Optimization"
- SIMP Method: Bendsøe & Sigmund, "Topology Optimization"
