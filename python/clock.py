from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("clock")

def time():
    string = strftime('%H:%M:%S %p')
    # h for hour m for minute s for seconds and p for am pm
    label.config(text = string)
    label.after(1000, time)

label = Label(root, background = "black",foreground = "cyan",
              font = ("ds-digital", 80))
label.pack(anchor = 'center')

time()
mainloop()
