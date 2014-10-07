from board import BoardGame
import random
# This will act as client side thing mostly
# The player ID would be sent form this to servers, and server only holds the player id and not the "OBJ"


class Player(object):
    def __init__(self,name):
        self.name = name
        #self.pawn = pawn # Character choice for pawn
        self.current_position = Player.random_position() # Tuple (row,column)
        self.direction = "U"# L- Left, R- Right, U- up, R- R
        self.bucket =0


    @staticmethod
    def random_position():
        return random.randint(1, 10), random.randint(1, 10)

    def move(self):
        new_position = BoardGame().check_and_update(self.name, self.current_position, self.direction)
        if new_position:
            self.current_position = new_position
            return self.current_position
        else:
            return None

    def view(self):
        return self.name,self.direction,self.current_position,self.bucket

    def view_all(self):
        return BoardGame().player_postions() # Connect to server, get all players May be dirctly from the shell

    def update_direction(self,direction):
        if len(direction) == 1 and direction.upper()  in ["U","D","L","R"]:
            self.direction = direction.upper()
            return self.direction
        else:
            raise ValueError("Invalid input.Should be  U(up),D(down),L(left),R(right) ")
