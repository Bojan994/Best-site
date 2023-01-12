class Vehicles:
    def __init__(self):
        self.type = str(input("What is the type of your vehicle: car , motorcycle or truck?"))
        if self.type == "car":
            self.car_model = input("What is your car model:?")
            self.car_engine_size = int(input("What is your car engine size in cc :?"))
            self.horse_power = int(input("What is your car horse power:?"))
            self.car_engine_type = input("What is your car engine type:?")
            self.car_year = int(input("How old is your car:?"))
            self.number_of_doors = int(input("How many doors does your car has:?"))
        elif self.type == "motorcycle":
            self.motorcycle_model = input("What is your motorcycle model:?")
            self.motor_engine_size = int(input("What is your motorcycle engine size in cc:?"))
            self.motor_horse_power = int(input("What is your motorcycle horse power:?"))
            self.motor_engine_type = str(input("What is your motor engine type:?"))
            self.motor_year = str(input("Is this the first year of your registration?"))
        else:
            self.truck_model = input("What is your truck model:?")
            self.truck_engine_size = int(input("What is you truck engine size:?"))
            self.truck_horse_power = int(input("What is your truck horse power:?"))
            self.truck_engine_type = input("What is your truck engine type:?")
            self.number_of_trailers = int(input("How many trailers does your truck has:?"))