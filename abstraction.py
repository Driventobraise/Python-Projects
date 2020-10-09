#ABSTRACTION ASSIGNMENT
#Create a class that utilizes the concept of abstraction.
#1. Your class should contain at least one abstract method and one regular method.
#2. Create a child class that defines the implementation of its parents abstract method.
#3. Create an object that utilizes both the parent and child methods.

from abc import ABC, abstractmethod

class Shape(ABC):    # Parent class with one regular method and one abstract method
    def print(self):
        print("Normal method inside the abstract class")

    def calculate_area(self):
        pass


class Rectangle(Shape):    #child class
    lenght = 7
    width = 4
    def calculate_area(self):
        return self.lenght * self.width

if __name__ == "__main__":
    rec = Rectangle()  #object created for the class Rectangle
    rec.print()
    print("Area of rectangle is:", rec.calculate_area())
