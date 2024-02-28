

# Estimate the value of pi using a Monte Carlo simulation of points inside a circle.
# It generates 'p' random points in a square region and calculates the ratio of points falling inside a quarter circle to the total number of points. 
# This ratio is then used to estimate the value of pi.


################################################################################################################################

# Importing necessary libraries
import numpy as np
import random

# Taking user input for the number of iterations
p = input('Enter a number of iterations: ')
p = int(p)

# Initializing counters for points inside and outside the circle
t = 0
s = 0

# Generating random points and checking if they fall inside the circle
for i in range(p):
    x = random.uniform(-0.5, 0.5)
    y = random.uniform(-0.5, 0.5)
    
    # Checking if the point is inside the circle with radius 0.5
    if (x**2) + (y**2) <= 0.25:
        t = t + 1
    else:
        s = s + 1

# Printing the counts of points inside and outside the circle
print('Points inside the circle:', t)
print('Points outside the circle:', s)

# Estimating the value of pi using the ratio of points inside the circle to the total points
estimated_pi = (t / p) / 0.25

# Printing the estimated value of pi
print('Estimated value of pi:', estimated_pi)
