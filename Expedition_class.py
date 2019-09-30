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


# Expeditions should have:
#an origin
#destination
#spaceship assigned to it
#list of passengers