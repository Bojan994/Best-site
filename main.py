from car import Car
from motorcycle import Motorcycle
from truck import Truck


class AllVehicles:
    car = Car()
    car_registration_price = car.final_amount()

    motor = Motorcycle()
    motor_registration_price = motor.calculating_motor_registration()

    truck = Truck()
    truck_registration_price = truck.calculating_truck_registration()

    printing_car_inputs = car.printing_car_registration()
    printing_motor_inputs = motor.printing_motor_registration()
    printing_truck_inputs = truck.printing_truck_registration()

    print("Amount for registration for all vehicles:",
          car_registration_price + motor_registration_price + truck_registration_price)