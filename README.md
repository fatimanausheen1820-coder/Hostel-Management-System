# Hostel Management System

## Project Overview

The Hostel Management System is a console-based Python application designed to manage basic hostel operations.

The system uses Python and file handling to store and retrieve hostel data.

## Features

### Student Management
- Add student
- View students
- Search student
- Validate student details

### Room Management
- Add room
- View rooms
- Allocate room
- Vacate room
- Validate room number

### Fee Management
- Add fee payment
- View fee records
- Validate fee amount

### Complaint Management
- Register complaint
- View complaints
- Resolve complaints

### Attendance Management
- Mark attendance
- View attendance records

### Reports
- View total students
- View total rooms
- View available rooms
- View allocated rooms
- View pending complaints
- View resolved complaints

## Technologies Used

- Python
- File Handling
- VS Code
- Git
- GitHub

## Project Structure

```text
hostel management system/
│
├── data/
│   ├── attendance.txt
│   ├── complaints.txt
│   ├── fees.txt
│   ├── rooms.txt
│   └── students.txt
│
├── tests/
│   └── test_validation.py
│
├── attendance.py
├── complaints.py
├── fees.py
├── main.py
├── reports.py
├── room.py
├── student.py
├── validation.py
├── README.md
└── .gitignore

## Non-Functional Requirements

### 1. Usability
The system should provide a simple and easy-to-understand console interface
so that hostel staff can perform common operations easily.

### 2. Reliability
The system should correctly store and retrieve hostel records using text files
and handle missing data files without crashing.

### 3. Maintainability
The project is divided into separate Python modules for students, rooms, fees,
complaints, attendance, reports, and validation.

### 4. Error Handling
The system validates important inputs and displays appropriate error messages
for invalid data and missing files.

### 5. Resource Efficiency
The application uses simple Python file handling and does not require a
database server or external services.
