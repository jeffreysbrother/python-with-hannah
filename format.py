from Tkinter import *

#create the window
root = Tk()

#modify root window
root.title("Format dat Shiz")
root.geometry("400x200")

app = Frame(root)
app.grid()

button1 = Button(app, text = "compute")
button1.grid()

button2 = Button(app)
button2.grid()
button2.configure(text = "pump it up")

button3 = Button(app)
button3.grid()
button3["text"] = "add content"

#kick off the event loop
root.mainloop()
