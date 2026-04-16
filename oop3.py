class Dog:
    name="Buddy"
    breed="Golden Retriever"
    sound=""
    eats=""
    
    def noise(self,sound):
        self.sound = sound
    def eats(self,food):
        self.eats = food
        print(f"{self.name} eats {self.eats} and says {self.sound}")
        
dog1=Dog()
dog1.name="Max"
dog1.noise("Woof!")
dog1.eats("Bone")

dog2=Dog()
dog2.name="Bella"
dog2.noise("Bark!")
dog2.eats("Dog Food")



class BankAccount:
    balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Balance: ${self.balance}")
        else:
            print("Insufficient funds.")

acc = BankAccount()
acc.deposit(500)     # Deposited $500. Balance: $500
acc.withdraw(200)    # Withdrew $200. Balance: $300
acc.withdraw(400)    # Insufficient funds.


# 1.Create a Greeter class with a name attribute and a greet() method that prints "Hello, my name is [name]!".
class Greeter:
    name=""
    
    def greet(self):
        print(f"Hello, my name is {self.name}!")

greeter=Greeter()
greeter.name="Sandesh"
greeter.greet()

# 2.Create a Rectangle class with width and height attributes and an area() method that returns width times height.
class Rectangle:
    width=0
    height=0
    
    def area(self):
        return self.width * self.height

rect1=Rectangle()
rect1.width=5
rect1.height=3
print(f"Area of rectangle: {rect1.area()}")

# 3.Extend the BankAccount example by adding a check_balance() method that simply prints the current balance.
class BankAccount:
    balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Balance: ${self.balance}")
        else:
            print("Insufficient funds.")
    
    def check_balance(self):
        print(f"Current balance: ${self.balance}")

acc = BankAccount()
acc.deposit(1000)     # Deposited $1000. Balance: $1000
acc.check_balance()   # Current balance: $1000
