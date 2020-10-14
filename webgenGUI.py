
import tkinter
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master                            #stylizes GUI
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(800, 300))
        self.master.title('Web Page Generator')
        self.master.config(bg='lightgrey')

        self.varPageInfo = StringVar()   #Variable to catch user input

        self.lblenterText = Label(self.master,text = 'Enter Text For Web Page:',font=("Helvetica", 16), fg='black', bg='lightgrey')
        self.lblenterText.grid(row=0, column=0,padx=(30,0), pady=(30,0))

        self.txtenterText = Entry(self.master, text=self.varPageInfo, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtenterText.grid(row= 0, column=1,padx=(30,0), pady=(30,0))

        self.btnGenerate = Button(self.master, text='Generate', width=10, height=2, command=self.GeneratePg)
        self.btnGenerate.grid(row=1, column=1,padx=(0,0), pady=(30,0))

        self.btnClose = Button(self.master, text='Close Program', width=10, height=2, command=self.cancel)
        self.btnClose.grid(row=1, column=0,padx=(0,90), pady=(30,0))


    def GeneratePg(self):    #This Function fetches input from the GUI and generates a html page
        Info = self.varPageInfo.get()
        f = open('summersales.html','w')

        message = """<html> 
                 <body> 
                <h1>
          {} 
               </h1>
                </body> 
                    </html>""".format(Info)

        f.write(message)
        f.close()

        webbrowser.open_new('summersales.html')

    def cancel(self):
        self.master.destroy()




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
