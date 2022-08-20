class VehicleClass:
    def speed(self):
        print("speed of vehicle : ")

class Car(VehicleClass):
    def speed(self):
        VehicleClass.speed(self)
        print("160")

class Bike(VehicleClass):
    def speed(self):
        VehicleClass.speed(self)
        print("80")

car = Car()
car.speed()

bike = Bike()
bike.speed()