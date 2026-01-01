"""
Name: KD
Date: 01-01-2026
Title: GradeBook Analyzer
Course: Programming for Problem Solving using Python
"""

import csv
import statistics

# ------------------------------
# TASK 1: Welcome Menu
# ------------------------------
def show_menu():
    print("\n=== GradeBook Analyzer ===")
    print("1. Enter student data manually")
    print("2. Load student data from CSV")
    print("3. Exit")


# ------------------------------
# TASK 2A: Manual Input
# ------------------------------
def manual_input():
    marks = {}
    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        score = int(input(f"Enter marks for {name}: "))
        marks[name] = score

    return marks


# ------------------------------
# TASK 2B: CSV Input
# ------------------------------
def csv_input():
    marks = {}
    filename = input("Enter CSV filename (example: marks.csv): ")

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                name = row[0]
                score = int(row[1])
                marks[name] = score
    except FileNotFoundError:
        print("File not found!")
    
    return marks


# ------------------------------
# TASK 3: Statistics Functions
# ------------------------------
def calculate_average(marks):
    return sum(marks.values()) / len(marks)

def calculate_median(marks):
    return statistics.median(marks.values())

def find_max_score(marks):
    return max(marks.values())

def find_min_score(marks):
    return min(marks.values())


# ------------------------------
# TASK 4: Grade Assignment
# ------------------------------
def assign_grades(marks):
    grades = {}

    for name, score in marks.items():
        if score >= 90:
            grades[name] = "A"
        elif score >= 80:
            grades[name] = "B"
        elif score >= 70:
            grades[name] = "C"
        elif score >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"

    return grades


def grade_distribution(grades):
    distribution = {"A":0, "B":0, "C":0, "D":0, "F":0}

    for grade in grades.values():
        distribution[grade] += 1

    return distribution


# ------------------------------
# TASK 5: Pass / Fail (List Comprehension)
# ------------------------------
def pass_fail_lists(marks):
    passed = [name for name, score in marks.items() if score >= 40]
    failed = [name for name, score in marks.items() if score < 40]
    return passed, failed


# ------------------------------
# TASK 6: Display Results Table
# ------------------------------
def display_table(marks, grades):
    print("\nName\tMarks\tGrade")
    print("-" * 30)
    for name in marks:
        print(f"{name}\t{marks[name]}\t{grades[name]}")


# ------------------------------
# MAIN PROGRAM LOOP
# ------------------------------
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        marks = manual_input()

    elif choice == "2":
        marks = csv_input()

    elif choice == "3":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
        continue

    if not marks:
        continue

    # Analysis
    grades = assign_grades(marks)

    print("\n--- Statistics Summary ---")
    print("Average:", calculate_average(marks))
    print("Median:", calculate_median(marks))
    print("Highest Score:", find_max_score(marks))
    print("Lowest Score:", find_min_score(marks))

    # Grade Distribution
    print("\n--- Grade Distribution ---")
    distribution = grade_distribution(grades)
    for grade, count in distribution.items():
        print(f"{grade}: {count}")

    # Pass / Fail
    passed, failed = pass_fail_lists(marks)
    print("\nPassed Students:", passed)
    print("Failed Students:", failed)

    # Results Table
    display_table(marks, grades)
