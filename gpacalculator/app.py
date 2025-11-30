from students.StudentService import student_menu
from courses.CoursesService import course_menu
from results.ResultService import result_menu
from gradereports.GradeReport import report_menu

def main_menu():
    while True:
        print("\n=== Student Grading System ===")
        print("1. Student Menu")
        print("2. Course Menu")
        print("3. Result Menu")
        print("4. GPA Report")
        print("5. Exit")
        
        choice = input("Enter choice: ")

        if choice == "1":
            student_menu()
        elif choice == "2":
            course_menu()
        elif choice == "3":
            result_menu()
        elif choice == "4":
            report_menu()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()