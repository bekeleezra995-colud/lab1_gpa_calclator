from fileservice.FileService import save_data, load_data

students = []   # list of dicts: {"id": "S001", "name": "Bekele"}
FILE_NAME = "students.txt"

def load_students_from_file():
    """Loads students from text file into the list."""
    global students
    students.clear()
    lines = load_data(FILE_NAME)
    for line in lines:
        try:
            # Format: id|name
            parts = line.split("|")
            if len(parts) == 2:
                students.append({"id": parts[0], "name": parts[1]})
        except Exception as e:
            print(f"Skipping invalid line in {FILE_NAME}: {line}")

def save_students_to_file():
    """Saves the current list of students to text file."""
    data_list = []
    for s in students:
        # Format: id|name
        line = f"{s['id']}|{s['name']}"
        data_list.append(line)
    save_data(FILE_NAME, data_list)

# Load data when module is imported
load_students_from_file()

def print_student_header():
    print(r"""
   ____  _             _            _   
  / ___|| |_ _   _  | | ___ _  | |_ 
  \___ \| | | | |/ _` |/ _ \ '_ \| |
   ___) | |_| |_| | (_| |  / | | | |_ 
  |____/ \|\__,_|\__,_|\___|_| |_|\__|
    """)
    print("=" * 60)

def register_student():
    print("\n--- Register New Student ---")
    while True:
        sid = input("Enter student ID: ").strip()
        if sid:
            break
        print("[!] Error: Student ID cannot be empty.")

    # Check if ID already exists
    if any(s['id'] == sid for s in students):
        print("[!] Error: Student with this ID already exists!")
        return

    while True:
        name = input("Enter student name: ").strip()
        if name:
            break
        print("[!] Error: Student name cannot be empty.")

    students.append({"id": sid, "name": name})
    save_students_to_file() # Save to file
    print("\n[+] Student registered successfully!")

def list_students():
    if not students:
        print("\n[!] No students registered yet!")
        return
    print("\n" + "=" * 60)
    print(f"{'ID':<15} {'Name':<30}")
    print("=" * 60)
    for s in students:
        print(f"{s['id']:<15} {s['name']:<30}")
    print("=" * 60)

def student_menu():
    while True:
        print_student_header()
        print("[1] Register Student")
        print("[2] List Students")
        print("[3] Back")
        print("-" * 60)
        choice = input("Enter choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            break
        else:
            print("\n[!] Invalid choice!")