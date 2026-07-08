class Shape:
    def area(self):
        return 0
    def describe(self):
        return f"This is a shape with area {self.area()}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

def showArea(shape):
    print(f"The area of the shape is: {shape.area()}")

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    showArea(shape)
    print(shape.describe())