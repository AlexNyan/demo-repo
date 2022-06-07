from email import message
from tkinter import * 
from tkinter import *
from tkinter import messagebox 
root = Tk()
root.geometry('500x500')
root['bg'] = "#982348"
root.title('This is radio button widget')
rdb = IntVar()
def test():
    if (rdb.get() == 1):
        messagebox.showinfo("Result", "You have selected Male.")
    if (rdb.get() == 2):
        messagebox.showinfo("Result", "You have selected Female.")
    if (rdb.get() == 3):
        messagebox.showinfo("Result", "You have selected Others.")
        
Label(root, text = "Select Gender").pack()
Radiobutton(root, text = "Male", variable =rdb, value = 1, command = test).place(x =50, y=20)
Radiobutton(root, text = "Female", variable =rdb, value = 2, command = test).place(x =50, y=40)
Radiobutton(root, text = "Other", variable =rdb, value = 3, command = test).place(x =50, y=60)
root.mainloop()
