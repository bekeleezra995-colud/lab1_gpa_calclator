from fileservices import FileService
# from fileservices.exceptions import PersistenceError # Removed

students = []
try:
    students = FileService.read_table('students.txt')
except (OSError, ValueError):
    # Fail silent on load
    pass

def get_all_students():
    """Returns a list of all students."""
    return students

def get_student_by_id(student_id):
    """Returns a student dictionary if found, else None."""
    for s in students:
        if s['id'] == student_id:
            return s
    return None

def create_student(student_id, name):
    """
    Registers a new student.
    Raises ValueError if ID already exists or inputs are invalid.
    Raises OSError if saving fails.
    """
    if not student_id:
        raise ValueError("Student ID cannot be empty.")
    if not name:
        raise ValueError("Student name cannot be empty.")
        
    if any(s['id'] == student_id for s in students):
        raise ValueError(f"Student with ID {student_id} already exists.")

    students.append({"id": student_id, "name": name})
    try:
        FileService.write_table('students.txt', students, ['id', 'name'])
    except OSError:
        students.pop() # Rollback
        raise # Re-raise