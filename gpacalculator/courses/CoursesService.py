courses = [
    {'code': 'CS101', 'title': 'Intro to CS', 'credit': 3},
    {'code': 'CoSc1212', 'title': 'Database', 'credit': 5},
    # Massive test data hardcoded as requested
    {'code':'cosc101', 'title':'Programming I', 'credit':3},
    {'code':'cosc102', 'title':'Database System', 'credit':3},
    {'code':'cosc103', 'title':'Networking', 'credit':3},
    {'code':'cosc104', 'title':'Operating System', 'credit':3},
    {'code':'cosc105', 'title':'AI', 'credit':3}
]

def print_course_header():
    print(r"""
    ____                              
   / ___|___  _   _ _  ___  ___ ___ 
  | |   / _ \| | | | '/ |/ _ \ |
  | || (_) | |_| | |  \ \  \ \
   \____\___/ \__,_|_|  |___/\___|___/
    """)
    print("=" * 60)

def register_course():
    print("\n--- Register New Course ---")
    while True:
        code = input("Enter course code: ").strip()
        if code:
            break
        print("[!] Error: Course code cannot be empty.")

    # Check if course already exists (case-insensitive)
    if any(c['code'].lower() == code.lower() for c in courses):
        print("[!] Error: Course with this code already exists!")
        return

    while True:
        title = input("Enter course title: ").strip()
        if title:
            break
        print("[!] Error: Course title cannot be empty.")

    while True:
        try:
            credit = int(input("Enter course credit: "))
            if credit > 0:
                break
            print("[!] Error: Credit must be a positive integer.")
        except ValueError:
            print("[!] Error: Invalid input! Please enter a number for credit.")

    courses.append({"code": code, "title": title, "credit": credit})
    # Saved to memory automatically
    print("\n[+] Course registered successfully!")

def list_courses():
    if not courses:
        print("\n[!] No courses registered yet!")
        return
    print("\n" + "=" * 60)
    print(f"{'Code':<15} {'Title':<30} {'Credit':<10}")
    print("=" * 60)
    for c in courses:
        print(f"{c['code']:<15} {c['title']:<30} {c['credit']:<10}")
    print("=" * 60)

def course_menu():
    while True:
        print_course_header()
        print("[1] Register Course")
        print("[2] List Courses")
        print("[3] Back")
        print("-" * 60)
        choice = input("Enter choice: ")

        if choice == "1":
            register_course()
        elif choice == "2":
            list_courses()
        elif choice == "3":
            break
        else:
            print("\n[!] Invalid choice!")