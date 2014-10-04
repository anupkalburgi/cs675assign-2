from board import BoardGame
import random
# This will act as client side thing mostly
# The player ID would be sent form this to servers, and server only holds the player id and not the "OBJ"


class Player(object):
    def __init__(self,name,pawn):
        self.name = name
        self.board = BoardGame() # may be I will have to send  the Height and Length
        self.pawn = pawn # Character choice for pawn
        self.current_position = Player.random_position() # Tuple (row,column)
        self.current_direction = "U"# L- Left, R- Right, U- up, R- R
        self.bucket = []


    @staticmethod
    def random_position():
        return random.randint(1, 10), random.randint(1, 10)

    def move(self):
        position = self.board.move(self.name, self.current_position, self.current_direction )
        new_position = self.board.check_and_update(self.name,position)
        if new_position:
            self.current_position = new_position
        else:
            return None

    def update_direction(self,direction):
        if len(direction) == 1 and direction.upper()  in ["U","D","L","R"]:
            self.current_direction = direction.upper()
        else:
            raise ValueError("Invalid input.Should be  U(up),D(down),L(left),R(right) ")
