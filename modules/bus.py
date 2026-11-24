
def add_bus(buses):
    bus_no = input("Enter Bus Number: ")

    if not bus_no:
        print("Bus number is required!")
        return

    for bus in buses:
        if bus["bus_no"] == bus_no:
            print("Bus already exists!")
            return

    try:
        capacity = int(input("Enter Seating Capacity: "))

        if capacity <= 0:
            print("Capacity must be greater than zero.")
            return

        buses.append({
            "bus_no": bus_no,
            "capacity": capacity
        })

        print("Bus added successfully!")

    except ValueError:
        print("Enter a valid number!")


def view_buses(buses):
    if not buses:
        print("No buses registered.")
        return

    print("\n===== BUS DETAILS =====")

    for bus in buses:
        print(
            "Bus:", bus["bus_no"],
            "| Capacity:", bus["capacity"]
        )
