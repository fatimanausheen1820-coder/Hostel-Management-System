from validation import validate_student_id, validate_amount
def add_fee():
    print("\n--- Add Fee Payment ---")

    student_id = input("Enter student ID: ")
    if not validate_student_id(student_id):
        print("Invalid student ID.")
        return

    amount = input("Enter fee amount: ")
    if not validate_amount(amount):
        print("Invalid fee amount.")
        return

    month = input("Enter month: ")

    with open("data/fees.txt", "a") as file:
        file.write(f"{student_id},{amount},{month},Paid\n")

    print("Fee payment recorded successfully!")


def view_fees():
    print("\n--- Fee Records ---")

    try:
        with open("data/fees.txt", "r") as file:
            fees = file.readlines()

        if not fees:
            print("No fee records found.")
            return

        for fee in fees:
            data = fee.strip().split(",")

            print(
                f"Student ID: {data[0]} | "
                f"Amount: {data[1]} | "
                f"Month: {data[2]} | "
                f"Status: {data[3]}"
            )

    except FileNotFoundError:
        print("Fee data file not found.")


def fee_menu():
    while True:
        print("\n--- Fee Management ---")
        print("1. Add Fee Payment")
        print("2. View Fee Records")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_fee()

        elif choice == "2":
            view_fees()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")