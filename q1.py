import numpy as np

# Step 1: Generate the array
np.random.seed(0)  # For reproducibility
arr = np.random.randint(1, 51, size=(5, 4))
print("Array:\n", arr)

# Step 2: Extract elements along the anti-diagonal
anti_diagonal = [arr[i, -i-1] for i in range(min(arr.shape))]
print("Anti-diagonal elements:", anti_diagonal)

# Step 3: Compute max value in each row
row_max = np.max(arr, axis=1)
print("Max value in each row:", row_max)

# Step 4: Create new array with elements <= mean
mean_value = np.mean(arr)
filtered_array = arr[arr <= mean_value]
print("Elements less than or equal to mean (", mean_value, "):", filtered_array)

# Step 5: Boundary traversal function
def numpy_boundary_traversal(matrix):
    if matrix.size == 0:
        return []

    top = matrix[0, :]
    right = matrix[1:-1, -1]
    bottom = matrix[-1, ::-1]
    left = matrix[-2:0:-1, 0]

    boundary = np.concatenate((top, right, bottom, left)).tolist()
    return boundary

# Example usage of boundary traversal
boundary_elements = numpy_boundary_traversal(arr)
print("Boundary traversal (clockwise):", boundary_elements)
