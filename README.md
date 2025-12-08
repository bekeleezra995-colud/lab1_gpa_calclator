# Student Grading System

## Description
This is a Python-based console application designed to manage student grades. It allows users to register students and courses, record grades, and calculate the Cumulative Grade Point Average (GPA) for students. The system uses a file-based storage approach to persist data across sessions.

## Features
- Register new students with ID and Name.##     
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
        fileservice/            # Module for file operations
            data/               # Directory where text files are saved
            FileService.py      # Handles reading and writing to files
        courses/                # Module for course management
            CoursesService.py   # Logic for registering and listing courses
        students/               # Module for student management
            StudentService.py   # Logic for registering and listing students
        results/                # Module for result management
            ResultService.py    # Logic for adding and listing results
        gradereports/           # Module for report generation
            GradeReport.py      # Logic for calculating and displaying GPA
            <img width="215" height="305" alt="image" src="https://github.com/user-attachments/assets/a5c54737-47fe-45dd-bc71-e4bff8776499" />


COURSE MANAGEMENT SYSTEM — FLOWCHART(  sample )
                                   ┌────────────────────────┐
                  │ Start Program          │
                  └───────────┬────────────┘
                              │
                              ▼
                ┌───────────────────────────┐
                │ Load courses from file     │
                │ (load_courses_from_file)   │
                └───────────┬────────────────┘
                            │
                            ▼
              ┌─────────────────────────────┐
              │ Display Course Menu          │
              ├─────────────────────────────┤
              │ 1. Register Course           │
              │ 2. List Courses              │
              │ 3. Back / Exit               │
              └───────────┬─────────────────┘
                          │
                          ▼
              ┌─────────────────────┐
              │ Read user choice    │
              └───────────┬────────┘
                          │
     ┌────────────────────┼──────────────────────────┐
     │                    │                          │
     ▼                    ▼                          ▼
┌─────────────┐   ┌────────────────┐         ┌────────────────────┐
│ Choice = 1  │   │ Choice = 2     │         │ Choice = 3         │
│ Register    │   │ List Courses   │         │ Exit Menu          │
└──────┬──────┘   └───────┬────────┘         └────────┬───────────┘
       │                  │                           │
       ▼                  ▼                           ▼
┌───────────────────┐   ┌───────────────────┐   ┌───────────────┐
│ Input course code  │   │ Are there courses?│   │ End Program    │
│ Input title        │   └────────┬──────────┘   └───────────────┘
│ Input credit       │            │
└───────────┬────────┘            ▼
            │               ┌────────────────┐
            ▼               │ Print courses   │
  ┌───────────────────┐     └────────────────┘
  │ Add to list        │
  │ Save to file       │
  │ (save_courses...)  │
  └─────────┬──────────┘
            │
            ▼
     ┌───────────────┐
     │ Return to Menu │
     └───────────────┘


 
    




## Prerequisites
- Python 3.x installed on your system.

## How to Run
1. Open your terminal or command prompt.
2. Navigate to the project directory:
   cd d:/CS-Studies 2025-2026/Bekele/lab1_gpa_calclator/gpacalculator
3. Run the application using Python:
   python app.py

## Usage Guide

### Main Menu
Upon running the application, you will see the main menu with the following options:
1. Student Menu
2. Course Menu
3. Result Menu
4. GPA Report
5. Exit

### Student Menu
- Register Student: Enter a unique Student ID and Name.
- List Students: View all registered students.

### Course Menu
- Register Course: Enter a unique Course Code, Title, and Credit hours.
- List Courses: View all registered courses.

### Result Menu
- Add Result: Enter Student ID, Course Code, and Grade (e.g., A, B+, C).
- List Results: View all recorded results.

### GPA Report
- Calculate GPA: Enter a Student ID to view their full transcript, including total credits, total grade points, and cumulative GPA.

## Grading System
The application uses the following grading scale:
- A+=90-100: 4.0
- A =85-89 : 4.0
- A-=80-84 : 3.75
- B+=75-79 : 3.50
- B =70-74 : 3.00
- B-=65-69 : 2.75
- C+=60-64 : 2.50
- C=55-59  : 2.00
- C-=50-54 : 1.75
- D=40-49  : 1.00
- F=below 40  : 0.00

## Author                 ID
Bekele Shimels...........dbu1700411
Birhanu Alagaw...........dbu1701340
