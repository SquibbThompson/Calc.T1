import numpy as np
import math

# Ask the user for the size of the matrices (accuracy level)
size = int(input("Enter the size of the matrices (accuracy level): "))
n = float(input("Enter the n value for the second sine wave: "))
cycles = float(input("Enter the number of sine wave cycles: "))

# Adjust the size of the matrix to accommodate for multiple cycles and negative amplitude
matrix_size = size * 2
periods = int(cycles * 4)  # Adjusted for quarter cycles

# Initialize the matrices with zeros
matrix1 = np.zeros((matrix_size, matrix_size * periods))
matrix2 = np.zeros((matrix_size, matrix_size * periods))

# Fill the matrices with the appropriate values based on the sine waves
for i in range(matrix_size * periods):
    # Calculate the angle in radians, shifted by pi/2
    angle = ((i / (matrix_size * periods)) * 2 * math.pi * cycles) - (math.pi / 2)

    # Calculate the sine of the angle
    sine1 = math.sin(angle)
    sine2 = math.sin(angle) / n

    # Scale and shift the sine values to match the matrix size and position
    y1 = int((sine1 + 1) / 2 * (matrix_size - 1))
    y2 = int((sine2 + 1) / 2 * (matrix_size - 1))

    # Place the '1' values in the matrices
    matrix1[y1, i] = 1
    matrix2[y2, i] = 1

    # Fill the area between the two sine waves
    if y1 < y2:
        matrix1[y1:y2, i] = 1
    else:
        matrix2[y2:y1, i] = 1

    # Reflect the sine waves about their maximum amplitude
    if (i % (matrix_size // 4) == 0) and (i != 0):  # Adjusted for quarter cycles
        matrix1[:, i - matrix_size // 4:i] = np.flipud(matrix1[:, i - matrix_size // 4:i])
        matrix2[:, i - matrix_size // 4:i] = np.flipud(matrix2[:, i - matrix_size // 4:i])

# Flip the matrices vertically
matrix1 = np.flipud(matrix1)
matrix2 = np.flipud(matrix2)

# Combine the matrices
combined_matrix = np.logical_or(matrix1, matrix2).astype(int)

# Change overlapping '1's to '10's
combined_matrix = combined_matrix + (matrix1.astype(int) & matrix2.astype(int)) * 9

# Set print options
np.set_printoptions(linewidth=np.inf, threshold=np.inf)

# Print the combined matrix
print(combined_matrix)

