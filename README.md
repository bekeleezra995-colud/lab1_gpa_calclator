# Student Grading System

## Description
This is a Python-based console application designed to manage student grades. It allows users to register students and courses, record grades, and calculate the Cumulative Grade Point Average (GPA) for students. The system uses a file-based storage approach to persist data across sessions.

## Features
- Register new students with ID and Name.
- Register new courses with Code, Title, and Credit hours.
- Record student grades for specific courses.
- Automatic Grade Point (GP) calculation based on the DBU grading system.
- Generate GPA reports showing course details and cumulative GPA.
- Data persistence using text files.
- Input validation and exception handling for robust operation.
- User-friendly command-line interface with ASCII art headers.

## Project Structure
The project is organized into the following modular structure:

lab1_gpa_calclator/
    gpacalculator/
        app.py                  # Main entry point of the application
        courses/                # Module for course management
            CoursesService.py   # Logic for registering and listing courses
        students/               # Module for student management
            StudentService.py   # Logic for registering and listing students
        results/                # Module for result management
            ResultService.py    # Logic for adding and listing results
        gradereports/           # Module for report generation
            GradeReport.py      # Logic for calculating and displaying GPA

## Prerequisites
- Python 3.x installed on your system.

## How to Run
1. Open your terminal or command prompt.
2. Navigate to the project directory:
   cd d:/CS-Studies 2025-2026/Bekele/lab1_gpa_calclator/gpacalculator
3. Run the application using Python:
   python app.py

## Application Workflows

This section outlines the step-by-step navigation for each feature in the application.

### 1. Student Management
- Register a New Student
  
  Main Menu [1] -> Student Menu [1] Register Student -> Enter ID -> Enter Name
  
- View All Students
  
  Main Menu [1] -> Student Menu [2] List Students
  
- Return to Main Menu
  
  Main Menu [1] -> Student Menu [3] Back
  

### 2. Course Management
- Register a New Course
  
  Main Menu [2] -> Course Menu [1] Register Course -> Enter Code -> Enter Title -> Enter Credit
  
- View All Courses
  
  Main Menu [2] -> Course Menu [2] List Courses
  
- Return to Main Menu
  
  Main Menu [2] -> Course Menu [3] Back
  

### 3. Result Management
- Record a Grade
  
  Main Menu [3] -> Result Menu [1] Add Result -> Enter Student ID -> Enter Course Code -> Enter Grade
  
- View All Results
  
  Main Menu [3] -> Result Menu [2] List Results
  
- Return to Main Menu
  
  Main Menu [3] -> Result Menu [3] Back
  

### 4. GPA Reporting
- Generate Student Transcript
  
  Main Menu [4] -> GPA Report [1] Calculate GPA -> Enter Student ID
  
  *(Displays Course list, Grades, Credits, Total GP, and Cumulative GPA)*
- Return to Main Menu
  
  Main Menu [4] -> GPA Report [2] Back
  

## Grading System
The application uses the following grading scale:
- A+ : 4.0
- A  : 4.0
- A- : 3.75
- B+ : 3.50
- B  : 3.00
- B- : 2.75
- C+ : 2.50
- C  : 2.00
- C- : 1.75
- D  : 1.00
- F  : 0.00

## Author
BEKELE SHIMELS