import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from courses import CoursesService
from gradereports.GradeReport import calculate_total_credit

@pytest.fixture
def cleanup_courses():
    CoursesService.courses.clear()
    yield
    CoursesService.courses.clear()

def test_calculate_total_credit():
    test_courses = [
        {"code": "C1", "credit": 5},
        {"code": "C2", "credit": 4},
        {"code": "C3", "credit": 3}
    ]
    total_credit = calculate_total_credit(test_courses)
    assert total_credit == 12

def test_create_course(cleanup_courses):
    """Migrated from test_app.py."""
    user_courses = [
        {'code':'cosc101', 'title':'Programming I', 'credit':3},
        {'code':'cosc102', 'title':'Database System', 'credit':3},
        {'code':'cosc103', 'title':'Networking', 'credit':3},
        {'code':'cosc104', 'title':'Operating System', 'credit':3},
        {'code':'cosc105', 'title':'AI', 'credit':3}
    ]
    
    for c in user_courses:
        CoursesService.create_course(c['code'], c['title'], c['credit'])
    
    courses = CoursesService.get_all_courses()
    assert len(courses) == 5
    assert courses[0]['code'] == 'cosc101'
    assert courses[4]['title'] == 'AI'
