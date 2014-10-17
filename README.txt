Experiment Details:
-------------------

Code Structure:
---------------
board.py  --  Server Side game logic. Maintains states for various players.                 
player.py --  Client side player boilerplate. Designed to maintain Players name, treasures and
              current location


board_shell_socket.py  -- Socket Client side shell to play the game
board_shell_rmi.py     -- RMI Client side shell to play the game

    Command Glossary 
    ==============
        Both Implement the following commands 
            A. move - moves one step forward in the present direction. If a treasure available 
            B. turn [L,R,U,D] -  [Left, Right, Up, Down]. Each moves direction is based on this
                usage: `turn r` or `turn R`

  
game_server_rmi.py    - RMI server implementation of board game, responsible for putting out a URL and binding the board object to daemon
game_server_socket.py - Socket implementation of board game, responsible for parsing the incoming request, dispatching the request to the correct                              function and replying back to the client     
            
rmi_client_test.py - The code that was used to generate the run time for RMI part
socket_client_test.py  - code that was used to generate the run time for socket part of the experiment. 


Experiment methods adopted:
--------------------------
Both socket and RMI run the same game logic (uses the same function calls and same parameters) so nothing in terms of game changes for both of them.

GAME (board) -- Keeps tack of the users position, 2 plyers cannot occupy the same cell at a given point of time. Generates treasure points on the board randomly. Players can choose to pick it up or else just leave it there. If picked up, the treasure will be deleted. 

In case of RMI: The server file is responsible for creating a object and listen to incoming requests. 
In case of Socket: The server file is responsible for parsing incoming requests and dispatching the request to the correct function with the arguments necessary 

Each RMI and Socket test files will create 20 players and all of 20 players make 20 moves.
This configuration was used for obtain the present stats. 

time *nix command was used to measure the execution times for both RMI and socket. 

    Example: time python socket_client_test.py
    O/P
    real	0m0.315s
    user	0m0.163s
    sys	0m0.165s
