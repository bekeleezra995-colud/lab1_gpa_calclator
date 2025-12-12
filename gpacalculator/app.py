from students import StudentService
from courses import CoursesService
from results import ResultService
from gradereports import GradeReport

def print_header():
    print(r"""
   ____ ____  _      ____      _            _       _             
  / ___|  _ \ / \   / ___| _| | ___ _   _| |  _| |_ ___  _  
  | |  _| |_) / _ \  | |   / _` | |/ | | | | |/ _` | / _ \| '|
  | |_| |  / ___ \ | || (_| | | (| |_| | | (_| | || (_) | |   
   \____|_| /_/   \_\ \____\,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
    """)
    print("=" * 60)
    print("        WELCOME TO THE STUDENT GRADING SYSTEM")
    print("=" * 60)

# --- Student UI ---
def manage_students():
    while True:
        print("\n--- Student Menu ---")
        print("[1] Register Student")
        print("[2] List Students")
        print("[3] Back")
        print("-" * 60)
        choice = input("Choice: ")
        
        if choice == '1':
            sid = input("Enter ID: ").strip()
            name = input("Enter Name: ").strip()
            try:
                StudentService.create_student(sid, name)
                print("[+] Student created!")
            except Exception as e:
                print(f"[!] Error: {e}")
        elif choice == '2':
            students = StudentService.get_all_students()
            if not students:
                print("[!] No students found.")
            else:
                print(f"\n{'ID':<15} | {'Name':<25}")
                print("-" * 45)
                for s in students:
                    print(f"{s['id']:<15} | {s['name']:<25}")
        elif choice == '3':
            break
        else:
            print("[!] Invalid choice.")

# --- Course UI ---
def manage_courses():
    while True:
        print("\n--- Course Menu ---")
        print("[1] Register Course")
        print("[2] List Courses")
        print("[3] Back")
        print("-" * 60)
        choice = input("Choice: ")
        
        if choice == '1':
            code = input("Code: ").strip()
            title = input("Title: ").strip()
            credit = input("Credit: ").strip()
            try:
                CoursesService.create_course(code, title, credit)
                print("[+] Course created!")
            except Exception as e:
                print(f"[!] Error: {e}")
        elif choice == '2':
            courses = CoursesService.get_all_courses()
            if not courses:
                print("[!] No courses found.")
            else:
                print(f"\n{'Code':<10} | {'Title':<30} | {'Credit':<5}")
                print("-" * 55)
                for c in courses:
                    print(f"{c['code']:<10} | {c['title']:<30} | {c['credit']:<5}")
        elif choice == '3':
            break
        else:
            print("[!] Invalid choice.")

# --- Result UI ---
def manage_results():
    while True:
        print("\n--- Result Menu ---")
        print("[1] Add Result")
        print("[2] List Results")
        print("[3] Back")
        print("-" * 60)
        choice = input("Choice: ")
        
        if choice == '1':
            sid = input("Student ID: ").strip()
            code = input("Course Code: ").strip()
            grade = input("Grade: ").strip().upper()
            try:
                ResultService.create_result(sid, code, grade)
                print("[+] Result added!")
            except Exception as e:
                print(f"[!] Error: {e}")
        elif choice == '2':
            results = ResultService.get_all_results()
            if not results:
                print("[!] No results found.")
            else:
                print(f"\n{'Student ID':<15} | {'Course':<10} | {'Grade':<5} | {'GP':<5}")
                print("-" * 45)
                for r in results:
                    print(f"{r['student_id']:<15} | {r['course_code']:<10} | {r['grade']:<5} | {r['gp']:<5}")
        elif choice == '3':
            break
        else:
            print("[!] Invalid choice.")

# --- Report UI ---
# Assuming GradeReport has pure calculation functions (e.g. calculate_gpa) 
# and we should implement the viewing logic here.
def manage_reports():
    while True:
        print("\n--- GPA Report ---")
        sid = input("Enter Student ID to view GPA (or 'q' to back): ").strip()
        if sid.lower() == 'q':
            break
            
        student = StudentService.get_student_by_id(sid)
        if not student:
            print("[!] Student not found.")
            continue
            
        # Helper logic to calculate GPA using pure functions
        results = ResultService.get_results_by_student(sid)
        if not results:
            print("[!] No results found for this student.")
            continue
            
        # Get courses for these results to calculate credits
        all_courses = CoursesService.get_all_courses() 
        # Note: calculate functions usually expect list of courses? 
        # Let's inspect GradeReport.py logic to be sure how to call it.
        # Assuming typical signature: calculate_total_grade_point(results, courses)
        
        try:
            total_gp = GradeReport.calculate_total_grade_point(results, all_courses)
            total_credits = GradeReport.calculate_total_credit([c for c in all_courses if c['code'] in [r['course_code'] for r in results]]) 
            # Note: The `calculate_total_credit` takes a list of courses. 
            # We need to filter courses that the student took! 
            # Wait, `calculate_total_credit` in previous checks summed ALL credits passed to it.
            # So I must pass ONLY the courses the student took.
            
            courses_taken = []
            for r in results:
                 c = CoursesService.get_course_by_code(r['course_code'])
                 if c: courses_taken.append(c)
            
            # Re-calculate with filtered list
            total_credits = GradeReport.calculate_total_credit(courses_taken)
            gpa = GradeReport.calculate_gpa_value(total_gp, total_credits)
            
            print("="*40)
            print(f"Student: {student['name']} ({student['id']})")
            print(f"Total Credits: {total_credits}")
            print(f"Total Grade Points: {total_gp}")
            print(f"GPA: {gpa:.2f}")
            print("="*40)
            
        except Exception as e:
            print(f"[!] Error calculating GPA: {e}")


def main_menu():
    while True:
        print_header()
        print("\n[1] Student Menu")
        print("[2] Course Menu")
        print("[3] Result Menu")
        print("[4] GPA Report")
        print("[5] Exit")
        print("-" * 60)
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            manage_students()
        elif choice == "2":
            manage_courses()
        elif choice == "3":
            manage_results()
        elif choice == "4":
            manage_reports()
        elif choice == "5":
            print("\nExiting... Goodbye!")
            break
        else:
            print("\n[!] Invalid choice! Please try again.")

if __name__ == "__main__": 
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")