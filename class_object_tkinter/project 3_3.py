class Employee:
    empCount = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.empCount += 1
    def displayEmployee(self):
        print("Name: ", self.name,"\n" , "Age: ", self.age)
emp1 = Employee("Alex", 17)
emp2 = Employee("Kph", 15)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee: ", Employee.empCount)