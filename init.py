class Dog:
    name="Buddy"
    breed="Golden Retriever"
    sound=""
    eats=""
    
    def __init__(self,name,breed,sound,eats):
        self.name = name
        self.breed = breed
        self.sound = sound
        self.eats = eats
    def noise(self,sound):
        self.sound = sound
    def eats(self,food):
        self.eats = food
        print(f"{self.name} eats {self.eats} and says {self.sound}")
        
dog1=Dog("Max", "Golden Retriever", "Woof!", "Bone")
dog2=Dog("Bella", " Labrador", "Bark!", "Dog Food")

#1.Create a Book class with an __init__ that takes title, author, and pages. Create two books and print their details.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
print(f"Book 1: {book1.title} by {book1.author}, {book1.pages} pages")
print(f"Book 2: {book2.title} by {book2.author}, {book2.pages} pages")

#2.Create a Car class where color defaults to "White". Create one car with a custom color and one without.
class Car:
    def __init__(self, color="White"):
        self.color = color
car1 = Car("Red")
car2 = Car()
print(f"Car 1: {car1.color}")
print(f"Car 2: {car2.color}")

#3.Create a Rectangle class with width and height in __init__, and an area() method that returns the area.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 4)
print(f"Area of Rectangle 1: {rect1.area()}")
print(f"Area of Rectangle 2: {rect2.area()}")

#1. Create a Restaurant class with attributes (name, cuisine, rating) and methods (serve_food, get_review). Create two restaurant objects.
class Restaurant:
    def __init__(self, name, cuisine, rating):
        self.name = name
        self.cuisine = cuisine
        self.rating = rating
    def serve_food(self):
        print(f"{self.name} serves delicious {self.cuisine} food!")
    def get_review(self):
        print(f"{self.name} has a rating of {self.rating}/5.")
restaurant1 = Restaurant("Pasta Palace", "Italian", 4.5)
restaurant2 = Restaurant("Sushi World", "Japanese", 4.8)
restaurant1.serve_food()
restaurant1.get_review()
restaurant2.serve_food()
restaurant2.get_review()

#2. Create a Pet class with attributes (name, species, energy) and methods (play, sleep, eat). Make the energy go down when playing and up when eating or sleeping.
class Pet:
    def __init__(self, name, species, energy):
        self.name = name
        self.species = species
        self.energy = energy
    def play(self):
        self.energy -= 10
        print(f"{self.name} is playing. Energy: {self.energy}")
    def sleep(self):
        self.energy += 20
        print(f"{self.name} is sleeping. Energy: {self.energy}")
    def eat(self):
        self.energy += 15
        print(f"{self.name} is eating. Energy: {self.energy}")
pet1 = Pet("Charlie", "Dog", 50)
pet1.play()
pet1.eat()
pet1.sleep()

#3. Pick any real-world object not covered in this lesson. Define a class for it with at least 3 attributes and 2 methods. Create two objects and demonstrate them working.
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life
    def make_call(self):
        print(f"{self.brand} {self.model} is making a call.")
    def charge(self):
        self.battery_life += 20
        print(f"{self.brand} {self.model} is charging. Battery life: {self.battery_life}%")
phone1 = Smartphone("Apple", "iPhone 13", 80)
phone2 = Smartphone("Samsung", "Galaxy S21", 70)
phone1.make_call()
phone1.charge()
phone2.make_call()
phone2.charge()