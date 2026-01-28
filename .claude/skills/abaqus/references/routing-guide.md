# Skill Routing Guide

This guide helps determine which Abaqus skill to invoke based on analysis type and user intent.

## By Analysis Type

| Analysis | Primary Skill | Supporting Module Skills |
|----------|---------------|--------------------------|
| Static stress | `/abaqus-static-analysis` | geometry, material, mesh, bc, load, step, output, job, odb |
| Modal/frequency | `/abaqus-modal-analysis` | geometry, material, mesh, bc, step, output, job, odb |
| Explicit dynamics | `/abaqus-dynamic-analysis` | geometry, material, mesh, bc, load, amplitude, step, interaction, output, job, odb |
| Implicit dynamics | `/abaqus-dynamic-analysis` | geometry, material, mesh, bc, load, amplitude, step, output, job, odb |
| Heat transfer | `/abaqus-thermal-analysis` | geometry, material, mesh, bc, load, step, output, job, odb |
| Coupled thermal-stress | `/abaqus-coupled-analysis` | geometry, material, mesh, bc, load, field, step, output, job, odb |
| Contact/multi-body | `/abaqus-contact-analysis` | geometry, material, mesh, bc, load, interaction, step, output, job, odb |
| Topology optimization | `/abaqus-topology-optimization` | geometry, material, mesh, bc, load, step, optimization, output, job, odb, export |
| Shape optimization | `/abaqus-shape-optimization` | geometry, material, mesh, bc, load, step, optimization, output, job, odb |
| Fatigue/durability | `/abaqus-fatigue-analysis` | static-analysis, amplitude, odb |

## By User Intent

### "I want to create/build..."

| User Wants... | Route To |
|---------------|----------|
| "Create a model from scratch" | Start with `/abaqus-geometry` |
| "Build a cantilever beam" | `/abaqus-static-analysis` (full workflow) |
| "Design an optimized bracket" | `/abaqus-topology-optimization` |
| "Set up a contact model" | `/abaqus-contact-analysis` |

### "I want to analyze..."

| User Wants... | Route To |
|---------------|----------|
| "Analyze stress in a part" | `/abaqus-static-analysis` |
| "Check if it will break" | `/abaqus-static-analysis` (factor of safety) |
| "Find natural frequencies" | `/abaqus-modal-analysis` |
| "Simulate a drop test" | `/abaqus-dynamic-analysis` |
| "Check thermal performance" | `/abaqus-thermal-analysis` |
| "Analyze fatigue life" | `/abaqus-fatigue-analysis` |

### "I want to modify..."

| User Wants... | Route To |
|---------------|----------|
| "Add a load to existing model" | `/abaqus-load` |
| "Change the mesh" | `/abaqus-mesh` |
| "Update boundary conditions" | `/abaqus-bc` |
| "Define a new material" | `/abaqus-material` |
| "Add contact between parts" | `/abaqus-interaction` |

### "I want to check/extract..."

| User Wants... | Route To |
|---------------|----------|
| "Check results" | `/abaqus-odb` |
| "Extract stress data" | `/abaqus-odb` |
| "Get displacement plot" | `/abaqus-odb` |
| "Export to STL" | `/abaqus-export` |
| "Run the analysis" | `/abaqus-job` |

### "I need help with..."

| User Wants... | Route To |
|---------------|----------|
| "Fix an error" | Check troubleshooting in relevant skill |
| "API reference" | `/abaqus-docs` |
| "Understand the syntax" | `/abaqus-docs` |
| "Learn about element types" | `/abaqus-mesh` |

## Trigger Phrases Quick Reference

### Static Analysis Triggers
- "stress", "displacement", "deflection", "deformation"
- "strength", "will it hold", "factor of safety"
- "load capacity", "stiffness", "reactions"
- "linear analysis", "static"

### Modal Analysis Triggers
- "frequency", "frequencies", "modal"
- "vibration", "resonance", "mode shapes"
- "natural frequency", "eigenvalue"
- "how does it vibrate"

### Dynamic Analysis Triggers
- "impact", "crash", "collision", "drop test"
- "explicit", "transient", "time-dependent"
- "blast", "explosion", "shock"
- "dynamic response", "impulse"

### Thermal Analysis Triggers
- "heat", "thermal", "temperature"
- "conduction", "convection", "radiation"
- "cooling", "heating", "heat transfer"
- "steady-state thermal", "transient thermal"

### Coupled Analysis Triggers
- "thermal stress", "thermal expansion"
- "temperature + stress", "thermomechanical"
- "heat and deformation", "warping from temperature"

### Optimization Triggers
- "optimize", "optimization", "topology"
- "minimize weight", "lightweight", "reduce mass"
- "material distribution", "where to remove material"
- "shape optimization", "stress concentration"

### Contact Analysis Triggers
- "contact", "friction", "touching"
- "assembly", "multi-body", "parts interacting"
- "interference", "press fit"

### Fatigue Analysis Triggers
- "fatigue", "durability", "cycles"
- "life prediction", "endurance", "S-N curve"
- "damage accumulation", "Miner's rule"

## Decision Flow for Ambiguous Requests

### "Analyze this part"
1. Ask: "What do you want to find out - stress/strength (static), vibration characteristics (modal), or something else?"
2. If structural strength --> `/abaqus-static-analysis`
3. If vibration --> `/abaqus-modal-analysis`

### "Optimize this design"
1. Ask: "Do you want to redistribute material (topology) or just modify the surface shape?"
2. If topology --> `/abaqus-topology-optimization`
3. If shape only --> `/abaqus-shape-optimization`

### "Temperature effects"
1. Ask: "Do you need just the temperature distribution, or also the thermal stress?"
2. If temperature only --> `/abaqus-thermal-analysis`
3. If thermal stress --> `/abaqus-coupled-analysis`

### "Dynamic analysis"
1. Ask: "Are you looking for natural frequencies (modal) or time-domain response (explicit/implicit dynamics)?"
2. If frequencies --> `/abaqus-modal-analysis`
3. If time response --> `/abaqus-dynamic-analysis`

## License Considerations

| Feature | Learning Edition | Full License |
|---------|------------------|--------------|
| Static analysis | Yes (1000 nodes max) | Yes |
| Modal analysis | Yes (1000 nodes max) | Yes |
| Dynamic explicit | Yes (1000 nodes max) | Yes |
| Thermal analysis | Yes (1000 nodes max) | Yes |
| Topology optimization | **NO** | Yes (requires Tosca) |
| Shape optimization | **NO** | Yes (requires Tosca) |
| Fatigue analysis | Limited | Yes (requires fe-safe or similar) |

When user has Learning Edition and requests topology optimization:
- Explain limitation
- Offer alternative: manual design iteration with static analysis
- Suggest considering full license for professional work
