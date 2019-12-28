import webbrowser
from tkinter import *
from zipfile import ZipFile

grey1= '#333333'
purple1= "#E5CCFF"

def open_browser():
    webbrowser.open(url="https://www.piskelapp.com/p/create")

#-------------TKINTER STUFF-------------
root= Tk()
root.geometry("500x500")
root.configure(bg=grey1)
root.iconbitmap(r"F:\Desktop\Python\pygine\python.ico")
root.title("Sprite Editor")

Frame1= Frame(root,bg=grey1)
Frame1.pack(side=TOP, anchor=W)

a1= Label(Frame1, text="1. Use the Button to open 'piskelapp.com/p/create' in order to draw your sprites", bg="grey").grid(row=0, column=0, sticky=W)
a2= Label(Frame1, text="2. Then, draw your sprites and on the right side of the screen, download them as a .zip file", bg="grey").grid(row=1,column=0, sticky=W)
a3= Label(Frame1, text=r"3. Save the .zip file on your machine under 'pygine\Sprite Editor' ", bg="grey").grid(row=2, sticky=W)
open_browser= Button(Frame1, text="Open Piskel in your Browser" ,command=open_browser, bg=purple1).grid(columnspan=2)
b1= Label(Frame1, text="These are your sprites so far: ", bg="grey").grid(row=4, column=0, sticky=W)

lol= []
for i in range(100):
    with ZipFile(r"New Piskel.zip", "r") as file:
        lol.append(file.printdir())

for i in range(len(lol)):
    filenames = Label(Frame1, text=f"{lol[i]}", bg=purple1).grid()

root.mainloop()