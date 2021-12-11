import tkinter
import time
import winsound

FREQ = 2500
DUR = 150

after_id = None
secs = 0

def beeper():
    global after_id
    global secs
    secs += 1
    if secs % 2 == 0:  # every other second
        winsound.Beep(FREQ, DUR)
    after_id = top.after(1000, beeper)  # check again in 1 second

def start():
    global secs
    secs = 0
    beeper()  # start repeated checking

def stop():
    global after_id
    if after_id:
        top.after_cancel(after_id)
        after_id = None

top = tkinter.Tk()
top.title('MapAwareness')
top.geometry('200x100')

startButton = tkinter.Button(top, height=2, width=20, text="Start",
                             command=start)
stopButton = tkinter.Button(top, height=2, width=20, text="Stop",
                            command=stop)
startButton.pack()
stopButton.pack()
top.mainloop()