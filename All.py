import os
import threading

def Dayi():
  os.system("python3 Dayi.py")

def Alcapone():
  os.system("python3 Alcapone.py")

def Yenna():
  os.system("python3 Yenna.py")

def Brenda():
  os.system("python3 Brenda.py")

def Duwars():
  os.system("python3 Duwars.py")

def Resurrection():
  os.system("python3 AltChacon2.py")

t1= threading.Thread(target=Dayi)
t2= threading.Thread(target=Alcapone)
t3= threading.Thread(target=Yenna)
t4= threading.Thread(target=Brenda)
t5= threading.Thread(target=Duwars)
t6= threading.Thread(target=Resurrection)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
