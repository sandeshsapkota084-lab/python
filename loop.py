#for loop
data='ram'
for i in data:
    print(i,end=' ')

data='python'
for i in data:
    print(i)

items=[1,2,3,4,5]
for i in items:
    if i%2==0:
        print(i)

items=[1,2,3,4,5,6,7,8]
even=[]
odd=[]
for i in items:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even:",even)
print("odd:",odd)

items=[10,23,45,67,89,90,34,22,11,'ab','cd']
enum=[]
onus=[]
lett=[]
for i in items:
    if type(i)==int:
        if i%2==0:
            enum.append(i)
        else:
            onus.append(i)
    else:
        lett.append(i)
print("even numbers:",enum)
print("odd numbers:",onus)
print("letters:",lett)

items=[1,2,3,'a','b','c',4,5,6,'d',-1,-2,-28]
num=[]
lett=[]
for i in items:
    if type(i)==int:
        if i>0 and i%2==0:
            num.append(i)
    elif type(i)==str:
        lett.append(i)
print("positive numbers:",num)
print("letters:",lett)

items=[1,2,3,4,5,6,7,8,'a','b']
odd=[]
even=[]
letters=[]
for i in items:
    if type(i)==int:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    else:
        letters.append(i)
print(odd)
print(even)
print(letters)

sty="programming"
vowels=set()
consonants=set()
for i in sty:
    if i in 'aeiou':
        vowels.add(i)
    else:
        consonants.add(i)
print("Vowel:",vowels)
print("consonant:",consonants)

items=[12,23,34,45,56,67,78,89,90,11,22,33,44,55]
even_sum=0
for i in items:
    if i%2==0:
        even_sum+=i
print("Sum of even numbers:",even_sum)

grocery=['apple','bread','milk','eggs']
a=int(input("Enter the index number (1-4): "))
for i in range(len(grocery)):
    if i+1==a:
        print(grocery[i])

grocery=['apple','bread','milk','eggs','cheese','butter']
for i in range(len(grocery)):
    print(f"{i+1}. {grocery[i]}")

student_names=['Ram','Hari','Sita']
for i in range(len(student_names)):
    print(f"Hi {student_names[i]},your course approval is ready!")

num=11
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")