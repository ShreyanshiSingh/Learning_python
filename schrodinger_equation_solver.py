
# This Python script deals with solving the Schrödinger equation for a given potential energy profile.
# It calculates energy levels, wavefunctions, and potential energy profiles for a particle in a piecewise-defined potential.

#####################################################################################################################################################################


# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Constants
mc2 = 0.511 * np.power(10.0, 6)  # Rest mass energy of the electron in eV
hcut2c2 = 197.3  # (h/2π)^2 * c^2 in eV

# Define the potential energy profile based on the chosen case
case = 1
if case == 1:
    V1 = 13.0
    V2 = 7.0
    L = 2.0
else:
    V1 = 13.0
    V2 = 13.0
    L = 2.0

a1 = np.power(2.0 * mc2 * V1 * np.power(hcut2c2, -2.0), 0.5)
a2 = np.power(2.0 * mc2 * V2 * np.power(hcut2c2, -2.0), 0.5)
b = a2 / a1

# Newton-Raphson method for finding roots of a function
def NewtonRaphson(f, df, x, tol=1e-9):
    h = f(x) / dfdx(x)
    i = 0
    while abs(h) >= tol:
        h = f(x) / dfdx(x)
        x = x - h
        i += 1
    return x

# Schrödinger equation functions
def f(x):
    return np.tan(a2 * L * np.power(x, 0.5)) - np.power(x, 0.5) * (
            b * np.power((1.0 - x), 0.5) + np.power((1.0 - np.power(b, 2) * x), 0.5)) * np.power(
        b * x - np.power(1.0 - x, 0.5) * np.power(1.0 - np.power(b, 2) * x, 0.5), -1.0)

def dfdx(x):
    u = np.power((1.0 - x), 0.5)
    v = np.power((1.0 - np.power(b, 2) * x), 0.5)
    w = np.power(x, 0.5)
    return (b * u + v + L * a2 * (
            -2.0 * b * (1.0 - x) * x + 2.0 * np.power(b, 3) * np.power(u, 2) * np.power(w, 4) + np.power(u, 3) * v + np.power(
        b, 2) * x * (2.0 * x - 1.0) * u * v) * np.power(np.cos(a2 * L * w), -2)) * np.power(
        2.0 * w * u * v * np.power(b * x - u * v, 2), -1)

def g(x, s):
    if x <= 0.0:
        return np.exp(a1 * np.power(1.0 - np.power(b, 2) * s, 0.5) * x)
    elif x >= L:
        return (
                (np.power(1.0 - np.power(b, 2) * s, 0.5) * np.power(s, -0.5) * np.power(b, -1) * np.sin(
                    a2 * np.power(s, 0.5) * L) + np.cos(a2 * np.power(s, 0.5) * L))) * np.exp(
            -a2 * np.power(1.0 - s, 0.5) * (x - L))
    else:
        return (
                np.power(1.0 - np.power(b, 2) * s, 0.5) * np.power(s, -0.5) * np.power(b, -1) * np.sin(
            a2 * np.power(s, 0.5) * x) + np.cos(a2 * np.power(s, 0.5) * x))

# Visualization of the potential energy profile
xpmin = -1.0
xpmax = 3.0
x = np.arange(0.0, 1.0, 0.0003)

# Chosen root points for visualization
if case == 1:
    xr = np.array([0.011858272825135843, 0.04740527655968007, 0.10655372748885153, 0.18914383953961159,
                   0.2949152637145596, 0.4234478771261506, 0.5740215798431181, 0.7451876122358929, 0.932313419269234])
else:
    xr = np.array([0.006505245037304427, 0.02601216549467455, 0.10390145764512826, 0.16216240291457718,
                   0.2331694186555868, 0.4127296320074679, 0.6400920247729884, 0.7697382968755168, 0.906499699281421])

yr = xr - xr

# Plotting the function and root points
plt.scatter(xr, yr, marker='*', color='red', s=200)
plt.scatter(0, 0, marker='*', color='black', s=200)
plt.axhline(y=0.0, color='k', linestyle='--')
plt.plot(x, f(x), linestyle='-', linewidth=3)
plt.axhline(y=0.0, color='k', linestyle='--')
plt.ylim([-5, 5])
plt.xlabel(r'$\xi$', size=20)
plt.ylabel('f(' + r'$\xi$' + ')', size=20)
plt.show()

# Calculate and visualize wavefunctions
s = []
c = 1
plt.axhline(y=0.0, color='k', linestyle='--')
for xi0 in [0.01, 0.04, 0.1, 0.19, 0.29, 0.42, 0.57, 0.74, 0.93]:
    print(' ')
    xi = NewtonRaphson(f, dfdx, xi0)
    print('Energy (n=' + str(c) + ')', format(xi * V2, '.4g'), 'eV')
    c = c + 1
    s.append(xi)
print(s)

vg = np.vectorize(g)
x = np.linspace(xpmin, xpmax, 10000)
plt.axhline(y=0.0, color='k', linestyle='--')
plt.axvline(x=0.0, color='k', linestyle='--')
plt.axvline(x=L, color='k', linestyle='--')
plt.xlabel(r'x in nm', size=20)
plt.ylabel(r'$\psi_n$(x)/$\psi_n$(x=0)', size=20)
n = 1
for sv in s:
    yv = vg(x, sv)
    plt.plot(x, yv, linestyle='-', linewidth=3, label='n = ' + str(n))
    n = n + 1
plt.legend(fontsize=10, loc="upper right")
plt.show()

# Visualize the potential energy profile
plt.hlines(0.0, xmin=0.0, xmax=L, color='k', linestyle='-', linewidth=3)
plt.vlines(0.0, ymin=0.0, ymax=V1, color='k', linestyle='-', linewidth=3)
plt.vlines(L, ymin=0.0, ymax=V2, color='k', linestyle='-', linewidth=3)
plt.hlines(V1, xmin=xpmin, xmax=0.0, color='k', linestyle='-', linewidth=3)
plt.hlines(V2, xmin=L, xmax=xpmax, color='k', linestyle='-', linewidth=3)

xv = np.linspace(0.0, L, 1000)
for sv in s:
    plt.plot(xv, np.ones(len(xv)) * sv * V2, linestyle='-', linewidth=3,
             label='E = ' + format(sv * V2, '.4g') + ' eV')
plt.xlabel(r'x in nm', size=15)
plt.ylabel(r'V(x) in eV', size=15)
plt.xlim(xpmin, xpmax)
plt.ylim(0.0, ((V1 % 5) + 0.2) * 5)
plt.legend(fontsize=10, loc="upper right")
plt.show()
