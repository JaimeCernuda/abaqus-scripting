# Broken Abaqus 2025 Optimization API Calls

These two API calls do not work in Abaqus 2025 noGUI mode. Both were tested systematically with multiple variations. The root cause is the same: the prototype job is never registered in the C++ optimization subsystem's internal map.

## 8c: writeParAndInputFiles()

**Error**: `KeyError: 'Block_Proto'`

Tested 4 variations, all fail identically:
- **A**: Save .cae first, then create OptimizationProcess, then writeParAndInputFiles()
- **B**: Create OptimizationProcess first, then save .cae, then writeParAndInputFiles()
- **C**: writeInput() on proto job first, then OptimizationProcess, then writeParAndInputFiles()
- **D**: Run full FEA first (submit + waitForCompletion), then OptimizationProcess, then writeParAndInputFiles()

All produce:
```
KeyError: 'Block_Proto'
  File "exp8c_write_par.py", line 181
    optProcess.writeParAndInputFiles()
```

See `slurm_output.txt` for complete output showing all 4 variations failing.

## 8d: OptimizationProcess.submit()

**Error**: Signal 11 (SEGV) — null pointer dereference

The process segfaults immediately on `submit()`, before any optimization runs. The crash dump callstack:

```
1) cow_Virtual<ajbC_Job>::Copy           ← null pointer dereference here
2) cow_COW<ajbC_Job>::Get
3) mdl_MapOfCowsRepository<...>::Get     ← job lookup in internal map fails
4) ajbK_OptimizationIntObj::Submit       ← submit() entry point
```

The segfault kills the entire Abaqus process, so no Python-level exception handling is possible. Only Variation A ran; the crash terminated the process before Variations B-E could execute.

See `crash_dump.txt` for the full exception file and `slurm_output.txt` for SLURM output.

## Root Cause

Both failures trace to the same issue: `mdb.OptimizationProcess()` creates a Python-level object, but the underlying C++ `mdl_MapOfCowsRepository` never registers the prototype job. When `writeParAndInputFiles()` or `submit()` tries to look up the job by name, it either:
- Gets a KeyError (Python catches the failed lookup — 8c)
- Gets a null pointer and dereferences it (C++ doesn't check — 8d)

This appears to be a noGUI-specific bug. The optimization subsystem may depend on GUI initialization that doesn't happen in noGUI mode.
