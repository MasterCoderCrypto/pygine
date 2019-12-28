'''
In diesem File befindet sich der Compiler für die Sprache in der Engine.
Das einzige was diese Klasse als Parameter benötigt ist der Code, 
und anschliessend ein Canvas-Widget, in dem das ganze Spiel dann läuft.
'''

import re
import tkinter

class Compiler:
    def __init__(self, code, canvas):
        self.code = code
        self.canvas = canvas
