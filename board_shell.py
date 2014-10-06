import cmd
from player import Player
import socket
import sys
import json

HOST, PORT = "localhost", 9999
data = {"a":1,"b":2,"c":3}
# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class Client( object ):
    rbufsize= -1
    wbufsize= 0
    def __init__( self, address=(HOST,PORT) ):
        self.server=socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        self.server.connect( address )
        self.rfile = self.server.makefile('rb', self.rbufsize)
        self.wfile = self.server.makefile('wb', self.wbufsize)

    def make_request( self, text ):
        """send a message and get a 1-line reply"""
        self.wfile.write( text + '\n' )
        data= self.rfile.read()
        self.server.close()
        return data


class GameShell(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = 'GAME~->'

    def preloop(self):
        print "Welcome! You can interact with the Board game using this shell."
        print "Getting started with the game U - Up, D - Down, L - Left, R - Right\n"
        name = raw_input("Please Enter your name: ")
        self.player = Player(name)

    def _execute(self,request):
        c= Client()
        request = json.dumps(request)
        response= c.make_request(request)
        return json.loads(response)

    def do_move(self, args):
        request = {"action":'check_and_update',
                "data":[ self.player.name,self.player.current_position,self.player.direction] }
        response = self._execute(request)
        self.player.current_position = response
        print self.player.current_position

    def do_show(self, args):#Connect to the server, get the positions array that is it.
        if args == "all":
            request = {"action":"postions","data":[]}
            print self._execute(request)
        else:
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


