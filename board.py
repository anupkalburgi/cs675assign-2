#TODO: Add treasure and its postion list
#Implement pickup

import random


class BoardGame(object):
    def __init__(self):
        self.max_length = 10
        self.positions = {} # Holds {"player_name":(row,column)}
        self.treasure = self._place_treasure()

    #Function to return the co-ordinates in the given direction.
    @staticmethod
    def random_position():
        return random.randint(1, 10), random.randint(1, 10)

    def _place_treasure(self):
        number_of_treasures = random.randint(1,10)
        return [self.random_position() for i in range(0,number_of_treasures)]

    def up(self, current_position):
        if current_position[0] - 1 >= 0:
            return current_position[0] - 1 , current_position[1]

    def down(self, current_position):
        if current_position[0] +1 <= self.max_length:
            return current_position[0] + 1 , current_position[1]

    def left(self,current_position):
        if current_position[1]-1 > 0:
            return current_position[0] ,current_position[1]-1

    def right(self,current_position):
        if current_position[1]+1 <= self.max_length:
            return current_position[0], current_position[1]+1

    def move(self, name, current_position, direction):
        move_func = {"U": self.up, "D": self.down, "L":self.left, "R":self.right}
        new_position = move_func.get(direction)
        print "In calculating new:",new_position(current_position)

        print self.treasure
        if new_position(current_position) in self.treasure:
            treasure = "You have treasure available"
        else:
            treasure = None
        return new_position(current_position),treasure

    def player_postions(self):
        return self.positions

    def pickup(self,postion):
        #check if the postion passed is in self.treasure if so remove the element a
        if tuple(postion) not in self.treasure:
            message = "It is either taken or You tried to fool me"
            return message
        if tuple(postion) in self.treasure:
            self.treasure.remove(tuple(postion))
            return "treasure"


    def check_and_update(self, name, current_position, current_direction):
        position = self.move(name, current_position, current_direction)
        print "We got New", position
        if position:
            if position not in self.positions.values():
                self.positions[name] = position  # if it is a new_player, it gets appended or else gets overwritten
                return self.positions.get(name)
        message = "You cannot be moving to {0}, Try going somewhere else".format(current_position)
        return message