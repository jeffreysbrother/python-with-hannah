from Tkinter import *

#create the window
root = Tk()

#modify root window
root.title("Format dat Shiz")
root.geometry("400x200")

app = Frame(root)
app.grid()
app.button_clicks = 0

# create a button, method 1
button1 = Button(app, text = "Nonsense")
button1.grid()

# create a button, method 2
button2 = Button(app)
button2.grid()
button2.configure(text = "pump it up")

def update_count(self):
    button3_clicks += 1
    button3.button["text"] = "Total Clicks: " + str(button3_clicks)

    # create a button, method 3

button3["command"] = update_count(self)
button3 = Button()
button3["text"] = "Total Clicks: 0"
button3.grid()



#kick off the event loop
root.mainloop()
