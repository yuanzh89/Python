from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        return "This is a shape."

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def describe(self):
        return f"This is a Rectangle with width {self.width} and height {self.height}"

def main():
    rectangle = Rectangle(150, 250)
    print(rectangle.describe())

if __name__ == '__main__':
    main()