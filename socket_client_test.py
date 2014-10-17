import cmd
from player import Player
import socket
import sys
import json
import random
import time
import threading


HOST, PORT = "localhost", 9999
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
        data = self.rfile.read()
        self.server.close()
        return data

    def execute(self,data):
        json_data = json.dumps(data)
        response = self.make_request(json_data)
        return json.loads(response)['resp']


def play_game(player):
    player.update_direction(random.choice(["U","D","R","L"]))

    for i in range(1,20):
        client = Client()
        request = {"action":'check_and_update',"data":[player.name, player.current_position, player.direction] }
        response = client.execute(request)
        if response != "OCC":
            if response[0] is not None:
                player.current_position = response[0]
            if response[1] == "TA":
                client = Client()
                pick_request = {"action":"pickup","data": [player.current_position]}
                response = client.execute(pick_request)
                if response == "TA":
                    player.bucket = +1

    return player




# player = Player("i")
# player = play_game(player)
# play_game(player)
def test_ply():
    player = Player(str(random.randint(1,10)))
    play_game(player)
    print player.bucket

# player = Player("i")
# play_game(player)

for i in range(1,20):
    t = threading.Thread(name='my_service', target=test_ply )
    t.start()




