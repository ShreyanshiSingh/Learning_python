# This code defines a function and a trapezoidal integration method to approximate the definite integral 
# of the given function over a specified interval. It then compares the result with the true value.

##################################################################################################################################

# Importing necessary libraries
import numpy as np

# Define the function to be integrated
def function(x):
    return np.power(x, 3) * np.exp(-x)

# Define the trapezoidal integration method
def Trapezoidal(function, a, b, n):
    # Calculate the step size
    h = (b - a) / n
    s = 0.0

    # Summing up the function values at each step
    for i in range(1, n):
        s = s + function(a + i * h)

    # Trapezoidal rule formula
    result = (h / 2) * (function(a) + 2.0 * s + function(b))
    return result

# Define the interval [a, b] and the number of subintervals (n)
a = 0.0
b = 1.0
n = 30

# Calculate the integral using the Trapezoidal method
I = Trapezoidal(function, a, b, n)

# True value of the integral for comparison
I_true = 6.0 - 16.0 / np.exp(1.0)

# Display the results
print(" I (Trapezoidal)             = ", I)  # Result of the trapezoidal integration
print(" I (True)                    = ", I_true)  # True value of the integral
print("|I (Trapezoidal) - I (True)| = ", np.abs(I - I_true))  # Absolute error between the approximated and true values
print('')
