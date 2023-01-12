from vehicles import Vehicles


class Truck(Vehicles):
    TRUCK = 10000
    TRAILER = 7000

    def __init__(self):

        super().__init__()
        self.truck_registration = 0

    def calculating_truck_registration(self):
        self.truck_registration = Truck.TRUCK + (self.number_of_trailers - 1) * Truck.TRAILER
        return self.truck_registration

    def get_calculating_truck_registration(self):
        return self.calculating_truck_registration()

    def printing_truck_registration(self):
        print("VEHICLE3:")
        print("Truck:", self.truck_model)
        print("Engine size:", self.truck_engine_size, "cc")
        print("Horse power:", self.truck_horse_power)
        print("Engine type:", self.truck_engine_type)
        print("Number of trailers", self.number_of_trailers)
        print("AMOUNT FOR REGISTRATION:", self.calculating_truck_registration())