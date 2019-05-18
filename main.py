#ask if on mobile, will modify wlkmsg call
device = input("are you on a phone? please type y or n")


#library import handling
import pyfiglet
from pyfiglet import Figlet as pyf
import time
import os

#.py import handling
import welcomemessage as wlkm

#variables
wndwx = os.get_terminal_size().columns
wndwxy = os.get_terminal_size().lines

#functions
def analyze(tba):
  if tba == "help":
    print("="*wndwx)
    print("Availible commands:")
    print("'play', will spin the reels")
    print("'chips', will tell you how many chips, and spins you have")
    print("="*wndwx)
    return "success"
  else:
    return "failed"

def ask():
  pin = input("what would you like to do, type 'help' to see options >>> ")

  return pin
  

#events


#init program
def slots_init():
  #welcome message
  wlkm.wlkmsg(device)
  
#handle init and program
#init
slots_init()

#while true to run program forever
while (True):
    pin = ask()
    ant = analyze(pin)

    if ant == "failed":
        raise Exception("bad input")