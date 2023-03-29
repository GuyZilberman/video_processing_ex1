import numpy as np

if __name__ == "__main__":
    # Generate a 5x6 matrix with values between 0 and 9
    matrix = np.random.randint(0, 10, size=(5, 6))

    # Print the original matrix
    print("Original Matrix:")
    print(matrix)

    # Find the 3rd smallest value in row #5
    row_five = matrix[4]
    sorted_row_five = np.sort(row_five)
    third_smallest = sorted_row_five[2]

    # Create a mask to mark the index of the 3rd smallest value
    third_smallest_mask = row_five == third_smallest

    # Replace the 3rd smallest value with 10
    row_five[third_smallest_mask] = 10

    # Print the updated matrix
    print("Updated Matrix:")
    print(matrix)
    print("HI)
