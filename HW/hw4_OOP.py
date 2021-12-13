# 1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def info_max_speed(self):
        print(f'You have {self.max_speed}')


car_1 = Vehicle(max_speed='140', mileage='60')
print(f'Vehicle has speed {car_1.mileage} and max speed {car_1.max_speed} ')


# Vehicle has speed 60 and max speed 140
# 2. Create a child class Bus that will inherit all the variables and methods of the Vehicle class
# and will have seating_capacity own method

class Bus(Vehicle):

    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

    def print_bus_parametr(self):
        print(f'Max speed {self.max_speed},mileage {self.mileage}, seating {self.seating_capacity}')


my_Bus = Bus(max_speed='140', mileage='60', seating_capacity='9')

print(f'Vehicle has {my_Bus.mileage} , {my_Bus.max_speed} ,{my_Bus.seating_capacity}')
my_Bus.print_bus_parametr()
# Max speed 140,mileage 60, seating 9
# 3. Determine which class a given Bus object belongs to (Check type of an object)
print(type(my_Bus))
# <class '__main__.Bus'>
print(isinstance(my_Bus, Bus))
# True
# 4. Create an instance of Bus named school_bus and determine if school_bus is also an instance of the Vehicle class
School_Bus = Bus(max_speed='100', mileage='50', seating_capacity='40')
print(isinstance(School_Bus, Vehicle))
# True
#
# 5. Create a new class School with get_school_id and number_of_students instance attributes
class School:

    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def get_schl_info(self):
        print(f'My School id {self.get_school_id} and in my class {self.number_of_students} students.')



# 6*. Create a new class SchoolBus that will inherit all the methods from School and Bus
# and will have its own - bus_school_color
class SchoolBus(School, Bus):

    def __init__(self, max_speed, mileage, seating_capacity, get_school_id, number_of_students, bus_school_color):
        School.__init__(self, get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        self.bus_school_color = bus_school_color

    def get_bus_color(self):
        print(f'School Bus colour {self.bus_school_color}')

my_schl_bus=SchoolBus(160,50,32,128,22,'yellow')

my_schl_bus.print_bus_parametr()
my_schl_bus.get_schl_info()
my_schl_bus.get_bus_color()
# Max speed 160,mileage 50, seating 32
# My School id 128 and in my class 22 students.
# School Bus colour yellow

# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.
class Bear:
    def __init__(self,sound):
        self.sound=sound

    def make_sound(self):
        print(f'{self.sound}')


class Wolf:
    def __init__(self, sound):
        self.sound= sound

    def make_sound(self):
        print(f'{self.sound}')

Bear_sound=Bear('Grrr')
Wolf_sound=Wolf('Wyyyyy')
all_sound=(Bear_sound,Wolf_sound)
for sound in all_sound:
    print(sound.make_sound())
# Grrr
# None
# Wyyyyy
# None


# Magic methods:
# Optional: 8*. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small". Hint: use magic methods / patterns
