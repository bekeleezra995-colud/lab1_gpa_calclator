from results.ResultService import results
from courses.CoursesService import courses
from students.StudentService import students

def calculate_gpa(student_id):
    student_results = [r for r in results if r['student_id'] == student_id]
    if not student_results:
        print("No results found for this student!")
        return

    # get student name
    student = next((s for s in students if s["id"] == student_id), None)
    name = student["name"] if student else "Unknown"

    total_credit = 0
    total_gp = 0

    print(f"\n--- Transcript for {name} ({student_id}) ---")
    print(f"{'Course':<10} {'Credit':<10} {'Grade':<10} {'GP':<10}")
    print("-" * 40)

    for r in student_results:
        course = next((c for c in courses if c["code"] == r["course_code"]), None)
        if not course:
            continue # Should not happen if data integrity is maintained
            
        credit = course["credit"]
        gp = r["gp"]

        total_credit += credit
        total_gp += (gp * credit)

        print(f"{r['course_code']:<10} {credit:<10} {r['grade']:<10} {gp:<10}")

    if total_credit == 0:
        gpa = 0.0
    else:
        gpa = total_gp / total_credit
        
    print("-" * 40)
    print(f"Total Credit: {total_credit}")
    print(f"Total Grade Point: {round(total_gp, 2)}")
    print(f"Cumulative GPA: {round(gpa, 2)}")

def report_menu():
    while True:
        print("\n--- GPA Report Menu ---")
        print("1. Calculate GPA by Student ID")
        print("2. Back")
        choice = input("Enter: ")

        if choice == "1":
            sid = input("Enter Student ID: ")
            calculate_gpa(sid)
        elif choice == "2":
            break
        else:
            print("Invalid choice!")