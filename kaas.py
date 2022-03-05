import tkinter
from tkinter import ttk
from tkinter.messagebox import askyesno, showinfo

vragen = ["Is de kaas geel?", "Zitten er gaten in?", "Is de kaas belachelijk duur?", "Is de kaas hard als steen?", "Heeft de kaas blauwe schimmels?", "Heeft de kaas een korst?", "Heeft de kaas een korst?"]
antwoorden = ["Emmenthaler", "Leerdammer", "Parmigiano Reggiano", "Goudse Kaas", "Blue de Rochbaron", "Foume d'Ambert", "Camembert", "Mozzarella"]
stap = 0
binary = 0
vraagnummer = 0

while stap < 3:
    answer = askyesno(message=vragen[vraagnummer])
    stap += 1
    binary = binary << 1
    vraagnummer += 1
    if not answer:
        vraagnummer += 1
        if(stap == 1):
            vraagnummer += 2
        binary += 1    

showinfo(message="De kaas is {}".format(antwoorden[binary]))