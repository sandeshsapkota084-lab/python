items={'1.':{'question':'which symbol is used to comment in python',
             'options':{'a':'/','b':'#','c':'//','d':'*/*'},'correct_answer':'b'},
       '2.':{'question':'which method is used to add a element in list',
             'options':{'a':'append()','b':'add()','c':'addlist()','d':'update()'},'correct_answer':'a'}}
score=0
for i,j  in items.items():
    print(i,'',j['question'])
    for key,value in j['options'].items():
        print(key,'',value)
    guess=input('choose the correct options:(a,b,c,d)')
    if guess==j['correct_answer']:
        score+=1
print(f'final score is:{score}')

str=input("Enter the Desired String = ")
vowel=[]
for i in str:
    if i in 'aeiou' and i not in vowel:
        vowel.append(i)
print(vowel)

dictionary = {}
user_input = int(input('how many words do you want to add: '))
for i in range(0, user_input + 1):
    choice = int(input('press 1. add 2. display 3. remove 4. exit: '))
    if choice == 1:
        word = input('enter a word: ')
        if word in dictionary:
            print(f'{word} already exists')
        else:
            meaning = input('enter a meaning of given word: ')
            dictionary[word] = meaning
    elif choice == 2:
        for i, j in dictionary.items():
            print(i, ':', j)
    elif choice == 3:
        word = input('enter a word you want to remove: ')
        if word not in dictionary:
            print(f'{word} not found')
        else:
            dictionary.pop(word)
    elif choice == 4:
        break
    else:
        print('invalid choice')

#1
t=0
while True:
    n= int(input("Enter a positive integer (0 to stop): "))
    if n==0:
        break
    elif n>0:
        t+=n
    else:
        print("Please enter only positive integers.")
print("The total sum is:",t)

#2
count=1
nu=int(input("Enter a positive integer to count down from: "))
print(nu)
while nu>1:
    if nu==1:
        break
    nu-=1
    print(nu)
    if nu==1:
        print("Countdown finished!")

#3
import random
number_to_guess = random.randint(1, 100)
co=0
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    co+=1
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {co} attempts.")
        break

#4
while True:
    pas=input("Enter password: ")
    if len(pas)<8:
        print("Password must be at least 8 characters long.")
    elif not any(char.isdigit() for char in pas):
        print("Password must contain at least one digit.")
    elif not any(char.isupper() for char in pas):
        print("Password must contain at least one uppercase letter.")
    elif not any(char.islower() for char in pas):
        print("Password must contain at least one lowercase letter.")
    else:
        print("Password is valid.")
        break

#5
total=0
count=1
while count <= 50:
    total += count
    count += 1
print("The total sum from 1 to 50 is:", total)

#6
num = int(input("Enter a number to print its table: "))
i=1
while i<=10:
    print(num, "x", i, "=", num * i)
    i += 1

#7
import random
rand_num=random.randint(1,50)
guess=0
count=0
while guess != rand_num:
    guess=int(input("Guess the number between 1 and 50: "))
    count += 1
    if count<=7:
        if guess < rand_num:
            print("Too low! Try again.")
        elif guess > rand_num:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {rand_num} in {count} attempts.")
    if count > 7:
        print(f"Sorry, you've exceeded the maximum number of attempts. The number was {rand_num}.")

#8
p1_s=0
p2_s=0
while True:
    p1=input("Player 1 - Enter rock, paper or scissors: ")
    p2=input("Player 2 - Enter rock, paper or scissors: ")
    if p1_s<5 and p2_s<5:
        if p1==p2:
            print("It's a tie")
        elif (p1=="rock" and p2=="scissors") or (p1=="scissors" and p2=="paper") or (p1=="paper" and p2=="rock"):
            print("Player 1 wins this round!")
            p1_s+=1
        else:
            print("Player 2 wins this round!")
            p2_s+=1
    elif p1_s==5 and p2_s!=5:
        print("Player 1 wins the game!")
        break
    else:
        print("Player 2 wins the game!")
        break

#1
while True:
    age = input("Enter age (or 'stop'): ")
    if age == "stop":
        break
    age = int(age)
    if age < 18:
        print("You are a minor.")
    elif 18 <= age <= 60:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")

#2
while True:
    vehicle = input("Enter vehicle: ")
    if vehicle == "bus":
        print("finally the wait is over")
        break
    print("waiting")

