from validation import validate_room_number
def add_room():
    print("\n--- Add Room ---")

    room_no = input("Enter room number: ")
    if not validate_room_number(room_no):
        print("Invalid room number.")
        return

    capacity = input("Enter room capacity: ")

    with open("data/rooms.txt", "a") as file:
        file.write(f"{room_no},{capacity},Available\n")

    print("Room added successfully!")


def view_rooms():
    print("\n--- Room List ---")

    try:
        with open("data/rooms.txt", "r") as file:
            rooms = file.readlines()

        if not rooms:
            print("No room records found.")
            return

        for room in rooms:
            data = room.strip().split(",")

            print(
                f"Room No: {data[0]} | "
                f"Capacity: {data[1]} | "
                f"Status: {data[2]}"
            )

    except FileNotFoundError:
        print("Room data file not found.")


def allocate_room():
    print("\n--- Allocate Room ---")

    room_no = input("Enter room number: ")
    student_id = input("Enter student ID: ")

    try:
        with open("data/rooms.txt", "r") as file:
            rooms = file.readlines()

        updated_rooms = []
        found = False

        for room in rooms:
            data = room.strip().split(",")

            if data[0] == room_no:
                if data[2] == "Available":
                    data[2] = f"Allocated-{student_id}"
                    found = True

            updated_rooms.append(",".join(data) + "\n")

        if found:
            with open("data/rooms.txt", "w") as file:
                file.writelines(updated_rooms)

            print("Room allocated successfully!")
        else:
            print("Room not available or room not found.")

    except FileNotFoundError:
        print("Room data file not found.")


def vacate_room():
    print("\n--- Vacate Room ---")

    room_no = input("Enter room number: ")

    try:
        with open("data/rooms.txt", "r") as file:
            rooms = file.readlines()

        updated_rooms = []
        found = False

        for room in rooms:
            data = room.strip().split(",")

            if data[0] == room_no:
                data[2] = "Available"
                found = True

            updated_rooms.append(",".join(data) + "\n")

        if found:
            with open("data/rooms.txt", "w") as file:
                file.writelines(updated_rooms)

            print("Room vacated successfully!")
        else:
            print("Room not found.")

    except FileNotFoundError:
        print("Room data file not found.")


def room_menu():
    while True:
        print("\n--- Room Management ---")
        print("1. Add Room")
        print("2. View Rooms")
        print("3. Allocate Room")
        print("4. Vacate Room")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_room()

        elif choice == "2":
            view_rooms()

        elif choice == "3":
            allocate_room()

        elif choice == "4":
            vacate_room()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")