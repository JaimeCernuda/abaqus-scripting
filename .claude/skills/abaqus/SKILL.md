---
name: abaqus
description: Master skill for Abaqus FEA scripting. Use for any finite element analysis, topology optimization, or Abaqus Python scripting task. Routes to appropriate specialized skills.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash(abaqus:*)
  - Bash(uv:*)
  - Skill
---

# Abaqus Master Skill

This is the master orchestrator for all Abaqus FEA tasks. It routes requests to the appropriate specialized skills based on the user's needs.

## How to Use This Skill

When a user asks for any Abaqus-related task:
1. Identify the analysis type from keywords and context
2. Route to the appropriate workflow or module skill
3. Gather required inputs systematically

## Analysis Type Decision Tree

### Primary Decision: What Physics?

```
User Request
    │
    ├── "stress", "displacement", "strength", "deflection", "load"
    │   └── Is it time-varying?
    │       ├── NO → /abaqus-static-analysis
    │       └── YES → /abaqus-dynamic-analysis
    │
    ├── "frequency", "modal", "vibration", "resonance", "natural"
    │   └── /abaqus-modal-analysis
    │
    ├── "optimize", "topology", "minimize weight", "lightweighting"
    │   └── Shape or topology?
    │       ├── Redistribute material → /abaqus-topology-optimization
    │       └── Change surface shape → /abaqus-shape-optimization
    │
    ├── "impact", "crash", "dynamic", "explicit", "transient"
    │   └── /abaqus-dynamic-analysis
    │
    ├── "heat", "thermal", "temperature", "conduction"
    │   └── Is there structural coupling?
    │       ├── Thermal only → /abaqus-thermal-analysis
    │       └── Thermal + structural → /abaqus-coupled-analysis
    │
    ├── "contact", "friction", "touching", "multi-body"
    │   └── /abaqus-contact-analysis
    │
    ├── "fatigue", "durability", "cycles", "life"
    │   └── /abaqus-fatigue-analysis
    │
    └── Not clear → Ask clarifying questions
```

### Boundary Between Similar Analyses

| If User Says... | But Also... | Route To |
|-----------------|-------------|----------|
| "stress analysis" | "with temperature" | `/abaqus-coupled-analysis` |
| "optimize" | "just shape, not holes" | `/abaqus-shape-optimization` |
| "dynamic" | "find frequencies" | `/abaqus-modal-analysis` |
| "dynamic" | "impact/crash" | `/abaqus-dynamic-analysis` |
| "vibration" | "forced response" | `/abaqus-dynamic-analysis` |

## Module Skills (Building Blocks)

For fine-grained control or when building custom workflows:

| Task | Module Skill | When to Use Directly |
|------|--------------|---------------------|
| Create geometry | `/abaqus-geometry` | Just need part/assembly |
| Define material | `/abaqus-material` | Adding material to existing model |
| Create mesh | `/abaqus-mesh` | Just meshing, no analysis |
| Apply BCs | `/abaqus-bc` | Adding constraints |
| Apply loads | `/abaqus-load` | Adding forces/pressures |
| Configure step | `/abaqus-step` | Specific step settings |
| Contact/ties | `/abaqus-interaction` | Multi-body connections |
| Time profiles | `/abaqus-amplitude` | Time-varying definitions |
| Initial conditions | `/abaqus-field` | Temperature, stress fields |
| Output requests | `/abaqus-output` | Custom output variables |
| Run job | `/abaqus-job` | Submission and monitoring |
| Extract results | `/abaqus-odb` | Post-processing |
| TO settings | `/abaqus-optimization` | Tosca task configuration |
| Export geometry | `/abaqus-export` | STL, STEP, INP export |
| Get API docs | `/abaqus-docs` | Download documentation |

## Required Information Checklist

### For ANY Analysis

| Input | Required | Default | Ask If Missing |
|-------|----------|---------|----------------|
| Geometry | YES | - | "What are the dimensions?" |
| Material | YES | Steel | "What material?" |
| BCs | YES | - | "How is it supported?" |
| Loads | YES* | - | "What loads?" (*not for modal) |
| Analysis type | YES | Static | "What do you want to find out?" |

### Analysis-Specific Requirements

| Analysis | Additional Required |
|----------|---------------------|
| Static | - |
| Modal | Density (for mass matrix) |
| Dynamic | Density, time parameters |
| Thermal | Conductivity, heat sources/sinks |
| Topology opt | Volume fraction, frozen regions |
| Contact | Surface definitions, contact properties |

## Multi-Analysis Scenarios

Sometimes users need combinations:

| Scenario | Approach |
|----------|----------|
| "Static then modal" | Run static first, then modal on same model |
| "Thermal stress" | Use `/abaqus-coupled-analysis` (sequential coupling) |
| "Optimize for vibration" | Topology opt with frequency constraint (advanced) |
| "Check buckling" | Static analysis, then eigenvalue buckling step |

## Escalation Paths

### When to Ask Questions

- **Ambiguous analysis type:** "Do you want to find stress (static) or natural frequencies (modal)?"
- **Missing critical input:** "Where is the structure supported?"
- **Conflicting requirements:** "You mentioned both optimization and fatigue - which is the primary goal?"

### When to Recommend Different Approach

- **Learning Edition + topology opt:** "Topology optimization requires full Abaqus license. Would you like a static analysis instead?"
- **Very large model:** "This may exceed Learning Edition limits. Consider using symmetry or coarser mesh."
- **Complex contact:** "Multi-body contact is complex. Shall we start with a simplified tie constraint?"

## Units System

All Abaqus skills use consistent SI units (mm-tonne-s-N-MPa):

| Quantity | Unit | Typical Value |
|----------|------|---------------|
| Length | mm | 100.0 |
| Force | N | 1000.0 |
| Stress/Modulus | MPa | 210000.0 |
| Density | tonne/mm³ | 7.85e-9 |
| Time | s | 1.0 |
| Temperature | °C or K | 20.0 |

## Running Abaqus Scripts

```bash
# With GUI (interactive)
abaqus cae script=script_name.py

# Headless (faster, no display)
abaqus cae noGUI=script_name.py

# Post-processing only (ODB access)
abaqus python script_name.py

# Submit job
abaqus job=JobName interactive
```

## Quick Reference: Workflow Skills

| Workflow | Skill | Primary Use |
|----------|-------|-------------|
| Static structural | `/abaqus-static-analysis` | Stress, displacement, reactions |
| Modal/frequency | `/abaqus-modal-analysis` | Natural frequencies, mode shapes |
| Topology opt | `/abaqus-topology-optimization` | Weight minimization |
| Shape opt | `/abaqus-shape-optimization` | Surface optimization |
| Explicit dynamics | `/abaqus-dynamic-analysis` | Impact, crash |
| Heat transfer | `/abaqus-thermal-analysis` | Temperature distribution |
| Thermomechanical | `/abaqus-coupled-analysis` | Thermal + structural |
| Contact | `/abaqus-contact-analysis` | Multi-body contact |
| Fatigue | `/abaqus-fatigue-analysis` | Durability analysis |

## API Documentation

For detailed Abaqus Python API syntax, use `/abaqus-docs` to download and reference:
- [API Documentation](../../docs/abaqus-api/README.md)
