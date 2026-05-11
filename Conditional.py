#Q1
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


#Q2
num=int(input('Enter a number: '))
if num>0 and num<101:
    print('Number is between 1 and 100')
else:
    print('Number is not between 1 and 100')


#Q3
number=int(input('Enter a number to check whether it is even or odd:'))
if number%2==0:
    print('number is even')
elif number%2!=0:
    print('number is odd')
else:
    print('error')

#Q4
grade=int(input('What is your marks(Q4):'))
if 89<grade<100:
    print('Your grade is A+')
elif 79<grade<90:
    print('Your grade is A')
elif 69<grade<80:
    print('Your grade is B+')
elif 59<grade<70:
    print('Your grade is B')
elif 49<grade<60:
    print('Your grade is C')
elif 39<grade<50:
    print('Your grade is D')
else:
    print('Your grade is E')

# #Q5
print('Welcome to my calculator')
num1=int(input('Enter num1:'))
num2=int(input('Enter num2:'))
calc=input('What do you want to do, addition, multiplication, subtraction, or division:')
if calc=='addition':
    result=(num1+num2)
    print(f'addition result is {result}')
elif calc=='multiplication':
    result=(num1*num2)
    print(f'your result is {result}')
elif calc=='subtraction':
    result=(num1-num2)
    print(f'your result is {result}')
elif calc=='division':
    result=(num1/num2)
    print(f'Your result is {result}')
else:
    print('invalid')

#Q6
age=int(input('Enter your age:'))
if age<18:
    print('you r eligible to vote')
else:
    print('you are not eligible')

#Q7
usn=(input('Enter your username:'))
username='User123'
password='12345678'
if usn==username:
    print('valid username')
    psw=(input('Enter a password:'))
    if psw==password:
        print('you have logged in')
    else:
        print('wrong password')
else:
    print('invalid username')

#Q8
num=int(input('Enter a number:'))
if num%7==0:
    print('the number is divisible by 7')
else:
    print('Number is not divisible by 7')

#Q9
age=int(input('Enter your age:'))
if age<18:
    print('you are eligible to vote')
else:
    print('you are not eligible to vote')


#different set of questions
#Q1
num1=int(input('Enter first number:'))
num2=int(input('Enter second number:'))
num3=int(input('Enter third number:'))
if num1==num2 and num2==num3:
    print('All numbers are equal')
elif num1==num2 and num1!=num3:
    print('2 numbers are equal')
elif num2==num3 and num2!=num1:
    print('2 numbers are equal')
elif num1==num3 and num1!=num2:
    print('2 numbers are equal')
else:
    print('All numbers are different')

#Q2
p1 = input("Player 1 (rock/paper/scissors): ").lower()
p2 = input("Player 2 (rock/paper/scissors): ").lower()
if p1 == "rock":
    if p2 == "rock":
        print("Tie")
    else:
        if p2 == "paper":
            print("Player 2 wins")
        else:
            print("Player 1 wins")
elif p1 == "paper":
    if p2 == "paper":
        print("Tie")
    else:
        if p2 == "rock":
            print("Player 1 wins")
        else:
            print("Player 2 wins")
elif p1 == "scissors":
    if p2 == "scissors":
        print("Tie")
    else:
        if p2 == "rock":
            print("Player 2 wins")
        else:
            print("Player 1 wins")
            
#Q3
num = int(input("Enter a number: "))
if num % 7 == 0:
    print("Divisible by 7")
else:
    print("Not divisible by 7")

#Q4
current_floor = 5
user_floor = int(input("Enter floor number: "))
if user_floor > current_floor:
    print("Lift should go up")
elif user_floor < current_floor:
    print("Lift should go down")
else:
    print("Lift stays at current floor")

#Q5
num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Not positive")

#Q6
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Greater number is:", a)
elif b > a:
    print("Greater number is:", b)
else:
    print("Both numbers are equal")
    if a > 0:
        print("Number is positive")
    elif a < 0:
        print("Number is negative")
    else:
        print("Number is zero")

