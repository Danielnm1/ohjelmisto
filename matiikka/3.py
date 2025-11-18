import numpy as np

# Degree values
angles_deg = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
# Convert all to radians
angles_rad = np.radians(angles_deg)

print("3. Asteet → radiaanit (taulukko):")
for deg, rad in zip(angles_deg, angles_rad):
    print(f"{deg:>3}° = {rad:.6f} rad")
