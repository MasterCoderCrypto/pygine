import tkinter as tk


def init(widht, height, div):
    globals()["widht"] = widht
    globals()["height"] = height
    globals()["div"] = div


class Intro(tk.Frame):

    def __init__(self, master, path_to_background, path_to_character):
        self.master = master
        self.path_to_background = path_to_background
        self.path_to_character = path_to_character








