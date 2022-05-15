class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name + ' is' ,self.age, "years old.")
p1 = student("Mg Mg", 15)
p2 = student("Hla Hla", 11)
p3 = student("Mya Mya", 16)
p1.info()
p2.info()
p3.info()