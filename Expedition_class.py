from Passenger_class import *

class Expedition():
    def __init__(self, destination, spaceship = '', origin = 'Gazorpazorp'):
        self.__origin = origin
        self.__destination = destination
        self.__spaceship = spaceship
        self.__passenger_list = []

    def assign_ship(self, ship):
        self.__spaceship = ship

    def expo_details(self):
        #Want to send a dictionary with
        #Origin, Destination, Ship, Passenger list
        dict_expo = {
            'origin': self.__origin,
            'destination': self.__destination,
            'ship': self.__spaceship,
            'passenger list': self.__passenger_list
        }
        return dict_expo

#Assign to each expedition assign 2 passengers (append)

    def add_passenger_expo(self, passenger):
        #get passenger list and add to it
        if self.__passenger_list.append(passenger):
            return True
        else:
            return False

    def get_origin(self):
        return self.__origin

    def get_destination(self):
        return self.__destination

    def get_ship(self):
        return self.__spaceship

    def get_pass_list(self):
        return self.__passenger_list

    def print_list_passengers(self):
        for passengers in self.get_pass_list():
            print('Name: ' + passengers.name, 'Species: '+ passengers.species, 'IDR: '+passengers.dnareg)




# Expeditions should have:
#an origin
#destination
#spaceship assigned to it
#list of passengers