#3
while True:
    fruit = input("Enter fruit: ")
    if fruit == "apple":
        print("You got it!")
        break
    print("Try again")

#4
while True:
    pwd = input("Enter password: ")
    if pwd == "open sesame":
        print("Access granted!")
        break
    print("Wrong password, try again.")

#5
ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
content_ratings = {}
i = 0
while i < len(ratings):
    rating = ratings[i]
    if rating in content_ratings:
        content_ratings[rating] += 1
    else:
        content_ratings[rating] = 1
    i += 1
print(content_ratings)

#6
import random
num = random.randint(1, 10)
attempts = 0
while True:
    guess = int(input("Guess 1-10: "))
    attempts += 1
    if guess == num:
        print(f"Correct! Attempts: {attempts}")
        break
    elif guess < num:
        print("guess higher")
    else:
        print("guess lower")

#7
attempts = 0
while attempts < 3:
    user = input("Username: ")
    pwd = input("Password: ")
    if user == "admin" and pwd == "1234":
        print("Login successful")
        break
    print("Invalid credentials, try again.")
    attempts += 1
else:
    print("Too many failed attempts.")

#8
import random
while True:
    a = random.randint(1, 30)
    b = random.randint(1, 30)
    while True:
        ans = input(f"{a} * {b} = (or 'exit'): ")
        if ans == "exit":
            exit()
        if int(ans) == a * b:
            print("Correct!")
            break
        print("Incorrect, try again.")

#9
while True:
    n = input("Enter number (or 'exit'): ")
    if n == "exit":
        break
    n = int(n)
    if n < 2:
        print("The number is not prime.")
        continue
    prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prime = False
            break
    print("The number is prime." if prime else "The number is not prime.")

#10
while True:
    guess = input("Guess word (or 'quit'): ")
    if guess == "quit":
        break
    if guess == "python":
        print("Congratulations, you guessed the word!")
        break
    print("Incorrect, try again")

#11
count = 0
while count < 3:
    name = input("Enter name: ")
    if name == "good luck":
        count += 1
        if count < 3:
            print(f"You typed the same word {count} times.")
        else:
            print("You typed good luck three times.")

#12
floor = 1
while True:
    dest = input("Destination floor (0 to exit): ")
    if dest == "0":
        print("Goodbye!")
        break
    try:
        dest = int(dest)
        if dest == floor:
            print("Already on this floor.")
        elif dest > floor:
            print("Going up")
        else:
            print("Going down")
        floor = dest
    except ValueError:
        print("Invalid input, enter a number.")

