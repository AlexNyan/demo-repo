from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Checkbox")
Label(root, text="Choose your favorite food.").pack()
Checkbutton(root,text="Apple ",width="15", onvalue=1, offvalue=0, ).place(x= 10, y =30)
Checkbutton(root,text="Orange ",width="15", onvalue=1, offvalue=0,).place(x= 10, y =60)
Checkbutton(root,text="Banana ",width="15", onvalue=1, offvalue=0,).place(x= 10, y =90)
root.mainloop()

