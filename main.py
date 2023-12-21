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
    from tkinter import *
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

a = True
while a:
    modulename = 'time'
    import time
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
        print("Unable to check for updates")
        data = version
except Exception as e:
        print('Unable to check for updates, Error:' + str(e))

if not data == version:
    print("Update found! please update when system has fully booted")
print("Checking for updates completed")

print("Getting user data")
users = os.listdir(path="userdata")
for x in users:
    print("Loaded user:", x)
print("Users loaded")

print("Deffining functions")

def create_menu(button):
    # Get the button position and size
    x, y, width, height = button.bbox()

    # Create a new menu above the button
    new_menu = tk.Menu(button, tearoff=0)

    # Add apps to the menu
    new_menu.add_command(label="App 1", command = "")
    new_menu.add_command(label="App 2", command = "")
    new_menu.add_command(label="App 3", command = "")

    # Display the menu at the correct position
    new_menu.post(y, x)

def on_button_click(button):
    create_menu(button)

def main(user):
    window = tk.Button(text = "Emas app 2", command=lambda: on_button_click(window))
    window.pack(side=tk.BOTTOM, anchor=tk.SW, padx=5, pady=5)

def checkingdata():
    global passwordcorrect
    userna.config(state= "disabled")
    passworda.config(state= "disabled")
    global users
    username = userna.get()
    password = passworda.get()
    passwordcorrect = False
    for x in users:
        if not x == username:
            continue
        if x == username:
            print("User found")
            usernamecorrect = True
            break
    if usernamecorrect == False:
        tkdiso.showerror("Wrong info!", "Username or password incorrect")
    else:
        with open("userdata/" + username + "/password.txt") as f:
            passwordreal = f.read()
        if password == passwordreal:
            passwordcorrect = True
    if passwordcorrect == False:
        tkdiso.showerror("Wrong info!", "Username or password incorrect")
    
    userna.config(state= "normal")
    passworda.config(state= "normal")
    print(passwordcorrect)
    if passwordcorrect == True:
        lavel1.destroy()
        lavel2.destroy()
        lavel3.destroy()
        submit.destroy()
        userna.destroy()
        passworda.destroy()
        lavel = Label(root,text="Logged in :)",)
        lavel.pack(pady=20)
        main(username)


print("Functions ready")

print("Starting screen")
root = tk.Tk()
root.title("Emas App 2")
root.geometry("1000x700")
root.configure(bg='white')
root.resizable(False, False)
print("Screen started")
print("Starting login")

lavel1 = Label(root,text="User login",)
lavel1.pack(pady=20)
#Create a text label
lavel2 = Label(root,text="Username",)
lavel2.pack(pady=20)
#Create Entry Widget for password
userna= Entry(root,width=20)
userna.pack()

#Create a text label
lavel3 = Label(root,text="Password",)
lavel3.pack(pady=20)
#Create Entry Widget for password
passworda= Entry(root,show="*",width=20)
passworda.pack()

submit= Button(root,text="Submit", command=checkingdata)
submit.pack()


root.mainloop()
