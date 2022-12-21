class Car:

    def __init__(self, model, engine_size, horse_power, engine_type, number_of_doors):
        self.model = model
        self.engine_size = engine_size
        self.horse_power = horse_power
        self.engine_type = engine_type
        self.number_of_doors = number_of_doors


ELECTRIC = 5000
DIESEL_AND_GASOLINE = 10000
CUBIC_BIGGER_THAN_2000 = 14000

car = Car("Opel", 2000, 150, "gasoline", 5)

print("Car model:", car.model)
print("Engine size:", car.engine_size)
print("Horse power:", car.horse_power)
print("Engine type:", car.engine_type)
print("Number of doors:", car.number_of_doors)
print("AMOUNT FOR REGISTRATION:", DIESEL_AND_GASOLINE)


class Motorcycle:
    def __init__(self, model, engine_size, horse_power, engine_type):
        self.model = model
        self.engine_size = engine_size
        self.horse_power = horse_power
        self.engine_type = engine_type


MOTORCYCLE = 5000
MOTORCYCLE_LESS_THAN_50_CC_AND_SECOND_YEAR_REGISTRATION = 1000

motor = Motorcycle("Suzuki", 50, 100, "gasoline")

print("VEHICLE 2")
print("Motor model:", motor.model)
print("Engine size:", motor.engine_size)
print("Engine type:", motor.engine_type)
print("AMOUNT FOR REGISTRATION:", MOTORCYCLE)


class Truck:
    def __init__(self, model, engine_size, horse_power, engine_type, number_of_trailers):
        self.model = model
        self.engine_size = engine_size
        self.horse_power = horse_power
        self.engine_type = engine_type
        self.number_of_trailers = number_of_trailers


TRUCK = 10000
ONE_TRAILER = 7000
TWO_TRAILERS = 14000
THREE_TRAILERS = 21000
FOUR_TRAILERS = 28000
FIVE_TRAILERS = 35000

truck = Truck("FAP-Tammic", 5000, 500, "diesel", 3)

print("VEHICLE 3")
print("Truck model:", truck.model)
print("Engine size:", truck.engine_size)
print("Horse power:", truck.horse_power)
print("Engine type:", truck.engine_type)
print("Number of trailers:", truck.number_of_trailers)
print("AMOUNT FOR REGISTRATION:", TRUCK + THREE_TRAILERS)

print("Amount for all three vehicles:", DIESEL_AND_GASOLINE + MOTORCYCLE + TRUCK + THREE_TRAILERS)
