students = []   # list of dicts

def register_student():
    sid = input("Enter student ID: ")
    name = input("Enter student name: ")

    students.append({"id": sid, "name": name})
    print("Student registered successfully!")

def list_students():
    if not students:
        print("No students registered yet!")
        return
    print("\n--- Registered Students ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']}")

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