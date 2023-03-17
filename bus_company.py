class Bus:
    bus_list = []

    def __init__(self, bus_number, route_key, driver):
        self.bus_number = bus_number  # Integer
        self.route_key = route_key
        self.driver = driver
        self.bus_list.append(self)

    def display_info(self):
        for bus in self.bus_list:
            if bus == self:
                print(f"Bus number = {bus.bus_number} on route "
                      f"{bus.route_key} with driver {bus.driver}")


# Instantiate 3 student objects
bus1 = Bus(2010, "Y", "Jack")
bus2 = Bus(2000, "P", "Greg")
bus3 = Bus(1570, "130", "Steve")

# print information
for bus in range (len(Bus.bus_list)):
    Bus.display_info(Bus.bus_list[bus])
