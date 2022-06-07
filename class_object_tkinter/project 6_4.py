from tkinter import * 
root = Tk()
root.geometry('500x500')
root['bg'] = "#982348"
root.title('This is radio button widget')
rdb = IntVar()
Label(root, text = "Select Gender").pack()
Radiobutton(root, text = "Male", variable =rdb, value = 1).place(x =50, y=20)
Radiobutton(root, text = "Female", variable =rdb, value = 2).place(x =50, y=40)
Radiobutton(root, text = "Other", variable =rdb, value = 3).place(x =50, y=60)
root.mainloop()
