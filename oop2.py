# 1. Fruit class
class Fruit:
    pass

fruit1 = Fruit()
fruit1.name = "Apple"

fruit2 = Fruit()
fruit2.name = "Banana"

fruit3 = Fruit()
fruit3.name = "Mango"

print("Fruits:")
print(fruit1.name)
print(fruit2.name)
print(fruit3.name)


# 2. Phone class
class Phone:
    pass

phone1 = Phone()
phone1.brand = "iPhone"

phone2 = Phone()
phone2.brand = "Samsung"

print("\nPhone Type Checking:")
print(type(phone1))
print(type(phone2))
print(isinstance(phone1, Phone))
print(isinstance(phone2, Phone))


# 3. Color class
class Color:
    pass

color1 = Color()
color1.name = "Red"

color2 = Color()
color2.name = "Blue"

# Change only one object
color1.name = "Green"

print("\nColors:")
print("color1:", color1.name)
print("color2:", color2.name)



# 1. Book class
class Book:
    pass

book1 = Book()
book1.title = "Atomic Habits"
book1.author = "James Clear"
book1.pages = 320

book2 = Book()
book2.title = "Rich Dad Poor Dad"
book2.author = "Robert Kiyosaki"
book2.pages = 336

print("Books:")
print(f"Title: {book1.title}, Author: {book1.author}, Pages: {book1.pages}")
print(f"Title: {book2.title}, Author: {book2.author}, Pages: {book2.pages}")

#2)Create a Pet class, create an object, set its name and age, then modify the age and print before and after.
class Pet:
    pass
pet1=Pet()
pet1.name='shammy'
pet1.age=3
print(pet1.age)
pet1.age=4
print(pet1.age)


#3)Create a Color class with a name attribute. Create two objects, change one's name, and print both to confirm
class color:
    name="red"
color1=color()
color1.name='blue'
color2=color()
print(color1.name)
print(color2.name)