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

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return {}


def SaveData(filename, data, indent=4): # this function saves the data to the file, it takes the filename, data to save, and an optional indent parameter for pretty-printing the JSON
    file_path = Path(filename)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent)


def UpdateData(filename, new_data, indent=4): # this function updates the data in the data file
    data = LoadData(filename)
    data.update(new_data)
    SaveData(filename, data, indent=indent)
    
def DeleteData(filename, key, indent=4): # this function deletes a specific key from the data file
    data = LoadData(filename)
    if key in data:
        del data[key]
        SaveData(filename, data, indent=indent)
        
    else:
        print(f"Key '{key}' not found in the data.")
        
def GetData(filename, key): # this function is useful for getting a specific value from the data file based on the key
    data = LoadData(filename)
    return data.get(key, None)

def clear_data(filename): # this function clears all data inside the file by saving an empty dictionary to it
    SaveData(filename, {}, indent=4)

    
