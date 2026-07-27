# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def computeSum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def computeAverage(numbers):
    total = computeSum(numbers)
    return total / len(numbers)


def computeMax(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def computeMin(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest



n = int(input("How many numbers? "))

if n <= 0:
    print("Error: N must be a positive integer.")
else:
    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    print()
    print("Results:")
    print(f"Sum:     {computeSum(numbers)}")
    print(f"Average: {computeAverage(numbers)}")
    print(f"Maximum: {computeMax(numbers)}")
    print(f"Minimum: {computeMin(numbers)}")