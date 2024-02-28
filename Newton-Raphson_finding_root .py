
# The provided code implements two variations of the Newton-Raphson method for finding the root of a function.
# This code defines two functions, NewtonRaphson and NewtonRaphsonRepeatedRoot, which implement the Newton-Raphson method for finding simple roots and repeated roots, respectively.
# The given function f(x) and its derivatives are used in the root-finding process. 
# The code then prints out the iterations and the resulting root approximation, along with the absolute error compared to the true root value.

##############################################################################################################################################


import numpy as np

# Function implementing the Newton-Raphson method for finding a simple root
def NewtonRaphson(f, dfdx, x, tol=1e-9):
    h = f(x) / dfdx(x)
    i = 0
    while abs(h) >= tol:
        h = f(x) / dfdx(x)
        x = x - h
        i += 1
        print('Iterations: ', i, '   ', 'Value: ', x)
    return x

# Function implementing the Newton-Raphson method for finding a repeated root
def NewtonRaphsonRepeatedRoot(f, dfdx, df2dx2, x, tol=1e-9):
    h = f(x) / dfdx(x)
    i = 0
    while abs(h) >= tol:
        h = f(x)*dfdx(x) / (np.power(dfdx(x),2) - f(x)*df2dx2(x))
        x = x - h
        i += 1
        print('Iterations: ', i, '   ', 'Value: ', x)
    return x

# Define the function, its first derivative, and its second derivative
def f(x):
    return np.power(x - 1, 4)*(x - 3)

def dfdx(x):
    return np.power(x - 1, 3)*(5*x - 13)

def df2dx2(x):
    return 4*np.power(x - 1, 2)*(5*x - 11)

# Initial guess
x0 = 0.4

# Perform Newton-Raphson iterations for finding a simple root
x = NewtonRaphson(f, dfdx, x0)

# Perform Newton-Raphson iterations for finding a repeated root
x = NewtonRaphsonRepeatedRoot(f, dfdx, df2dx2, x0)

# True root for comparison
xtrue = 1.0
print(' ')
print(' x =           ', format(x, '.16g'))
print(' xtrue =       ', format(xtrue, '.16g'))
print('|xtrue - x| =  ', np.abs(x - xtrue))
