# Mulilevel Inheritance
class student:
    def getStudent(self):
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.gender = input("Gender: ")
class test(student):
    def getMarks(self):
        self.stuClass = input("Class: ")
        print("Enter your marks! ")
        self.bio = int(input("Biology: "))
        self.chem = int(input("Chemistry: "))
        self.math = int(input("Mathematics: "))
class marks(test):
    def display(self):
        print("\n \n Name:", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Class: ", self.stuClass)
        print(f"Total Marks: {self.bio+ self.chem + self.math} ")
student_1 = marks()
student_1.getStudent()
student_1.getMarks()
student_1.display()
