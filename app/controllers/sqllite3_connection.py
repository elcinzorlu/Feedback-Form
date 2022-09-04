VERSION = "1.0.0"
SECRET_KEY = "123eorieeppsq23098ncbxyz"
SESSION_COOKIE_NAME = "mysession"
import sqlite3

def connection_close():
    vt = sqlite3.connect("/home/elcinzorlu/Desktop/pythonProject31.08.22/MitesFeedbackForm/grhyhh.sqlite")
    vt.commit()
    vt.close()