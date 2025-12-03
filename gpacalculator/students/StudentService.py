students = [
    {"id": "S001", "name": "Bekele"},
    {"id": "DBU1601567", "name": "BEKELE EZRA"},
    {"id": "DBU10001", "name": "Test Student"}
]

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
    # Saved to memory (list) automatically
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