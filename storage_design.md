# Storage Design

## Storage Method

The Hostel Management System uses text files for persistent data storage.

The data files are stored inside the `data/` folder.

## Data Files

| File | Purpose | Data Stored |
|------|---------|-------------|
| students.txt | Student records | ID, name, age, course, room number |
| rooms.txt | Room records | Room number, capacity, status |
| fees.txt | Fee records | Student ID, amount, month, status |
| complaints.txt | Complaint records | Student ID, complaint, status |
| attendance.txt | Attendance records | Student ID, date, attendance status |

## Storage Structure

```text
data/
│
├── students.txt
├── rooms.txt
├── fees.txt
├── complaints.txt
└── attendance.txt