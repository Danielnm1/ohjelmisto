import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# 1) Table of angles (degrees -> radians) and unit circle marking
degrees = np.array([30, 45, 60, 90, 120, 150, 180, 270])
radians = np.deg2rad(degrees)
table = pd.DataFrame({'degrees': degrees, 'radians': radians})
print(table.to_string(index=False))


fig1, ax1 = plt.subplots(figsize=(6,6))
circle = plt.Circle((0,0),1, fill=False, linewidth=2)
ax1.add_patch(circle)
ax1.set_aspect('equal', 'box')
ax1.axhline(0, color='gray', linewidth=1)
ax1.axvline(0, color='gray', linewidth=1)

from fractions import Fraction
for d, r in zip(degrees, radians):
    x = np.cos(r)
    y = np.sin(r)
    ax1.scatter([x],[y], s=80)
    frac = r / pi
    fr = Fraction(frac).limit_denominator(12)
    label = f"{d}°\n"
    if abs(fr - frac) < 1e-8:
        if fr.numerator == 0:
            label += "0"
        elif fr.numerator == fr.denominator:
            label += "π"
        else:
            if fr.denominator == 1:
                label += f"{fr.numerator}π"
            else:
                label += f"{fr.numerator}π/{fr.denominator}"
    else:
        label += f"{r:.3f}"
    ax1.annotate(label, xy=(x,y), xytext=(15,10), textcoords='offset points',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.3"))
ax1.set_xlim(-1.3, 1.3)
ax1.set_ylim(-1.3, 1.3)
ax1.set_title("Unit circle — marked angles")
plt.show()

# 2) Trig curves with modified figure size and styles over -3π..3π (width tripled)
X = np.linspace(-3*pi, 3*pi, 1000)
C = np.cos(X)
S = np.sin(X)

fig2, ax2 = plt.subplots(figsize=(19.2, 4.8))  # width tripled from default 6.4
ax2.plot(X, C, label='cos(x)', color='tab:blue', linestyle='-', linewidth=2)
ax2.plot(X, S, label='sin(x)', color='tab:orange', linestyle='--', linewidth=2)
ax2.plot(X, 0.5*np.sin(0.5*X)+0.2, label='0.5*sin(0.5x)+0.2', color='tab:green', linestyle=':')

ax2.set_xlim(-3*pi, 3*pi)
ax2.set_ylim(-1.5, 1.5)
ax2.set_title("Trig functions from -3π to 3π")
ax2.legend()

# 3) π-style ticks on x-axis
xticks = np.array([-3*pi, -2*pi, -1.5*pi, -1*pi, -0.5*pi, 0, 0.5*pi, 1*pi, 1.5*pi, 2*pi, 3*pi])
xticks = np.unique(xticks)

def pi_label(x):
    frac = x / pi
    fr = Fraction(frac).limit_denominator(6)
    if fr.numerator == 0:
        return "0"
    if fr.denominator == 1:
        if fr.numerator == 1:
            return "π"
        elif fr.numerator == -1:
            return "-π"
        else:
            return f"{fr.numerator}π"
    if fr.denominator == 2:
        if fr.numerator == 1:
            return "π/2"
        elif fr.numerator == -1:
            return "-π/2"
        else:
            return f"{fr.numerator}π/2"
    return f"{fr.numerator}π/{fr.denominator}"

labels = [pi_label(x) for x in xticks]
ax2.set_xticks(xticks)
ax2.set_xticklabels(labels)
ax2.grid(True, which='major', alpha=0.4)
ax2.minorticks_on()
plt.show()
