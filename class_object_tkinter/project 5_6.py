from tkinter import *
window = Tk()
window.geometry("500x300")
window.title("Change background color during mouse click")
btn = Button(window,text = "Submit",bg='#000000',activebackground='#00ff00')
btn.pack()
window.mainloop()