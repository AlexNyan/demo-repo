class student:
    List = []
    SCount = 0
    def __init__(self, name, age, room, subject):
        self.name = name
        self.age = age
        self.room = room
        self.subject = subject
        student.SCount += 1
    #This function will add things user input to empty list
    def appendtolist(self):
        student.List.append(self.name)
        student.List.append(self.age)
        student.List.append(self.room)
        student.List.append(self.subject)
#Student Number
SNo = int(input("Student Number: "))
for i in range(SNo):
    #Name, Age, Room, Subject
    N = input("Enter your name: ")
    A = int(input("Enter your age: "))
    R = int(input("Enter your room number: "))
    S = input("Enter your subject: ")
    i = student(N, A, R, S)
# s2 = student("Alex",14,"342", "Maths")
# s3 = student("Joe",18,"721", "Economics")
# s4 = student("John",19,"842", "Accounting")
    i.appendtolist()
    if SNo > 1:
        print("Fill Another Student . . .")
print(student.List)

