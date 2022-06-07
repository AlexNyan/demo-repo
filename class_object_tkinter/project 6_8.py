from tkinter import *
root = Tk()
root.title("Multiple Selection")
yscrollbar = Scrollbar(root)
yscrollbar.pack(side=RIGHT, fill=Y)
label = Label(root, font= ("Times New Roman",10), padx=10, pady=10)
label.pack()
list = Listbox(root, selectmode= "multiple", yscrollcommand=yscrollbar.set)
list.pack(expand=YES , fill="both", padx=10, pady=10)
x = ["PHP","C","C++","Python","Java", "R", "Rust", "C#", "SQL", "Perl", "HTML/CSS", "wordpress", "Swift"]
for eachItem in range(len(x)):
    list.insert(END, x[eachItem])
    list.itemconfig(eachItem, bg ="yellow"
    if eachItem % 2 ==0
    else "cyan")
yscrollbar.config(command= list.yview)
root.mainloop()