# Amplitude API Quick Reference

## TabularAmplitude (most common)
```python
model.TabularAmplitude(
    name='AmpName',
    data=((time1, value1), (time2, value2), ...),
    timeSpan=STEP  # or TOTAL
)
```
- data: tuples of (time, amplitude_factor)
- amplitude_factor multiplies the load magnitude
- timeSpan=STEP: time relative to step start (default)
- timeSpan=TOTAL: time from analysis start

## SmoothStepAmplitude
```python
model.SmoothStepAmplitude(
    name='Smooth',
    data=((t1, a1), (t2, a2))
)
```
- Polynomial transition, no discontinuities
- Good for dynamics to avoid shocks
- First and second derivatives are zero at data points

## PeriodicAmplitude
```python
model.PeriodicAmplitude(
    name='Sine',
    frequency=10.0,  # Hz
    start=0.0,
    a_0=0.0,         # constant term
    data=((1.0, 0.0),)  # (A_n, B_n) Fourier coefficients
)
```
- Fourier series: a_0 + sum(A_n*cos + B_n*sin)
- data contains (A_n, B_n) coefficient pairs
- For pure sine: data=((0.0, 1.0),)
- For pure cosine: data=((1.0, 0.0),)

## DecayAmplitude
```python
model.DecayAmplitude(
    name='Decay',
    initial=1.0,
    maximum=1.0,
    start=0.0,
    decayTime=0.5  # time constant
)
```
- Exponential decay: A * exp(-t/decayTime)
- Useful for damped response or impact

## ModulatedAmplitude
```python
model.ModulatedAmplitude(
    name='Modulated',
    initial=0.0,
    magnitude=1.0,
    start=0.0,
    frequency1=10.0,  # carrier frequency
    frequency2=1.0    # modulation frequency
)
```
- Amplitude modulated wave
- Useful for complex vibration excitation

## Using Amplitudes
```python
# With concentrated force
model.ConcentratedForce(..., amplitude='AmpName')

# With pressure
model.Pressure(..., amplitude='AmpName')

# With displacement BC
model.DisplacementBC(..., amplitude='AmpName')

# With temperature BC
model.TemperatureBC(..., amplitude='AmpName')

# With surface traction
model.SurfaceTraction(..., amplitude='AmpName')
```

## Important Notes
- Amplitude is a **multiplier** applied to the load/BC magnitude
- Amplitude of 1.0 means 100% of specified magnitude
- Time values in data must be monotonically increasing
- For multi-step analyses, consider timeSpan=TOTAL
