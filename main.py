import argparse
from server import MiniRedisServer
from client import MiniRedisClient

parser = argparse.ArgumentParser()
parser.add_argument("mode", choices=["server", "client"])
parser.add_argument("--host", default="127.0.0.1")
parser.add_argument("--port", type=int, default=6379)
args = parser.parse_args()

if args.mode == "server":
    server = MiniRedisServer(host=args.host, port=args.port)
    server.start()
else:
    client = MiniRedisClient(host=args.host, port=args.port)
    client.start()
