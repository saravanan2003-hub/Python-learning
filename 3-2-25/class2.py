class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def getGrade(self):
       return self.grade


s1 = Student("saravanan", 21, 100)
s2 = Student("bala", 18, 100)
s3 = Student("senthil", 17, 30)

print(s1.getGrade())

class Courses():
    def __init__(self,name,maxStudent):
        self.name = name
        self.maxStudent = maxStudent
        self.students = []

    def addStu(self,a):
        self.students.append(a)

    def getAverage(self):
        value = 0
        for student in self.students:
            value += student.getGrade()
        
        print(value/len(self.students))
        
        
c1 = Courses("english", 3)

c1.addStu(s1)
c1.addStu(s2)
c1.addStu(s3)

c1.getAverage()












