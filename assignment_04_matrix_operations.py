# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def transposeMatrix(matrix, rows, cols):
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result


def addMatrices(a, b, rows, cols):
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]
    return result


def multiplyMatrices(a, b, m, n, p):
    result = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result


def readMatrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = input(f"Enter row {i + 1}: ").split()
        row = [int(x) for x in row]
        matrix.append(row)
    return matrix


def printMatrix(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(f"{matrix[i][j]:5}", end="")
        print()


# Main block
print("Matrix Operations Menu:")
print("1. Transpose a Matrix")
print("2. Add Two Matrices")
print("3. Multiply Two Matrices")
choice = int(input("Enter choice: "))

if choice == 1:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = readMatrix(rows, cols)
    result = transposeMatrix(matrix, rows, cols)

    print("\nOriginal Matrix:")
    printMatrix(matrix, rows, cols)
    print("\nTransposed Matrix:")
    printMatrix(result, cols, rows)

elif choice == 2:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("\nEnter values for Matrix A:")
    a = readMatrix(rows, cols)
    print("\nEnter values for Matrix B:")
    b = readMatrix(rows, cols)

    result = addMatrices(a, b, rows, cols)

    print("\nSum Matrix:")
    printMatrix(result, rows, cols)

elif choice == 3:
    m = int(input("Enter rows of Matrix A (M): "))
    n = int(input("Enter columns of Matrix A (N): "))
    n2 = int(input("Enter rows of Matrix B (must equal N): "))
    p = int(input("Enter columns of Matrix B (P): "))

    if n != n2:
        print("Error: Columns of A must equal rows of B.")
    else:
        print("\nEnter values for Matrix A:")
        a = readMatrix(m, n)
        print("\nEnter values for Matrix B:")
        b = readMatrix(n, p)

        result = multiplyMatrices(a, b, m, n, p)

        print("\nProduct Matrix:")
        printMatrix(result, m, p)

else:
    print("Invalid choice.")