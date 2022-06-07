from tkinter import * 
from tkinter import messagebox
root = Tk()
root.title("Listbox Widget")
root['bg'] = "#482392"
Lb1 = Listbox()
Lb1.insert(1, "Python")
Lb1.insert(2, "Java")
Lb1.insert(3, "C")
Lb1.insert(4, "C++")
Lb1.insert(5, "Ruby")
Lb1.insert(6, "JavaScript")
Lb1.pack()
root.mainloop()