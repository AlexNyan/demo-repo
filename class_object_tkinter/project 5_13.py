from tkinter import messagebox
from tkinter import *
window = Tk()
window.geometry("500x500")
window['bg'] = 'red'
window.title("Call function using button click")
def test():
    messagebox.showinfo("Hello", "Thanks and Fuck You")
Button(window,text ="Click Me!", bg='orange', command = test).pack()
window.mainloop()
