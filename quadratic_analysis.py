# This code illustrates the graphical representation of a quadratic function,
# calculates its roots using the quadratic formula, and demonstrates the
# iterative process of finding a root using the Newton-Raphson method.

####################################################################################################################

import numpy as np
import matplotlib.pyplot as plt

# Coefficients of the quadratic function: f(x) = ax^2 + bx + c
a = 1.0
b = -3.0
c = 2.0

# Define the quadratic function
def f(x):
    return a * x**2 + b * x + c

# Generate x values for plotting the function
x_values = np.arange(0, 3.1, 0.1)

# Plot the quadratic function
plt.plot(x_values, f(x_values))
plt.axhline(y=0.0, color='r', linestyle='-')  # Horizontal line at y=0
plt.xlim([0, 3])
plt.ylim([-1, 3])
plt.show()

# Calculate the roots using the quadratic formula
r1 = (-b + np.sqrt(b**2 - 4.0 * a * c)) / (2.0 * a)
r2 = (-b - np.sqrt(b**2 - 4.0 * a * c)) / (2.0 * a)

# Display the roots
print('r1 = ', r1, 'and', 'r2 = ', r2)
print(' ')

# Newton-Raphson method for iterative root-finding
x = 4.0
print(x)

# Iteratively refine the root approximation
for k in np.arange(1, 10, 1):
    x = x - (a * x**2 + b * x + c) / (2 * a * x + b)
    print(k, '  ', x)

print(' ')
