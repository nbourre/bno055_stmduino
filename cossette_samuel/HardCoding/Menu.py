from functools import singledispatch
from os import _AddedDllDirectory
import tkinter
from tkinter.constants import FALSE, LEFT, OFF, ON, RIGHT, TOP
from typing import Sized
import serial
import csv
from datetime import datetime
import threading

ser = serial.Serial('com3',115200)
ser.flushInput()

def show_about():
    about_window = tkinter.Toplevel(app)
    about_window.title("À propos")
    lb = tkinter.Label(about_window, text = "Nombre de tag = au nombre de choix de label que l'on veut./n/n Le type de mouvement = l'élément qui va être ajouter à la fin pour connaître le mouvement fait")
    lb.pack()

def bouton():
    root = tkinter.Tk()
    root.geometry('300x100')
    B1 = tkinter.Button(root, text="Write Data", command= main) 
    B1.pack(side = LEFT)
    B2 = tkinter.Button(root, text="ON/OFF", command= read)
    B2.pack(side = RIGHT)

def main():
    now = datetime.now()
    prefix = now.strftime("%Y-%m-%d_%H;%M;%S")
    while True:
        try:
            ser_bytes = ser.readline()
            decoded_bytes = ser_bytes[:-2].decode("utf-8")+"\n"
            print(decoded_bytes)
            with open(prefix + "_databrute.csv","a") as f:
                f.writelines(decoded_bytes)
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            break
  

def read():
        print("Actif")

#grosseur/titre de l'app
app = tkinter.Tk()
app.geometry("1080x720")
app.title("Embeded")
app.resizable(height=False, width=False)

mainmenu = tkinter.Menu(app)
#premier onglet contenu
first_menu = tkinter.Menu(mainmenu, tearoff=0)
first_menu.add_command(label="Read data from Arduino", command = bouton)
first_menu.add_command(label="Write data to Arduino", command = read)
first_menu.add_command(label="Quitter", command= app.quit)
#deuxième onglet contenu
second_menu = tkinter.Menu(mainmenu,  tearoff=0)
second_menu.add_command(label="Nombre de tag")
second_menu.add_command(label="Type de mouvement")
second_menu.add_command(label="READ.ME", command = show_about)
#séparation des onglets avec contenu à l'intérieur
mainmenu.add_cascade(label="Fichier", menu = first_menu)
mainmenu.add_cascade(label="Format", menu = second_menu)

app.config(menu=mainmenu)
app.mainloop()