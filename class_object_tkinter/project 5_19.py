from tkinter import * 
from tkinter import messagebox
w = Tk()
w.geometry("500x500")
w.title("Say Hello")

#Say Hello
def hello():
    messagebox.showinfo("Hello! ", "Hello Python Developer")
btn1 = Button(w, text= "Say Hello!", command=hello)
btn1.pack()
w.mainloop()