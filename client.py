import socket

class MiniRedisClient:
    def __init__(self, host="127.0.0.1", port=6379):
        self.client_socket = socket.socket()
        self.client_socket.connect((host, port))

    def start(self):
        while True:
            cmd = input(">> ")
            self.client_socket.send(cmd.encode())
            response = self.client_socket.recv(1024).decode()
            print(response)
            if cmd.upper() == "QUIT":
                break
        self.client_socket.close()
