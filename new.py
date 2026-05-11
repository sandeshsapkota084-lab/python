var1=int(input("Enter a number: "))
var2=float(input("Enter another number: "))
var3=str(input("Enter a string: "))
var4=bool(input("Enter a boolean value (True/False): "))
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))

#convert string to integer and adding something to it
str_num=input("Enter a number as a string: ")
int_num=int(str_num)
print("The integer value is:",int_num)
print("The integer value plus 50 is:",int_num + 50)

#creating a list of 3 fruits and a dictionary with name and age
fruits=["apple","banana","orange"]
print("List of fruits:",fruits)
person={"name":"Sandesh","age":18}
print("Dictionary with name and age:",person)