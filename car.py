from vehicles import Vehicles


class Car(Vehicles):
    ELECTRIC = 5000
    DIESEL_AND_GASOLINE = 10000
    CUBIC_CAPACITY_BIGGER_THAN_2000 = 14000

    def __init__(self):

        super().__init__()
        self.car_registration = 0

    def calculating_car_registration(self):

        if self.car_engine_size > 2000:
            self.car_registration = Car.CUBIC_CAPACITY_BIGGER_THAN_2000
            return self.car_registration
        elif self.car_engine_size < 2000 and self.car_engine_type == "electric":
            self.car_registration = Car.ELECTRIC
            return self.car_registration
        else:
            self.car_registration = Car.DIESEL_AND_GASOLINE
            return self.car_registration

    def get_calculating_car_registration(self):
        return self.calculating_car_registration()

    def car_older_than_5_years(self):

        if self.car_year > 5:
            self.car_registration = (self.car_year - 5) * 0.05 * self.car_registration
            return self.car_registration
        else:
            return 0

    def final_amount(self):
        final_amount = self.get_calculating_car_registration() + self.get_car_older_than_5_years()
        return final_amount.__round__()

    def get_car_older_than_5_years(self):
        return self.car_older_than_5_years()

    def printing_car_registration(self):
        print("All vehicles:")
        print("VEHICLE1:")
        print("Car:", self.car_model)
        print("Engine size:", self.car_engine_size, "cc")
        print("Horse powers:", self.horse_power)
        print("Engine type:", self.car_engine_type)
        print("Number of doors:", self.number_of_doors)
        print("AMOUNT FOR REGISTRATION:", self.final_amount())