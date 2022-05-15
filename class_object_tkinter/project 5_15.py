from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry('400x500')
window.title("Add Two Numbers")
n1 = IntVar() #Declaration
n2 = IntVar()
def add(): #Addition of two numbers
    num1 = n1.get()
    num2 = n2.get()
    messagebox.showinfo("Sum:", (num1+num2))
Label(window, text = 'Enter first number: ', width ='15').place(x=50, y=50)
Label(window, text = 'Enter second number: ', width ='15').place(x=50, y=90)
Entry(window, textvariable= n1).place(x = 200, y = 50 )
Entry(window, textvariable= n2).place(x = 200, y = 90 )
Button(window, text= 'Add',command=add).place(x = 150, y = 130)
window.mainloop()
