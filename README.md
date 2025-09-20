# Mini Redis in Python

A simplified Redis-like **in-memory key-value store** built with Python, demonstrating **DSA, OOP, Networking, and Persistence** concepts.

---

## **Project Overview**

Mini Redis is a lightweight, simplified version of Redis with the following features:

- **Key-Value Store**: Store data as key-value pairs in memory.
- **LRU Cache**: Frequently accessed keys are cached for faster retrieval.
- **TTL (Time-To-Live)**: Keys can expire automatically after a given time.
- **Persistence**: Data is saved to a JSON file to survive server restarts.
- **Multi-Client Support**: Handles multiple clients concurrently using threading.
- **Redis-like Commands**: `SET`, `GET`, `DEL`, `EXPIRE`, `PERSIST`, `PING`, `QUIT`.

---

## **Data Structures Used**

- **Dictionary** → Main key-value store (O(1) access).
- **OrderedDict** → LRU Cache for eviction of least recently used keys.
- **Heap** → TTL expiration management (efficient lookup of next key to expire).
- **Lock (Threading)** → Thread-safe access to store and cache.

---

## **Commands**

| Command | Description |
|---------|-------------|
| `SET key value [EX seconds]` | Store a key-value pair with optional TTL. |
| `GET key` | Retrieve value of a key (checks cache first). |
| `DEL key` | Delete a key from store and cache. |
| `EXPIRE key seconds` | Set TTL for an existing key. |
| `PERSIST key` | Remove TTL from a key. |
| `PING` | Health check → returns `PONG`. |
| `QUIT` | Disconnect client. |

---

## **How to Run**

### 1. Start the server
```bash
python main.py server --host 127.0.0.1 --port 6379
### 2. Start the Client
python main.py client --host 127.0.0.1 --port 6379
### 3. Example Session
>> SET name Vivek
OK
>> GET name
Vivek
>> EXPIRE name 5
OK
>> PING
PONG
>> DEL name
OK
>> QUIT
BYE
