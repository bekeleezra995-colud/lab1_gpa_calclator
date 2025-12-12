from fileservices import FileService
from students import StudentService
from courses import CoursesService

grade_points = {
    'A': 4.0, 'A-': 3.75, 'B+': 3.5, 'B': 3.0,
    'B-': 2.75, 'C+': 2.5, 'C': 2.0, 'C-': 1.75,
    'D': 1.0, 'F': 0.0
}

def get_grade_point(grade):
    return grade_points.get(grade, 0.0)

results = []
try:
    results = FileService.read_table('results.txt')
except (OSError, ValueError):
    pass

def get_all_results():
    return results

def get_results_by_student(student_id):
    return [r for r in results if r['student_id'] == student_id]

def create_result(student_id, course_code, grade):
    """
    Adds or updates a result.
    Raises ValueError for invalid inputs.
    Raises OSError on save failure.
    """
    if not student_id:
        raise ValueError("Student ID required.")
    if not course_code:
        raise ValueError("Course Code required.")
    
    # Validation
    student = StudentService.get_student_by_id(student_id)
    if not student:
        raise ValueError(f"Student {student_id} not found.")
        
    course = CoursesService.get_course_by_code(course_code)
    if not course:
        raise ValueError(f"Course {course_code} not found.")
        
    grade = grade.upper()
    if grade not in grade_points:
        raise ValueError(f"Invalid grade. Allowed: {', '.join(grade_points.keys())}")
        
    gp = grade_points[grade]

    # Update existing
    for r in results:
        if r['student_id'] == student_id and r['course_code'].lower() == course_code.lower():
            old_grade = r['grade']
            old_gp = r['gp']
            r['grade'] = grade
            r['gp'] = gp
            try:
                FileService.write_table('results.txt', results, ['student_id', 'course_code', 'grade', 'gp'])
            except OSError:
                # Rollback in-memory
                r['grade'] = old_grade
                r['gp'] = old_gp
                raise
            return

    # Add new
    new_result = {"student_id": student_id, "course_code": course_code.upper(), "grade": grade, "gp": gp}
    results.append(new_result)
    try:
        FileService.write_table('results.txt', results, ['student_id', 'course_code', 'grade', 'gp'])
    except OSError:
        results.pop()
        raise
