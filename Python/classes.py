class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3);

customers = ["Kerim", "Rahym", "Dovlet", "Sukur"]

for customer in customers:
    if flight.add_passenger(customer):
        print(f"Customer {customer} successfully added")
    else:
        print(f"No available seat for {customer}")
