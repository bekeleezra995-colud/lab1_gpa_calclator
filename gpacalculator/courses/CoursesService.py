from fileservice.FileService import save_data, load_data

courses = []  # list of dicts: {"code": "CS101", "title": "Intro", "credit": 3}
FILE_NAME = "courses.txt"

def load_courses_from_file():
    """Loads courses from text file into the list."""
    global courses
    courses.clear() # Clear existing data
    lines = load_data(FILE_NAME)
    for line in lines:
        try:
            # Format: code|title|credit
            parts = line.split("|")
            if len(parts) == 3:
                courses.append({"code": parts[0], "title": parts[1], "credit": int(parts[2])})
        except Exception as e:
            print(f"Skipping invalid line in {FILE_NAME}: {line}")

def save_courses_to_file():
    """Saves the current list of courses to text file."""
    data_list = []
    for c in courses:
        # Format: code|title|credit
        line = f"{c['code']}|{c['title']}|{c['credit']}"
        data_list.append(line)
    save_data(FILE_NAME, data_list)

# Load data when module is imported
load_courses_from_file()

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

    # Check if course already exists
    if any(c['code'] == code for c in courses):
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
    save_courses_to_file() # Save to file
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