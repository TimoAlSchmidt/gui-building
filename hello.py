import tkinter
from tkinter import ttk


def labelMaker(texter):
    label = ttk.Label(window, text=texter)
    label.grid()

def removeWidgets():
    for widget in window.winfo_children():
        widget.destroy()



def helloPrint():
    removeWidgets()
    labelMaker("Hello from function town")

window = tkinter.Tk()
window.title("Magic")
window.geometry("200x200")

button = ttk.Button(window, text="???", command=helloPrint)
button.grid()

window.mainloop()