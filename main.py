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

a = True
while a:
    modulename = 'random'
    import random
    if modulename not in sys.modules:
        print("Problem importing ", modulename, " trying again")
    else:
        print("Imported", modulename + "! countinuing")
        a = False

a = True
while a:
    modulename = 'secrets'
    import secrets
    if modulename not in sys.modules:
        print("Problem importing ", modulename, " trying again")
    else:
        print("Imported", modulename + "! countinuing")
        a = False



print("Loading modules completed.")

print("Generating overide auth")
overideauth = secrets.token_hex(16) + "DO_NOT_USE"
print("Generated overide auth")

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

if version > data:
    print("Warning! Local version bigger than the online version!")
    print("For security reasons Emas App 2 is now turning off")
    exit()
else:
    pass

if not data == version:
    print("Update found! please update when system has fully booted")
print("Checking for updates completed")

print("Getting user data")
users = os.listdir(path="userdata")
for x in users:
    print("Loaded user:", x)
print("Users loaded")

print("Deffining functions")


def testinfo():
    tkdiso.showinfo(title="Test info", message="This is a test info box")

def shutdown_computer(override=False, overrideauth=""):
    global overideauth
    if override != True:
     confirmation = tkdiso.askyesno(title= "Shutdown?", message= "Do you wanna shutdown?")
    elif override == True and overrideauth == overideauth:
        print("Override activated")
        confirmation = True
    if confirmation == True:
     if os.name == 'na':
          # For Windows operating system
          os.system('shutdown /s /t 0')
     elif os.name == 'posix':
          # For Unix/Linux/Mac operating systems
          os.system('sudo shutdown now')
     else:
          tkdiso.showerror(title="Uh oh!", message="Unsupported operating system!")
def github():
    os.startfile("https://github.com/Emila-Software/Emas-App-2")

def shutdown_program():
    confirmation = tkdiso.askyesno(title= "Shutdown?", message= "Do you wanna shutdown Emas App 2?")
    if confirmation == True:
        exit()
    else:
        return("User said nuh uh")

def shutdown_options():
    shutdown_menu = tk.Tk()
    shutdown_menu.title("Power menu")
    shutdown_menu.resizable(False, False)
    power = Button(shutdown_menu, text='Shutdown computer', command=lambda: shutdown_computer())
    power.pack()
    turnoff = Button(shutdown_menu, text='Shutdown Emas App 2', command=lambda: shutdown_program())
    turnoff.pack()
    shutdown_menu.mainloop()

def create_menu(button,user):
    # Get the button position and size
    x, y, width, height = button.bbox()

    # Create a new menu above the button
    new_menu = tk.Menu(button, tearoff=0)

    # Add current user
    new_menu.add_command(label="Logged in as " + user)

    # Find Python files in the apps folder
    app_files = [f for f in os.listdir('apps') if f.endswith('.py') and not f.startswith('__')]

    # Add apps to the menu
    for app_file in app_files:
        app_name_display = os.path.splitext(app_file)[0].replace('-', ' ')
        app_name_run = os.path.splitext(app_file)[0]
        new_menu.add_command(label=app_name_display, command=lambda app=app_name_run: run_app(app))

    # Add shutdown menu to the menu
    new_menu.add_command(label="Shutdown", command=shutdown_options)

    new_menu.add_command(label="Emas app 2 github", command=github)

    # Display the menu at the correct position
    new_menu.post(y, x)

def run_app(app_name):
    # Run the app using exec
    app_path = os.path.join('apps', f'{app_name}.py')
    with open(app_path) as f:
        code = compile(f.read(), app_name, 'exec')
        # Check if the code contains any references to 'shutdown_computer'
        if 'shutdown_computer' in code.co_names or 'shutdown_program' in code.co_names or 'overideauth' in code.co_names:
            tkdiso.showwarning(title="PROGRAM UNSAFE", message="This program has blacklisted code!")
        else:
            try:
                exec(code)
            except SystemExit:
                tkdiso.showwarning(title="PROGRAM UNSAFE", message="This program has tried shutting down Emas App 2! Do not try opening it again!")
                pass

def on_button_click(button, user):
    create_menu(button,user)

def main(user):
    window = tk.Button(text = "Emas app 2", command=lambda: on_button_click(window, user))
    eshutdown = tk.Button(text = "Emergency shutdown", command=lambda: shutdown_computer(True, overideauth))
    eshutdown.pack(side=tk.RIGHT)
    window.pack(side=tk.BOTTOM, anchor=tk.SW, padx=5, pady=5)
def checkingdata():
    global passwordcorrect
    userna.config(state= "disabled")
    passworda.config(state= "disabled")
    global users
    username = userna.get()
    password = passworda.get()
    passwordcorrect = False
    usernamecorrect = False
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
        lavel.after(3000,lambda: lavel.destroy())
        main(username)
        return(None)


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
