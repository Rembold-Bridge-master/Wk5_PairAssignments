##################################################
# Pair Programming Problem 2 - Wk 5
##################################################

class Vehicle:
    """ Generic class to store information about any vehicle. """
    def __init__(self, terrain, weight):
        self.terrain = terrain
        self.weight = weight

    def __repr__(self):
        return f"Vehicle({self.terrain},{self.weight})"

    def get_terrain(self):
        """ Gets the terrain the vehicle traverses. """
        return self.terrain

    def set_terrain(self, new_terrain):
        """ Set a new terrain type for the vehicle.
        Inputs:
            new_terrain (str): The new terrain type
        """
        self.terrain = new_terrain

    def get_weight(self):
        """ Get the weight of the vehicle. """
        return self.weight

    def set_weight(self, new_weight):
        """ Set a new weight for the vehicle. 
        Inputs:
            new_weight (float): The new vehicle weight
        """
        self.weight = new_weight

# You can go ahead and insert your class definitions below!












if __name__ == '__main__':
    # These are just some basic tests of the starting Vehicle class! Remove them and
    # add your own for your newly defined classes or just add your own to the end.
    car = Vehicle("asphalt", 2000)
    print(car)
    print(car.get_terrain())
    print(car.get_weight())
    car.set_terrain("road")
    car.set_weight(2400)
    print(car)
