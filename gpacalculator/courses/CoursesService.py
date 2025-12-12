from fileservices import FileService
# from fileservices.exceptions import PersistenceError # Removed

courses = []
try:
    courses = FileService.read_table('courses.txt')
except (OSError, ValueError):
    pass

def get_all_courses():
    return courses

def get_course_by_code(code):
    for c in courses:
        if c['code'].lower() == code.lower():
            return c
    return None

def create_course(code, title, credit):
    """
    Registers a new course.
    Raises ValueError for invalid inputs.
    Raises OSError on save failure.
    """
    if not code:
        raise ValueError("Course code cannot be empty.")
    if not title:
        raise ValueError("Course title cannot be empty.")
    try:
        credit = int(credit)
        if credit <= 0:
            raise ValueError("Credit must be positive.")
    except ValueError:
        raise ValueError("Credit must be a number.")

    if any(c['code'].lower() == code.lower() for c in courses):
        raise ValueError(f"Course with code {code} already exists.")

    courses.append({"code": code, "title": title, "credit": credit})
    try:
        FileService.write_table('courses.txt', courses, ['code', 'title', 'credit'])
    except OSError:
        courses.pop()
        raise