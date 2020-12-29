#!/bin/python3

import os
from colorama import Fore
print(Fore.RED)

print("╭━━━┳━━━┳━━━━┳╮╱╭╮╭━╮╱╱╱╱╱╭╮")
print("┃╭━╮┃╭━╮┃╭╮╭╮┃┃╱┃┃┃╭╯╱╱╱╱╱┃┃")
print("┃╰━╯┃┃╱┃┣╯┃┃╰┫╰━╯┣╯╰┳┳━╮╭━╯┣━━┳━╮")
print("┃╭━━┫╰━╯┃╱┃┃╱┃╭━╮┣╮╭╋┫╭╮┫╭╮┃┃━┫╭╯")
print("┃┃╱╱┃╭━╮┃╱┃┃╱┃┃╱┃┃┃┃┃┃┃┃┃╰╯┃┃━┫┃")
print("╰╯╱╱╰╯╱╰╯╱╰╯╱╰╯╱╰╯╰╯╰┻╯╰┻━━┻━━┻╯")
print("Add A/ Python /Or a Bash Script To PATH.")
print(Fore.CYAN)

def menu():
    print("Input your shell: press [1] for bash, [2] for zsh, [3] for fish,\n\n[4] to exit")
    print()
    choice = input()
    print()

    if choice == '1':
        print()
        addClone = str(input("ADD Python Git Here: "))
        clone = os.system(f"git clone {addClone}")
        lookup = os.system("ls")
        print()
        folder = str(input("Enter Target Folder Name: "))
        current = str(input("Add your curent file PATH: "))
        copy1 = os.system(f"sudo scp -r {current}{folder} /bin/")
        copy2 = os.system(f"sudo scp -r {current}{folder} /usr/local/bin/")
        print()
        print('Add Text below to vim:')
        print()
        print(f"export PATH=$HOME/bin/{folder}:/usr/local/bin/{folder}:$PATH")
        
        def ready1():
            print()
            print("Press y when ready")
            r = input()

            if r == 'y':
                vim = os.system("vim ~/.bashrc")
        ready1()

    if choice == '2':
        print()
        addClone = str(input("ADD Python Git Here: "))
        clone = os.system(f"git clone {addClone}")
        lookup = os.system("ls")
        print()
        folder = str(input("Enter Target Folder Name: "))
        current = str(input("Add your curent file PATH: "))
        copy1 = os.system(f"sudo scp -r {current}{folder} /bin/")
        copy2 = os.system(f"sudo scp -r {current}{folder} /usr/local/bin/")
        print()
        print('Add Text below to vim:')
        print()
        print(f"export PATH=$HOME/bin/{folder}:/usr/local/bin/{folder}:$PATH")
        
        def ready2():
            print()
            print("Press y when ready")
            r = input()

            if r == 'y':
                vim = os.system("vim ~/.zshrc")
        ready2()

    if choice == '3':
        print()
        addClone = str(input("ADD Python Git Here: "))
        clone = os.system(f"git clone {addClone}")
        lookup = os.system("ls")
        print()
        folder = str(input("Enter Target Folder Name: "))
        current = str(input("Add your curent file PATH: "))
        copy1 = os.system(f"sudo scp -r {current}{folder} /bin/")
        copy2 = os.system(f"sudo scp -r {current}{folder} /usr/local/bin/")
        print()
        print('Add Text below to vim:')
        print()
        print(f"export PATH=$HOME/bin/{folder}:/usr/local/bin/{folder}:$PATH")
        
        def ready3():
            print()
            print("Press y when ready")
            r = input()

            if r == 'y':
                vim = os.system("vim ~/.fishrc")
        ready3()

    
    if choice == '4':
        exit()

menu()
