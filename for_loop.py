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