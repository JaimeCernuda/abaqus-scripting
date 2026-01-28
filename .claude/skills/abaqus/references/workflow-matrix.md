# Workflow Matrix

Maps analysis types to the skills and API modules needed.

## Analysis Type → Required Skills

| Analysis Type | Geometry | Material | Mesh | BC | Load | Step | Interaction | Output | Job | ODB |
|---------------|:--------:|:--------:|:----:|:--:|:----:|:----:|:-----------:|:------:|:---:|:---:|
| Static Linear | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | - | ✓ | ✓ | ✓ |
| Static Nonlinear | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ○ | ✓ | ✓ | ✓ |
| Dynamic Explicit | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ○ | ✓ | ✓ | ✓ |
| Dynamic Implicit | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ○ | ✓ | ✓ | ✓ |
| Modal | ✓ | ✓ | ✓ | ✓ | - | ✓ | - | ✓ | ✓ | ✓ |
| Heat Transfer | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ○ | ✓ | ✓ | ✓ |
| Coupled Thermal | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ○ | ✓ | ✓ | ✓ |
| Contact | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Topology Opt | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | - | ✓ | ✓ | ✓ |
| Shape Opt | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | - | ✓ | ✓ | ✓ |

Legend: ✓ = Required, ○ = Optional, - = Not needed

## Skill Dependencies

```
abaqus-static-analysis
├── abaqus-geometry
├── abaqus-material
├── abaqus-mesh
├── abaqus-bc
├── abaqus-load
├── abaqus-step (StaticStep)
├── abaqus-output
├── abaqus-job
└── abaqus-odb

abaqus-dynamic-analysis
├── abaqus-geometry
├── abaqus-material
├── abaqus-mesh
├── abaqus-bc
├── abaqus-load
├── abaqus-amplitude (time-varying)
├── abaqus-step (ExplicitDynamicsStep or ImplicitDynamicsStep)
├── abaqus-interaction (optional contact)
├── abaqus-output
├── abaqus-job
└── abaqus-odb

abaqus-modal-analysis
├── abaqus-geometry
├── abaqus-material
├── abaqus-mesh
├── abaqus-bc
├── abaqus-step (FrequencyStep)
├── abaqus-output
├── abaqus-job
└── abaqus-odb

abaqus-thermal-analysis
├── abaqus-geometry
├── abaqus-material (thermal properties)
├── abaqus-mesh
├── abaqus-bc (thermal BCs)
├── abaqus-load (thermal loads)
├── abaqus-step (HeatTransferStep)
├── abaqus-output
├── abaqus-job
└── abaqus-odb

abaqus-coupled-analysis
├── abaqus-geometry
├── abaqus-material (thermal + mechanical)
├── abaqus-mesh
├── abaqus-bc
├── abaqus-load
├── abaqus-field (temperature field)
├── abaqus-step (CoupledTempDisplacementStep)
├── abaqus-output
├── abaqus-job
└── abaqus-odb

abaqus-contact-analysis
├── abaqus-geometry
├── abaqus-material
├── abaqus-mesh
├── abaqus-bc
├── abaqus-load
├── abaqus-interaction (REQUIRED)
├── abaqus-step
├── abaqus-output
├── abaqus-job
└── abaqus-odb

abaqus-topology-optimization
├── abaqus-geometry
├── abaqus-material
├── abaqus-mesh
├── abaqus-bc
├── abaqus-load
├── abaqus-step
├── abaqus-optimization (REQUIRED)
├── abaqus-output
├── abaqus-job
├── abaqus-odb
└── abaqus-export (for STL output)
```

## Step Type Selection

| Analysis Goal | Step Type | Key Parameters |
|--------------|-----------|----------------|
| Linear static stress | `StaticStep` | nlgeom=OFF |
| Nonlinear static | `StaticStep` | nlgeom=ON, increment control |
| Buckling | `BuckleStep` | numEigen |
| Natural frequencies | `FrequencyStep` | numEigen, frequency range |
| Steady-state dynamics | `SteadyStateDynamicsStep` | frequency range |
| Transient dynamics (implicit) | `ImplicitDynamicsStep` | time period, incrementation |
| Transient dynamics (explicit) | `ExplicitDynamicsStep` | time period |
| Heat transfer | `HeatTransferStep` | steady/transient |
| Coupled thermal-displacement | `CoupledTempDisplacementStep` | time period |
| Soils | `SoilsStep` | consolidation |
| Mass diffusion | `MassDiffusionStep` | time period |
