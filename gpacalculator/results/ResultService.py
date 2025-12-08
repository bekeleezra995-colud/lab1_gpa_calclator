from students.StudentService import students
from courses.CoursesService import courses
from fileservice.FileService import save_data, load_data

results = []  # {"student_id": "", "course_code": "", "grade": "", "gp": float}
FILE_NAME = "results.txt"

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

def load_results_from_file():
    """Loads results from text file into the list."""
    global results
    results.clear()
    lines = load_data(FILE_NAME)
    for line in lines:
        try:
            # Format: student_id|course_code|grade|gp
            parts = line.split("|")
            if len(parts) == 4:
                results.append({
                    "student_id": parts[0], 
                    "course_code": parts[1], 
                    "grade": parts[2], 
                    "gp": float(parts[3])
                })
        except Exception as e:
            print(f"Skipping invalid line in {FILE_NAME}: {line}")

def save_results_to_file():
    """Saves the current list of results to text file."""
    data_list = []
    for r in results:
        # Format: student_id|course_code|grade|gp
        line = f"{r['student_id']}|{r['course_code']}|{r['grade']}|{r['gp']}"
        data_list.append(line)
    save_data(FILE_NAME, data_list)

# Load data when module is imported
load_results_from_file()

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
    if not any(c["code"] == code for c in courses):
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
        if r['student_id'] == sid and r['course_code'] == code:
            print("[!] Result for this course already exists. Updating...")
            r['grade'] = grade
            r['gp'] = gp
            save_results_to_file() # Save update
            return

    results.append({"student_id": sid, "course_code": code, "grade": grade, "gp": gp})
    save_results_to_file() # Save new result
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
