def mark_attendance():
    print("\n--- Mark Attendance ---")

    student_id = input("Enter student ID: ")
    date = input("Enter date (DD-MM-YYYY): ")
    status = input("Enter attendance (Present/Absent): ")

    with open("data/attendance.txt", "a") as file:
        file.write(f"{student_id},{date},{status}\n")

    print("Attendance marked successfully!")


def view_attendance():
    print("\n--- Attendance Records ---")

    try:
        with open("data/attendance.txt", "r") as file:
            records = file.readlines()

        if not records:
            print("No attendance records found.")
            return

        for record in records:
            data = record.strip().split(",")

            print(
                f"Student ID: {data[0]} | "
                f"Date: {data[1]} | "
                f"Status: {data[2]}"
            )

    except FileNotFoundError:
        print("Attendance data file not found.")


def attendance_menu():
    while True:
        print("\n--- Attendance Management ---")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            mark_attendance()

        elif choice == "2":
            view_attendance()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")