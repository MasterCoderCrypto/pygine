import tkinter as tkinter


def init(widht, height, div):
    globals()["widht"] = widht
    globals()["height"] = height
    globals()["div"] = div


class Intro(tkinter.Frame):

    def __init__(self, master, path_to_background, path_to_character):
        super().__init__(master)
        self.master = master
        self.path_to_background = path_to_background
        self.path_to_character = path_to_character








