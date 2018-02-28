from tkinter import *
from Tabelle import *
from  BudgetApp import *

class Eingabe(Frame):

    def __init__(self):
        self.a = None
        self.b = None
        self.c = None

        self.rootEingabe = Tk()
        self.rootEingabe.resizable(False, False)

        Frame.__init__(self)
        self.pack
        self.createEingabeWidgets()
        self.showEingabe()

    def showEingabe(self):
        self.rootEingabe.title("Eintrag hinzufügen")
        width = 500
        height = 200

        screenWidth = self.rootEingabe.winfo_screenwidth()
        screenHeight = self.rootEingabe.winfo_screenheight()

        x_coordinate = (screenWidth / 2) - (width / 2)
        y_coordinate = (screenHeight / 2) - (height / 2)

        self.rootEingabe.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))

        mainloop()

    def createEingabeWidgets(self):


        #Buttons
        self.ready = Button(self.rootEingabe, text="Fertig", bg="#5e5e5e", fg="#a1dbcd", height=2, width=10, command = self.readyF)

        #Label/Entry
        lzzz = Label(self.rootEingabe)

        l1 = Label(self.rootEingabe, text="Zweck", height = 2)
        l2 = Label(self.rootEingabe, text="Betrag in Euro", height = 2)
        l3 = Label(self.rootEingabe, text="Anmerkung", height = 2)

        self.zEntry = Entry(self.rootEingabe, width= 60)
        self.bEntry = Entry(self.rootEingabe, width= 60)
        self.aEntry = Entry(self.rootEingabe, width= 60)

        lzzz.grid(row = 0)
        l1.grid(row =1)
        l2.grid(row=2)
        l3.grid(row=3)

        self.zEntry.grid(row=1, column=1)
        self.bEntry.grid(row=2, column=1)
        self.aEntry.grid(row=3, column=1)
        self.ready.grid(row = 4, column=1)

    def readyF(self):
        #Application.count += 1
        Application.ifclicked()
        self.a = self.zEntry.get()
        self.b = self.bEntry.get()
        self.c = self.aEntry.get()
        self.rootEingabe.destroy()









