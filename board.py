class BoardGame(object):
    def __init__(self):
        self.max_length = 10
        self.positions = {} # Holds {"player_name":(row,column)}

    #Function to return the co-ordinates in the given direction.

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
        return new_position(current_position)

    def player_postions(self):
        return self.positions

    def check_and_update(self, name, current_position, current_direction):
        position = self.move(name, current_position, current_direction)
        print "We got New", position
        if position:
            if position not in self.positions.values():
                self.positions[name] = position  # if it is a new_player, it gets appended or else gets overwritten
                return self.positions.get(name)

        raise ValueError("We already have some one at {0}, Try going somewhere else".format(position))