#1. Create a Password class that stores a private password. Add a check_password(guess) method that returns True or False, but never reveals the actual password.
class Password:
    def __init__(self,password):
        self.__password = password

    def check_password(self, guess):
        if guess == self.__password:
            return True
        return False
guess = Password("secret123")
print(guess.check_password("secret123"))

#2. Create a Temperature class with a private __celsius attribute. Add a set_temperature() method that only accepts values between -273.15 and 1000.
class Temperature:
    def __init__(self):
        self.__celsius = 0

    def set_temperature(self, temp):
        if -273.15 <= temp <= 1000:
            self.__celsius = temp
        else:
            print("Temperature must be between -273.15 and 1000 degrees Celsius.")
temp = Temperature()
temp.set_temperature(25)

#3. Take the unprotected BankAccount example and add a withdraw() method that prevents the balance from going negative.
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds. Withdrawal denied.")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
account = BankAccount(100)
account.withdraw(150)  # This will print "Insufficient funds. Withdrawal denied."
print(account.get_balance())  # This will print the updated balance.

#1. Create a Person class with a public name, protected _email, and private __password. Try accessing all three from outside the class.
class Person:
    def __init__(self, name, email, password):
        self.name = name
        self._email = email
        self.__password = password
person = Person("Sandesh", "sandeshsapkota095@gmail.com", "secret456")
print(person.name)  # This will print "Sandesh"
print(person._email)  # This will print "sandeshsapkota095@gmail.com"
print(person.__password)  # This will raise an AttributeError

#2. Create a SecretVault class with a private __code. Try accessing it directly, then through name mangling. Observe the difference.
class SecretVault:
    def __init__(self, code):
        self.__code = code

vault = SecretVault("my_secret_code")
print(vault._SecretVault__code)

#3. For the Person class above, add a verify_password(guess) method that returns True/False without exposing the actual password.
class Person:
    def __init__(self, name, email, password):
        self.name = name
        self._email = email
        self.__password = password

    def verify_password(self, guess):
        return guess == self.__password
person = Person("Sandesh", "sandeshsapkota095@gmail.com", "secret456")
print(person.verify_password("secret456"))  # This will print True
print(person.verify_password("wrong_password"))  # This will print False

#1. Create a Temperature class with a @property for celsius that rejects values below -273.15 (absolute zero).
class Temperature:
    def __init__(self):
        self._celsius = 0

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, temp):
        if temp < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")
        self._celsius = temp
temp = Temperature()
temp.celsius = -300  # This will raise a ValueError
print(temp.celsius)  # This will print the current temperature in Celsius.

#2. Create an Employee class with a read-only employee_id property and a settable salary property that only accepts positive values.
class Employee:
    def __init__(self, employee_id, salary):
        self._employee_id = employee_id
        self._salary = salary

    @property
    def employee_id(self):
        return self._employee_id

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary must be a positive value.")
        self._salary = value
employee = Employee("E123", 50000)
print(employee.employee_id)  # This will print "E123"

#3. Create a Rectangle class where width and height have setters (positive values only), and area is a read-only computed property.
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be a positive value.")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be a positive value.")
        self._height = value

    @property
    def area(self):
        return self._width * self._height
rect = Rectangle(5, 10)
print(rect.area)  # This will print 50

#1. Extend the BankAccount class with a transfer(other_account, amount) method that withdraws from one account and deposits into another.
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds. Withdrawal denied.")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def transfer(self, other_account, amount):
        if amount > self.__balance:
            print("Insufficient funds. Transfer denied.")
        else:
            self.withdraw(amount)
            other_account.deposit(amount)
account1 = BankAccount(100)
account2 = BankAccount(50)
account1.transfer(account2, 30)
print(account1.get_balance())  # This will print 70
print(account2.get_balance())  # This will print 80

#2. Create a Library class that has a private list of books. Add methods to add a book, remove a book, and search by title. The book list should never be directly accessible.
class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, title):
        self.__books.append(title)

    def remove_book(self, title):
        if title in self.__books:
            self.__books.remove(title)
        else:
            print("Book not found in the library.")

    def search_by_title(self, title):
        return title in self.__books
library = Library()
library.add_book("The Great Gatsby")
print(library.search_by_title("The Great Gatsby"))  # This will print True
library.remove_book("The Great Gatsby")

#3. Create an Inventory class with private stock counts per item. Add methods to add stock, sell items (with validation that stock does not go below zero), and a read-only property for total items in stock.
class Inventory:
    def __init__(self):
        self.__stock = {}

    def add_stock(self, item, quantity):
        if item in self.__stock:
            self.__stock[item] += quantity
        else:
            self.__stock[item] = quantity

    def sell_item(self, item, quantity):
        if item not in self.__stock or self.__stock[item] < quantity:
            print("Insufficient stock. Sale denied.")
        else:
            self.__stock[item] -= quantity

    @property
    def total_items_in_stock(self):
        return sum(self.__stock.values())
inventory = Inventory()
inventory.add_stock("Widget", 100)
inventory.sell_item("Widget", 30)
print(inventory.total_items_in_stock)  # This will print 70