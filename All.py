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

def Noelle():
  os.system("python3 Noelle.py")

def Baam():
  os.system("python3 Baam.py")

def Kawa():
  os.system("python3 Kawa.py")

def Chacon():
  os.system("python3 Chacon.py")

def Alcapone():
  os.system("python3 Luis.py")

def Yenna():
  os.system("python3 Salamy.py")

t1= threading.Thread(target=Dayi)
t2= threading.Thread(target=Alcapone)
t3= threading.Thread(target=Yenna)
t4= threading.Thread(target=Brenda)
t5= threading.Thread(target=Duwars)
t6= threading.Thread(target=Resurrection)
t7= threading.Thread(target=Noelle)
t8= threading.Thread(target=Baam)
t9= threading.Thread(target=Kawa)
t10= threading.Thread(target=Chacon)
t11= threading.Thread(target=Luis)
t12= threading.Thread(target=Salamy)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()
