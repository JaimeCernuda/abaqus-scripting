# Common Amplitude Patterns

## Linear Ramp (0 to 100%)
```python
model.TabularAmplitude(name='Ramp', data=((0.0, 0.0), (1.0, 1.0)))
```
Most common pattern - load increases linearly from zero to full magnitude.

## Step Function (instant on)
```python
model.TabularAmplitude(name='Step', data=((0.0, 1.0), (1.0, 1.0)))
```
Full load applied instantly at start. May cause convergence issues in dynamics.

## Triangular Pulse
```python
model.TabularAmplitude(name='Pulse', data=(
    (0.0, 0.0), (0.5, 1.0), (1.0, 0.0)
))
```
Load ramps up to peak, then back down. Good for impact approximation.

## Sinusoidal (1 Hz)
```python
model.PeriodicAmplitude(name='Sine', frequency=1.0, start=0.0,
                        a_0=0.0, data=((0.0, 1.0),))
```
Pure sine wave at specified frequency.

## Load-Unload Cycle
```python
model.TabularAmplitude(name='Cycle', data=(
    (0.0, 0.0), (0.25, 1.0), (0.5, 0.0), (0.75, -1.0), (1.0, 0.0)
))
```
Full cycle with tension and compression. Good for fatigue loading.

## Smooth Ramp (No Discontinuity)
```python
model.SmoothStepAmplitude(name='SmoothRamp', data=(
    (0.0, 0.0), (1.0, 1.0)
))
```
Smooth transition with zero derivatives at endpoints. Best for dynamics.

## Two-Stage Ramp
```python
model.TabularAmplitude(name='TwoStage', data=(
    (0.0, 0.0), (0.3, 0.5), (1.0, 1.0)
))
```
Fast initial ramp, slower final approach.

## Hold at Peak
```python
model.TabularAmplitude(name='RampHold', data=(
    (0.0, 0.0), (0.5, 1.0), (1.0, 1.0)
))
```
Ramp up to peak, hold constant.

## Impulse (Short Duration)
```python
model.TabularAmplitude(name='Impulse', data=(
    (0.0, 0.0), (0.001, 1.0), (0.002, 0.0)
))
```
Very short pulse for impact simulation.

## Exponential Decay
```python
model.DecayAmplitude(name='Decay', initial=1.0, maximum=1.0,
                     start=0.0, decayTime=0.5)
```
Exponential decay from initial value.

## Multiple Cycles
```python
# 3 complete cycles over step time
import math
n_cycles = 3
n_points = 50
data = tuple((i/n_points, math.sin(2*math.pi*n_cycles*i/n_points))
             for i in range(n_points+1))
model.TabularAmplitude(name='MultiCycle', data=data)
```
Multiple oscillations using tabular data.

## Chirp (Frequency Sweep)
```python
# Linearly increasing frequency
import math
n_points = 100
f_start, f_end = 1.0, 10.0  # Hz
data = tuple((t, math.sin(2*math.pi*(f_start + (f_end-f_start)*t/2)*t))
             for t in [i/n_points for i in range(n_points+1)])
model.TabularAmplitude(name='Chirp', data=data)
```
Frequency sweep for vibration testing.
