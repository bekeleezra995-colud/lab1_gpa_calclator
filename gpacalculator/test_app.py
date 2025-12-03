import sys
import os
import pytest

# Add the current directory to sys.path to allow imports
sys.path.append(os.path.join(os.getcwd(), 'gpacalculator'))

from courses.CoursesService import courses, register_course
from students.StudentService import students, register_student
from results.ResultService import results, add_result, grade_points, get_grade_point
from gradereports.GradeReport import calculate_total_credit, calculate_total_grade_point, calculate_gpa_value

@pytest.fixture
def cleanup_data():
    """Fixture to clear data before each test."""
    # Since we are using in-memory lists now, we just clear them.
    # Note: This will wipe the 'hardcoded' initial data as well, 
    # so we might need to be careful if tests rely on that initial data 
    # instead of setting up their own.
    # The current tests set up their own data, so clearing is fine and correct.
    courses.clear()
    students.clear()
    results.clear()
    yield
    courses.clear()
    students.clear()
    results.clear()

def test_calculate_total_credit():
    test_courses = [
        {"code": "C1", "credit": 5},
        {"code": "C2", "credit": 4},
        {"code": "C3", "credit": 3}
    ]
    total_credit = calculate_total_credit(test_courses)
    assert total_credit == 12

def test_calculate_total_grade_point():
    st_results = [
        {"course_code": "C1", "grade": "A", "gp": 4.0}, 
        {"course_code": "C2", "grade": "B", "gp": 3.0}
    ]
    course_info = [
        {"code": "C1", "credit": 5},
        {"code": "C2", "credit": 4}
    ]
    total_gp = calculate_total_grade_point(st_results, course_info)
    assert total_gp == 32.0

def test_calculate_gpa_value():
    gpa = calculate_gpa_value(32.0, 9)
    expected_gpa = 32.0 / 9
    assert abs(gpa - expected_gpa) < 0.001

def test_grade_point_lookup():
    assert get_grade_point("A") == 4.0
    assert get_grade_point("B+") == 3.5

def test_massive_course_registration(cleanup_data):
    """Refactored to use user-provided course list as 'Massive' data set."""
    user_courses = [
        {'code':'cosc101', 'title':'Programming I', 'credit':3},
        {'code':'cosc102', 'title':'Database System', 'credit':3},
        {'code':'cosc103', 'title':'Networking', 'credit':3},
        {'code':'cosc104', 'title':'Operating System', 'credit':3},
        {'code':'cosc105', 'title':'AI', 'credit':3}
    ]
    
    # Simulate loading process (direct append for testing logic or mocking input)
    
    courses.extend(user_courses)
    
    assert len(courses) == 5
    assert courses[0]['code'] == 'cosc101'
    assert courses[4]['title'] == 'AI'

def test_massive_student_grade_calculation(cleanup_data):
    """Refactored to use user-provided student grade list."""
    
    # 1. Setup Data
    user_courses = [
        {'code':'cosc101', 'title':'Programming I', 'credit':3},
        {'code':'cosc102', 'title':'Database System', 'credit':3},
        {'code':'cosc103', 'title':'Networking', 'credit':3},
        {'code':'cosc104', 'title':'Operating System', 'credit':3},
        {'code':'cosc105', 'title':'AI', 'credit':3}
    ]
    courses.extend(user_courses)
    
    student_grades = [
        {'studentid':'DBU10001', 'code':'CoSc101', 'letter':'A'},
        {'studentid':'DBU10001', 'code':'CoSc104', 'letter':'B+'},
        {'studentid':'DBU10001', 'code':'CoSc105', 'letter':'C'},
        {'studentid':'DBU10001', 'code':'CoSc102', 'letter':'B'},
        {'studentid':'DBU10001', 'code':'CoSc103', 'letter':'A-'}
    ]
    
    # 2. Register Student
    students.append({'id': 'DBU10001', 'name': 'Test Student'})
    
    # 3. Process Grades (Simulate adding results)
    for entry in student_grades:
        gp = get_grade_point(entry['letter'])
        results.append({
            "student_id": entry['studentid'],
            "course_code": entry['code'], # Stored as is
            "grade": entry['letter'],
            "gp": gp
        })
    # 4. Perform Calculation using library functions
    
    # Calculate total credit (sum of all credits for courses user took)
    # The user took 5 courses, all 3 credits each = 15 credits.
    current_calculated_credit = calculate_total_credit(user_courses)
    assert current_calculated_credit == 15
    
    # Calculate GP
    # We need to pass the student's results and the full course list (or ample course list) to the function
    student_res = [r for r in results if r['student_id'] == 'DBU10001']
    current_calculated_gp = calculate_total_grade_point(student_res, courses)
    
    # Expected: 48.75
    # A(4.0)*3 + B+(3.5)*3 + C(2.0)*3 + B(3.0)*3 + A-(3.75)*3
    # = 12 + 10.5 + 6 + 9 + 11.25 = 48.75
    assert abs(current_calculated_gp - 48.75) < 0.001, f"Expected 48.75, got {current_calculated_gp}"
    
    # Calculate GPA
    current_gpa = calculate_gpa_value(current_calculated_gp, current_calculated_credit)
    expected_gpa = 48.75 / 15 # 3.25
    
    assert abs(current_gpa - expected_gpa) < 0.001, f"Expected {expected_gpa}, got {current_gpa}"