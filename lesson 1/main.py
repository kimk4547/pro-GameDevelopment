# oops: object oriented programming structure
# class - blueprint of an opject
class Student():
    #properties
    def __init__(self, name, age, grade, favColor, sport,):
        self.name = name
        self.age = age
        self.grade = grade
        self.favColor = favColor
        self.sport = sport
        self.intro = " "

    #functions
    def showDetails(self):
        print("The details of the student are : ")
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Grade : ", self.grade)
        print("Favorite Color: ", self.favColor)
        print("Sport : ", self.sport)
        print()

    def introStudent(self):
        self.intro = input("Pls intro yourself : ")
        print(self.intro)

    #objects - instance of the class
    
s1 = Student("Keimaya", 12, 7, "blue", "volleyball")
s2 = Student("Sindhuja", 14, 9, "pink", "cricket")

s1.showDetails()
s1.introStudent()

s2.showDetails()
s2.introStudent()