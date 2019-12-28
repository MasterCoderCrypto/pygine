'''
In dieses Modul gehören alle Widgets, also jedes Fenster der Applikation.
Ein Fenster muss dabei eine Klasse sein die von tkinter.Frame erbt und als ersten
Parameter der __init__-Funktion einen master übergeben bekommt, mit dem ihr dann die Superklasse
instanziiert. Unter den Kopf einer Klasse müssen alle Attribute und Methoden mit Beschreibung aufgelistet sein.

Es ist besser wenn wir statt der Methode pack() die Methode place() verwenden, die relativ zu den unten angegebenen
Geometrien proportions die Elemente platziert. Um das ganze dann komfortabler zu machen muss jede Klasse die Methode
resize(self) implementieren, die durch einen Event-Listener bei der Formatierung des Fensters alle Elemente wieder relativ zur
aktuellen Fenstergröße platziert. resize muss wiederum die Methode replace() aufrufen, die nun alles neu platziert.

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
        tkinter.Frame.__init__(master)
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
from farbkonstanten import constants as const
import PIL
import time

proportions = [800, 600]

class WIN(ABC):
    @abstractmethod
    def resize(self):
        pass
    @abstractmethod
    def replace(self):
        pass

class Logscreen(tkinter.Frame, WIN):
    '''
    Diese Klasse zeigt den Ladebildschirm an. Die Loadbar muss durch eine Methode extern konfiguriert werden.
    Sie bekommt als Parameter den Pfad zum gif als String, das im Hintergrund laufen soll.

    ATTRS:

    self.canvas            | Das Canvas im dem alles Dargestellt wird
    self.gif               | Das eigene Gif
    self.namelabel         | Das Label, das als Anzeige zum Nutzernamen fungiert
    self.labelwidth & height | Die Höhe und Breite der inneren label
    self.entrywidth & height | Die Höhe und Breite der inneren entrys
    self.fontsize          | Die Schrifgtgröße
    self.master            | Der Master, um proportions anzupassen

    METHODS:

    resize(self)           | Die resize Methode
    bind_all(self)         | Bindet alle inneren Widgets an die gesuchten Methoden.
    format_background(self)| Formatiert das Gif passend zum Hintergrund
    replace(self)          | PLatziert alle Widgets, erstellt sie gegebenenfalls neu
    get_info(self)         | G

    '''
    def __init__(self, master):
        super().__init__(master)
        self.place(x=0, y=0, width=proportions[0], height=proportions[1])
        #Master zwischenspeichern
        self.master = master
        #canvas erstellen
        self.canvas = tkinter.Canvas(self)
        #Die eigenen Entry-und Label Weiten
        self.labelwidth = 120
        self.labelheight = 50
        self.entrywidth = 90
        self.entryheight = 50
        #Die Schriftgröße
        self.fontsize = 14
        #alles relativ platzieren
        self.replace()
        #alles binden
        self.bind_all()

    def bind_all(self):
        pass

    def resize(self):
        pass

    def replace(self):
        '''
        In dieser Methode werden alle inneren Widgets neu platziert, und
        das Hintergrundbild wird formatiert.
        '''
        #Alles zerstören
        self.canvas.destroy()
        #Canvas kreiren
        self.canvas = tkinter.Canvas(self)
        self.canvas.place(x=0, y=0, height=proportions[0], width=proportions[1])
        self.canvas.place(x=0, y=0, width=proportions[0], height=proportions[1])
        #alle label erstellen
        self.namelable = self.namelabel = tkinter.PhotoImage(file=r'Bilder\Intro\Label.png', height=90)
        self.canvas.create_image(proportions[0]//2-(self.labelwidth//2+self.entrywidth//2),
        proportions[1]//2-self.labelheight*3, image=self.namelable, anchor='nw')
        #Text in die Label schreiben
        self.canvas.create_text(proportions[0]//2-(self.labelwidth//2+self.entrywidth//2)+85,
        proportions[1]/2-self.labelheight*3+75, text='Nutzername', fill='white', font=('arial', self.fontsize, 'normal'))
        #Entrys erstellen
        self.nameentry = tkinter.Entry(self.canvas)
        self.username = tkinter.StringVar('')
        self.nameentry['textvariable'] = self.username

        #Nun noch formatieren
        self.format_background()

    def format_background(self):
        pass

class Loadscreen(tkinter.Frame, WIN):
    '''
    Diese Klasse zeigt den Ladebildschirm

    ATTRS:

    self.canvas        | das eigene Canvas
    self.gif           | Das im Hintergrund abgespielte Gif
    selg.bg            | Der Transparente schleier
    self.background_image| Das Hintergrund-Gif
    self.fontsize      | Die Schriftgröße
    self.loaded        | Der Ladefrtschritt
    seld.load_width, load_height | Die weite bzw höhe des Ladebalkens

    METHODS:

    resize & replace | bekannt
    actualize(self, percent) | aktualisiert den Ladebalken
    bind_all(self)   | Bindet alle Elemente

    '''
    def __init__(self, master, gif=None):
        super().__init__(master)
        #canvas erstellen
        self.place(x=0, y=0, width=proportions[0], height=proportions[1])
        self.canvas = tkinter.Canvas(self)
        self.gif = gif
        self.loaded = 0
        self.fontsize = 20
        self.load_length = 200
        self.load_height = 30
        #widgets placen
        self.replace()

    def resize(self):
        pass

    def replace(self):
        '''
        Diese Methode platziert alle inneren Widgets neu
        '''
        self.canvas.destroy()
        self.canvas = tkinter.Canvas(self)
        self.canvas.place(x=0, y=0, width=proportions[0], height=proportions[1])
        #Das Gif setzen
        if self.gif is not None:
            self.background_image = tkinter.PhotoImage(file=self.gif, width=proportions[0], height=proportions[1])
            self.canvas.create_image(0-100, 0-100, image=self.background_image, anchor='nw')
        #Die Transparenz setzen
        self.bg = tkinter.PhotoImage(file=r'Bilder\Load\schleier.png', width=proportions[0], height=proportions[1])
        self.canvas.create_image(0, 0, image=self.bg, anchor='nw')
        #Text schreiben
        self.canvas.create_text(proportions[0]//2-self.fontsize//2,
        proportions[1]//2-self.fontsize//2, text='Loading '+str(self.loaded)+'%', font=('arial', self.fontsize, 'normal'), fill='white')
        self.canvas.create_rectangle(proportions[0]//2-self.fontsize//2-90,
        proportions[1]//2+30, proportions[0]//2-self.fontsize//2+self.load_length-90, proportions[1]//2+self.load_height+30)
        #LadeBalken
        self.canvas.create_rectangle(proportions[0]//2-self.fontsize//2-90,
        proportions[1]//2+30, round((self.loaded/100*self.load_length)+proportions[0]//2-self.fontsize//2-90),
        proportions[1]//2+self.load_height+30, fill='#8000FF')

    def bind_all(self):
        pass

    def actualize(self, value):
        self.loaded += value
        self.replace()
        self.update()

    def demo(self):
        for t in range(100):
            time.sleep(0.2)
            self.actualize(1)
