import numpy as np

# Given triangle sides (legs)
a = 1.6   # meters
b = 2.3   # meters

# Calculate the hypotenuse using NumPy's hypot function
c = np.hypot(a, b)

print("4. Suorakulmaisen kolmion hypotenuusa:")
print(f"Kateetit: a = {a} m, b = {b} m")
print(f"Hypotenuusa: c = {c:.3f} m")
