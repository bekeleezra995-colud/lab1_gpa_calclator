from results.ResultService import results
from courses.CoursesService import courses
from students.StudentService import students

def print_report_header():
    print(r"""
   ____ ____    _    
  / ___|  _ \  / \   
 | |  _| |_) |/ _ \  
 | |_| |  __// ___ \ 
  \____|_|  /_/   \_\
    """)
    print("=" * 60)


def calculate_total_credit(course_list):
    """Calculates total credit from a list of course objects."""
    return sum(c['credit'] for c in course_list)

def calculate_total_grade_point(student_results, courses_list):
    """Calculates total grade points based on results and course info."""
    total_gp = 0
    for r in student_results:
        course = next((c for c in courses_list if c["code"].lower() == r["course_code"].lower()), None)
        if course:
            total_gp += r["gp"] * course["credit"]
    return total_gp

def calculate_gpa_value(total_gp, total_credit):
    """Calculates GPA value."""
    if total_credit == 0:
        return 0.0
    return total_gp / total_credit

def calculate_gpa(student_id):
    student_results = [r for r in results if r['student_id'] == student_id]
    if not student_results:
        print("\n[!] Error: No results found for this student!")
        return

    # get student name
    student = next((s for s in students if s["id"] == student_id), None)
    name = student["name"] if student else "Unknown"

    # Gather course objects for the student's results
    student_courses = []
    for r in student_results:
         course = next((c for c in courses if c["code"] == r["course_code"]), None)
         if course:
             student_courses.append(course)

    total_credit = calculate_total_credit(student_courses)
    total_gp = calculate_total_grade_point(student_results, courses)
    gpa = calculate_gpa_value(total_gp, total_credit)

    print(f"\n--- Transcript for {name} ({student_id}) ---")
    print("=" * 60)
    print(f"{'Course':<15} {'Credit':<15} {'Grade':<15} {'GP':<15}")
    print("=" * 60)

    for r in student_results:
        course = next((c for c in courses if c["code"] == r["course_code"]), None)
        if not course:
            continue
            
        credit = course["credit"]
        gp = r["gp"]

        print(f"{r['course_code']:<15} {credit:<15} {r['grade']:<15} {gp:<15}")

    print("=" * 60)
    print(f"Total Credit:      {total_credit}")
    print(f"Total Grade Point: {round(total_gp, 2)}")
    print(f"Cumulative GPA:    {round(gpa, 2)}")
    print("=" * 60)

def report_menu():
    while True:
        print_report_header()
        print("[1] Calculate GPA by Student ID")
        print("[2] Back")
        print("-" * 60)
        choice = input("Enter: ")

        if choice == "1":
            while True:
                sid = input("Enter Student ID: ").strip()
                if sid:
                    break
                print("[!] Error: Student ID cannot be empty.")
            calculate_gpa(sid)
        elif choice == "2":
            break
        else:
            print("\n[!] Invalid choice!")