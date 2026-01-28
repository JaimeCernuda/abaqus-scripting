---
name: abaqus-docs
description: Download and manage abqpy API documentation for offline reference. Use when setting up the project or needing to refresh documentation.
allowed-tools:
  - Read
  - Write
  - Bash(uv:*)
  - Bash(python:*)
---

# Abaqus Documentation Downloader

## When to Use This Skill

**USE when you need to:**
- Set up API documentation for a new project
- Refresh outdated local documentation
- Access offline API reference
- Look up specific Abaqus Python API methods

**Do NOT use for:**
- Learning Abaqus concepts (use other skills for guidance)
- Running analyses → use workflow skills
- Checking syntax for specific modules → read the downloaded docs directly

## What Gets Downloaded

The script crawls the abqpy documentation and extracts:

| Module | Content |
|--------|---------|
| mdb | Model database operations |
| odb | Output database access |
| part | Part creation and features |
| sketcher | 2D sketch operations |
| assembly | Instance and assembly |
| material | Material definitions |
| property | Section properties |
| mesh | Meshing operations |
| step | Analysis step types |
| load | Load definitions |
| bc | Boundary conditions |
| interaction | Contact and connectors |
| amplitude | Time-varying definitions |
| field | Initial/predefined fields |
| output | Output requests |
| optimization | Tosca optimization |
| job | Job management |

## Usage

### Download Documentation
```bash
uv run .claude/skills/abaqus-docs/scripts/download_abqpy_docs.py
```

### Force Refresh
```bash
uv run .claude/skills/abaqus-docs/scripts/download_abqpy_docs.py --force
```

## Output Location

Documentation is saved to:
```
.claude/docs/abaqus-api/
├── README.md           # Index and usage
├── index.json          # Structured index
└── modules/
    ├── mdb.md
    ├── odb.md
    ├── part.md
    └── ...
```

## Dependencies

Install with:
```bash
uv add crawl4ai httpx beautifulsoup4 markdownify
```

## Source URLs

- Main documentation: https://hailin.wang/abqpy/en/2025/reference/
- GitHub: https://github.com/haiiliin/abqpy
