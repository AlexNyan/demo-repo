from tkinter import *
window = Tk()
window.geometry('400x500')
window['bg'] = "black"
label = Label(window, text= 'Enter first number: ').place(x=50, y=50)
entry = Entry(window).place(x = 200, y = 50)
window.mainloop()
