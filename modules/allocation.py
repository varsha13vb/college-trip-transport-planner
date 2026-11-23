def group_passengers(passengers):
    groups = {}

    for passenger in passengers:
        pickup = passenger["pickup"]

        if pickup not in groups:
            groups[pickup] = []

        groups[pickup].append(passenger)

    return groups


def allocate_buses(passengers, buses):
    allocations = {bus["bus_no"]: [] for bus in buses}

    groups = group_passengers(passengers)

    bus_index = 0

    for pickup, group in groups.items():

        for passenger in group:

            while bus_index < len(buses):

                bus = buses[bus_index]
                bus_no = bus["bus_no"]

                if len(allocations[bus_no]) < bus["capacity"]:
                    allocations[bus_no].append(passenger)
                    break

                bus_index += 1

            else:
                print("Not enough seats for:", passenger["name"])

    return allocations