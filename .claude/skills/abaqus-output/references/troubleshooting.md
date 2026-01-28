# Output Troubleshooting

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| Variable not in ODB | Not requested | Add to FieldOutputRequest variables |
| ODB too large | Too much output | Increase frequency, reduce variables |
| "Region not found" | Set doesn't exist | Create set before output request |
| History output empty | Wrong region type | Use node set for displacements |
| "Variable not available" | Wrong element type or analysis | Check element/analysis compatibility |
| "Invalid variable" | Typo in variable name | Check spelling (case-sensitive) |
| No contact output | Contact not defined | Define contact interaction first |
| "Step not found" | Wrong step name | Verify step name matches exactly |

## Variable Compatibility

### Element Type Restrictions
| Variable | Requires |
|----------|----------|
| S, E | Stress/strain elements (not rigid) |
| CSTRESS | Contact pairs defined |
| HFL | Heat transfer elements |
| PEEQ | Plasticity in material |

### Analysis Type Requirements
| Variable | Analysis Type |
|----------|---------------|
| V, A | Dynamic analysis |
| NT, HFL | Heat transfer or coupled |
| CSTRESS | Contact defined |

## ODB Size Management

### Problem: ODB file too large

**Solutions (in order of impact):**

1. **Reduce output frequency**
   ```python
   frequency=10  # Every 10th increment instead of every 1
   ```

2. **Use numIntervals instead of frequency**
   ```python
   numIntervals=20  # Exactly 20 frames total
   ```

3. **Reduce variables**
   ```python
   variables=('S', 'U')  # Only what you need
   ```

4. **Output only specific regions**
   ```python
   region=assembly.sets['CriticalArea']
   ```

5. **Delete default outputs**
   ```python
   del model.fieldOutputRequests['F-Output-1']
   ```

## History Output Issues

### Problem: History output shows nothing

**Check these:**
1. Region is a node set (not element set) for nodal variables
2. Set exists before HistoryOutputRequest is created
3. Variable is appropriate for region type
4. Step name matches exactly

### Problem: Can't find history data in ODB

**Solutions:**
- History data is at integration points or nodes, not elements
- Use `odb.steps['Step'].historyRegions` to list available regions
- Check if the node/element set was meshed

## Restart Issues

### Problem: Can't restart analysis

**Check these:**
1. RestartRequest was defined in original analysis
2. Restart files (.res, .sta) exist
3. Job was not deleted after original run
