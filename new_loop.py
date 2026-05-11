# Multiplication table for any number using for loop
num = int(input("Enter a number: "))
print(f"Multiplication table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Loop through a list of 5 names and print each with position using enumerate
names = ["Aashu","Atharva","Shivanz","Sandesh","Hillsun"]
print("\nNames with their positions:")
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")

# Calculate sum of alleven numbers from 1 to 50 using range
sum_even = 0
for i in range(1, 51):
    if i % 2 == 0:
        sum_even += i
print(f"\nSum of all even numbers from 1 to 50: {sum_even}")

# Countdown from 10 to 1 using while loop and print "Liftoff!" at the end
print("\nCountdown:")
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Liftoff!")

# Keep asking user for password until they enter "Secret123"
while True:
    password = input("Enter password: ")
    if password == "Secret123":
        print("Access granted!")
        break
    else:
        print("Incorrect password. Try again.")

# Create a simple number gussing game
import random
number_to_guess = random.randint(1, 100)
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break

# Write a function is_even that takes a number as input and returns True if it's even and False if it's odd
def is_even(num):
    return num % 2 == 0

number = int(input("Enter a number to check if it's even: "))
if is_even(number):
    print("True")
else:
    print("False")

# Function calculate_area(length, width) that calculates and returns the area of 3 rectangles
def calcualte_area(length, width):
    return length * width

for i in range(3):
    length = float(input(f"Enter length of rectangle {i+1}: "))
    width = float(input(f"Enter width of rectangle {i+1}: "))
    area = calcualte_area(length, width)
    print(f"Area of rectangle {i+1}: {area}")

# Function create_reciept(item, price, quantity) and return formatted string with the total
def create_receipt(item, price, quantity):
    total = price * quantity
    return f"Item: {item}, Price: ${price:.2f}, Quantity: {quantity}, Total: ${total:.2f}"

item = input("Enter item name: ")
price = float(input("Enter item price: "))
quantity = int(input("Enter item quantity: "))
receipt = create_receipt(item, price, quantity)
print("\nReceipt:")
print(receipt)

