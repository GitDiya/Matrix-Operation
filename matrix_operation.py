import numpy as np

def input_matrix(rows, cols):
    """
    Function to take matrix input from the user.
    """
    matrix = []
    print(f"Enter the elements for a {rows}x{cols} matrix row by row:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
    return np.array(matrix)

def matrix_addition(matrix1, matrix2):
    """
    Perform matrix addition.
    """
    try:
        result = np.add(matrix1, matrix2)
        return result
    except ValueError:
        print("Matrices must have the same dimensions for addition.")
        return None

def matrix_subtraction(matrix1, matrix2):
    """
    Perform matrix subtraction.
    """
    try:
        result = np.subtract(matrix1, matrix2)
        return result
    except ValueError:
        print("Matrices must have the same dimensions for subtraction.")
        return None

def matrix_multiplication(matrix1, matrix2):
    """
    Perform matrix multiplication.
    """
    try:
        result = np.dot(matrix1, matrix2)
        return result
    except ValueError:
        print("The number of columns of the first matrix must be equal to the number of rows of the second matrix.")
        return None

def matrix_transpose(matrix):
    """
    Perform matrix transpose.
    """
    return np.transpose(matrix)

def matrix_determinant(matrix):
    """
    Calculate matrix determinant.
    """
    if matrix.shape[0] == matrix.shape[1]:  # Matrix must be square
        return np.linalg.det(matrix)
    else:
        print("Determinant can only be calculated for square matrices.")
        return None

def display_matrix(matrix):
    """
    Display a matrix in a structured format.
    """
    print("\nResultant Matrix:")
    print(matrix)
    print("\n")

def main():
    while True:
        print("\nMatrix Operations Tool")
        print("1. Matrix Addition")
        print("2. Matrix Subtraction")
        print("3. Matrix Multiplication")
        print("4. Matrix Transpose")
        print("5. Matrix Determinant")
        print("6. Exit")
        
        choice = input("Choose an operation (1-6): ")

        if choice == '6':
            print("Exiting the tool...")
            break

        # Input matrices for operations that require two matrices
        if choice in ['1', '2', '3']:
            rows1 = int(input("Enter the number of rows for Matrix 1: "))
            cols1 = int(input("Enter the number of columns for Matrix 1: "))
            matrix1 = input_matrix(rows1, cols1)

            rows2 = int(input("Enter the number of rows for Matrix 2: "))
            cols2 = int(input("Enter the number of columns for Matrix 2: "))
            matrix2 = input_matrix(rows2, cols2)

        elif choice == '4' or choice == '5':
            rows = int(input("Enter the number of rows for the matrix: "))
            cols = int(input("Enter the number of columns for the matrix: "))
            matrix = input_matrix(rows, cols)

        # Perform the chosen operation
        if choice == '1':
            result = matrix_addition(matrix1, matrix2)
            if result is not None:
                display_matrix(result)
        
        elif choice == '2':
            result = matrix_subtraction(matrix1, matrix2)
            if result is not None:
                display_matrix(result)

        elif choice == '3':
            result = matrix_multiplication(matrix1, matrix2)
            if result is not None:
                display_matrix(result)

        elif choice == '4':
            result = matrix_transpose(matrix)
            display_matrix(result)

        elif choice == '5':
            result = matrix_determinant(matrix)
            if result is not None:
                print(f"Determinant: {result}\n")

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
