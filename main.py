with open("version") as f:
    version = f.read()
import sys
print("©Emīla Software")
print("Booting Emas App 2 version", version)
print("Loading all systems")
a = True
while a:
    modulename = 'os'
    import os
    if modulename not in sys.modules:
        print("Problem importing ", modulename, " trying again")
    else:
        print("Imported", modulename + "! countinuing")
        a = False
a = True
while a:
    modulename = 'tkinter'
    import tkinter as tk
    if modulename not in sys.modules:
        print("Problem importing ", modulename, " trying again")
    else:
        print("Imported", modulename + "! countinuing")
        a = False
a = True
while a:
    modulename = 'tkinter.messagebox'
    import tkinter.messagebox as tkdiso
    if modulename not in sys.modules:
        print("Problem importing ", modulename, " trying again")
    else:
        print("Imported", modulename + "! countinuing")
        a = False
a = True
while a:
    modulename = 'requests'
    import requests
    if modulename not in sys.modules:
        print("Problem importing ", modulename, " trying again")
    else:
        print("Imported", modulename + "! countinuing")
        a = False
print("Loading modules completed.")
print("Trying to connect to App store")
try:
    response = requests.get(
        'https://pastebin.com/raw/V4AxdhXy')
    data = response.text
    print("Connected!")
except Exception as e:
        print('Unable to Connect to the App Store, Error:' + str(e))
print("Moving to checking for updates")
try:
    response = requests.get(
        'https://raw.githubusercontent.com/Emila-Software/Emas-App-2/main/version')
    data = response.text
    if not data == "404: Not Found":
        print("Connected!")
    else:
        print("Unabble to check for updates")
except Exception as e:
        print('Unable to check for updates, Error:' + str(e))
