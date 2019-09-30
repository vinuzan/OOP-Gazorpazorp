class Spaceship():
    def __init__(self, name, captain, signature):
        self.__name = name
        self.captain = captain
        self.__signature =signature

    def identify(self):
        return self.__signature

    def identity_name(self):
        return self.__name

    def change_name(self, name):
        self.__name = name


#Spaceships should have:
#name
#captain
#intergalaticw_warp_drive_signature
