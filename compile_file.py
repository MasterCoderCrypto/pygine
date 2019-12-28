'''
Der Compiler besitzt die Methoden renewal, compile, und run.

renewal legt den eigenen Code zum Compilieren fest

compile kompiliert den Code, und soll ihn abspeicherbar in self.current_code innehalten

run führt den Code im Fenster in einer durch Tastenkombination abbruchbaren Endlosschleife aus.
'''

import re
import tkinter

class Compiler:
    
    def __init__(self):
        self.code = None
        self.canvas = None
    
    def renewal(self, code, canvas):
        self.code = code
        self.canvas = canvas
    
    def compile(self):
        pass
    
    def run(self):
        pass
    
