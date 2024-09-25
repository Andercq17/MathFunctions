import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from sympy import fourier_series, pi
from sympy.abc import x

f = x**3
s = fourier_series(f, (x, -pi, pi))
s1 = s.truncate(n=1)
s2 = s.truncate(n=2)
s3 = s.truncate(n=5)
x_vals = np.linspace(-np.pi, np.pi, 400)
s1_vals = np.array([float(s1.subs(x, val).evalf()) for val in x_vals])
s2_vals = np.array([float(s2.subs(x, val).evalf()) for val in x_vals])
s3_vals = np.array([float(s3.subs(x, val).evalf()) for val in x_vals])
fig, ax = plt.subplots()
ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(min(s3_vals) - 1, max(s3_vals) + 1)
line1, = ax.plot([], [], label="Truncación n=1", color='b')
line2, = ax.plot([], [], label="Truncación n=2", color='g')
line3, = ax.plot([], [], label="Truncación n=5", color='r')
ax.legend()
def update(frame):
    line1.set_data(x_vals[:frame], s1_vals[:frame])
    line2.set_data(x_vals[:frame], s2_vals[:frame])
    line3.set_data(x_vals[:frame], s3_vals[:frame])
    return line1, line2, line3
ani = animation.FuncAnimation(fig, update, frames=len(x_vals), interval=50, blit=True, repeat=False)
plt.show()
