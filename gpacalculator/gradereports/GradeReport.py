from services.resultsService import results
from services.courseService import courses
from services.studentService import students

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
    print("Course\tCredit\tGrade\tGP")

    for r in student_results:
        course = next(c for c in courses if c["code"] == r["course_code"])
        credit = course["credit"]
        gp = r["gp"]

        total_credit += credit
        total_gp += (gp * credit)

        print(f"{course['code']}\t{credit}\t{r['grade']}\t{gp}")

    gpa = total_gp / total_credit
    print("-------------------------------------")
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