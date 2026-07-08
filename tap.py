# A base class Device has a method operate(). You have a Light and a Thermostat. Task: Override operate() so that Light prints "Glowing" and Thermostat prints "Adjusting Temperature". 
class Device:
    def operate(self):
        pass

class Light(Device):
    def operate(self):
        print("Glowing")

class Thermostat(Device):
    def operate(self):
        print("Adjusting Temperature")

light = Light()
thermostat = Thermostat()
light.operate()
thermostat.operate()

# Create a class hierarchy Person → Student → GraduateStudent. Task: Use super() to initialize attributes across all levels.
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

class GraduateStudent(Student):
    def __init__(self, name, student_id, thesis_title):
        super().__init__(name, student_id)
        self.thesis_title = thesis_title

grad_student = GraduateStudent("Ben Jamin", "12345", "CSAI")
print(grad_student.name)
print(grad_student.student_id)
print(grad_student.thesis_title)

# Create an abstract class Shape with an abstract method calculateArea(). Implement subclasses Circle and Rectangle. 
class Shape:
    def calculateArea(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculateArea(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculateArea(self):
        return self.width * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)
print(circle.calculateArea())
print(rectangle.calculateArea())

# Create a class hierarchy Animal → Mammal → Dog. Task: Use method overriding to implement a speak() method that returns "Woof" for Dog and "Generic Mammal Sound" for Mammal.
class Animal:
    def speak(self):
        return "Generic Animal Sound"
    
class Mammal(Animal):
    def speak(self):
        return "Generic Mammal Sound"

class Dog(Mammal):
    def speak(self):
        return "Woof"
    
dog = Dog()
mammal = Mammal()
animal = Animal()
print(dog.speak())
print(mammal.speak())
print(animal.speak())

# Create a class hierarchy Vehicle → Car → ElectricCar. Task: Use method overriding to implement a fuelType() method that returns "Electric" for ElectricCar and "Gasoline" for Car.
class Vehicle:
    def fuelType(self):
        return "Generic Vehicle Fuel"
    
class Car(Vehicle):
    def fuelType(self):
        return "Gasoline"
    
class ElectricCar(Car):
    def fuelType(self):
        return "Electric"

electric_car = ElectricCar()
car = Car()
vehicle = Vehicle()
print(electric_car.fuelType())
print(car.fuelType())
print(vehicle.fuelType())