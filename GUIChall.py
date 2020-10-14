
import tkinter
from tkinter import *
from tkinter import filedialog
import os

class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)


        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(400, 200))
        self.master.title('Check files')
        self.master.config(bg='lightgrey')

        self.varBrowse = StringVar()
        self.varBrowse2 = StringVar()

        self.btnBrowse = Button(self.master, text='Browse...', width=15, height=1, command=self.askdirectory )
        self.btnBrowse.grid(row=2, column=0,padx=(15,0), pady=(15,0))

        self.txtBrowse = Entry(self.master, text=self.varBrowse, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtBrowse.grid(row= 2, column=1, columnspan=6, padx=(15,0), pady=(15,0))

        self.btnBrowse2 = Button(self.master, text='Browse...', width=15, height=1, command=self.askdirectory )
        self.btnBrowse2.grid(row=3, column=0,padx=(15,0), pady=(15,0))

        self.txtBrowse2 = Entry(self.master, text=self.varBrowse2, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtBrowse2.grid(row= 3, column=1, columnspan=6, padx=(15,0), pady=(15,0))

        self.btnCheckfile = Button(self.master, text='Check for files...', width=15, height=2, )
        self.btnCheckfile.grid(row=4, column=0,padx=(15,0), pady=(15,0))

        self.btnClose = Button(self.master, text='Close Program', width=15, height=2, command=self.Close)
        self.btnClose.grid(row=4, column=4,padx=(15,0), pady=(15,0))

        
    def Close(self):
        self.master.destroy()


    def askdirectory(self):
        dirname = filedialog.askdirectory()
        self.varBrowse.set(dirname)
        




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()


