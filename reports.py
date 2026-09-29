def hostel_report():
    print("\n--- Hostel Summary Report ---")

    try:
        with open("data/students.txt", "r") as file:
            students = file.readlines()

        with open("data/rooms.txt", "r") as file:
            rooms = file.readlines()

        with open("data/complaints.txt", "r") as file:
            complaints = file.readlines()

        print("\nTotal Students:", len(students))
        print("Total Rooms:", len(rooms))

        available_rooms = 0
        allocated_rooms = 0

        for room in rooms:
            data = room.strip().split(",")

            if len(data) >= 3:
                if data[2] == "Available":
                    available_rooms += 1
                else:
                    allocated_rooms += 1

        pending_complaints = 0
        resolved_complaints = 0

        for complaint in complaints:
            data = complaint.strip().split(",")

            if len(data) >= 3:
                if data[2] == "Pending":
                    pending_complaints += 1
                elif data[2] == "Resolved":
                    resolved_complaints += 1

        print("Available Rooms:", available_rooms)
        print("Allocated Rooms:", allocated_rooms)
        print("Pending Complaints:", pending_complaints)
        print("Resolved Complaints:", resolved_complaints)

    except FileNotFoundError:
        print("Required data file not found.")


def reports_menu():
    while True:
        print("\n--- Reports ---")
        print("1. Hostel Summary Report")
        print("2. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            hostel_report()

        elif choice == "2":
            break

        else:
            print("Invalid choice.")