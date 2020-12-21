# PATHmaker
An automated script for sending Python or Bash programms to your shell's global PATH.

# How It Works
Run program by typing `./pathmaker.sh` or `python3 pathmaker.py`. Then choose the shell of your choice by pressing the corresponding number. PATHmaker will then put the your desired programs into the needed /bin/ folders, and then create a PATH command for you to past into your ~/.shell-rc file. PATHmaker will open `vim` for you. Press `Shift + I` and then past the command into the file. 

To save the file with the new path, Press `Esc` and then type `:wq!` then press `Enter`. Your program has successfully been added into your shell. Now you can type the name of program file from any directory.

![Example](screenshot.png "Example")
