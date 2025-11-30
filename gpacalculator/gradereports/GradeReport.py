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

def calculate_gpa(student_id):
    student_results = [r for r in results if r['student_id'] == student_id]
    if not student_results:
        print("\n[!] Error: No results found for this student!")
        return

    # get student name
    student = next((s for s in students if s["id"] == student_id), None)
    name = student["name"] if student else "Unknown"

    total_credit = 0
    total_gp = 0

    print(f"\n--- Transcript for {name} ({student_id}) ---")
    print("=" * 60)
    print(f"{'Course':<15} {'Credit':<15} {'Grade':<15} {'GP':<15}")
    print("=" * 60)

    for r in student_results:
        course = next((c for c in courses if c["code"] == r["course_code"]), None)
        if not course:
            continue # Should not happen if data integrity is maintained
            
        credit = course["credit"]
        gp = r["gp"]

        total_credit += credit
        total_gp += (gp * credit)

        print(f"{r['course_code']:<15} {credit:<15} {r['grade']:<15} {gp:<15}")

    if total_credit == 0:
        gpa = 0.0
    else:
        gpa = total_gp / total_credit
        
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