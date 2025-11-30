students = []   # list of dicts: {"id": "S001", "name": "Bekele"}

def register_student():
    sid = input("Enter student ID: ")
    name = input("Enter student name: ")

    # Check if ID already exists
    if any(s['id'] == sid for s in students):
        print("Student with this ID already exists!")
        return

    students.append({"id": sid, "name": name})
    print("Student registered successfully!")

def list_students():
    if not students:
        print("No students registered yet!")
        return
    print("\n--- Registered Students ---")
    print(f"{'ID':<10} {'Name':<20}")
    print("-" * 30)
    for s in students:
        print(f"{s['id']:<10} {s['name']:<20}")

def student_menu():
    while True:
        print("\n--- Student Menu ---")
        print("1. Register Student")
        print("2. List Students")
        print("3. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")