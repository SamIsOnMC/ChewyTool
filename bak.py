#!/usr/bin/env python
import click
import time
import os
import pathlib
import subprocess
os.system('printf "\033[8;20;130t"')
homedir = os.path.expanduser("~")
os.system('clear')
click.echo(click.style('       ▆▆▆▆    ▆     ▆   ▆▆▆▆▆▆▆▆  ▆           ▆           ▆  ▆▆▆▆▆▆▆▆▆      ▆▆▆▆▆        ▆▆▆▆▆      ▆           ▆▆▆▆▆▆▆▆▆       ', fg='magenta', bg="bright_black"))
click.echo(click.style('     ▆         ▆     ▆   ▆          ▆         ▆ ▆         ▆       ▆         ▆     ▆      ▆     ▆     ▆          ▆                ', fg='magenta', bg="bright_black"))
click.echo(click.style('   ▆           ▆     ▆   ▆           ▆       ▆   ▆       ▆        ▆        ▆       ▆    ▆       ▆    ▆         ▆                 ', fg='magenta', bg="bright_black"))
click.echo(click.style(' ▆             ▆▆▆▆▆▆▆   ▆▆▆▆         ▆     ▆     ▆     ▆         ▆       ▆         ▆  ▆         ▆   ▆          ▆▆▆▆▆▆▆▆▆▆       ', fg='magenta', bg="bright_black"))
click.echo(click.style('   ▆           ▆     ▆   ▆             ▆   ▆       ▆   ▆          ▆        ▆       ▆    ▆       ▆    ▆                    ▆      ', fg='magenta', bg="bright_black"))
click.echo(click.style('     ▆         ▆     ▆   ▆              ▆ ▆         ▆ ▆           ▆         ▆     ▆      ▆     ▆     ▆                   ▆       ', fg='magenta', bg="bright_black"))
click.echo(click.style('       ▆▆▆▆    ▆     ▆   ▆▆▆▆▆▆▆▆        ▆           ▆            ▆          ▆▆▆▆▆        ▆▆▆▆▆      ▆▆▆▆▆▆▆▆   ▆▆▆▆▆▆▆▆▆        ', fg='magenta', bg="bright_black"))
print()
print()
print()
click.echo(click.style('1. Command Line Tool', fg='blue'))
click.echo(click.style('2. CMD line websites', fg='blue'))
click.echo(click.style('3. Arch Better Installer', fg='blue'))
chewtools = input(": ")
if chewtools == "1":
    click.echo(click.style('Entering CMD line mode...', fg='red'))
    time.sleep(1.5)
    os.system('clear')
    while True:
        cmd = input("[ " + os.getcwd() + ' ]' + ' : ')
        if cmd == "exit":
            import chewtool
        elif cmd == "cd":
            path = input("Path: ")
            if path == "~":
                os.chdir(homedir)
                print("Set cd to: " + homedir)
            else:
                os.chdir(path)
        else:
            os.system(cmd)
elif chewtools == "3":
    os.system("clear")
    package = input("Package name: ")
    os.system('git clone https://aur.archlinux.org/' + package + ".git")
    os.system('cd ' + package)
    os.chdir(os.getcwd() + "/" + package)
    os.system("ls")
    os.system("makepkg")
    print("Please install the dependencies if you get an error.")
    os.system('sudo pacman -U ' + package + "*.pkg.tar.zst")
    time.sleep(5)
    os.system("clear")
    os.system("cd " + homedir + "Py")
    os.chdir(homedir + "/Py")
    os.system("python chewtool.py")
    exit()
else:
    click.echo(click.style('Invalid answer.', fg='red'))
    time.sleep(1)
    os.system("python chewtool.py")
    exit()