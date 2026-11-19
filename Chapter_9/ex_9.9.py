# 9.9
class Car():
    """parrent class car"""

    def __init__(self, make, model, year):
        """initalizing car atributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometr = 0

    def get_discriptive_name(self):
        """return formatted description"""
        long_name = f'{self.make} {self.model} {self.year}'
        return long_name.title()

class ElectricCar(Car):
    """child class electric car"""

    def __init__(self, make, model, year):
        """initalizing car and electric car atributes"""
        super().__init__(make, model, year)
        self.battary_size = Battery()

class Battery:
    """main battary class"""

    def __init__(self, battery_size=40):
        """initalizing battary atributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """displayed bnattery size"""
        print(f'Car battery size {self.battery_size} kWh.')

    def get_range(self):
        """displays the aproxximatebattary range"""
        if self.battery_size == 40:
            range = 120
        elif self.battery_size == 65:
            range = 195
        print(f'This car can go about {range} km on a full charge')            

    def upgrade_battery(self):
        """upgraded battery size"""
        if self.battery_size < 65:
            self.battery_size = 65
        else:
            pass

electric_car_1 = ElectricCar('volga', '#21', '1975')
print(electric_car_1.get_discriptive_name())
electric_car_1.battary_size.get_range()
electric_car_1.battary_size.upgrade_battery()
electric_car_1.battary_size.get_range()