import time
import heapq
from threading import Lock

class KeyValueStore:
    def __init__(self):
        self.store = {}
        self.expiry = {}  # key -> expire_at timestamp
        self.ttl_heap = []  # min-heap for expiry
        self.lock = Lock()

    def set(self, key, value, ttl=None):
        with self.lock:
            self.store[key] = value
            if ttl:
                expire_at = time.time() + ttl
                self.expiry[key] = expire_at
                heapq.heappush(self.ttl_heap, (expire_at, key))
            elif key in self.expiry:
                # Remove existing TTL
                del self.expiry[key]

    def get(self, key):
        with self.lock:
            # Remove expired key
            self._cleanup()
            return self.store.get(key, None)

    def delete(self, key):
        with self.lock:
            self.store.pop(key, None)
            self.expiry.pop(key, None)

    def _cleanup(self):
        now = time.time()
        while self.ttl_heap and self.ttl_heap[0][0] <= now:
            _, key = heapq.heappop(self.ttl_heap)
            if key in self.expiry and self.expiry[key] <= now:
                self.store.pop(key, None)
                self.expiry.pop(key, None)
