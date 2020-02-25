'''
Das Haupt-File. Stellt die Virtuelle Umgebung für pygine bereit.
'''
import tkinter
import platform

'''
Anlegen der Variablen
'''

#Weite, Höhe
width, height = 800, 800
#Verschiebung
moved = (False if platform.platform().startswith('Windows') else True)
#Kontrolle der Plattform
divider = ('\\'if platform.platform().startswith('Windows') else '/')

'''
Erstellen der Haupt-Klasse
'''
class Main:
    '''
    Die Haupt-Klasse der Anwendung. Durch sie wird das Programm gesteuert.
    '''
    def __init__(self):
        #Meister definieren
        self.master = tkinter.Tk()
        #Weite und Höhe festlegen
        self.master['width'], self.master['height'] = width, height
        self.master.mainloop()

HAUPT = Main()
