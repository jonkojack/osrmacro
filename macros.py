#!/usr/bin/python2

from Tkinter import *
import os

### My Modules
from modules import RS


cwd = os.getcwd()

class App:
    def __init__(self, master):
        frame = Frame(master, 
                bg='black')
        frame.pack()

        self.dropper_btn = Button(frame, 
                text="DROP",
                fg='red',
                bg='orange',
                command=self.dropper)
        self.dropper_btn.pack()

        self.herbClean_btn = Button(frame, 
                text="Clean Herb",
                fg='white',
                bg='green',
                command=self.herbClean)
        self.herbClean_btn.pack()

        self.fletcher_btn = Button(frame,
                text="Fletch",
                fg='white',
                bg='#133B18',
                command=self.fletch)
        self.fletcher_btn.pack()

        self.plankmake = Button(frame,
                text="Make Plank",
                fg='white',
                bg='#65453F',
                command=self.making)
        self.plankmake.pack()

        self.login_btn = Button(frame, 
                text="LogIn",
                fg='cyan',
                bg='blue',
                command=self.login)
        self.login_btn.pack()

        self.center_btn = Button(frame, 
                text="Center RS",
                fg='black',
                bg='yellow',
                command=self.centering)
        self.center_btn.pack()

        self.rezise_btn = Button(frame,
                text="Resize RS",
                fg="black",
                bg='yellow',
                command=self.resize_rs)
        self.rezise_btn.pack()


    def making(self):
        cwd = os.getcwd()
        os.system(cwd+'/plankmake.py')
    def resize_rs(self):
        os.system('xdotool search --name old windowsize --sync 767 564')

    def centering(self):
        #os.system(cwd+'/setup.py')
        RS.center_window()
    def herbClean(self):
        os.system(cwd+'/herbCleaner.py')
    def dropper(self):
        os.system(cwd+'/findndrop.py')
    def fletch(self):
        os.system(cwd+'/fletcher.py')
    def login(self):
        os.system(cwd+'/login.py')

root = Tk()
root.title('Various Macros')
app = App(root)
root.mainloop()
