import numpy as np
import math

# Ask the user for the size of the matrices (accuracy level)
size = int(input("Enter the size of the matrices (accuracy level): "))

# Initialize the matrix with zeros
matrix = np.zeros((size, size))

# Fill the matrix with the appropriate values based on the sine wave
for i in range(size):
    # Calculate the angle in radians, shifted by pi/2
    angle = ((i / size) * 2 * math.pi) - (math.pi / 2)

    # Calculate the sine of the angle
    sine = math.sin(angle)

    # Scale and shift the sine value to match the matrix size and position
    y = int((sine + 1) / 2 * (size - 1))

    # Place the '1' value in the matrix
    matrix[y, i] = 1

matrix = np.flipud(matrix)


np.set_printoptions(threshold=np.inf)



# Set print options
np.set_printoptions(linewidth=np.inf)

# Print the matrix
print(matrix)
