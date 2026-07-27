# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def addStudent(students):
    name = input("Student name: ")
    studentId = int(input("Student ID: "))
    numScores = int(input("How many scores? "))

    scores = []
    for i in range(numScores):
        score = int(input(f"Enter score {i + 1}: "))
        scores.append(score)

    student = {
        "name": name,
        "id": studentId,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')


def displayStudents(students):
    if len(students) == 0:
        print("No students have been added yet.")
        return

    print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average':<10}")
    print("-" * 50)
    for student in students:
        average = sum(student["scores"]) / len(student["scores"])
        scoresStr = ", ".join(str(s) for s in student["scores"])
        print(f"{student['name']:<15}{student['id']:<12}{scoresStr:<15}{average:<10.2f}")
    print("-" * 50)


def calculateAverage(students):
    studentId = int(input("Enter student ID: "))

    for student in students:
        if student["id"] == studentId:
            average = sum(student["scores"]) / len(student["scores"])
            print(f"{student['name']}'s average score: {average:.2f}")
            return

    print("Error: Student ID not found.")


students = []

while True:
    print("=" * 33)
    print("  STUDENT RECORD SYSTEM MENU")
    print("=" * 33)
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        addStudent(students)
    elif choice == "2":
        displayStudents(students)
    elif choice == "3":
        calculateAverage(students)
    elif choice == "4":
        break
    else:
        print("Error: Invalid choice. Please enter a number from 1 to 4.")