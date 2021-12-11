from tkinter import *
import tkinter
import serial
import csv
from datetime import datetime
from threading import *
stopflag = False

ser = serial.Serial('com3',115200)
ser.flushInput()
gui = Tk()
var = IntVar()
s = Spinbox(
        gui,
        textvariable=var,
        from_ = -360,
        to = 360,
        font=('sans-serif', 14), 
        width= 24,
        justify=CENTER,
        bg='#02ffff'
        
    )
def sel():
    selected = "You have selected : " + str(v.get()) + " " + str(s.get())
    label.config(text = selected, font=('sans-serif', 14), width= 24, padx=8)
v = StringVar()
txt = StringVar() 
lr = Radiobutton(gui, text="LR", variable=v, value="LR", background = '#ffb5d8', font=('sans-serif', 14), justify=CENTER, width=22, padx= 6, relief=RAISED, command=sel)
rr = Radiobutton(gui, text="RR", variable=v, value="RR", background = 'orange', font=('sans-serif', 14),justify=CENTER, width=22, padx= 6, relief=RAISED, command=sel)
t = Radiobutton(gui, text="T", variable=v, value="T", background = 'yellow', font=('sans-serif', 14),justify=CENTER, width=22, padx= 6, relief=RAISED, command=sel)
b = Radiobutton(gui, text="B", variable=v, value="B", background = 'lime', font=('sans-serif', 14), justify=CENTER, width=22, padx= 6, relief=RAISED, command=sel)
fp = Radiobutton(gui, text="FP", variable=v, value="FP", background = 'cyan', font=('sans-serif', 14), justify=CENTER, width=22, padx= 6, relief=RAISED, command=sel)
rp = Radiobutton(gui, text="RP", variable=v, value="RP", background = '#856ff8', font=('sans-serif', 14), justify=CENTER, width=22, padx= 6, relief=RAISED, command=sel)
def main():
    gui.resizable(height=False, width=False)
    gui.title("Embeded")
    gui.config(bg='black')
def spinbox():
    cb2 = StringVar()
    lab3 = Label(gui, width=24, padx=8, textvariable=cb2, font=('sans-serif', 14), background='purple', justify=CENTER)
    cb2.set("Choose the measure")
    lab3.pack(anchor = W)
    var.set(0)
    s.pack(anchor = W)
def radiobutton(): 
    cb1 = StringVar()
    lab2 = Label(gui, width=24, padx=8, textvariable=cb1, font=('sans-serif', 14), background='purple', justify=CENTER)
    cb1.set("Choose the desired tag") 
    lab2.pack(anchor = W)
    lr.pack(anchor = W)
    rr.pack(anchor = W)
    t.pack(anchor = W)
    b.pack(anchor = W)
    fp.pack(anchor = W)
    rp.pack(anchor = W)
def threadingstart():
    stopflag = False
    t1.start()
    
def threadingstop():
    stopflag = True
    
def read():
    now = datetime.now()
    prefix = now.strftime("%Y-%m-%d_%H;%M;%S")
    tag = str(v.get())
    angle = str(s.get())
    while stopflag:
        try:
            ser_bytes = ser.readline()
            decoded_bytes = ser_bytes[:-2].decode("utf-8")+ tag +";" + angle + "\n"
            print(decoded_bytes)
            with open(prefix + "_databrute.csv","a") as f:
                f.writelines(decoded_bytes)
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            break
        #if stopflag == True:
         #   break

t1 = Thread(target=read)  
t2 = Thread(target= read)
if __name__ == '__main__':
    main()
    spinbox()
    radiobutton()
     
label = Label(gui)
label.pack(anchor= W)  
B1 = tkinter.Button(gui, text="Write Data", justify=CENTER, width=12, bg='lime', font=('sans-serif', 14), command = threadingstart) 
B1.pack(side = LEFT)
B2 = tkinter.Button(gui, text="Stop Write Data", justify=CENTER, width=12, bg ='red', font=('sans-serif', 14), command = threadingstop)
B2.pack(side = RIGHT)

gui.mainloop()
