from tkinter import * 
window = Tk()
window.geometry("300x200")
window.title("Tkinter Label")
window['bg'] = '#328492'
uname = Label(window,text = "Hello " ,fg="black").place(x=30, y=40)
window.mainloop()