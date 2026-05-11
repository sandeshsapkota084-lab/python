#positive negative zero
num=int(input("enter a number"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")

#take score and print grade
score=int(input("enter score"))
if score>=90:
    print("grade A")
elif score>=80:
    print("grade B")
elif score>=70:
    print("grade C")
elif score>=60:
    print("grade D")
else:
    print("grade F")

#ask age and print ticket price
age=int(input("enter age"))
if age<12:
    print("$5")
elif age>=12 and age<=64:
    print("$10")
else:
    print("$7")