import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, sympify

# Define the symbols
x = symbols('x')

# Ask the user for the two functions
func1_input = input("Enter function 1 in terms of x: ")
func2_input = input("Enter function 2 in terms of x: ")

# Convert the input strings into sympy expressions
func1_sympy = sympify(func1_input)
func2_sympy = sympify(func2_input)

# Convert the sympy expressions into lambda functions that can be used with numpy and scipy
f1 = lambdify(x, func1_sympy, 'numpy')
f2 = lambdify(x, func2_sympy, 'numpy')

# Define the function representing the difference
def diff(x):
    return f1(x) - f2(x)

# Ask the user for the limits of integration
min_val = float(input("Enter the lower limit of integration: "))
max_val = float(input("Enter the upper limit of integration: "))

# Compute the integral
integral_value, error = spi.quad(diff, min_val, max_val)

# Ask the user for the number of decimal places
decimals = int(input("Enter the number of decimal places for the result: "))

print("The integral value is: ", integral_value)

# Generate x values
x = np.linspace(min_val, max_val, 1000)

# Generate y values for each function
y1 = f1(x)
y2 = f2(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=func1_input)
plt.plot(x, y2, label=func2_input)
plt.fill_between(x, y1, y2, where=(y1>y2), interpolate=True, alpha=0.3)

# Add a legend
plt.legend()

# Show the plot
plt.show()
