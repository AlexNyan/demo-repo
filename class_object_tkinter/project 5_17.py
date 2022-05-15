from tkinter import *
from functools import partial

from pyparsing import col
def validatePassword():
    print("Username entered is ", username.get())
    print("Passwordentered is ", password.get())
    return
window = Tk()
window.geometry("500x500")
window.title("Username and Password")

#Take Username and Password from User
usernameLabel = Label(window, text = "Username: ").grid(row=0,column=0)
passwordLabel = Label(window, text = "Password: ").grid(row=1,column=0)
username = StringVar()
password = StringVar()
usernameEntry = Entry(window, textvariable = username).grid(row=0, column=1)
passwordEntry = Entry(window, textvariable = password, show="*").grid(row=1, column=1)

#loginButton
loginButton = Button(window, text= "Login", command=validatePassword).grid(row = 4, column= 0)
window.mainloop()