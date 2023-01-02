#!/bin/python3
import os

try:
  import colorama, hashlib, pycrypto, telegram
  os.system("clear")
  os.system("python3 main.py")
  

except:
  os.system("pip3 install colorama")
  os.system("pip3 install hashlib")
  os.system("pip3 install telegram")
  os.system("pip3 install pycryptodome")
  os.system("pip3 install python-telegram-bot")
  os.system("clear")
  os.system("python3 main.py")
  
