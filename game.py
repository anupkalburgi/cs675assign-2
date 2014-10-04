from board import Board

class Game(object):
    def __init__(self):
        self.positions = {} # Holds {"player_name":(row,column)}

    def check_and_update(self, name, position, current_direction):
        if position not in self.positions.values():
            self.positions[name] = position  # if it is a new_player, it gets appended or else gets overwritten
        else:
            raise ValueError("We already have some one at {0}, Try going somewhere else".format(position))

