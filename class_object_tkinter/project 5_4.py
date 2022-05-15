from tkinter import *
window = Tk()
window.geometry("500x400")
window.title("Tkinter Button")
window['bg'] = "#792"
btn = Button(window, text = "Click Me!").place(x = 50, y = 50)
window.mainloop()
