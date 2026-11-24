
def group_passengers(passengers):
    groups = {}

    for passenger in passengers:
        pickup = passenger["pickup"]

        if pickup not in groups:
            groups[pickup] = []

        groups[pickup].append(passenger)

    return groups


def allocate_buses(passengers, buses):

    if not passengers:
        print("No passengers available for allocation.")
        return {}

    if not buses:
        print("No buses available!")
        return {}

    allocations = {bus["bus_no"]: [] for bus in buses}

    groups = group_passengers(passengers)

    # Sort pickup groups from largest to smallest
    sorted_groups = sorted(
        groups.items(),
        key=lambda item: len(item[1]),
        reverse=True
    )

    unallocated_groups = []

    for pickup, group in sorted_groups:

        group_size = len(group)
        assigned = False

        # Find a bus with enough seats for the entire group
        for bus in buses:

            bus_no = bus["bus_no"]
            available_seats = bus["capacity"] - len(allocations[bus_no])

            if available_seats >= group_size:

                allocations[bus_no].extend(group)
                assigned = True

                print(
                    pickup,
                    "-",
                    group_size,
                    "passengers allocated to",
                    bus_no
                )

                break

        if not assigned:
            unallocated_groups.append((pickup, group))

    # Display allocation summary
    print("\n===== ALLOCATION SUMMARY =====")

    allocated_count = sum(
        len(passenger_list)
        for passenger_list in allocations.values()
    )

    unallocated_count = sum(
        len(group)
        for pickup, group in unallocated_groups
    )

    print("Total Passengers:", len(passengers))
    print("Allocated Passengers:", allocated_count)
    print("Unallocated Passengers:", unallocated_count)

    if unallocated_groups:

        print("\n===== GROUPS NOT ALLOCATED =====")

        for pickup, group in unallocated_groups:
            print(
                pickup,
                "-",
                len(group),
                "passengers could not be allocated together"
            )

    else:
        print("\nAll pickup groups allocated successfully!")

    # Display bus-wise seat availability
    print("\n===== BUS CAPACITY DETAILS =====")

    for bus in buses:

        bus_no = bus["bus_no"]
        occupied = len(allocations[bus_no])
        available = bus["capacity"] - occupied

        print("\nBus:", bus_no)
        print("Occupied Seats:", occupied)
        print("Available Seats:", available)

    return allocations
