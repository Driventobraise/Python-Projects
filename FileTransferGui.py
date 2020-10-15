import tkinter
from tkinter import *
from tkinter import filedialog
import os
import shutil
import time

class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)


        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(600, 300))
        self.master.title('Transfer files')
        self.master.config(bg='lightgrey')

        self.varBrowse = StringVar()
        self.varBrowse2 = StringVar()

        self.lblFName = Label(self.master,text = 'Chose file to transfer from:',font=("Helvetica", 16), fg='black', bg='lightgrey')
        self.lblFName.grid(row=0, column=0,padx=(15,0), pady=(15,0))

        self.btnBrowse = Button(self.master, text='Browse...', width=15, height=1, command=self.askdirectory )
        self.btnBrowse.grid(row=2, column=0,padx=(15,0), pady=(15,0))

        self.txtBrowse = Entry(self.master, text=self.varBrowse, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtBrowse.grid(row= 2, column=1, columnspan=6, padx=(15,0), pady=(15,0))

        self.lblFName = Label(self.master,text = 'Chose file to transfer to:',font=("Helvetica", 16), fg='black', bg='lightgrey')
        self.lblFName.grid(row=3, column=0,padx=(15,0), pady=(15,0))


        self.btnBrowse2 = Button(self.master, text='Browse...', width=15, height=1, command=self.askdirectory2 )
        self.btnBrowse2.grid(row=4, column=0,padx=(15,0), pady=(15,0))

        self.txtBrowse2 = Entry(self.master, text=self.varBrowse2, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtBrowse2.grid(row= 4, column=1, columnspan=6, padx=(15,0), pady=(15,0))

        self.btnTransfer = Button(self.master, text='Transfer files', width=15, height=2, command=self.fileTransfer)
        self.btnTransfer.grid(row=5, column=0,padx=(15,0), pady=(15,0))

        self.btnClose = Button(self.master, text='Close Program', width=15, height=2, command=self.Close)
        self.btnClose.grid(row=5, column=4,padx=(15,0), pady=(15,0))

        
    def Close(self):
        self.master.destroy()


    def askdirectory(self):                 #sets source files are to be transfered from
        dirname = filedialog.askdirectory()
        self.varBrowse.set(dirname)

    def askdirectory2(self):             #sets source files are to be transfered to   
        dirname = filedialog.askdirectory()
        self.varBrowse2.set(dirname)

    def fileTransfer(self):                 # function to transfer files
        src = self.txtBrowse.get()
        dst = self.txtBrowse2.get()
        seconds_in_day = 24*60*60

        now = time.time()
        before = now - seconds_in_day  

        files = os.listdir(src)

        def last_mod_time(fName):
            return os.path.getmtime(fName)


        for fName in files:
            src_fName = os.path.join(src, fName)
            if last_mod_time(src_fName) > before:
                dst_fName = os.path.join(dst, fName)
                shutil.move(src_fName, dst_fName)





if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
