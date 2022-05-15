from tkinter import*
window = Tk()
window.geometry("500x300")
window.title("Change text of the Tkinter button programmatically")
def changeText():
    button['text'] = "Submitted"
button = Button(window, text = "Submit", command=changeText)
button.pack()
window.mainloop()