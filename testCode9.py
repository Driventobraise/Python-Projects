

# parent class

class Person:
    name = "Unknown"
    email = "Unknown"

    def Welcome(self):
        msg = "\nWelcome {}".format(self.name)
        return msg

# child class 1

class Student(Person):
    name = "John Doe"
    email = "JDoe@gmail.com"
    GPA = 3.5
    classes = "Math, History, English, Science"

    def Welcome(self):
        msg = "\nWelcome {}, you are currently taking {} and your GPA is {}.".format(self.name,self.classes,self.GPA)
        return msg


# child class 2

class Teacher(Person):
    name = "Mary Willow"
    email = "mWillow@CompuServe.com"
    classes = "History"
    room = "1A"

    def Welcome(self):
        msg = "\nWelcome {}, Today you are teaching {} in Room {}".format(self.name,self.classes,self.room)
        return msg
    






if __name__ == "__main__":
    student = Student()
    print(student.Welcome())

    teach = Teacher()
    print(teach.Welcome())
