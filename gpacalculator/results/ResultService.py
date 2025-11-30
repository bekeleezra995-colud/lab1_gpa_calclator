from students.StudentService import students
from courses.CoursesService import courses

results = []  # {"student_id": "", "course_code": "", "grade": "", "gp": float}

# DBU Grading System (Assumed based on provided code)
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
    
    # Validate student
    if not any(s["id"] == sid for s in students):
        print("Student not found! Please register the student first.")
        return

    code = input("Enter course code: ")
    
    # Validate course
    if not any(c["code"] == code for c in courses):
        print("Course not found! Please register the course first.")
        return

    grade = input("Enter grade (A+, A, A-, B+, B, B-, C+, C, C-, D, F): ").upper()

    if grade not in grade_points:
        print("Invalid grade!")
        return

    gp = grade_points[grade]
    
    # Check if result already exists for this student and course
    for r in results:
        if r['student_id'] == sid and r['course_code'] == code:
            print("Result for this course already exists. Updating...")
            r['grade'] = grade
            r['gp'] = gp
            return

    results.append({"student_id": sid, "course_code": code, "grade": grade, "gp": gp})
    print("Result added successfully!")

def list_results():
    if not results:
        print("No results recorded!")
        return
    print("\n--- Results ---")
    print(f"{'Student ID':<15} {'Course Code':<15} {'Grade':<10} {'GP':<5}")
    print("-" * 50)
    for r in results:
        print(f"{r['student_id']:<15} {r['course_code']:<15} {r['grade']:<10} {r['gp']:<5}")

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