Das ist die Aufgabenverteilung für diese Woche. Ich würde sagen die Frist ist nächste Woche Montag, den 24.2.20.

Ziel diese Woche: --Alle Komponenten für den Ladebildschirm beim Starten des Programms perfekt fertigstellen

Jacob & Thassilo: Hintergrunddesign
                
                  Sprecht euch zusammen ab, ich würde vorschlagen einer von euch erstellt den Hintergrund, während der andere
                  einen Charakter erstellt.
                  
                  Hintergrund: Der Hintergrund muss das Format(800x800) Pixel besitzen, da der Ladebildschirm
                               erstmal so startet und erst anschließend auf Bildschirmgröße vergrößert wird. Das Bild
                               muss ästhetisch wirken und detailreich sein. Es müssen klare Jump-and-run Strukturen
                               wie z.B Hindernisse, verschiedene Ebenen usw. erkennbar sein. Es dürfen allerdings keine
                               Gegner-Charaktere eingezeichnet werden, da die Animation programmtechnisch erfolgt.
                               Es reicht ein einzelnes Bild, kein Gif.
                  
                  Charakter: Der Charakter muss eine Lauf-sowie Sprunganimation besitzen, die gut und flüssig aussehen soll.
                             Dabei sollen diese keine Gifs sein, sondern einzelne Bilder. Ich empfehle den Sprite im Format
                             (64x64).
                             
                             Ratsam ist: 1xCharakter in stehender Pose, Blick nach rechts
                                         10xBilder zur Sprung-Animation
                                         5xBilder zur Lauf-Animation
                                         ___________________________
                                         Total: 16 Bilder
                                         
                             Die Gestaltung des Aussehens des 
                             Charakters ist dem Gestalter frei überlassen.
                  
                   Der Charakter soll in die Atmosphäre des Hintergrundbilds hineinpassen, also sprecht euch ab.
                   (z.B. Fischmensch in Wasserwelt, Feuergeist in Lavawelt usw.)
                   Die Lauf-und Sprunganimation reicht erstmal, einzelne Bilder werden benötigt da die 
                   Implementierung der Animation programmtechnisch erfolgt. Das Hintergrundbild soll in den Ordner
                   Bilder\Intro als Hintergrund.png gespeichert werden, Der Charakter in den Ordner Bilder\Intro\Charakter,
                   dabei wird das Bild des stehenden Charakters als stehend.png abgespeichert, die Lauf-Animation
                   in den Unterordner Bilder\Intro\Charakter\Laufend mit durchnummerierung z.B laufend_1.png, laufend_2.png.
                   und zuletzt die Sprung-Animation in den Ordner Bilder\Intro\Charakter\Springend, ebenfalls
                   durchnummeriert. Das wärs dann auch schon für diese Woche.
                  
Marvin: Modulare Erstellung der Darstellungsebene
        
                   Du erstellst ein Modul-Skript namens intro_frames.py, das enthalten soll:
                   
                   -eine Funktion im Modul namens init, die die Parameter width, height, moved(für Bildverschiebung) und div
                    (für das Ordner-Trennzeichen des jeweiligen Betriebsystems(Linux: '/', Windows: '\'))
                    erwartet, und sie in den globalen Namensraum durch den Aufruf globals()['Name'] = Wert überträgt.
                    Die Übergebenen Parameter sind nun an jeder Stelle des Moduls aufrufbar.
                   
                   WICHIG: Nutze diese Parameter in den Klassen weitestgehend wie möglich, damit keine Inkompatibilität
                           später festgestellt wird.
                           
                           -width: Weite des gesamten Bildschirms
                           -height: Höhe des gesamten Bildschirms
                           -moved: Etwas Komplexer:
                                   
                                   Unter Linux und MacOs wir der Anfangspunkt x=0, y=0 eines Bildes nicht oben links festgelegt,
                                   sondern in der Mitte des Bildes. Deshalb musst du beim Einfügen eines Bildes prüfen, ob
                                   moved=True ist. Ist das so, wird es einfach um width//2 und height//2 auf x bzw.y-Position
                                   verschoben.
                                   
                           -div: Trennzeichen zwischen Ordnern als String.(Brauchst du erstmal nicht nutzen, da der Pfad zum Bild
                                 als Schnittstelle in deine Klasse übergeben wird.(Von dem main.py Skript, das ich schreiben werde.))
                           
                   
                   -eine Klasse namens Intro, die von tkinter.Frame erbt.
                    
                    Parameter für die __init__ Methode: 
                    
                        -master(logisch, die tkinter.Tk Instanz)
                        -path_to_background(Der Pfad zum Hintergrundbild)
                        -path_to_charakter(Der Pfad zum Charakter)
                   
                   Die Klasse muss eine Methode namens redraw besitzen, die sich selbst am Ende durch self.after(10, self.redraw)
                   aufruft. Am Anfang dieser muss durch canvas.delete(*canvas.find_all()) erstmal der Bildschirm gelöscht werden,
                   und dann alles innerhalb der Funktion nachgezeichnet werden, das sorgt für eine flüssige Animation.
                   Gezeichnet werden muss erstmal das Hintergrundbild, sowie eine Transparenzschicht die von links
                   bis rechts eingeblendet wird, gesteuert durch die Variable self.fortschritt(Der Ladefortschritt in Prozent)
                   (1-100). Das alles geschieht in einem canvas. Der Charakter muss vorerst nicht animiert werden, das ist Stoff
                   der nächsten Woche. Gespeichert wird das Modul einfach ganz oben in der Ordnerhirarchie, wie main.py
                   
                   WICHTIG:  Ausführliche! Dokumentation deiner Funktion und deiner Klasse im Ordner Dokumentation.
            
Paul(Ich): Implementieren einer Testumgebung für das Intro und einer Klasse Ladebalken, die mit der Klasse Intro interagiert.
           (Die Interaktion nehme ich ausserhalb Marvins Klasse vor.)
           
           Ich werde die in Marvins Beschreibung genannten Variablen implementieren und durch die Funktion init aus Marvins Modul
           in dieses übergeben. Die Detailbeschreibung spare ich mir, da ich bereits weiß wie ich es implementieren werde.
           Ich werde eine Dokumentation über mein Modul sowie über die Klasse Ladebalken in den Ordner Dokumentation stellen, 
           in dem ihr alles technische Relevante für die Virtuelle Umgebung(das main.py file) nachlesen könnt. 
                    
                   
                             
                  
                  
