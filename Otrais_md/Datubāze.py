from Datubāžu_connect import *
import sqlite3

def Savienošana():

    config = config_load('Ārējs_konfigurācijas_fails.json')

    connection = sqlite3.connect(config)

    return connection

