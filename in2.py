#1
class Animal:
    def sound (self):
        print("makes sound")

class Dog(Animal):
    pass

class Cow(Animal):
    pass

bd=Dog()
bd.sound()  # Output: makes sound
c=Cow()
c.sound()  # Output: makes sound

#2
class Animal:
    def __init__(self, name):
        self.name = name
    def sound (self):
        print(f"{self.name} makes sound")

class Dog(Animal):
    pass

class Cow(Animal):
    pass

bd=Dog("Max")
bd.sound()  # Output: Max makes sound
c=Cow("Laxmi")
c.sound()  # Output: Laxmi makes sound

#3
class Animal:
    def __init__(self, name,breed):
        self.name = name
        self.breed = breed

    def sound (self):
        print(f"{self.name} makes sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, breed)
    def eat(self):
        print(f"{self.name} eats meat")

bd=Dog("Max", "Labrador")
bd.sound()  # Output: Max makes sound
bd.eat()    # Output: Max eats meat 

#4.
class Animal:
    def __init__(self, name,breed):
        self.name = name
        self.breed = breed

    def sound (self):
        print(f"{self.name} makes sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, breed)
    def sound(self):
        print(f"{self.name} Barks")

class Cow(Animal):
    def __init__(self, name, breed):
        super().__init__(name, breed)
    def sound(self):
        print(f"{self.name} Moos")
bd=Dog("Max", "Labrador")
bd.sound()  # Output: Max Barks
c=Cow("Laxmi", "Hereford")
c.sound()  # Output: Laxmi Moos

#5
class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def sound (self):
        print(f"{self.name} makes sound")
    def eat(self):
        print(f"{self.name} eats food")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, breed)
    def sound(self):
        print(f"{self.name} Barks")
    def eat(self):
        print(f"{self.name} eats meat")

class Cow(Animal):
    def __init__(self, name, breed):
        super().__init__(name, breed)
    def sound(self):
        print(f"{self.name} Moos")
    def eat(self):
        print(f"{self.name} eats grass")

bd=Dog("Max", "Labrador")
bd.sound()  # Output: Max Barks
bd.eat()    # Output: Max eats meat
c=Cow("Laxmi", "Hereford")
c.sound()  # Output: Laxmi Moos
c.eat()    # Output: Laxmi eats grass