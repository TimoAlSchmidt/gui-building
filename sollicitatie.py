import tkinter
from tkinter import ttk, Scrollbar
from tkinter.messagebox import askyesno, showinfo


def removeWidgets():
    for widget in window.winfo_children():
        widget.destroy()


def labelMaker(texter):
    label = ttk.Label(window, text=texter,font=("Arial",8))
    label.grid()


def entryMaker(texter=None):
    entry = ttk.Entry(window, text=texter,width=20)
    entry.grid()


def einde():
    sol = False
    removeWidgets()
    if int(lengte.get()) < 150 or int(gewicht.get()) < 90 or ((int(dierjaar.get()) < 4) and (int(jongleerjaar.get()) < 5) and (int(acrobatiekjaar.get() < 3))) or mbo.get() == "Nee" or vrachtwagen.get() == "Nee" or hoed.get() == "Nee" or (geslacht.get() == "Man" and int(snor.get()) < 10) or (geslacht.get() == "Vrouw" and not (haar.get() == "Ja" or (int(lengteHaar.get()) >= 20))) or certificaat.get() == "Nee":
        sol = False
    if(sol):
        labelMaker("Beste "+naam.get()+",\nProficiat! U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV")
    else:
        labelMaker("Helaas voldoet U niet aan onze strenge eisen, het spijt ons.")

    btn = ttk.Button(window, text="Eind",command=lambda : window.destroy())
    btn.grid()

def conditionalEntry(var, varjaar, quest1, quest2):
    varjaren = ttk.Entry(window, text=varjaar,state="disabled")
    labelMaker(quest1)
    g = ttk.Radiobutton(window, value="Ja", text="Ja", variable=var, command= lambda: varjaren.config(state="enabled", text=varjaar.set("0")))
    g.grid()
    g = ttk.Radiobutton(window, value="Nee", text="Nee", variable=var, command= lambda: varjaren.config(state="disabled", text=varjaar.set("0")))
    g.grid()

    labelMaker(quest2)
    varjaren.grid()


def yesOrNo(yes, no, var, quest):
    labelMaker(quest)
    g = ttk.Radiobutton(window, value=yes, text=yes,variable=var)
    g.grid()
    g = ttk.Radiobutton(window, value=no, text=no,variable=var)
    g.grid()



window = tkinter.Tk()
window.title("Solicitatie")

naam = tkinter.StringVar()
geslacht = tkinter.StringVar()
lengte = tkinter.IntVar()
gewicht = tkinter.IntVar()
dier = tkinter.StringVar()
dierjaar = tkinter.IntVar()
jongleer = tkinter.StringVar()
jongleerjaar = tkinter.IntVar()
acrobatiek = tkinter.StringVar()
acrobatiekjaar = tkinter.IntVar()
mbo = tkinter.StringVar()
vrachtwagen = tkinter.StringVar()
hoed = tkinter.StringVar()
haar = tkinter.StringVar()
lengteHaar = tkinter.StringVar()
certificaat = tkinter.StringVar()

snor = tkinter.IntVar()
antwoord = tkinter.StringVar()

labelMaker("Wat is uw naam?")
entryMaker(naam)

yesOrNo("Man", "Vrouw", geslacht, "Welk geslacht bent u?")

labelMaker("Hoe lang bent u? Graag gehele centimeters.")
entryMaker(lengte)


labelMaker("Hoe zwaar bent u? Graag gehele kilogrammen.")
entryMaker(gewicht)



conditionalEntry(dier, dierjaar, "Heeft u praktijkervaring met dieren-dressuur?", "Hoeveel jaren ervaring heeft u gehad?")
conditionalEntry(jongleer, jongleerjaar, "Heeft u ervaring met jongleren?", "Hoeveel jaren ervaring heeft u met jongeleren?")
conditionalEntry(acrobatiek, acrobatiekjaar, "Heeft u ervaring met acrobatiek?", "Hoeveel jaren ervaring heeft u met acrobatiek?")


yesOrNo("Ja", "Nee", mbo, "Heeft u bezit van een MBO-4 diploma?")
yesOrNo("Ja", "Nee", vrachtwagen, "Heeft u bezit van een geldig vrachtwagen rijbewijs?")
yesOrNo("Ja", "Nee", tkinter.StringVar(), "Heeft u bezit van een pizza bakkerij's diploma?")
yesOrNo("Ja", "Nee", hoed, "Heeft u bezit van een hoge hoed?")

#Important if male
labelMaker("Hoe breed is uw snor? Graag gehele centimeters.")
entryMaker(snor)
#    if not snor.get() > 10:
#        solliciteren = False

#Important if female
yesOrNo("Ja", "Nee", haar, "Heeft u rood krulhaar?")

#if(input() == "N"):
#   solliciteren = False
#ABOVE OR BELOW, DOESN'T HAVE TO BE BOTH.

labelMaker("Hoe lang is uw haar? Graag gehele centimeters.")
entryMaker(lengteHaar)
#if(lengteHaar.get()) < 20):
#   solliciteren = False

#importance end


yesOrNo("Ja", "Nee", tkinter.StringVar(), "Heeft u zwarte kleding thuis?")

labelMaker("Hoe snel kunt u rennen?")
entryMaker()

yesOrNo("Ja", "Nee", certificaat, "Heeft u een certificaat \"Overleven met gevaarlijk personeel\"?")
#if(input() == "N"):
#   solliciteren = False

btn = ttk.Button(window, text="Klaar", command=einde)
btn.grid(row=0, column=1)
        


window.mainloop()