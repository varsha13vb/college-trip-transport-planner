
def add_passenger(passengers):
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    pickup = input("Enter Pickup Point: ")

    if not student_id or not name or not pickup:
        print("All fields are required!")
        return

    for passenger in passengers:
        if passenger["id"] == student_id:
            print("Student ID already exists!")
            return

    passenger = {
        "id": student_id,
        "name": name,
        "pickup": pickup
    }

    passengers.append(passenger)
    print("Passenger added successfully!")


def view_passengers(passengers):
    if not passengers:
        print("No passengers registered.")
        return

    print("\n===== PASSENGER DETAILS =====")

    for p in passengers:
        print(
            "SRN:", p["id"],
            "| Name:", p["name"],
            "| Pickup:", p["pickup"]
        )
