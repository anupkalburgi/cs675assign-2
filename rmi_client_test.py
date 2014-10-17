from player import Player
import Pyro4
import random
import threading


def play_game(player):
    board = Pyro4.Proxy("PYRO:game.board@localhost:9090")
    player.update_direction(random.choice(["U","D","R","L"]))

    for i in range(1,20):
        new_position = board.check_and_update(player.name, player.current_position,player.direction)
        if new_position != "OCC" and new_position[0] != None:
            player.current_position = new_position[0]
        if  new_position[1] == "TA":
            resp = board.pickup(player.current_position)
            if resp[1] == "TA":
                player.bucket = +1


def test_ply(i):
    player = Player(i)
    play_game(player)
    print player.bucket


for i in range(1,20):
    t = threading.Thread(name='my_service', target=test_ply, args=( str(i),) )
    t.start()
