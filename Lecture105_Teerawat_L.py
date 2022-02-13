class Vehicle:
    lecenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(Vehicle):
    pass
class Pickup(Vehicle):
    pass
class Van(Vehicle):
    pass

car1=Car()
car1.turnOnAirConditioner()

pickup1 = Pickup()
pickup1.turnOnAirConditioner()

van1 = Van()
van1.turnOnAirConditioner()
