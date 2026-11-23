from modules.passenger import add_passenger, view_passengers
from modules.bus import add_bus, view_buses
from modules.allocation import group_passengers, allocate_buses
from modules.reports import generate_passenger_lists


passengers = []
buses = []
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

        for pickup, group in groups.items():
            print(pickup, ":", len(group), "passengers")

    elif choice == "6":
        allocations = allocate_buses(passengers, buses)
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