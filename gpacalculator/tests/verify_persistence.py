import sys
import os

# Ensure we can import from current directory
sys.path.append(os.getcwd())

from students import StudentService
from courses import CoursesService
from results import ResultService
from fileservices import FileService

def verify_persistence():
    print("--- 1. Initial Data Check ---")
    st_count = len(StudentService.students)
    co_count = len(CoursesService.courses)
    re_count = len(ResultService.results)
    print(f"Students: {st_count}, Courses: {co_count}, Results: {re_count}")
    
    print("\n--- 2. Registering New Data ---")
    
    # Register Student
    new_student_id = "VERIFY_S001"
    if not any(s['id'] == new_student_id for s in StudentService.students):
        # We simulate input by mocking input or just interacting? 
        # Since the services use input(), we can't easily call register_student() without mocking.
        # But we can call the underlying write manually or modify the list and call write?
        # The services expose register_student() which calls input().
        # However, we modified the service to use FileService.write_csv
        # Let's just append to list and call write_csv directly to simulate what register_student does, 
        # enabling us to verify persistence without user input.
        
        print("Adding student directly...")
        StudentService.students.append({"id": new_student_id, "name": "Verification User"})
        FileService.write_csv('students.csv', StudentService.students, ['id', 'name'])
    
    # Register Course
    new_course_code = "VERIFY_C001"
    if not any(c['code'] == new_course_code for c in CoursesService.courses):
        print("Adding course directly...")
        CoursesService.courses.append({"code": new_course_code, "title": "Verify Course", "credit": 3})
        FileService.write_csv('courses.csv', CoursesService.courses, ['code', 'title', 'credit'])
        
    print("\n--- 3. Verifying File Content ---")
    # Read files back directly using FileService
    loaded_students = FileService.read_csv('students.csv')
    loaded_courses = FileService.read_csv('courses.csv')
    
    s_found = any(s['id'] == new_student_id for s in loaded_students)
    c_found = any(c['code'] == new_course_code for c in loaded_courses)
    
    print(f"Student '{new_student_id}' found in file: {s_found}")
    print(f"Course '{new_course_code}' found in file: {c_found}")
    
    if s_found and c_found:
        print("\nSUCCESS: Persistence verified.")
    else:
        print("\nFAILURE: Persistence check failed.")

if __name__ == "__main__":
    verify_persistence()
