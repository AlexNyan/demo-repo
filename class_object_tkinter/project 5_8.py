from tkinter import *
window = Tk()
window.geometry("500x400")
window.title("Change button background color during mouse click")
btn = Button(window, text = "Submit", bg ="#ffffff", activeforeground='red')
btn.pack()
window.mainloop()
