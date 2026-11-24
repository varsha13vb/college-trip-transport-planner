
from modules.passenger import add_passenger, view_passengers
from modules.bus import add_bus, view_buses
from modules.allocation import group_passengers, allocate_buses
from modules.reports import generate_passenger_lists


# Hardcoded sample passenger data

passengers = [
    {"id": "101", "name": "Aarav", "pickup": "Dharwad"},
    {"id": "102", "name": "Anu", "pickup": "Hubballi"},
    {"id": "103", "name": "Ravi", "pickup": "Bengaluru"},
    {"id": "104", "name": "Diya", "pickup": "Mysuru"},
    {"id": "105", "name": "Arjun", "pickup": "Belagavi"},
    {"id": "106", "name": "Meera", "pickup": "Mangaluru"},
    {"id": "107", "name": "Adi", "pickup": "Davanagere"},
    {"id": "108", "name": "Sana", "pickup": "Shivamogga"},
    {"id": "109", "name": "Vikram", "pickup": "Udupi"},
    {"id": "110", "name": "Isha", "pickup": "Tumakuru"},
    {"id": "111", "name": "Kiran", "pickup": "Dharwad"},
    {"id": "112", "name": "Priya", "pickup": "Hubballi"},
    {"id": "113", "name": "Rahul", "pickup": "Bengaluru"},
    {"id": "114", "name": "Nisha", "pickup": "Mysuru"},
    {"id": "115", "name": "Sid", "pickup": "Belagavi"},
    {"id": "116", "name": "Kavya", "pickup": "Mangaluru"},
    {"id": "117", "name": "Manu", "pickup": "Davanagere"},
    {"id": "118", "name": "Aisha", "pickup": "Shivamogga"},
    {"id": "119", "name": "Dev", "pickup": "Udupi"},
    {"id": "120", "name": "Pooja", "pickup": "Tumakuru"},
    {"id": "121", "name": "Neil", "pickup": "Dharwad"},
    {"id": "122", "name": "Tanvi", "pickup": "Hubballi"},
    {"id": "123", "name": "Hari", "pickup": "Bengaluru"},
    {"id": "124", "name": "Riya", "pickup": "Mysuru"},
    {"id": "125", "name": "Akash", "pickup": "Belagavi"},
    {"id": "126", "name": "Sneha", "pickup": "Mangaluru"},
    {"id": "127", "name": "Varun", "pickup": "Davanagere"},
    {"id": "128", "name": "Maya", "pickup": "Shivamogga"},
    {"id": "129", "name": "Kabir", "pickup": "Udupi"},
    {"id": "130", "name": "Sana", "pickup": "Tumakuru"},
    {"id": "131", "name": "Nikhil", "pickup": "Dharwad"},
    {"id": "132", "name": "Lavi", "pickup": "Hubballi"},
    {"id": "133", "name": "Om", "pickup": "Bengaluru"},
    {"id": "134", "name": "Tara", "pickup": "Mysuru"},
    {"id": "135", "name": "Yash", "pickup": "Belagavi"}
]


# Hardcoded sample bus data
buses = [
    {"bus_no": "KA01AB1234", "capacity": 10},
    {"bus_no": "KA01CD5678", "capacity": 10},
    {"bus_no": "KA01EF9012", "capacity": 8},
    {"bus_no": "KA02CD3344", "capacity": 9}
]

allocations = {}


while True:

    print("\n===== COLLEGE TRIP TRANSPORT PLANNER =====")
    print("1. Add Passenger")
    print("2. View Passengers")
    print("3. Add Bus")
    print("4. View Buses")
    print("5. Group Passengers by Pickup Point")
    print("6. Allocate Passengers to Buses")
    print("7. Generate Passenger Lists")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_passenger(passengers)

    elif choice == "2":
        view_passengers(passengers)

    elif choice == "3":
        add_bus(buses)

    elif choice == "4":
        view_buses(buses)

    elif choice == "5":
        groups = group_passengers(passengers)

        if not groups:
            print("No passengers available.")
        else:
            print("\n===== PASSENGER GROUPS =====")
            for pickup, group in groups.items():
                print(pickup, ":", len(group), "passengers")

    elif choice == "6":
        allocations = allocate_buses(passengers, buses)
        if allocations:
            print("Bus allocation completed!")

    elif choice == "7":
        if not allocations:
            print("Please allocate passengers first.")
        else:
            generate_passenger_lists(allocations, buses)

    elif choice == "8":
        print("Thank you for using the planner!")
        break

    else:
        print("Invalid choice! Try again.")
