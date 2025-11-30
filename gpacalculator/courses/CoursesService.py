courses = []  # list of dicts: {"code": "CS101", "title": "Intro", "credit": 3}

def register_course():
    code = input("Enter course code: ")
    title = input("Enter course title: ")
    while True:
        try:
            credit = int(input("Enter course credit: "))
            break
        except ValueError:
            print("Invalid credit! Please enter a number.")

    courses.append({"code": code, "title": title, "credit": credit})
    print("Course registered successfully!")

def list_courses():
    if not courses:
        print("No courses registered yet!")
        return
    print("\n--- Registered Courses ---")
    print(f"{'Code':<10} {'Title':<20} {'Credit':<5}")
    print("-" * 40)
    for c in courses:
        print(f"{c['code']:<10} {c['title']:<20} {c['credit']:<5}")

def course_menu():
    while True:
        print("\n--- Course Menu ---")
        print("1. Register Course")
        print("2. List Courses")
        print("3. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            register_course()
        elif choice == "2":
            list_courses()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")