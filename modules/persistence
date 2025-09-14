import json

def save_state(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f)

def load_state(filename):
    with open(filename, "r") as f:
        return json.load(f)
