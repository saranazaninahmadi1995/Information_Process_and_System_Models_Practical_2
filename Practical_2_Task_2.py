"""Practical work 2, variant 1: solve the finite-difference system."""
import numpy as np

# Coefficients of y1, y2 and y3 in the three equations.
coefficients = [
    [-13 / 7, 1, 0],
    [0.905, -1.875, 1],
    [0, -30, 32]
]

# Right sides. The first entry is an exact fraction.
right_sides = [-30691 / 70000, 0.016, 2.14]

solution = np.linalg.solve(coefficients, right_sides)

x_points = [0.7, 0.8, 0.9, 1.0]
y_points = [0.51, solution[0], solution[1], solution[2]]

for i in range(4):
    print(f"x = {x_points[i]:.1f}, y = {y_points[i]:.8f}")