students = ["Ram", "Hari"]
while True:
    print("\n--- Student Management System ---")
    print("1. Create (Add Student)")
    print("2. Read (View Students)")
    print("3. Update (Edit Student)")
    print("4. Delete (Remove Student)")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        name = input("Enter student name to add: ")
        students.append(name)
        print(f"'{name}' added successfully!")
    elif choice == "2":
        if len(students) == 0:
            print("No students found. The list is empty.")
        else:
            print("\nList of Students:")
            for index, student in enumerate(students):
                print(f"{index} → {student}")
    elif choice == "3":
        if len(students) == 0:
            print("No students available to update.")
        else:
            try:
                index = int(input("Enter index number to update: "))
                if 0 <= index < len(students):
                    new_name = input("Enter new name: ")
                    students[index] = new_name
                    print("Update complete!")
                else:
                    print("Invalid index. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    elif choice == "4":
        if len(students) == 0:
            print("No students available to delete.")
        else:
            try:
                index = int(input("Enter index number to delete: "))
                if 0 <= index < len(students):
                    removed_student = students.pop(index)
                    print(f"'{removed_student}' deleted successfully!")
                else:
                    print("Invalid index. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif choice == "5":
        print("Exiting Student Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

library = [{"title": "Python Basics", "author": "John Doe"},{"title": "Data Structures", "author": "Jane Smith"}]
while True:
    print("\n--- Library Book Management System ---")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Update Book")
    print("4. Remove Book")
    print("5. Search Book")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        library.append({"title": title, "author": author})
        print(f"Book '{title}' by {author} added successfully!")
    elif choice == "2":
        if len(library) == 0:
            print("No books found in the library.")
        else:
            print("\nList of Books:")
            for index, book in enumerate(library):
                print(f"{index} → Title: {book['title']}, Author: {book['author']}")
    elif choice == "3":
        if len(library) == 0:
            print("No books available to update.")
        else:
            try:
                index = int(input("Enter index number to update: "))
                if 0 <= index < len(library):
                    print(f"Current Book → Title: {library[index]['title']}, Author: {library[index]['author']}")
                    new_title = input("Enter new title (leave blank to keep current): ")
                    new_author = input("Enter new author (leave blank to keep current): ")
                    if new_title.strip():
                        library[index]['title'] = new_title
                    if new_author.strip():
                        library[index]['author'] = new_author
                    print("Book updated successfully!")
                else:
                    print("Invalid index number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif choice == "4":
        if len(library) == 0:
            print("No books available to remove.")
        else:
            try:
                index = int(input("Enter index number to remove: "))
                if 0 <= index < len(library):
                    removed_book = library.pop(index)
                    print(f"Book '{removed_book['title']}' removed successfully!")
                else:
                    print("Invalid index number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif choice == "5":
        if len(library) == 0:
            print("No books found in the library.")
        else:
            search_title = input("Enter book title to search: ").lower()
            found_books = [book for book in library if search_title in book['title'].lower()]
            if found_books:
                print("\nSearch Results:")
                for book in found_books:
                    print(f"Title: {book['title']}, Author: {book['author']}")
            else:
                print("Book not found.")
    elif choice == "6":
        print("Exiting Library Book Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

items = [3, 4, 5]
i = 0
while i < len(items):
    num = items[i]
    print(f"\nMultiplication Table for {num}:")
    j = 1
    while j <= 10:
        print(f"{num} x {j} = {num * j}")
        j += 1
    i += 1

dict={}
def sum():
    total = 0
    for value in dict.values():
        total += value
    return total

#name starting with r and ending with m using filter function
names = ['ram', 'shyam', 'rotem', 'ravi', 'mohan', 'rahim']
result = list(filter(lambda name: name.startswith('r') and name.endswith('m'), names))
print(result)

#1
items = ['sql', '123', 'python']
alphabetic_items = list(filter(lambda x: x.isalpha(), items))
print(alphabetic_items)

#2
products = [{'id': 1, 'name': 'laptop', 'category': 'electronics', 'price': 1200, 'instock': True},{'id': 2, 'name': 'smartphone', 'category': 'electronics', 'price': 800, 'instock': False}]
instock_products = list(filter(lambda p: p['instock'], products))
print(instock_products)

#3
def calculate_sum(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total
print(calculate_sum(1, 5))
print(calculate_sum(10, 15))

#4
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
def calculator():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue
            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
        else:
            print("Invalid choice! Please select a valid option.")
calculator()

#5
course = [{'title': 'Ancient Civilizations', 'genre': 'history'},{'title': 'Corporate Finance', 'genre': 'commerce'},{'title': 'Modern World History', 'genre': 'history'}]
history_courses = list(filter(lambda c: c['genre'] == 'history', course))
print(history_courses)

#6
emails = ['ram.sharma@gmail.com', 'spam@hooya.com', 'virus@malware.net', 'shyam.kumar@workcorp.com']
blacklist = ('@hooya.com', '@malware.net')
spam_emails = list(filter(lambda email: any(domain in email for domain in blacklist), emails))
print(spam_emails)

#7
price = [100, 50, 200, 75]
discounted_prices = list(map(lambda p: p * 0.8, price))
print(discounted_prices)

#8
def skip_two(lst):
    return [lst[i] for i in range(1, min(len(lst), 12), 3)]
print(skip_two([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]))

#9
def remove_at_idx(lst, idx):
    if idx < 0 or idx >= len(lst):
        return "Error: Index out of range"
    return lst[:idx] + lst[idx+1:]
print(remove_at_idx([10, 20, 30, 40, 50], 2))

#10
def clean_input(user_input):
    cleaned = ''.join([ch if ch.isalnum() else '#' for ch in user_input])
    return cleaned
text = input("Enter your message: ")
print("Cleaned message:", clean_input(text))

#11
users_db = {}
def register_user(username, password, email):
    if username in users_db:
        return "Username already exists"
    else:
        users_db[username] = {"password": password, "email": email}
        return f"Registration successful for {username}"
def login_user(username, password):
    if username not in users_db:
        return "User not found"
    elif users_db[username]["password"] != password:
        return "Incorrect password"
    else:
        return f"Welcome back, {username}"
print(register_user("ram", "ram123", "ram@email.com"))
print(register_user("shyam", "shyam456", "shyam@email.com"))
print(register_user("hari", "hari231", "hari@email.com"))
print(login_user("ram", "ram123"))
print(login_user("shyam", "wrongpass"))
print(login_user("unknown", "test123"))

#12
inventory = [{'name': 'Laptop', 'price': 50000, 'quantity': 5}]
def add_product(name, price, quantity):
    for product in inventory:
        if product['name'].lower() == name.lower():
            return "Error: Product already exists!"
    if price <= 0 or quantity <= 0:
        return "Error: Price and quantity must be positive numbers!"
    inventory.append({'name': name, 'price': price, 'quantity': quantity})
    return f"Product '{name}' added successfully!"
def view_products():
    print("\n--- Inventory ---")
    print("{:<15} {:<10} {:<10}".format("Name", "Price", "Quantity"))
    print("-" * 40)
    for product in inventory:
        print("{:<15} {:<10} {:<10}".format(product['name'], product['price'], product['quantity']))
def update_product(name, price=None, quantity=None):
    for product in inventory:
        if product['name'].lower() == name.lower():
            if price is not None:
                if price <= 0:
                    return "Error: Price must be positive!"
                product['price'] = price
            if quantity is not None:
                if quantity <= 0:
                    return "Error: Quantity must be positive!"
                product['quantity'] = quantity
            return f"Product '{name}' updated successfully!"
    return "Error: Product not found!"
def delete_product(name):
    for product in inventory:
        if product['name'].lower() == name.lower():
            inventory.remove(product)
            return f"Product '{name}' deleted successfully!"
    return "Error: Product not found!"

#13
contacts = [{'name': 'Ram kc', 'phone': '9801234567', 'email': 'ram@email.com'}]
def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10
def validate_email(email):
    return '@' in email and '.' in email
def is_duplicate(name):
    return any(contact['name'].lower() == name.lower() for contact in contacts)
def add_contact(name, phone, email):
    if is_duplicate(name):
        return "Error: Contact already exists!"
    if not validate_phone(phone):
        return "Error: Invalid phone number! Must be 10 digits."
    if not validate_email(email):
        return "Error: Invalid email format!"
    contacts.append({'name': name, 'phone': phone, 'email': email})
    return f"Contact '{name}' added successfully!"
def display_contacts():
    print("\n--- Contact List ---")
    print("{:<20} {:<15} {:<25}".format("Name", "Phone", "Email"))
    print("-" * 60)
    for contact in contacts:
        print("{:<20} {:<15} {:<25}".format(contact['name'], contact['phone'], contact['email']))
def search_contact(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            return contact
    return "Error: Contact not found!"
def update_contact(name, phone=None, email=None):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            if phone:
                if not validate_phone(phone):
                    return "Error: Invalid phone number!"
                contact['phone'] = phone
            if email:
                if not validate_email(email):
                    return "Error: Invalid email format!"
                contact['email'] = email
            return f"Contact '{name}' updated successfully!"
    return "Error: Contact not found!"
def delete_contact(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            return f"Contact '{name}' deleted successfully!"
    return "Error: Contact not found!"
def sort_contacts():
    contacts.sort(key=lambda c: c['name'].lower())
    return "Contacts sorted alphabetically!"
def menu():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add contact")
        print("2. Display all contacts")
        print("3. Search contact by name")
        print("4. Update contact information")
        print("5. Delete contact")
        print("6. Sort contacts alphabetically")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone (10 digits): ")
            email = input("Enter email: ")
            print(add_contact(name, phone, email))
        elif choice == '2':
            display_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            result = search_contact(name)
            print(result if isinstance(result, str) else result)
        elif choice == '4':
            name = input("Enter name to update: ")
            phone = input("Enter new phone (or press Enter to skip): ")
            email = input("Enter new email (or press Enter to skip): ")
            phone = phone if phone else None
            email = email if email else None
            print(update_contact(name, phone, email))
        elif choice == '5':
            name = input("Enter name to delete: ")
            print(delete_contact(name))
        elif choice == '6':
            print(sort_contacts())
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")
menu()