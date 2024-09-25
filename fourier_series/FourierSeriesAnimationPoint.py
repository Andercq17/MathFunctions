from sympy import *
from sympy.abc import x
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Function
f = x**2
s = fourier_series(f, (x, -pi, pi))
s1 = s.truncate(n=7)
x_vals = np.linspace(-np.pi, np.pi, 400)
s1_vals = np.array([float(s1.subs(x, val).evalf()) for val in x_vals])
fig, ax = plt.subplots()
ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(min(s1_vals) - 1, max(s1_vals) + 1)
point, = ax.plot([], [], 'bo')
def update(frame):
    point.set_data([x_vals[frame]], [s1_vals[frame]])
    return point,
ani = animation.FuncAnimation(fig, update, frames=len(x_vals), interval=50, repeat=False)
plt.show()
