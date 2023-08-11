import scipy.integrate as spi
import numpy as np
from sympy import symbols, lambdify, sympify

# Define the symbol
x = symbols('x')

# Ask the user for the function
func_input = input("Enter function in terms of x: ")

# Convert the input string into a sympy expression
func_sympy = sympify(func_input)

# Convert the sympy expression into a lambda function that can be used with numpy and scipy
f = lambdify(x, func_sympy, 'numpy')

# Define a safe dictionary with numpy constants that the user is allowed to use
safe_dict = {'np': np}

# Ask the user for the limits of integration and evaluate them using the safe dictionary
min_val = eval(input("Enter the lower limit of integration: "), {"__builtins__": None}, safe_dict)
max_val = eval(input("Enter the upper limit of integration: "), {"__builtins__": None}, safe_dict)

# Compute the integral
integral_value, error = spi.quad(f, min_val, max_val)

# Ask the user for the number of decimal places
decimals = int(input("Enter the number of decimal places for the result: "))

# Print the integral value with the specified number of decimal places
print("The integral value is: {0:.{1}f}".format(integral_value, decimals))
