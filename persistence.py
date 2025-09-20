import json

class Persistence:
    def __init__(self, filename="store.json"):
        self.filename = filename

    def save(self, store):
        with open(self.filename, "w") as f:
            json.dump(store, f)

    def load(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
