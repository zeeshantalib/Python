class Student:
    def __init__(self,fname,lname,cgpa):
        self.fname=fname
        self.lname=lname
        self.cgpa=cgpa
    def reward(self):
        if self.cgpa>3.0:
            print("Congratulations !")
        else:
            print("Please Improve youself")
    def show_student(self):
        print("I am a Student")

class Student_Punjab(Student):
    def show(self):
        print("I am a Pubjabi Student")

s1=Student("Zeeshan","Talib",3.1)
print(s1.fname)
print(s1.lname)
print(s1.cgpa)
s1.reward()

s2=Student_Punjab("Zeeshan","Talib",3.1)
s2.show()
