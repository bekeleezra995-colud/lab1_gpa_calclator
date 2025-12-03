from students.StudentService import students
from courses.CoursesService import courses

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
<<<<<<< HEAD
=======
}
grade_ranges = {
    "A+": "90-100",
    "A": "85-89",
    "A-": "80-84",
    "B+": "75-79",
    "B": "70-74",
    "B-": "65-69",
    "C+": "60-64",
    "C": "55-59",
    "C-": "50-54",
    "D": "40-49",
    "F": "below 40"
>>>>>>> 1657cd0185e0155732e162f174353bf83310be4d
}

def get_grade_point(grade):
    """Returns the grade point for a given letter grade."""
    return grade_points.get(grade, 0.0)

# Initialize results with existing file data and test data
results = [
    # Existing file data
    {"student_id": "S001", "course_code": "CS101", "grade": "A", "gp": 4.0},
    {"student_id": "DBU1601567", "course_code": "CoSc1212", "grade": "A", "gp": 4.0},
    # Massive test data
    {'student_id':'DBU10001', 'course_code':'CoSc101', 'grade':'A', 'gp': 4.0},
    {'student_id':'DBU10001', 'course_code':'CoSc104', 'grade':'B+', 'gp': 3.5},
    {'student_id':'DBU10001', 'course_code':'CoSc105', 'grade':'C', 'gp': 2.0},
    {'student_id':'DBU10001', 'course_code':'CoSc102', 'grade':'B', 'gp': 3.0},
    {'student_id':'DBU10001', 'course_code':'CoSc103', 'grade':'A-', 'gp': 3.75}
]

def print_result_header():
    print(r"""
   ____                 _ _       
  |  _ \ ___  ___ _   _| | |_ ___ 
  | |_) / _ \/ | | | | | / |
  |  _ <  /\__ \ |_| | | |_\__ \
  |_| \_\___||___/\__,_|_|\__|___/
    """)
    print("=" * 60)

def add_result():
    print("\n--- Add New Result ---")
    while True:
        sid = input("Enter student ID: ").strip()
        if sid:
            break
        print("[!] Error: Student ID cannot be empty.")
    
    # Validate student
    if not any(s["id"] == sid for s in students):
        print("[!] Error: Student not found! Please register the student first.")
        return

    while True:
        code = input("Enter course code: ").strip()
        if code:
            break
        print("[!] Error: Course code cannot be empty.")
    
    # Validate course
    if not any(c["code"].lower() == code.lower() for c in courses):
        print("[!] Error: Course not found! Please register the course first.")
        return

    while True:
        grade = input("Enter grade (A+, A, A-, B+, B, B-, C+, C, C-, D, F): ").strip().upper()
        if grade in grade_points:
            break
        print("[!] Error: Invalid grade! Please enter a valid grade from the list.")

    gp = grade_points[grade]
    
    # Check if result already exists for this student and course
    for r in results:
        if r['student_id'] == sid and r['course_code'].lower() == code.lower():
            print("[!] Result for this course already exists. Updating...")
            r['grade'] = grade
            r['gp'] = gp
            r['gp'] = gp
            # Saved to memory (list) automatically
            return

    results.append({"student_id": sid, "course_code": code, "grade": grade, "gp": gp})
    # Saved to memory (list) automatically
    print("\n[+] Result added successfully!")

def list_results():
    if not results:
        print("\n[!] No results recorded!")
        return
    print("\n" + "=" * 60)
    print(f"{'Student ID':<15} {'Course Code':<15} {'Grade':<10} {'GP':<5}")
    print("=" * 60)
    for r in results:
        print(f"{r['student_id']:<15} {r['course_code']:<15} {r['grade']:<10} {r['gp']:<5}")
    print("=" * 60)

def result_menu():
    while True:
        print_result_header()
        print("[1] Add Result")
        print("[2] List Results")
        print("[3] Back")
        print("-" * 60)
        choice = input("Enter: ")

        if choice == "1":
            add_result()
        elif choice == "2":
            list_results()
        elif choice == "3":
            break
        else:
            print("\n[!] Invalid choice!")
