#This class will be used to monitor cargo for various expeditions
from Expedition_class import *
class Cargo(Expedition):
    def __init__(self, destination, weight, cargo, spaceship = '', origin = 'Gazorpazorp'):
        super().__init__(destination, spaceship, origin)    #super runs the init in parent class.
        self.weight = weight
        self.cargo = cargo

    def expo_details(self):
        cargo_details = {
            'origin': self.__origin,
            'destination': self.__destination,
            'ship': self.__spaceship,
            'passenger list': self.__passenger_list,
            'weight': self.weight,
            'Cargo': self.cargo
        }
        return cargo_details

    def pay_tax(self):
        return self.weight * 1.12

cargo_example = Cargo('Lisbon', 1500, 'Banana', 'Milenium', 'Tardis')

print(cargo_example.expo_details())