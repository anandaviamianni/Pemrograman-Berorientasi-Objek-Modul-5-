class Airplane():
    def __init__(self, airline, plane_type):
        self.airline = airline
        self.plane_type = plane_type

    def takeoff(self):
        print("Airplane\t:", self.plane_type)
        print("Airline\t\t:",self.airline)
        print("Takeoff")

airbus = Airplane("Emirates", "Airbus A380")
airbus.takeoff()