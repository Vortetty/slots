#libraries
import pyfiglet
from pyfiglet import Figlet as pyf
import time

#welcome message
def wlkmsg(device):
  if device == "n":
      block = pyf(font="block")
      print(block.renderText("Welcome"))
      print(block.renderText("to the"))
      print(block.renderText("Lucky"))
      print(block.renderText("Py Slots"))
      time.sleep(3)
      for i in range(0,33):
          print("\n")
          time.sleep(.2)
  else:
      print("welcome to the lucky py slots")