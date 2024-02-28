
# This Python script demonstrates the Bisection method for finding the root of a given function.
# The Bisection method is an iterative numerical technique that narrows down the root of a continuous function within a specified interval.
# Bisection Method:
#   - Requires an initial interval [x1, x2] with opposite signs for f(x1) and f(x2).
#   - Iteratively narrows down the interval by halving it.
#   - Converges to a root within the specified tolerance or after a set number of iterations.


####################################################################################################################################################

# load required libraries
import numpy as np

def Bisection(f, x1, x2, tol=1e-9):
    # Evaluate function values at the initial points
    f1 = f(x1)
    if f1 == 0:
        return x1
    f2 = f(x2)
    if f2 == 0:
        return x2
    
    # Check if the initial points bracket the root
    if np.sign(f1) == np.sign(f2):
        print('Root is not bracketed')
        return None
    
    # Maximum number of iterations
    n = 20
    print(n)

    # Bisection iterations
    for i in range(n): 
        x3 = 0.5 * (x1 + x2)
        f3 = f(x3)
        
        # Check if the root is found
        if f3 == 0: 
            return x3
        elif np.sign(f2) != np.sign(f3):
            x1 = x3
            f1 = f3
        else: 
            x2 = x3
            f2 = f3
        
        # Print iteration details
        print('Iterations: ', i, '   ', 'Value: ', format(x3, '.16g'))
    
    return x3

# Define the function for which the root is sought
def f(x):
    return x**2 - 2

# Apply the Bisection method to find the root in the interval [0.0, 2.0]
x = Bisection(f, 0.0, 2.0)

# True value of the root (square root of 2)
xtrue = np.power(2.0, 0.5)

# Print the results
print(' ')
print(' x =           ', format(x, '.16g')) # Approximate root obtained by the bisection method
print(' xtrue =       ', format(xtrue, '.16g')) # True root of the function
print('|xtrue - x| =  ', np.abs(x - xtrue)) # Absolute error between the true and approximate roots
