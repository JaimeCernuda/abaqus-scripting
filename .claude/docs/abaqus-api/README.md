# Abaqus API Documentation

Local copy of the abqpy API documentation for Claude Code skills.

## Source

Downloaded from: https://hailin.wang/abqpy/en/2025/reference/

## Modules

| Module | Description | File |
|--------|-------------|------|
| mdb | Model Database - core model operations | [modules\mdb.md](modules\mdb.md) |
| mdb_model | Model object and methods | [modules\mdb_model.md](modules\mdb_model.md) |
| odb | Output Database - results access | [modules\odb.md](modules\odb.md) |
| part | Part creation and features | [modules\part.md](modules\part.md) |
| sketcher | 2D sketch operations | [modules\sketcher.md](modules\sketcher.md) |
| assembly | Instance and assembly operations | [modules\assembly.md](modules\assembly.md) |
| material | Material definitions | [modules\material.md](modules\material.md) |
| property | Section properties | [modules\property.md](modules\property.md) |
| mesh | Meshing operations | [modules\mesh.md](modules\mesh.md) |
| step | Analysis step types | [modules\step.md](modules\step.md) |
| load | Load definitions | [modules\load.md](modules\load.md) |
| bc | Boundary conditions | [modules\bc.md](modules\bc.md) |
| interaction | Contact and connectors | [modules\interaction.md](modules\interaction.md) |
| amplitude | Time-varying definitions | [modules\amplitude.md](modules\amplitude.md) |
| field | Initial/predefined fields | [modules\field.md](modules\field.md) |
| output | Output requests | [modules\output.md](modules\output.md) |
| optimization | Tosca optimization | [modules\optimization.md](modules\optimization.md) |
| job | Job management | [modules\job.md](modules\job.md) |

## Usage

Reference these docs from skill files:
```markdown
For detailed API, see:
- [Material API](modules/material.md)
- [Step API](modules/step.md)
```

Search with grep:
```bash
grep -r "Elastic" .claude/docs/abaqus-api/
```

## Updating

Re-run the download script:
```bash
uv run .claude/skills/abaqus-docs/scripts/download_abqpy_docs.py --force
```
