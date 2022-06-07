import string
import tkinter as tk
text = ""
def update_text():
    global cbs
    string = ""
    for name,checkbutton in cbs.items():
        if checkbutton.var.get():
            string += checkbutton ["text"] + " selected"
text.delete('1.0', tk.END)
text.insert('1.0',string)

if __name__ == '__main__':
    root = tk.Tk()
    text = tk.Text(root)

root.geometry('500x300')
cb_list = ["pencil", "pen","book", "watch"]
cbs = dict()

for i, value in enumerate(cb_list):
    cbs[value].var+tk.BooleanVar(root,value = False)
    cbs[value]["variable"] = cbs[value].var
    cbs[value].grid(row=i,column=0)

text.grid()
root.mainloop()