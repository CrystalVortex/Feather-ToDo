from pathlib import Path

import os

import shutil

print("type 'help' for help.")



while True: #create a loop so it doesnt close when you type something in
    cmd = input()
    cmd = cmd.lower()
    if cmd not in ["help", "create", "edit", "mark"]: #makes sure that you are typing commands that exist
        print("type 'help' for help.")

    if cmd == "help": #when you type help this command will execute
        print("Commands: create (creates a ToDo), edit (edit a ToDo), mark (marks a Todo as done and deletes it), help (shows this help command)")

    if cmd == "create": #when you type create this command will execute
        name = input('Name: ')
        open(f"{name}.ftd", "w+")
        x = open(f"{name}.ftd", "r+")
        x = x.readlines()
        os.system(f"notepad {name}.ftd")
        Path("todo").mkdir(parents=True, exist_ok=True)
        try:
            c = shutil.move(f"{name}.ftd", "todo")
            print("ToDo has been created")
        except shutil.Error as error:
            print("ToDo Exists!")
            os.remove(f"{name}.ftd")
            pass
            
        
    
    if cmd == "edit": #when you type edit this command will execute
        name = input('Name: ')
        os.system(f"notepad todo/{name}.ftd")
        print("ToDo has been edited")
        
    if cmd == "mark": #when you type mark this command will execute
        name = input('Name: ')
        print("Are you sure you want to delete this ToDo (mark as read)? (y, n)")
        con = input(': ')
        if con not in ["Y", "y", "N", "n"]:
            print("aborted")
        try:
            os.remove(f"todo/{name}.ftd")
            print("Todo marked as done!")
        except FileNotFoundError:
            print("Todo does not exist!")
