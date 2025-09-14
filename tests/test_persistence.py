import os
from modules.persistence import save_state, load_state

def test_save_and_load():
    data = {"query": "top products", "result": {"A": [1,2,3]}}
    filename = "test_state.json"
    
    save_state(filename, data)
    loaded = load_state(filename)
    
    assert loaded == data
    os.remove(filename)
