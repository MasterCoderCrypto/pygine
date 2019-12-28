'''
In dieses Modul gehören alle Widgets, also jedes Fenster der Applikation.
Ein Fenster muss dabei eine Klasse sein die von tkinter.Frame erbt und als ersten 
Parameter der __init__-Funktion einen master übergeben bekommt, mit dem ihr dann die Superklasse
instanziiert. Unter den Kopf einer Klasse müssen alle Attribute und Methoden mit Beschreibung aufgelistet sein.

Es ist besser wenn wir statt der Methode pack() die Methode place() verwenden, die relativ zu den unten angegebenen 
Geometrien proportions die Elemente platziert. Um das ganze dann komfortabler zu machen muss jede Klasse die Methode
resize(self) implementieren, die durch einen Event-Listener bei der Formatierung des Fensters alle Elemente wieder relativ zur
aktuellen Fenstergröße platziert.

Die Fenster können nun allerdings nicht mehr mit der Methode forget() und pack gewechselt werden, sattdessen verwenden wir destroy()
und instanziieren dann einfach eine neue Klasse.

Zur Vereinfachung lasst eure Klassen nicht nur von tkinter.Frame sondern auch von der Abstrakten Klasse WIN erben.

Später werden alle Klassen aus diesem Modul in das Main-Modul importiert, wo sie dann von einer
Veraltungsklasse verwaltet werden.

Bsp:

class Menu(tkinter.Frame, WIN):
    """
    self.button  | Der Button der Klasse Menu
    
    self.resize  | Resize Methode
    """
    def __init__(self, master):
        super().__init__(master)
        self.place(x=0, y=0, width=proportions[0], height=proportions[1])
        ...
        self.button = tkinter.Button(self)
    
    def resize(self):
        ...
        
        
proportions ist eine Liste, die ebenfalls importiert wird, sie gibt die aktuelle Fenstergröße, [1] ist dabei die Weite
und [2] die Höhe der Anwendung
'''

from abc import ABC, abstractmethod
import tkinter

proportions = [800, 600]

class WIN(ABC):
    @abstractmethod 
    def resize(self):
        pass
