#!/bin/python3
import os

try:
  import colorama, hashlib, pycrypto
  os.system("clear")
  os.system("python3 main.py")
  

except:
  os.system("pip3 install colorama")
  os.system("pip3 install hashlib")
  os.system("pip3 install pycrypto")
  os.system("clear")
  os.system("python3 main.py")
  