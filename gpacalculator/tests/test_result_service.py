import pytest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from results import ResultService
from courses import CoursesService
from students import StudentService
from gradereports.GradeReport import calculate_total_grade_point, calculate_gpa_value

@pytest.fixture
def cleanup_data():
    ResultService.results.clear()
    CoursesService.courses.clear()
    StudentService.students.clear()
    yield
    ResultService.results.clear()
    CoursesService.courses.clear()
    StudentService.students.clear()

def test_get_grade_point():
    assert ResultService.get_grade_point("A") == 4.0
    assert ResultService.get_grade_point("B+") == 3.5

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

def test_create_result(cleanup_data):
    """Refactored massive calculation test."""
    
    # 1. Setup Data
    user_courses = [
        {'code':'cosc101', 'title':'Programming I', 'credit':3},
        {'code':'cosc102', 'title':'Database System', 'credit':3},
        {'code':'cosc103', 'title':'Networking', 'credit':3},
        {'code':'cosc104', 'title':'Operating System', 'credit':3},
        {'code':'cosc105', 'title':'AI', 'credit':3}
    ]
    for c in user_courses:
        CoursesService.create_course(c['code'], c['title'], c['credit'])
    
    student_grades = [
        {'studentid':'DBU10001', 'code':'CoSc101', 'letter':'A'},
        {'studentid':'DBU10001', 'code':'CoSc104', 'letter':'B+'},
        {'studentid':'DBU10001', 'code':'CoSc105', 'letter':'C'},
        {'studentid':'DBU10001', 'code':'CoSc102', 'letter':'B'},
        {'studentid':'DBU10001', 'code':'CoSc103', 'letter':'A-'}
    ]
    
    # 2. Register Student
    StudentService.create_student('DBU10001', 'Test Student')
    
    # 3. Process Grades
    for entry in student_grades:
        ResultService.create_result(entry['studentid'], entry['code'], entry['letter'])
    
    student_res = ResultService.get_results_by_student('DBU10001')
    current_calculated_gp = calculate_total_grade_point(student_res, CoursesService.get_all_courses())
    
    assert abs(current_calculated_gp - 48.75) < 0.001
