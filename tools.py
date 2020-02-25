
'''
In dieses File gehören alle Klassen oder Funktionen, die sich nicht direkt einem
Nutzen zuordnen lassen, aber trotzdem unerlässlich sind.
'''
import tkinter

class Loadbar:
    '''
    Ein Ladebalken
    '''
    class ValError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return str(self.value) + ' ist kein gültiger Wert im Bereich 0-100'

    def __init__(self, master, x, y, color='#80FF00', width=200, height=100, text='',
                 outline='#000000', fontcolor='black', font=('Arial', 30),
                 animation=False, animation_color=None):
        #Master Zuweisen, der Master ist ein Canvas
        self.master = master
        #Farbe zuweisen
        self.color = color
        #Weite und Höhe
        self.width, self.height = width, height
        #Fortschritt in Prozent
        self.__loaded = 0
        #eigener Text
        self.text = text
        #Koordinaten
        self.x = x
        self.y = y
        #thickness
        self.thickness = 1
        #Outline festlegen
        self.outline = outline
        #Farbe der Schrift
        self.fontcolor = fontcolor
        #Font
        self.font = font
        #Animation: Ja oder Nein?
        self.animation = animation
        #Für die Lade-animation
        self.__xl, self.__xr = self.x, self.x
        #Breite der Animation
        self.__an_width = self.width//10
        self.__an_speed = 0.9
        #Lowerer
        self.lower = 100
        #Animationsfarbe
        self.an_color = animation_color

    def config(self, *, color=None, width=None, height=None, text=None, x=None, y=None,
               outline=None, fontcolor=None, font=None, animation=None,
               lower=None, animation_color=None, animation_width=None):
        '''
        Konfiguriert den Ladebalken im Nachhinein
        '''
        if color is not None:
            self.color = color
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if text is not None:
            self.text = text
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if outline is not None:
            self.outline = outline
        if fontcolor is not None:
            self.fontcolor = fontcolor
        if font is not None:
            self.font = font
        if animation is not None:
            self.animation = animation
        if lower is not None:
            self.lower = lower
        if animation_color is not None:
            self.an_color = animation_color
        if animation_width is not None:
            self.__an_width = animation_width

    def draw(self):
        '''
        Malt den Ladebalken in das als Master übergebene Canvas.
        '''
        self.delete()
        if not self.text:
            #Aussenkasten
            self.rect = self.master.create_rectangle(self.x, self.y,
            self.x+self.width, self.y+self.height, outline=self.outline, width=self.thickness)
            #Eigentlicher Ladebalken
            self.balken = self.master.create_rectangle(self.x+self.thickness, self.y+self.thickness,
            self.x+self.width//100*self.__loaded, self.y+self.height-self.thickness,
            fill=self.color)
            #Erstellt die Lade-Animation
            if self.animation:
                #Anfang:
                if self.__xl == self.x and self.__xr - self.__xl < self.__an_width and self.__xr < self.x+self.width//100*self.__loaded:
                    self.__xr += self.__an_speed
                #Das Ende
                elif self.__xl != self.x and self.__xr >= self.x+self.width//100*self.__loaded and self.__xl <= self.x+self.width//100*self.__loaded:
                    self.__xl += self.__an_speed
                elif self.__xr - self.__xl >= self.__an_width:
                    self.__xr += self.__an_speed
                    self.__xl += self.__an_speed
                else:
                    self.__xr = self.x
                    self.__xl = self.x
                zahl = self.__lower_hexa(self.color, self.lower)
                try:
                    self.anime = self.master.create_rectangle(round(self.__xl+self.thickness), self.y+self.thickness*2,
                    round(self.__xr), self.y+self.height-self.thickness*2, fill=(zahl if not self.an_color else self.an_color),
                     outline=(zahl if not self.an_color else self.an_color))
                except:
                    pass
        else:
            #Text erstellen
            #Prüfen ob das Escape-Zeichen für den Ladefortschritt gesetzt wurde
            ergebnis = self.text
            if '%l' in ergebnis:
                ergebnis = ergebnis.replace('%l', str(round(self.__loaded)))
            #Label erstellen
            label = tkinter.Label(self.master, text=ergebnis, fg=self.fontcolor, font=self.font)
            self.master.create_window(self.x, self.y, window=label, anchor='nw')
            #Loadbar erstellen
            self.master.create_rectangle(self.x, self.y+self.font[1]+20, self.x+self.width,
            self.y+self.height, outline=self.outline)
            self.master.create_rectangle(self.x+self.thickness, self.y+self.font[1]+self.thickness+20,
            self.x+self.width//100*self.__loaded, self.y+self.height-self.thickness, fill=self.color)
            #Die Animation erstellen
            if self.animation:
                #Anfang:
                if self.__xl == self.x and self.__xr - self.__xl < self.__an_width and self.__xr < self.x+self.width//100*self.__loaded:
                    self.__xr += self.__an_speed
                #Das Ende
                elif self.__xl != self.x and self.__xr >= self.x+self.width//100*self.__loaded and self.__xl <= self.x+self.width//100*self.__loaded:
                    self.__xl += self.__an_speed
                elif self.__xr - self.__xl >= self.__an_width:
                    self.__xr += self.__an_speed
                    self.__xl += self.__an_speed
                else:
                    self.__xr = self.x
                    self.__xl = self.x
                zahl = self.__lower_hexa(self.color, self.lower)
                try:
                    self.anime = self.master.create_rectangle(round(self.__xl+self.thickness), self.y+self.thickness*2+self.font[1]+20,
                    round(self.__xr), self.y+self.height-self.thickness*2, fill=(zahl if not self.an_color else self.an_color),
                    outline=(zahl if not self.an_color else self.an_color))
                except:
                    pass


    def stop_animation(self):
        '''
        Stoppt die Animation.
        '''
        if self.animation:
            self.animation = not self.animation

    def animate(self):
        '''
        Startet die Animation
        '''
        if not self.animation:
            self.animation = not self.animation


    def set(self, val):
        '''
        Setzt den Ladebalken auf den Wert val
        '''
        if val < 0 or val > 100:
            raise Loadbar.ValError(val)
        else:
            self.__loaded = val

    def delete(self):
        '''
        Zerstört den Ladebalken
        '''
        try:
            self.master.delete(self.rect)
            self.master.delete(self.balken)
            self.master.delete(self.anime)
        except Exception:
            pass

    def get_loaded(self):
        '''
        Loaded holen
        '''
        return self.__loaded

    def set_loaded(self, val):
        '''
        Loaded setzen
        '''
        if val > 100 or val < 0:
            raise Loadbar.ValError(val)
        else:
            self.__loaded = val

    def del_loaded(self):
        '''Loaded soll nicht gelöscht werden'''
        pass

    def __lower_hexa(self, val, m):
        '''
        Erniedrigt einen Hexa-String um m
        '''
        zahl = int(val[1:], 16)
        zahl -= m
        #In zahl ist jetzt der Wert, der in hexa umgewandelt werden soll
        ergebnis = '#'
        grad = 0
        while zahl > 0:
            while zahl > 16**grad:
                grad += 1
            grad -= 1
            u = zahl//16**grad
            ergebnis += self.to_s(u)
            zahl %= 16**grad
        return ergebnis

    def to_s(self, g):
        if g < 10:
            return str(g)
        elif g == 10:
            return 'A'
        elif g == 11:
            return 'B'
        elif g == 12:
            return 'C'
        elif g == 13:
            return 'D'
        elif g == 14:
            return 'E'
        elif g == 15:
            return 'F'



    loaded = property(get_loaded, set_loaded, del_loaded)
