#Ask for username and password and grant access if correct
username = input("Enter username: ")
password = input("Enter password: ")
if username == "I_am_a_user" and password == "I_am_a_password":
    print("Access granted")
else:
    print("Access denied")

#check if a number is between 1 and 100 using and
number = int(input("Enter a number: "))
if number > 1 and number < 100:
    print("Number is between 1 and 100")
else:
    print("Number is not between 1 and 100")

#checks if a year is leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Year is a leap year")
else:
    print("Year is not a leap year")