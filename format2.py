from Tkinter import *

class Application(Frame):
    """ A GUI application """

    def __init__(self, master):
        """ initialize the Frame """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        """ create 3 buttons """
        # create a button, method 1
        self.button1 = Button(app, text = "compute")
        self.button1.grid()

        # create a button, method 2
        self.button2 = Button(app)
        self.button2.grid()
        self.button2.configure(text = "pump it up")

        # create a button, method 3
        self.button3 = Button(app)
        self.button3.grid()
        self.button3["text"] = "add content"
        
root = Tk()
root.title("Buttons and shit")
root.geometry("200x200")

app = Application(root)

root.mainloop()