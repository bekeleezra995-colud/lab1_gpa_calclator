from Services.StudentService import students
from Services.CourseService import courses

results = []  # {"student_id": "", "course_code": "", "grade": "", "gp": float}

grade_points = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.75,
    "B+": 3.50,
    "B": 3.00,
    "B-": 2.75,
    "C+": 2.50,
    "C": 2.00,
    "C-": 1.75,
    "D": 1.00,
    "F": 0.00
}

def add_result():
    sid = input("Enter student ID: ")
    code = input("Enter course code: ")
    grade = input("Enter grade (A+, A, A-, B+, B, B-, C+, C, C-, D, F): ").upper()

    # validate student, course, grade
    if not any(s["id"] == sid for s in students):
        print("Student not found!")
        return
    if not any(c["code"] == code for c in courses):
        print("Course not found!")
        return
    if grade not in grade_points:
        print("Invalid grade!")
        return

    gp = grade_points[grade]
    results.append({"student_id": sid, "course_code": code, "grade": grade, "gp": gp})

    print("Result added successfully!")

def list_results():
    if not results:
        print("No results recorded!")
        return
    print("\n--- Results ---")
    for r in results:
        print(f"Student: {r['student_id']} | Course: {r['course_code']} | Grade: {r['grade']}")

def result_menu():
    while True:
        print("\n--- Result Menu ---")
        print("1. Add Result")
        print("2. List Results")
        print("3. Back")
        choice = input("Enter: ")

        if choice == "1":
            add_result()
        elif choice == "2":
            list_results()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")