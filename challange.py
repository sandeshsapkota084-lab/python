#challenge 1
a=input("Enter full name:")
b=a.lower()
c=b.title()
d=c.lstrip()
e=d.rstrip()
f="_".join(e.split())
print("Your username is:",f)

#challenge 2
pa=input("Enter your secret password:")
pb=pa.lower()
pc=pa.replace('a','@').replace('s','$').replace('i','!').replace('o','0')
print("Your strong password is:",pc +'0##9')

#challenge 3
em=input("Enter your email address:")
un=em[:em.index('@')]
print("Your username is:",un)

#challenge 4
ph=input("Enter your phone number:")
pp=ph.replace('-','').replace(' ','').replace('(','').replace(')','')
print("Your phone number is:",pp)

#challenge 5
n=input("Enter a string:")
m=n.lower().title()
print("Formatted string is:",m)

#challenge 6
s=input("Enter Sentence:")
ts=s.lower().title().split()
j=' '.join(reversed(ts))
print("Reversed Sentence is:",j)