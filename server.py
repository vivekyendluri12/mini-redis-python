import socket
import threading
from key_value_store import KeyValueStore
from lru_cache import LRUCache
from persistence import Persistence

class MiniRedisServer:
    def __init__(self, host="127.0.0.1", port=6379):
        self.kv_store = KeyValueStore()
        self.cache = LRUCache()
        self.persistence = Persistence()
        # Load existing data
        self.kv_store.store = self.persistence.load()
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        print(f"Server running on {host}:{port}")

    def start(self):
        while True:
            client_conn, addr = self.server_socket.accept()
            print(f"Client connected: {addr}")
            threading.Thread(target=self.handle_client, args=(client_conn,)).start()

    def handle_client(self, conn):
        with conn:
            while True:
                data = conn.recv(1024).decode().strip()
                if not data:
                    break
                response = self.execute_command(data)
                conn.send(response.encode())

    def execute_command(self, command_line):
        parts = command_line.split()
        cmd = parts[0].upper()
        if cmd == "SET":
            key = parts[1]
            value = parts[2]
            ttl = int(parts[4]) if len(parts) == 5 and parts[3].upper() == "EX" else None
            self.kv_store.set(key, value, ttl)
            self.cache.put(key, value)
            self.persistence.save(self.kv_store.store)
            return "OK"
        elif cmd == "GET":
            key = parts[1]
            value = self.cache.get(key)
            if value is None:
                value = self.kv_store.get(key)
                if value:
                    self.cache.put(key, value)
            return str(value) if value else "(nil)"
        elif cmd == "DEL":
            key = parts[1]
            self.kv_store.delete(key)
            self.cache.cache.pop(key, None)
            self.persistence.save(self.kv_store.store)
            return "OK"
        elif cmd == "PING":
            return "PONG"
        elif cmd == "QUIT":
            return "BYE"
        else:
            return "Unknown Command"
