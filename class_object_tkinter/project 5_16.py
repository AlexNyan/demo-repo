from tkinter import*
class MyWindow:
    def __init__(self,win):
        self.lb1 = Label(win, text ="First Number: ").place(x=80, y=50)
        self.lb2 = Label(win, text ="Second Number: ").place(x=80, y=100)
        self.lb3 = Label(win, text ="Result: ").place(x=80, y=200)
        self.ent1 = Entry()
        self.ent2 = Entry()
        self.ent3 = Entry()
        self.btn1 = Button(win, text= "Add")
        self.btn2 = Button(win, text= "Subtract")
        self.b1 = Button(win, text= "Add", command=self.add).place(x=100,y=150)
        self.b2 = Button(win, text= "Subtract", command=self.sub).place(x=200,y=150)
        self.ent1.place(x=200, y = 50)
        self.ent2.place(x=200, y = 100)
        self.ent3.place(x=200, y = 200)
        self.btn2.place(x=200, y = 150)
    def add(self):
        self.ent3.delete(0, 'end')
        num1 = int(self.ent1.get())
        num2 = int(self.ent2.get())
        result = num1+num2
        self.ent3.insert(END, str(result))
    def sub(self):
        self.ent3.delete(0, 'end')
        num1 = int(self.ent1.get())
        num2 = int(self.ent2.get())
        result = num1-num2
        self.ent3.insert(END, str(result))
window = Tk()
mywin = MyWindow(window)
window.title("Tktiner Python")
window.geometry('500x500')
window.mainloop()