import tkinter
from tkinter import ttk
from tkinter.messagebox import askyesno, showinfo

klaar = False
hoeveelheidPerMaat = [0,0,0]
smallPrijs = 11.79
mediumPrijs = 13.79
largePrijs = 16.79
smallTotaal = 0.0
mediumTotaal = 0.0
largeTotaal = 0.0
totaalPrijs = 0.0

window = tkinter.Tk()
window.title("Pizza Calculator")
window.geometry("500x200")
maat = tkinter.StringVar()
hoeveelheid = tkinter.IntVar()

maten = {"Small" : 0, "Medium" : 1, "Large" : 2}


def removeWidgets():
    for widget in window.winfo_children():
        widget.destroy()


def start():
    removeWidgets()
    label = ttk.Label(window, text="Kies uw maat:")
    label.pack()
    m = ttk.Radiobutton(window, value="Small", text="Small (25 cm; €"+str(smallPrijs)+")",variable=maat)
    m.pack()
    m = ttk.Radiobutton(window, value="Medium", text="Medium (30 cm; €"+str(mediumPrijs)+")",variable=maat)
    m.pack()
    m = ttk.Radiobutton(window, value="Large", text="Large (35 cm; €"+str(largePrijs)+")",variable=maat)
    m.pack()
    btn = ttk.Button(window, text="Verder gaan", command=kiesHoeveel)
    btn.pack()


def kiesHoeveel():
    removeWidgets()
    label = ttk.Label(window, text="Hoeveel pizza's wilt u?")
    label.pack()
    entry = ttk.Entry(window, text=hoeveelheid)
    entry.pack()
    btn = ttk.Button(window, text="Verder gaan", command=einde)
    btn.pack()


def einde():
    global totaalPrijs
    hoeveelheidPerMaat[maten[maat.get()]] = int(hoeveelheid.get())
    smallTotaal = round(hoeveelheidPerMaat[0]*smallPrijs, 2)
    mediumTotaal = round(hoeveelheidPerMaat[1]*mediumPrijs, 2)
    largeTotaal = round(hoeveelheidPerMaat[2]*largePrijs, 2)
    totaalPrijs = round(smallTotaal+mediumTotaal+largeTotaal, 2)
    removeWidgets()
    label = ttk.Label(window, text="U heeft nu "+str(hoeveelheidPerMaat[0])+" Small pizza's (€"+str(smallTotaal)+"), "+str(hoeveelheidPerMaat[1])+" Medium pizza's (€"+str(mediumTotaal)+") en "+str(hoeveelheidPerMaat[2])+" Large pizza's (€"+str(largeTotaal)+").")
    label.pack()
    label = ttk.Label(window, text="Dit kost €"+str(totaalPrijs)+".\nIs dit alles?")
    label.pack()
    btn = ttk.Button(window, text="Ja", command=bon)
    btn.pack()
    btn = ttk.Button(window, text="Nee", command=start)
    btn.pack()


def bon():
    removeWidgets()
    label = ttk.Label(window, text="De totale prijs is €"+str(totaalPrijs))
    label.pack()


start()

window.mainloop()