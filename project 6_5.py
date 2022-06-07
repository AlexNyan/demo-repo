from tkinter import messagebox
from tkinter import *
root = Tk()
root.geometry('500x500')
def showOutput():
    if rdb.get() == 1:
        messagebox.showinfo("Result", "You Selected Male. ")
    if rdb.get() == 2:
        messagebox.showinfo("Result", "You Selected Female. ")
    if rdb.get() == 3:
        messagebox.showinfo("Result", "You Selected Others. ")
rdb = IntVar()
Label(root, text = "Select Gender.").pack()
Radiobutton(root,text = "Male", variable = rdb, value = 1, command = showOutput).place(x = 50, y =20)
Radiobutton(root,text = "Female", variable = rdb, value = 2, command = showOutput).place(x = 50, y =40)
Radiobutton(root,text = "Others", variable = rdb, value = 3, command = showOutput).place(x = 50, y =60)
root.mainloop()

