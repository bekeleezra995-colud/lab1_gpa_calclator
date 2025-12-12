def calculate_total_credit(course_list):
    """Calculates total credit from a list of course objects."""
    if not course_list:
        return 0
    return sum(c['credit'] for c in course_list)

def calculate_total_grade_point(student_results, courses_list):
    """Calculates total grade points based on results and course info."""
    total_gp = 0
    for r in student_results:
        # Find corresponding course
        # Note: courses_list should be a list of dicts with 'code' and 'credit'
        course = next((c for c in courses_list if c["code"].lower() == r["course_code"].lower()), None)
        if course:
            total_gp += r["gp"] * course["credit"]
    return total_gp

def calculate_gpa_value(total_gp, total_credit):
    """Calculates GPA value."""
    if total_credit == 0:
        return 0.0
    return total_gp / total_credit