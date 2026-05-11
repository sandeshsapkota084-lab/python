#1. Create a Vehicle class with a brand attribute and a honk() method. Then create a Car class that inherits from it and test calling honk() on a Car object.
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def honk(self):
        return "Beep beep!"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

my_car = Car("Toyota", "Camry")
print(my_car.honk())  # Output: Beep beep!

#2. Create a Person class with name and age. Create a Student class that inherits from Person using pass. Verify the student can access name and age.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    pass
student = Student("Alice", 20)
print(student.name)  # Output: Alice
print(student.age)   # Output: 20

#3. 