import numpy as np
import matplotlib.pyplot as plt

# Parabolic Tc model parameters
Tc_max = 92.0  # K
delta_opt = 0.07
a = 500.0  # K^{-1} (standard)
delta_range = np.linspace(0.0, 0.5, 100)  # Doping range

# Standard model
def tc_parabolic(delta, Tc_max, delta_opt, a):
    return Tc_max - a * (delta - delta_opt)**2

# Variants
def tc_noise(tc, std=2.0):
    return tc + np.random.normal(0, std, len(tc))  # Gaussian inhomogeneity

def tc_broader_dome(delta, Tc_max, delta_opt, a=300):
    return tc_parabolic(delta, Tc_max, delta_opt, a)  # Less sharp

def tc_inhomogeneous(delta, delta_std=0.05):
    delta_noisy = delta + np.random.normal(0, delta_std, len(delta))
    return tc_parabolic(delta_noisy, Tc_max, delta_opt, a)

# Run simulations
tc_standard = tc_parabolic(delta_range, Tc_max, delta_opt, a)
tc_noisy = tc_noise(tc_standard)
tc_broad = tc_broader_dome(delta_range, Tc_max, delta_opt)
tc_inhom = tc_inhomogeneous(delta_range)

# Sample values (first 5 points)
print("Sample Tc values (standard):", tc_standard[:5])
print("Mean Tc across variants (first 5 points):", np.mean([tc_standard[:5], tc_noisy[:5], tc_broad[:5], tc_inhom[:5]], axis=0))

# Plot main model
plt.figure(figsize=(8, 6))
plt.plot(delta_range, tc_standard, label='Standard parabolic')
plt.scatter([0.0, 0.07, 0.20, 0.5], [89.55, 92.0, 83.55, 0.0], color='red')
plt.xlabel('Doping δ')
plt.ylabel('Tc (K)')
plt.title('YBCO Tc vs Doping')
plt.legend()
plt.grid(True)
plt.savefig('ybco_tc_model.png')
plt.close()

# Plot sensitivity with variants
plt.figure(figsize=(8, 6))
plt.plot(delta_range, tc_standard, label='Standard (a=500)')
plt.plot(delta_range, tc_noisy, label='With noise (±2 K)')
plt.plot(delta_range, tc_broad, label='Broader dome (a=300)')
plt.plot(delta_range, tc_inhom, label='Inhomogeneous doping (δ_std=0.05)')
plt.xlabel('Doping δ')
plt.ylabel('Tc (K)')
plt.title('YBCO Tc Model with Mathematical Variants')
plt.legend()
plt.grid(True)
plt.savefig('ybco_tc_sensitivity.png')
plt.close()

print("Plots saved: ybco_tc_model.png and ybco_tc_sensitivity.png")

# Simple pseudogap model (antinodal gap)
k = np.linspace(0, np.pi, 100)  # Momentum along (π,0) to (0,π)
E_gap = 50 * np.sin(k) ** 2  # meV, max at antinodes
plt.plot(k, E_gap, label='Pseudogap (antinodal)')
plt.xlabel('Momentum k (rad)')
plt.ylabel('Gap energy (meV)')
plt.title('YBCO Pseudogap Model')
plt.legend()
plt.savefig('ybco_pseudogap.png')
