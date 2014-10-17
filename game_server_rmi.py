import Pyro4
from board import BoardGame


def main():
    board = BoardGame()
    Pyro4.Daemon.serveSimple(
        {
            board: "game.board"
        },
        port=9090,
        ns=False)

if __name__=="__main__":
    main()
