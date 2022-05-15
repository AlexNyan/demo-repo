from tkinter import *
w = Tk() 
w.geometry("500x500")
var = StringVar()
label = Message(w, textvariable = var, relief= RAISED)

var.set("Hello! Welcome Python Developer")
label.pack()
w.mainloop()

