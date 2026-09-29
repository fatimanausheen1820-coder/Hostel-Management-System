def add_complaint():
    print("\n--- Register Complaint ---")

    student_id = input("Enter student ID: ")
    complaint = input("Enter complaint: ")

    with open("data/complaints.txt", "a") as file:
        file.write(f"{student_id},{complaint},Pending\n")

    print("Complaint registered successfully!")


def view_complaints():
    print("\n--- Complaint Records ---")

    try:
        with open("data/complaints.txt", "r") as file:
            complaints = file.readlines()

        if not complaints:
            print("No complaints found.")
            return

        for complaint in complaints:
            data = complaint.strip().split(",")

            print(
                f"Student ID: {data[0]} | "
                f"Complaint: {data[1]} | "
                f"Status: {data[2]}"
            )

    except FileNotFoundError:
        print("Complaint data file not found.")


def resolve_complaint():
    print("\n--- Resolve Complaint ---")

    student_id = input("Enter student ID: ")

    try:
        with open("data/complaints.txt", "r") as file:
            complaints = file.readlines()

        updated_complaints = []
        found = False

        for complaint in complaints:
            data = complaint.strip().split(",")

            if data[0] == student_id and data[2] == "Pending":
                data[2] = "Resolved"
                found = True

            updated_complaints.append(",".join(data) + "\n")

        if found:
            with open("data/complaints.txt", "w") as file:
                file.writelines(updated_complaints)

            print("Complaint resolved successfully!")
        else:
            print("Pending complaint not found.")

    except FileNotFoundError:
        print("Complaint data file not found.")


def complaint_menu():
    while True:
        print("\n--- Complaint Management ---")
        print("1. Register Complaint")
        print("2. View Complaints")
        print("3. Resolve Complaint")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_complaint()

        elif choice == "2":
            view_complaints()

        elif choice == "3":
            resolve_complaint()

        elif choice == "4":
            break

        else:
            print("Invalid choice.")