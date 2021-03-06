import SocketServer
import json
from board import BoardGame


class MyTCPHandler(SocketServer.BaseRequestHandler):


    def process_request(self,action,data):
        actions_map = {"check_and_update":self.server.board.check_and_update,
                       "postions":self.server.board.player_postions,
                       "pickup": self.server.board.pickup}
        func = actions_map.get(action)
        return func(*data)

    def handle(self):
        self.data = self.request.recv(1024).strip()
        #print("{0} wrote:".format(self.client_address[0]))
        request = json.loads(self.data)
        action =  request.get("action")
        data = request.get("data")
        response = self.process_request(action, data)
        resp = json.dumps({"resp": response })
        print request,resp
        self.request.sendall(resp)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server.board = BoardGame()
    server.serve_forever()