from tkinter import *
import tkinter


gui = Tk()
var = IntVar()
s = Spinbox(
        gui,
        textvariable=var,
        from_ = -360,
        to = 360,
        font=('sans-serif', 14), 
        width= 22,
        justify=CENTER,
        
    )
def sel():
    selected = "Vous avez sélectionné : " + str(v.get()) + " " + str(s.get()) + " "+ str(txt.get())
    label.config(text = selected, font=('sans-serif', 14))
v = StringVar()
txt = StringVar() 
lr = Radiobutton(gui, text="LR", variable=v, value="LR", background = 'red', font=('sans-serif', 14), justify=CENTER, width=20, padx= 5, relief=RAISED, command=sel)
rr = Radiobutton(gui, text="RR", variable=v, value="RR", background = 'orange', font=('sans-serif', 14),justify=CENTER, width=20, padx= 5, relief=RAISED, command=sel)
t = Radiobutton(gui, text="T", variable=v, value="T", background = 'yellow', font=('sans-serif', 14),justify=CENTER, width=20, padx= 5, relief=RAISED, command=sel)
b = Radiobutton(gui, text="B", variable=v, value="B", background = 'lime', font=('sans-serif', 14), justify=CENTER, width=20, padx= 5, relief=RAISED, command=sel)
fp = Radiobutton(gui, text="FP", variable=v, value="FP", background = 'cyan', font=('sans-serif', 14), justify=CENTER, width=20, padx= 5, relief=RAISED, command=sel)
rp = Radiobutton(gui, text="RP", variable=v, value="RP", background = 'pink', font=('sans-serif', 14), justify=CENTER, width=20, padx= 5, relief=RAISED, command=sel)
none = Radiobutton(gui, text="NONE", variable=v, value="NONE", background = '#856ff8', font=('sans-serif', 14),justify=CENTER, width=20, padx= 5, relief=RAISED, command=sel)
cm = Radiobutton(gui, text="cm", variable = txt, value="cm", background = '#856ff8', font=('sans-serif', 14),justify=CENTER, width=20, padx= 5, relief=RAISED, command=sel)
dg = Radiobutton(gui, text="degré", variable=txt, value="degré", background = 'pink', font=('sans-serif', 14), justify=CENTER, width=20, padx= 5, relief=RAISED, command=sel)
def main():
    gui.resizable(height=False, width=False)
    gui.title("Embeded")
    gui.config(bg='black')
def spinbox():
    var.set(0)
    s.pack(anchor = W)
def radiobutton(): 
    cb1 = StringVar()
    lab2 = Label(gui, width=22, padx=6, textvariable=cb1, font=('sans-serif', 14), background='purple', justify=CENTER)
    cb1.set("Choisir le tag voulue") 
    lab2.pack(anchor = W)
    lr.pack(anchor = W)
    rr.pack(anchor = W)
    t.pack(anchor = W)
    b.pack(anchor = W)
    fp.pack(anchor = W)
    rp.pack(anchor = W)
    none.pack(anchor = W)
    cb = StringVar()
    lab = Label(gui, width=22, padx=6, textvariable=cb, font=('sans-serif', 14), background='purple', justify=CENTER)
    cb.set("Choisir le type de donnée")
    lab.pack(anchor = W)
    cm.pack(anchor = W)
    dg.pack(anchor = W)
def touch1():
    print("Actif")
    gui.config(bg='lime')
def touch2():
    print("STOP")
    gui.config(bg='red')
if __name__ == '__main__':
    main()
    spinbox()
    radiobutton()
label = Label(gui)
label.pack()  
B1 = tkinter.Button(gui, text="Write Data", justify=CENTER, width=18, command = touch1) 
B1.pack(side = LEFT)
B2 = tkinter.Button(gui, text="OFF", justify=CENTER, width=18, command = touch2)
B2.pack(side = RIGHT)

gui.mainloop()
