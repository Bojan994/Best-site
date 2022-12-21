ELECTRIC = 5000
DIESEL_AND_GASOLINE = 10000
CUBIC_CAPACITY_BIGGER_THAN_2000 = 14000

car_model = input("What is your car model?")
cubic_capacity = int(input("What is your car cubic capacity?"))
if cubic_capacity > 2000:
    cubic_capacity = CUBIC_CAPACITY_BIGGER_THAN_2000
else:
    cubic_capacity = DIESEL_AND_GASOLINE
horse_power = int(input("What is your car horse power?"))
engine_type = str(input("What is the engine type of your car?"))
if engine_type == "gasoline":
    engine_type = DIESEL_AND_GASOLINE
elif engine_type == "diesel":
    engine_type = DIESEL_AND_GASOLINE
else:
    engine_type = ELECTRIC

number_of_doors = int(input("How many doors your car has?"))

car_registration = 0
cubic = int(input("What is your cubic capacity?"))
if cubic < 2000:
    car_registration = DIESEL_AND_GASOLINE
    type_engine = str(input("What is your engine type? gasoline , diesel or electric?"))
    if type_engine == "electric":
        car_registration = ELECTRIC
    else:
        car_registration = DIESEL_AND_GASOLINE
else:
    car_registration = CUBIC_CAPACITY_BIGGER_THAN_2000

print("All vehicles:")
print("VEHICLE1:")
print("Car:", car_model)
print("Engine size:", cubic_capacity)
print("Horse powers:", horse_power)
print("Engine type:", engine_type)
print("Number of doors:", number_of_doors)
print("AMOUNT FOR REGISTRATION:", car_registration)


MOTORCYCLE = 5000
CUBIC_CAPACITY_LESS_THAN_50_SECOND_YEAR = 1000

motor_model = input("What is your motor model?")
motor_cubic_capacity = int(input("What is your motor cubic capacity?"))
if motor_cubic_capacity < 50:
    capacity = str(input("Is this the first year of registration?"))
    if capacity == "yes":
        motor_cubic_capacity = CUBIC_CAPACITY_LESS_THAN_50_SECOND_YEAR
    else:
        motor_cubic_capacity = MOTORCYCLE
else:
    motor_cubic_capacity = MOTORCYCLE

motor_horse_power = int(input("What is your motor horse power?"))
motor_engine_type = input("What is your motor engine type?")

motor_registration = 0
cubic_2 = int(input("What is your motor cubic?"))
year = str(input("Is this the first year of registration?"))
if cubic_2 < 50:
    motor_registration = MOTORCYCLE
    if year == "no":
        motor_registration = CUBIC_CAPACITY_LESS_THAN_50_SECOND_YEAR
    else:
        motor_registration = MOTORCYCLE
else:
    motor_registration = MOTORCYCLE

print("VEHICLE2:")
print("Motorcycle:", motor_model)
print("Engine size:", motor_cubic_capacity)
print("Horse power:", motor_horse_power)
print("Engine type:", motor_engine_type)
print("AMOUNT FOR REGISTRATION:", motor_registration)


TRUCK = 10000
TRAILER = 7000

truck_model = input("What is your truck model?")
engine_size = input("What is the engine size of your truck?")
truck_horse_power = input("What is your truck horse power?")
truck_engine_type = input("What is the engine type of your truck?")
number_of_trailer = int(input("How many trailers does your truck has?"))
truck_registration = TRUCK + number_of_trailer * TRAILER
FINAL_AMOUNT = car_registration + motor_registration + truck_registration

print("VEHICLE3:")
print("Truck:", truck_model)
print("Engine size:", engine_size)
print("Horse power:", horse_power)
print("Engine type:", engine_type)
print("Number of trailers",number_of_trailer)
print("AMOUNT FOR REGISTRATION:", truck_registration)
print("Amount for registration for 3 vehicles is:", FINAL_AMOUNT)