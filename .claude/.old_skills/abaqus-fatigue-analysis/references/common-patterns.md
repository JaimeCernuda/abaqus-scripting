# Common Fatigue Patterns

## Constant Amplitude Loading

```python
# 1. Static analysis with unit load
# 2. Scale stress by load amplitude
# 3. Apply S-N curve

def constant_amplitude_life(stress_max, stress_min, sn_func, S_u=None):
    """Calculate fatigue life for constant amplitude loading.

    Args:
        stress_max: Maximum stress (MPa)
        stress_min: Minimum stress (MPa)
        sn_func: S-N curve function (amplitude -> cycles)
        S_u: Ultimate strength for mean stress correction (optional)

    Returns:
        Predicted cycles to failure
    """
    S_a = (stress_max - stress_min) / 2  # Amplitude
    S_m = (stress_max + stress_min) / 2  # Mean

    # Apply mean stress correction if ultimate strength provided
    if S_u is not None and S_m > 0:
        S_a = S_a / (1 - S_m / S_u)  # Goodman

    return sn_func(S_a)
```

## Variable Amplitude (Palmgren-Miner)

```python
# Palmgren-Miner damage accumulation
# D = sum(n_i / N_i)
# Failure when D >= 1.0

def palmgren_miner_damage(stress_cycle_pairs, sn_func):
    """Calculate cumulative damage using Palmgren-Miner rule.

    Args:
        stress_cycle_pairs: List of (stress_amplitude, cycle_count)
        sn_func: Function returning life for given amplitude

    Returns:
        Cumulative damage ratio (failure at D >= 1.0)
    """
    total_damage = 0
    for S_a, n_i in stress_cycle_pairs:
        N_i = sn_func(S_a)  # Life from S-N curve
        if N_i > 0 and N_i != float('inf'):
            total_damage += n_i / N_i

    return total_damage

# Example usage
cycles = [
    (200, 1000),   # 1000 cycles at 200 MPa
    (150, 5000),   # 5000 cycles at 150 MPa
    (100, 50000),  # 50000 cycles at 100 MPa
]

D = palmgren_miner_damage(cycles, sn_fatigue_life)
if D >= 1.0:
    print(f"Fatigue failure expected (D = {D:.3f})")
else:
    print(f"Component is safe (D = {D:.3f})")
```

## Variable Amplitude (Rainflow Counting)

```python
# Use rainflow counting library for complex load histories
# pip install fatpack (external to Abaqus, run separately)

# Example with fatpack library
import fatpack

# stress_history = array of stress values over time
cycles = fatpack.find_rainflow_ranges(stress_history)

# Extract cycle ranges and counts
ranges, counts = fatpack.find_rainflow_matrix(stress_history)

# Calculate damage
for range_val, count in zip(ranges, counts):
    S_a = range_val / 2  # Range to amplitude
    N = sn_curve(S_a)
    damage += count / N
```

## Mean Stress Correction Methods

```python
def mean_stress_correction(S_a, S_m, S_u, method='goodman'):
    """Apply mean stress correction to get equivalent fully-reversed amplitude.

    Args:
        S_a: Alternating stress amplitude (MPa)
        S_m: Mean stress (MPa)
        S_u: Ultimate tensile strength (MPa)
        method: 'goodman', 'gerber', or 'soderberg'

    Returns:
        Equivalent fully-reversed stress amplitude
    """
    S_y = 0.9 * S_u  # Approximate yield (use actual if known)

    if method == 'goodman':
        # Conservative for tensile mean stress
        # S_a / S_ar + S_m / S_u = 1
        return S_a / (1 - S_m / S_u)

    elif method == 'gerber':
        # Less conservative, parabolic
        # S_a / S_ar + (S_m / S_u)^2 = 1
        return S_a / (1 - (S_m / S_u) ** 2)

    elif method == 'soderberg':
        # Very conservative, uses yield strength
        # S_a / S_ar + S_m / S_y = 1
        return S_a / (1 - S_m / S_y)

    else:
        raise ValueError(f"Unknown method: {method}")


# Example
S_a = 100    # Alternating stress (MPa)
S_m = 50     # Mean stress (MPa)
S_u = 500    # Ultimate strength (MPa)

S_eq_goodman = mean_stress_correction(S_a, S_m, S_u, 'goodman')
S_eq_gerber = mean_stress_correction(S_a, S_m, S_u, 'gerber')

print(f"Goodman equivalent: {S_eq_goodman:.1f} MPa")
print(f"Gerber equivalent: {S_eq_gerber:.1f} MPa")
```

## Smith-Watson-Topper (SWT) for Strain-Life

```python
def swt_parameter(epsilon_a, sigma_max, E):
    """Calculate SWT parameter for mean stress effects in strain-life.

    SWT = sqrt(sigma_max * epsilon_a * E)

    Args:
        epsilon_a: Strain amplitude
        sigma_max: Maximum stress (MPa)
        E: Elastic modulus (MPa)

    Returns:
        SWT parameter
    """
    if sigma_max <= 0:
        return 0  # No tensile stress, no fatigue damage

    return (sigma_max * epsilon_a * E) ** 0.5


# SWT life prediction
def swt_life(epsilon_a, sigma_max, Sf_prime, ef_prime, b, c, E):
    """Predict life using SWT approach.

    sigma_max * epsilon_a = (Sf'^2/E) * (2Nf)^(2b) + Sf' * ef' * (2Nf)^(b+c)
    """
    # Numerical solution needed - iterate to find Nf
    pass
```

## Multiaxial Fatigue (Critical Plane)

```python
def critical_plane_search(stress_tensor_history, num_angles=36):
    """Search for critical plane in multiaxial fatigue.

    Evaluates shear stress and normal stress on all planes
    to find the most damaging orientation.
    """
    import numpy as np

    max_damage = 0
    critical_plane = None

    for theta in np.linspace(0, 180, num_angles):
        for phi in np.linspace(0, 360, num_angles):
            # Calculate stress on plane defined by (theta, phi)
            # ... (transform stress tensor to plane)
            # Calculate damage parameter
            # Track maximum
            pass

    return critical_plane, max_damage
```

## Factor of Safety

```python
def fatigue_factor_of_safety(S_a, S_m, S_e, S_u, method='goodman'):
    """Calculate fatigue factor of safety.

    Args:
        S_a: Alternating stress amplitude
        S_m: Mean stress
        S_e: Endurance limit (fully reversed)
        S_u: Ultimate strength
        method: 'goodman' or 'gerber'

    Returns:
        Factor of safety (n > 1 is safe)
    """
    if method == 'goodman':
        # Modified Goodman line
        n = 1 / (S_a / S_e + S_m / S_u)
    elif method == 'gerber':
        # Gerber parabola
        n = 0.5 * (S_u / S_m) ** 2 * (S_a / S_e) * (
            -1 + (1 + (2 * S_m * S_e / (S_u * S_a)) ** 2) ** 0.5
        )

    return n
```
