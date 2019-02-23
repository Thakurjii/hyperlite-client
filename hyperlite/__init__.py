import socket
from hyperlite.event import Event


class Connection(socket.socket):
    def __init__(self, host, port):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        Event.on('request', self.sendRequest)

    def connect(self, **kwargs) -> bool:
        try:
            super().connect((self.host, self.port))
            print("[#] Connected to Hyperlite Database ..")
            return True
        except Exception as ex:
            return False

    def sendRequest(self, data):
        super().send(str(data).encode("UTF-8"))
        response = super().recv(1024).decode('UTF-8')
        Event.emmit("response", response)
