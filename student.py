from validation import validate_student_id, validate_age, validate_room_number
def add_student():
    print("\n---Add Student---")
    student_id = input("Enter student ID:")
    name = input("Enter student name:")
    age = input("Enter student age:")
    course = input("enter course:")
    room_no = input("Enter room number:")
    if not validate_student_id(student_id):
        print("Invalid student ID.")
        return
    if not validate_age(age):
        print("Invalid age.")
        return
    if not validate_room_number(room_no):
        print("Invalid room number.")
        return
    with open("data/students.txt", "a") as file:
        file.write(f"{student_id},{name},{age},{course},{room_no}\n")
    print("Student added successfully!")

def view_student():
    print("\n---Student List---")
    try:
        with open("data/students.txt", "r") as file:
            students = file.readlines()
        if not students:
            print("No students found.")
            return
        for student in students:
            data = student.strip().split(",")
            print(f"ID:{data[0]}|"f"Name:{data[1]}|"f"Age:{data[2]}|"f"Course:{data[3]}|"f"Room:{data[4]}|")
    except FileNotFoundError:
        print("Students data file not found.")
def search_student():
    print("\n---Search Student---")
    student_id = input("Enter student ID:")
    try:
        with open("data/students.txt","r") as file:
            students = file.readlines()
        for student in students:
            data = student.strip().split(",")
            if data[0] == student_id:
                print("\nStudent found!")
                print("ID:",data[0])
                print("Name:",data[1])
                print("Age:",data[2])
                print("Course:",data[3])
                print("Room:",data[4])
                return
            print("student not found.")
    except FileNotFoundError:
        print("Student data file not found.")

def student_menu():
    while True:
        print("\n---Student Management---")
        print("1. Add student")
        print("2. View students")
        print("3. Search students")
        print("4. back")
        choice = input("Enter your choice (1-4):")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")