#Q7
n = int(input("Enter a number: "))
if n % 3 == 0 and n % 5 == 0:
    print("Fizz Buzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)

#Q8
import random
num = random.randint(0, 5)
if num == 0:
    print("Flamingos turn pink from eating shrimp.")
elif num == 1:
    print("The only food that doesn't spoil is honey.")
elif num == 2:
    print("Shrimp can only swim backwards.")
elif num == 3:
    print("A taste bud's life span is about 10 days.")
elif num == 4:
    print("It is impossible to sneeze while sleeping.")
else:
    print("It is illegal to sing off-key in North Carolina.")

#Q9
total_amount = float(input("Enter total purchase amount: "))
is_member = input("Are you a member? (True/False): ")
is_member = True if is_member == "True" else False
if total_amount > 1000 and is_member:
    discount = 0.20
elif total_amount > 1000 and not is_member:
    discount = 0.10
else:
    discount = 0
final_amount = total_amount - (total_amount * discount)
print("Final Amount:", final_amount)

#Q10
weight = float(input("Enter your Earth weight: "))
planet = int(input("Enter planet number (1-7): "))
if planet == 1:
    gravity = 0.38
elif planet == 2:
    gravity = 0.91
elif planet == 3:
    gravity = 0.38
elif planet == 4:
    gravity = 2.53
elif planet == 5:
    gravity = 1.07
elif planet == 6:
    gravity = 0.89
elif planet == 7:
    gravity = 1.14
else:
    print("Invalid planet number")
    exit()
print("Your weight on that planet is:", weight * gravity)

#Q11
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
total = m1 + m2 + m3 + m4
percentage = (total / 400) * 100
print("Total:", total)
print("Percentage:", percentage)
if percentage > 70:
    print("Grade: Distinction")
elif percentage > 60:
    print("Grade: First")
elif percentage > 40:
    print("Grade: Pass")
else:
    print("Grade: Fail")

#Q12
price = float(input("Enter cost price of bike: "))
if price > 100000:
    tax = 0.15
elif price > 50000:
    tax = 0.10
else:
    tax = 0.05
print("Road Tax:", price * tax)

#Q13
years = int(input("Enter years of service: "))
if years > 10:
    bonus = 0.10
elif years >= 6:
    bonus = 0.08
else:
    bonus = 0.05
print("Bonus:", bonus * 100, "%")

#Q14
score = int(input("Enter subject score: "))
if score > 90:
    print("Congratulations!")
elif score >= 50:
    print("Needs improvement.")
else:
    print("Consider retaking the course.")

#Q15
age = int(input("Enter age: "))

if age >= 18:
    degree = input("Do you have a degree? (yes/no): ").lower()
    if degree == "yes":
        exp = float(input("Enter years of experience: "))
        if exp > 3:
            print("Highly Eligible")
        elif exp >= 1:
            print("Eligible")
        else:
            print("Under Review")
    else:
        print("Not Eligible (No degree)")
else:
    print("Not Eligible (Age < 18)")

#Q16
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
days = int(input("Enter number of working days: "))
if age >= 18 and age < 30:
    if gender == "M":
        wage = 700
    else:
        wage = 750
elif age >= 30 and age <= 40:
    if gender == "M":
        wage = 800
    else:
        wage = 850
else:
    print("No wage category found")
print("Total wages:", wage * days)

#Q17
is_valid = True
balance = 50000
correct_pin = 123
pin = int(input("Enter PIN: "))
if pin == correct_pin:
    print("1. Withdraw")
    print("2. Check Balance")
    print("3. Exit")
    choice = int(input("Enter option: "))
    if choice == 1:
        amount = int(input("Enter amount: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawn. New balance:", balance)
        else:
            print("Insufficient funds")
    elif choice == 2:
        print("Balance:", balance)
    elif choice == 3:
        print("Thank you for visiting")
    else:
        print("Invalid option")
else:
    print("Wrong PIN")

#Q18
print("Welcome to the Magic Forest")
direction = input("Do you want to go north or south? ").lower()
if direction == "south":
    print("Game Over")
else:
    step2 = input("Do you want to cross the river or follow the path? ").lower()
    
    if step2 == "cross the river":
        print("Game Over")
    else:
        creature = input("Choose: fairy, ogre, or elf: ").lower()
        
        if creature == "elf":
            print("You Win")
        else:
            print("Game Over")

#Q19
print("Welcome to the Haunted House")
direction = input("Do you want to go upstairs or downstairs? ").lower()
if direction == "downstairs":
    print("Game Over")
else:
    step2 = input("Do you want to enter the room or stay outside? ").lower()
    
    if step2 == "enter the room":
        print("Game Over")
    else:
        monster = input("Choose: ghost, vampire, or werewolf: ").lower()
        
        if monster == "werewolf":
            print("You Win")
        else:
            print("Game Over")

# 1. Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 2. Vowel or Consonant
ch = input("Enter a character: ").lower()
if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")

# 3. Minor or Adult
age = int(input("Enter age: "))
if age < 18:
    print("Minor")
else:
    print("Adult")

# 4. Pass or Fail
marks = int(input("Enter marks (0-100): "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# 5. Largest of 3 numbers using if-else only
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

# 6. Month name from number
month = int(input("Enter month number (1-12): "))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid month number")

# 7. Temperature categories
temp = float(input("Enter temperature in Celsius: "))
if temp > 35:
    print("Hot")
elif temp >= 25:
    print("Warm")
else:
    print("Cold")

# 8. Salary classification
salary = int(input("Enter salary: "))
if salary > 50000:
    print("High")
elif salary > 30000:
    print("Medium")
else:
    print("Low")

# 9. Positive, Negative, or Zero
n = float(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# 10. Weekday or Weekend
day = int(input("Enter day number (1-7): "))
if day in (6, 7):
    print("Weekend")
elif 1 <= day <= 5:
    print("Weekday")
else:
    print("Invalid day number")

# 11. Divisible by both 5 and 7
num2 = int(input("Enter a number: "))
if num2 % 5 == 0 and num2 % 7 == 0:
    print("Divisible by both")
else:
    print("Not divisible by both")