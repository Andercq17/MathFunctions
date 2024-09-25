from sympy import fourier_series, pi, plot 
from sympy.abc import x

f = x**2 # Function
s = fourier_series(f, (x, -pi, pi))
s1 = s.truncate(n = 1)
s2 = s.truncate(n = 2)
s3 = s.truncate(n = 5)
p = plot(f, s1, s2, s3, (x, -pi, pi), show = True, legend=True)
