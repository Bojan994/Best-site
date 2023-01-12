from vehicles import Vehicles


class Motorcycle(Vehicles):
    MOTORCYCLE = 5000
    CUBIC_CAPACITY_LESS_THAN_50_SECOND_YEAR = 1000

    def __init__(self):

        super().__init__()
        self.motorcycle_registration = 0

    def calculating_motor_registration(self):

        if self.motor_engine_size < 50 and self.motor_year == "no":
            self.motorcycle_registration = Motorcycle.CUBIC_CAPACITY_LESS_THAN_50_SECOND_YEAR
            return self.motorcycle_registration
        else:
            self.motorcycle_registration = Motorcycle.MOTORCYCLE
            return self.motorcycle_registration

    def get_calculating_motor_registration(self):
        return self.calculating_motor_registration()

    def printing_motor_registration(self):
        print("VEHICLE2:")
        print("Motorcycle:", self.motorcycle_model)
        print("Engine size:", self.motor_engine_size, "cc")
        print("Horse power:", self.motor_horse_power)
        print("Engine type:", self.motor_engine_type)
        print("AMOUNT FOR REGISTRATION:", self.get_calculating_motor_registration())