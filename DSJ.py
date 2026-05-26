# DSJ - Data Saver and JSON Handler
# Author: Ayson JJVG

# =========================================================================
# what it does: This module provides functions to save, load, and update 
# data in JSON format. It uses the built-in `json` library for handling 
# JSON data and `pathlib` for file path management.
# =========================================================================


import json
from pathlib import Path

def LoadData(file_path):
    filepath = Path(file_path)
    
    if not filepath.exists():
        return {}
    
    else:
        with open(filepath, 'r') as f:
            return json.load(f)
        
def SaveData(filename, data, indent=4):
    file_path = Path(filename)
    
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=indent)
        
def UpdateData(filename, new_data, indent=4):
    data = LoadData(filename)
    data.update(new_data)
    SaveData(filename, data, indent=indent)

    