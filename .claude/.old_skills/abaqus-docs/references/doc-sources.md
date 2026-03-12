# Documentation Sources

## Primary Source
abqpy documentation: https://hailin.wang/abqpy/

GitHub repository: https://github.com/haiiliin/abqpy

## Official Dassault Documentation
https://help.3ds.com/2025/English/DSSIMULIA_Established/

Note: Official docs require license/subscription for full access.

## When to Re-download
- New Abaqus version released
- Missing module documentation
- Corrupted files
- Need updated API coverage

## Download Process
Documentation was downloaded using web scraping and markdown conversion.
Files are static and do not auto-update.

To refresh documentation:
```bash
uv run .claude/skills/abaqus-docs/scripts/download_abqpy_docs.py --force
```

## File Format
Each module file contains:
- Class definitions with signatures
- Method parameters and types
- Return value documentation
- Usage examples where available

## Version Compatibility
The abqpy documentation targets Abaqus 2025 API.
Most patterns are backward-compatible with Abaqus 2020+.
