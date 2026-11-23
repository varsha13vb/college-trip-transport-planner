def generate_passenger_lists(allocations, buses):

    for bus in buses:

        bus_no = bus["bus_no"]
        passengers = allocations.get(bus_no, [])

        print("\n==========================")
        print("BUS:", bus_no)
        print("==========================")

        if not passengers:
            print("No passengers assigned.")

        for i, passenger in enumerate(passengers, start=1):
            print(
                i,
                passenger["name"],
                "-",
                passenger["pickup"]
            )

        occupied = len(passengers)
        available = bus["capacity"] - occupied

        print("--------------------------")
        print("Occupied Seats:", occupied)
        print("Available Seats:", available)