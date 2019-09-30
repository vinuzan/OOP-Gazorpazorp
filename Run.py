from Passenger_class import *
from Expedition_class import *
from Spaceship_class import *

#create object here
    #generate 6 passengers
passenger_1 = Passenger('Vinu', 'Human', '007')
passenger_2 = Passenger('Thanu', 'Marching', '068')
passenger_3 = Passenger('David', 'Whitch', '666')
passenger_4 = Passenger('Vishnu', 'Venus', '900')
passenger_5 = Passenger('Sharik', 'Pluton', '045')
passenger_6 = Passenger('Lenny', 'Wookie', '887')

    #generate 3 spaceships
ship_1 = Spaceship('Morgan', 'RPS', 'AK1345')
ship_2 = Spaceship('Marvel', 'Dissapointos', 'AK1365')
ship_3 = Spaceship('Sparrow', 'Black Pearl', 'AK1868')
ship_4 = Spaceship('Cage', 'Nicolaus', 'AK1867')

#generate 3 expeditions using ship objects (instances)
expo_1 = Expedition ('Mars', ship_3)
expo_2 = Expedition ('Death Star', ship_2)
expo_3 = Expedition ('Final Destination', ship_1)

#keep list of generated expedition (add to empty list)
expo_list =[]
expo_list.append(expo_1)
expo_list.append(expo_2)
expo_list.append(expo_3)

#assign a spaceship to each one
    #Should be able to assign on creation of object / post factual
expo_3.assign_ship(ship_4)

    #Assign to each expedition assign 2 passengers (append)
expo_1.add_passenger_expo(passenger_1)
expo_1.add_passenger_expo((passenger_2))

expo_2.add_passenger_expo(passenger_3)
expo_2.add_passenger_expo(passenger_4)

expo_3.add_passenger_expo(passenger_5)
expo_3.add_passenger_expo(passenger_6)

    #iterate over list of expedition and print
for expo in expo_list: #Getting an expeditin object
#Use expo_details as a dictionary
# We want to get out origin, destination and ship - nicely formatted
    print(expo.get_origin(), expo.get_destination(), expo.get_ship().identity_name())

# for expo in expo_list:
#     for keys in expo.expo_details():
#         print(keys, expo.expo_details()[keys])

#Iterate over list of passenger object
#Print out passenger details



#creare while loop here
    #Use input to get user input and generate objects dynamically.
