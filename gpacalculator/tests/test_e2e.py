import pytest
import sys
import os

# Ensure proper import paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from students import StudentService
from courses import CoursesService
from results import ResultService
from gradereports.GradeReport import calculate_total_credit, calculate_total_grade_point, calculate_gpa_value

@pytest.fixture
def cleanup_e2e_data():
    """Fixture to ensure a clean state for E2E testing."""
    StudentService.students.clear()
    CoursesService.courses.clear()
    ResultService.results.clear()
    yield
    # Cleanup after test
    StudentService.students.clear()
    CoursesService.courses.clear()
    ResultService.results.clear()

def test_full_gpa_calculation_flow(cleanup_e2e_data):
    """
    End-to-End Test Scenario:
    1. Register a student.
    2. Register courses.
    3. Add results for the student (Simulating 'Grade' entry).
    4. Calculate GPA and verify the output.
    """
    print("\n--- Starting E2E Test ---")

    # 1. Register Student
    student_id = "E2E_S01"
    student_name = "End To End Student"
    StudentService.create_student(student_id, student_name)
    
    # Verify student added
    assert len(StudentService.students) == 1
    assert StudentService.students[0]['id'] == student_id

    # 2. Register Courses
    c1_code = "E2E101"
    c2_code = "E2E102"
    CoursesService.create_course(c1_code, "Test Course 1", 4)
    CoursesService.create_course(c2_code, "Test Course 2", 3)

    # Verify courses added
    assert len(CoursesService.courses) == 2

    # 3. Add Results
    ResultService.create_result(student_id, c1_code, "A")
    ResultService.create_result(student_id, c2_code, "B")

    # Verify results added
    assert len(ResultService.results) == 2

    # 4. Calculate GPA
    # Fetch results for student
    student_results = [r for r in ResultService.results if r['student_id'] == student_id]
    
    # Calculate totals
    total_credits = calculate_total_credit(CoursesService.courses)
    # Note: calculate_total_credit sums ALL courses in the system. 
    # In a real scenario, we usually want credits for courses taken by the student.
    # However, existing logic in GradeReport might assume provided list is the list of courses taken?
    # Let's check calculate_total_credit implementation via reading if needed. 
    # Based on previous tests: total_credit = calculate_total_credit(test_courses)
    # It sums the credit of the list passed. 
    
    # So we should filter courses taken by student roughly, or if the system assumes student takes all courses in that context.
    # Let's filter courses list to only those relevant to results.
    courses_taken_codes = [r['course_code'] for r in student_results]
    courses_taken = [c for c in CoursesService.courses if c['code'] in courses_taken_codes]
    
    calculated_credits = calculate_total_credit(courses_taken)
    assert calculated_credits == 7
    
    calculated_gp = calculate_total_grade_point(student_results, courses_taken)
    assert calculated_gp == 25.0
    
    gpa = calculate_gpa_value(calculated_gp, calculated_credits)
    
    print(f"Calculated GPA: {gpa}")
    
    assert abs(gpa - (25.0 / 7)) < 0.001
    
    print("--- E2E Test Passed ---")
