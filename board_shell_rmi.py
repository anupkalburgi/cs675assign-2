import cmd
from player import Player
import Pyro4

class GameShell(cmd.Cmd):
    def __init__(self):
        self.board = Pyro4.Proxy("PYRO:game.board@localhost:9090")
        cmd.Cmd.__init__(self)
        self.prompt = 'GAME~->'

    def preloop(self):
        print "Welcome! You can interact with the Board game using this shell."
        print "Getting started with the game U - Up, D - Down, L - Left, R - Right\n"
        name = raw_input("Please Enter your name: ")
        self.player = Player(name)
        print self.board

    def do_move(self, args):
        new_position = self.board.check_and_update(self.player.name,self.player.current_position,self.player.direction)
        if len(new_position) ==2:
            if new_position[0] is not None:
                self.player.current_position = new_position[0]
            if new_position[1]:
                print new_position[1]
            print self.player.current_position
        else:
            print new_position


    def do_show(self, args):#Connect to the server, get the positions array that is it.
        if args == "all":
            print self.board.player_postions()
        else:
            print self.player.view()

    def do_pickup(self, args=None):
        resp = self.board.pickup(self.player.current_position)
        if resp[1] == "TA":
            self.player.bucket = +1
            print "Picked Up!! Move on"
        else:
            print resp

    def do_turn(self, direction):
        if direction.upper() in ["U","D","R","L"]:
            print self.player.update_direction(direction.upper())
        else:
            print "Invalid direction"


    def do_EOF(self, line):
        print "Bye!!"
        return True


if __name__ == '__main__':
    GameShell().cmdloop()


