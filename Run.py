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
passenger_1 = Passenger('Lenny', 'Wookie', '887')
    #generate 3 spaceships
ship_1 = Spaceship('Morgan', 'RPS', 'AK1345')
ship_2 = Spaceship('Marvel', 'Dissapointos', 'AK1365')
ship_3 = Spaceship('Sparrow', 'Black Pearl', 'AK1868')
    #generate 3 expeditions
expo_1 = Expedition ('Mars', ship_3)
expo_2 = Expedition ('Death Star', ship_2)
expo_3 = Expedition ('Final Destination', ship_1)
        #keep list of generated expedition (add to empty list)
        #assign a spaceship to each one
            #Should be able to assign on creation of object / post factual
    #Assign to each expedition assign 2 passengers (append)
expo_1.add_passenger_expo(passenger_1)
expo_1.add_passenger_expo((passenger_2))
print(expo_1.expo_details())

    #iterate over list of expedition and print

    #iterate over a list of expedition and print
        #Iterate over list of passenger object
        #Print out passenger details


#creare while loop here
    #Use input to get user input and generate objects dynamically.
