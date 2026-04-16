#A program that takes two numbers and performs all 7 basic mathematical operations on them.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
    print(f"{num1} % {num2} = {num1 % num2}")
else:
    print("Cannot divide by zero.")
    print("Cannot calculate modulus by zero.")
print(f"{num1} ** {num2} = {num1 ** num2}")

# Creating a tip calculator that takes the bill amount and tip percentage as input and calculates the total amount to be paid.
bill_amount = float(input("Enter the bill amount: "))
tip_percentage = float(input("Enter the tip percentage: "))
tip_amount = (tip_percentage / 100) * bill_amount
total_amount = bill_amount + tip_amount
print(f"Tip Amount: {tip_amount:.2f}")
print(f"Total Amount to be paid: {total_amount:.2f}")

#Checking foe Even or Odd using modulus
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an Even number.")
else:
    print(f"{number} is an Odd number.")