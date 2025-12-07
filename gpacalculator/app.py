from students.StudentService import student_menu
from courses.CoursesService import course_menu
from results.ResultService import result_menu
from gradereports.GradeReport import report_menu

def print_header():
    print(r"""
   ____ ____  _      ____      _            _       _             
  / ___|  _ \ / \   / ___| _| | ___ _   _| |  _| |_ ___  _  
 | |  _| |_) / _ \  | |   / _` | |/ | | | | |/ _` | / _ \| '|
 | |_| |  / ___ \ | || (_| | | (| |_| | | (_| | || (_) | |   
  \____|_| /_/   \_\ \____\,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
    """)
    print("=" * 60)
    print("        WELCOME TO THE  DBU STUDENT GRADING SYSTEM")
    print("=" * 60)

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
            student_menu()
        elif choice == "2":
            course_menu()
        elif choice == "3":
            result_menu()
        elif choice == "4":
            report_menu()
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