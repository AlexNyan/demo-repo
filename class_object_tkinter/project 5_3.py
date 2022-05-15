from tkinter import * #To use functions from Tk library
window = Tk()
btn = Button(window, text= "Click Me!" ,width = 40, height = 3, bg="#0052cc", fg = "#ffffff", activebackground="#0052cc",activeforeground="#aaffaa")
btn.pack() #To recompile all the functions concerning btn.
window.title("Tkinter Button")
window.geometry("500x300")
window.mainloop()
