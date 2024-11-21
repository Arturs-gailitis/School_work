import json
import sqlite3

def config_load(file_path):

    with open(file_path, "r") as file:

        return json.load(file)

def connecting_database(config):

    path = config.get("database_path")
    connection = sqlite3.connect(path)

    return connection