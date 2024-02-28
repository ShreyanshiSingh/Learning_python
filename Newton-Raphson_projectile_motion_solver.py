

# This code implements the Newton-Raphson method for solving a system of
# Nonlinear equations. The specific system of equations represents the solution of a projectile motion problem with air resistance.
# The Newton-Raphson method is an iterative numerical technique used to find the roots of a real-valued function or solutions to a system of nonlinear equations.

###########################################################################################################################################

#importing libraries
import numpy as np

# Given constants for the projectile motion problem
g = 9.8
v0 = 100.0
theta = np.pi/3
d = 789.3540333394579  

# System of nonlinear equations representing the projectile motion with air resistance
def f(x):
    return np.array([x[0] - (1 - np.exp(-x[0]*x[1]))*(g + v0*x[1]*np.sin(theta))/g/x[1],
                     -d + (1 - np.exp(-x[0]*x[1]))*v0*np.cos(theta)/x[1]])

# Jacobian matrix of the system
def j(x):
    return np.array([[1 - np.exp(-x[0]*x[1])*(g + v0*x[1]*np.sin(theta))/g,
                     (1 - np.exp(-x[0]*x[1])*(g + g*x[0]*x[1] + v0*x[0]*np.power(x[1],2)*np.sin(theta))/g)/x[1]*np.power(x[1], -2.0)],
                     [np.exp(-x[0]*x[1])*v0*np.cos(theta),
                      np.exp(-x[0]*x[1])*v0*(-1.0 + np.exp(x[0]*x[1]) - x[0]*x[1])*np.cos(theta)*np.power(x[1], -2.0)]])

# Newton-Raphson method for solving the system of equations
def NewtonRaphsonSystem(f, j, x, tol=1e-9, itmax=200):
    fx = f(x)
    jx = j(x)
    h = np.linalg.solve(jx, fx)
    hnorm = np.linalg.norm(h, ord=2)  # l2 norm of vector
    i = 0
    while abs(hnorm) > tol and i < itmax:
        fx = f(x)
        jx = j(x)
        h = np.linalg.solve(jx, fx)
        x = x - h
        fx = f(x)
        fnorm = np.linalg.norm(fx, ord=2)
        i += 1
        print('Iterations: ', i, '   ', 'Value: ', x)
    return x

# Initial guess for the solution
x = NewtonRaphsonSystem(f, j, x=np.array([14.5, 0.02]))

# Display the final solution
print(' ')
print(' x =           ', x)
