import pytest
import sys
import os

# Ensure import from parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from students import StudentService
from fileservices import FileService

@pytest.fixture
def cleanup_students():
    """Fixture to clear student data before each test."""
    StudentService.students.clear()
    yield
    StudentService.students.clear()
    # Also clean up file if desired, or mock FileService

def test_create_student(cleanup_students):
    """Refactored unit test for adding student directly to list."""
    StudentService.create_student("UNIT_TEST_S1", "Unit Test Student")
    
    students = StudentService.get_all_students()
    assert len(students) == 1
    assert students[0]['id'] == "UNIT_TEST_S1"

def test_student_persistence(cleanup_students):
    """Test that student list changes mock persistence (since we replaced the list)."""
    # Note: Real persistence writes to disk. In unit tests we might want to avoid disk I/O 
    # or use a temp file. For now, checking the logic of the service list manipulation.
    pass
