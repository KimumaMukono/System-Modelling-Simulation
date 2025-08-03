import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
frequency = 1e9  # 1 GHz
wavelength = 3e8 / frequency  # Wavelength in meters
k = 2 * np.pi / wavelength  # Wave number
length = wavelength / 2  # Dipole length (half-wavelength dipole)

# Define angular grid for 3D pattern
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

# Dipole antenna radiation pattern (normalized power)
# For a half-wave dipole, the pattern is proportional to (sin(theta))^2
def dipole_pattern(theta):
    # Avoid division by zero at theta = 0 or pi
    with np.errstate(divide='ignore', invalid='ignore'):
        pattern = (np.cos(np.pi / 2 * np.cos(theta)) / np.sin(theta))**2
        pattern = np.nan_to_num(pattern, nan=0.0, posinf=0.0, neginf=0.0)
    return pattern

# Calculate radiation pattern
pattern = dipole_pattern(theta)

# Convert to Cartesian coordinates for 3D plotting
X = pattern * np.sin(theta) * np.cos(phi)
Y = pattern * np.sin(theta) * np.sin(phi)
Z = pattern * np.cos(theta)

# Create 3D plot
fig = plt.figure(figsize=(12, 5))

# 3D surface plot
ax1 = fig.add_subplot(121, projection='3d')
surf = ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('3D Antenna Radiation Pattern')
fig.colorbar(surf, ax=ax1, label='Normalized Power')

# 2D polar plot (E-plane, phi=0)
ax2 = fig.add_subplot(122, projection='polar')
theta_2d = np.linspace(0, 2 * np.pi, 100)
pattern_2d = dipole_pattern(theta_2d)
ax2.plot(theta_2d, pattern_2d)
ax2.set_title('2D Radiation Pattern (E-plane)')
ax2.set_theta_zero_location('N')
ax2.set_theta_direction(-1)

plt.tight_layout()
plt.show()