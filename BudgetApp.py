from tkinter import *
from Tabelle import *
from Eingabefeld import *
import sys


class Application(Frame):

    def __init__(self):
        self.root = Tk()
        #self.root.resizable(False, False)
        Frame.__init__(self)
        self.pack
        self.createWidgets()
        self.Window()

    def Window(self):
        table = Table(self.root, ["Zweck", "Betrag in Euro", "Anmerkung"], column_minwidths=[None, None, None])
        table.pack(expand=True, fill=X, padx=10, pady=10)
        table.set_data([[1, 1, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
        table.cell(0, 0, "")
        table.cell(1, 1, "Hi")
        self.root.title("Kostenplan")
        width = 700
        height = 500

        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        x_coordinate = (screenWidth / 2) - (width / 2)
        y_coordinate = (screenHeight / 2) - (height / 2)

        self.root.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))

        mainloop()

    def createWidgets(self):
        # Buttons
        self.erstellen = Button(self.root, text="Eintrag hinzufügen", bg="#5e5e5e", fg="#a1dbcd", height=2, width=100, command = self.EingabeWindow)


        # hinzufügen +
        self.erstellen.pack(side=BOTTOM)

    def EingabeWindow(self):
        Eingabe()


Application()
