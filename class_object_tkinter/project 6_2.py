from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x500")
root.title("Checkbox")
def strOutput():
    str = ""
    if chk1.get() == 1:
        str = str + "Apple "
    if chk2.get() == 1:
        str = str + "Orange "
    if chk3.get() == 1:
        str = str + "Banana "
    messagebox.showinfo("Result", str + "Selected")
chk1 = IntVar()
chk2 = IntVar()
chk3 = IntVar()
Label(root, text="Choose your favorite food.").pack()
Checkbutton(root,text="Apple ",variable = chk1,width="15", onvalue=1, offvalue=0, ).place(x= 10, y =30)
Checkbutton(root,text="Orange ",variable = chk2,width="15", onvalue=1, offvalue=0,).place(x= 10, y =60)
Checkbutton(root,text="Banana ",variable = chk3,width="15", onvalue=1, offvalue=0,).place(x= 10, y =90)
Button(root, text="Click", command=strOutput).place(x=10, y=120)
root.mainloop()    