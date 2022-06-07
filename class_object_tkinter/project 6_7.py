from tkinter import *
root = Tk()
root.title("Multiple Selection")
list = Listbox(root, selectmode= "multiple")
list.pack(expand=YES , fill="both")
x = ["PHP","C","C++","Python","Java"]
for eachItem in range(len(x)):
    list.insert(END, x[eachItem])
    list.itemconfig(eachItem, bg ="yellow"
    if eachItem % 2 ==0
    else "cyan")
root.mainloop()