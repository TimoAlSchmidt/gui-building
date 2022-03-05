import random, tkinter
from tkinter import ttk

random.seed()

status = {
    "won" : 0,
    "verloren" : 0
}

won = False
temperatuur = 0
raadGetal = 0
getal = 0
geradenGetallen = 0
flag = True
raadNr = 0


window = tkinter.Tk()
window.title("Rader")

getal = tkinter.IntVar()



def removeWidgets():
    for widget in window.winfo_children():
        widget.destroy()


def removeSpecificWidgets():
    for widget in window.winfo_children():
        if type(widget) is ttk.Label:
            texts = widget.cget("text")
            if "Iets" in texts or "Je" in texts:
                widget.destroy()


def labelMaker(texter):
    label = ttk.Label(window, text=texter)
    label.pack()


def start():    
    global raadGetal
    raadGetal = random.randint(1, 100)
    removeWidgets()
    labelMaker("Raad en getal tussen 1-100.")
    entry = ttk.Entry(window, text=getal)
    entry.pack()
    btn = ttk.Button(window, text="Raden!", command=raden)
    btn.pack()


def raden():
    global raadNr
    removeSpecificWidgets()
    raadNr += 1
    temperatuur = raadGetal - getal.get()
    texts = ""
    if temperatuur < 0:
        texts = "Iets lager"
    elif temperatuur != 0:
        texts = "Iets hoger"

    labelMaker(texts)

    temperatuur = abs(temperatuur)
    if temperatuur == 0:
        labelMaker("Gefeliciteerd!")
        return end("won")
    elif temperatuur <= 20:
        texts = "Je bent heel warm."
    elif temperatuur <= 50:
        texts = "Je bent warm."
    
    if not "Iets" in texts:
        labelMaker(texts)
    if raadNr >= 10:
        end("verloren")


def end(texter):
    global status, raadNr, geradenGetallen
    removeWidgets()
    geradenGetallen += 1
    raadNr = 0
    status[texter] += 1

    if geradenGetallen >= 20:
        return stop()

    labelMaker("Gewonnen: "+str(status["won"])+"\nVerloren: "+str(status["verloren"]))
    labelMaker("Nog een ronde spelen?")

    btn = ttk.Button(window, text="Ja",command=start)
    btn.pack()
    btn = ttk.Button(window, text="Nee",command=stop)
    btn.pack()


def stop():
    removeWidgets()
    labelMaker("Eindscore: "+str(status["won"])+"/"+str(status["verloren"]+status["won"])+" gewonnen")
    btn = ttk.Button(window, text="Eind",command=lambda : window.destroy())
    btn.pack()


start()

window.mainloop()
