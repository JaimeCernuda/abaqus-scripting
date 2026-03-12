# Documentation Quick Reference

## Location
All API docs are at: `.claude/docs/abaqus-api/`

## Module Index
| Module | Path | Key Classes |
|--------|------|-------------|
| Model | `modules/mdb.md` | Model, Mdb |
| Model Details | `modules/mdb_model.md` | Model internals |
| Part | `modules/part.md` | Part, Feature |
| Sketcher | `modules/sketcher.md` | ConstrainedSketch |
| Assembly | `modules/assembly.md` | Assembly, Instance |
| Material | `modules/material.md` | Material, Elastic, Plastic |
| Property | `modules/property.md` | Section types |
| Mesh | `modules/mesh.md` | MeshPart, ElemType |
| Step | `modules/step.md` | StaticStep, FrequencyStep |
| Load | `modules/load.md` | ConcentratedForce, Pressure |
| BC | `modules/bc.md` | EncastreBC, DisplacementBC |
| Interaction | `modules/interaction.md` | ContactProperty, SurfaceToSurface |
| Amplitude | `modules/amplitude.md` | TabularAmplitude |
| Field | `modules/field.md` | PredefinedField |
| Output | `modules/output.md` | FieldOutputRequest |
| Job | `modules/job.md` | Job |
| ODB | `modules/odb.md` | Odb, FieldOutput |
| Optimization | `modules/optimization.md` | TopologyTask |

## Usage
Read specific sections with:
```
Read .claude/docs/abaqus-api/modules/material.md
```

## Common Lookups

### Creating Geometry
- Part creation: `modules/part.md`
- Sketching: `modules/sketcher.md`
- Assembly: `modules/assembly.md`

### Defining Properties
- Materials: `modules/material.md`
- Sections: `modules/property.md`

### Analysis Setup
- Steps: `modules/step.md`
- Loads: `modules/load.md`
- BCs: `modules/bc.md`
- Contact: `modules/interaction.md`

### Mesh and Run
- Meshing: `modules/mesh.md`
- Jobs: `modules/job.md`

### Results
- ODB access: `modules/odb.md`
- Output requests: `modules/output.md`
