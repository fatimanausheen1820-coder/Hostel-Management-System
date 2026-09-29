from student import student_menu
from room import room_menu
from fees import fee_menu
from complaints import complaint_menu
from attendance import attendance_menu
from reports import reports_menu
def main_menu():
    while True:
        print("\n"+"=" *40)
        print("HOSTEL MANAGEMENT SYSTEM")
        print("\n"+"=" *40)
        print("1. Student Management")
        print("2. Room Management")
        print("3. Fee Management")
        print("4. Complaint Management")
        print("5. Attendance Management")
        print("6. Reports")
        print("7. Exit")
        choice=input("\nEnter your choice (1-7):")
        if choice == "1":
            student_menu()
        elif choice =="2":
            room_menu()
        elif choice == "3":
            fee_menu()
        elif choice == "4":
            complaint_menu()
        elif choice == "5":
            attendance_menu()
        elif choice == "6":
            reports_menu()
        elif choice == "7":
            print("\nThank you for using Hostel Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 7.")
if __name__ == "__main__":
    main_menu()
