'''
Das ist das Skript, mit dessen Start die Anwendung ausgeführt wird.
Zuerst wird alles Relevante importiert, und dann wird die Hauptfunktionalität durch die
Klasse Verwalter bereitgestellt.

Der Master der bei den Klassen von widgets.py übergeben werden muss ist self.master in der Klasse Verwalter.

Hier nichts ohne Absprache Coden!
'''

from widgets import (proportions, Loadscreen, Logscreen)
from compile_file import Compiler
from save import Saver
import tkinter

class Verwalter:
    def __init__(self):
        self.master = tkinter.Tk()
        self.master['width'] = proportions[0]
        self.master['height'] = proportions[1]
        self.compiler = Compiler()
        self.loadscreen = Loadscreen(self.master)
        self.loadscreen.demo()
        


MAIN = Verwalter()
