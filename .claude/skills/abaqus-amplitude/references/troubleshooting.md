# Amplitude Troubleshooting

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| "Amplitude not found" | Typo in amplitude name | Check spelling matches exactly |
| "Time out of range" | Step time exceeds amplitude data | Extend amplitude data or use timeSpan=TOTAL |
| Sudden jumps in results | Discontinuous amplitude | Use SmoothStepAmplitude |
| Load doesn't vary | Forgot amplitude= parameter | Add amplitude='AmpName' to load |
| "Amplitude not monotonic in time" | Time values not increasing | Fix time sequence order |
| "Amplitude exceeds 1.0" | Misunderstanding purpose | Amplitude is a multiplier; adjust magnitude in load |
| Convergence issues | Step function or sudden change | Use smooth ramp or increase time resolution |

## Debugging Tips

### Verify Amplitude Exists
```python
# Check if amplitude is defined
print(model.amplitudes.keys())
```

### Check Amplitude Data
```python
amp = model.amplitudes['MyAmp']
print(amp.data)
```

### Visualize Amplitude
```python
import matplotlib.pyplot as plt
amp = model.amplitudes['MyAmp']
times = [d[0] for d in amp.data]
values = [d[1] for d in amp.data]
plt.plot(times, values)
plt.xlabel('Time')
plt.ylabel('Amplitude Factor')
plt.show()
```

## Best Practices

### For Static Analysis
- Use linear ramp to avoid sudden load application
- Ramp time should be long enough to avoid inertial effects

### For Dynamic Analysis
- Use SmoothStepAmplitude to avoid numerical shocks
- Ensure time increment is small enough to capture amplitude variations
- For explicit dynamics, avoid discontinuities

### For Multi-Step Analysis
- Consider timeSpan=TOTAL for continuous loading history
- Define separate amplitudes for different steps if needed

### Time Resolution
- Provide enough data points to capture the shape
- For sinusoidal: at least 20 points per cycle
- For sharp transitions: use more points near the transition

## Common Mistakes

1. **Forgetting to apply amplitude**: Defining amplitude but not referencing it in load/BC
2. **Wrong time span**: Using STEP when TOTAL is needed for multi-step
3. **Mixing up magnitude and amplitude**: Amplitude is multiplier, not the actual load value
4. **Time mismatch**: Amplitude time range doesn't cover the step duration
5. **Discontinuities in explicit dynamics**: Causes numerical instability
