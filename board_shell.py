import cmd
from player import Player


class GameShell(cmd.Cmd):
    def __init__(self):
        self.player = Player("anup", "X")
        cmd.Cmd.__init__(self)
        self.prompt = 'GAME~->'

    def preloop(self):
        print "Welcome! You can interact with the Board game using this shell.\n"
        print "Getting started with the game U - Up, D - Down, L - Left, R - Right"

    def do_move(self, args):
        print self.player.move()

    def do_show(self, args):#Connect to the server, get the positions array that is it.
        print self.player.view()

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


