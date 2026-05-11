#nested for loop
a=[[1,2],[4,5,6],[7,8,9]]
for i in a:
    for j in i:
        print(j,end=' ')
    print()

#multiplication table
a=[4,5,6,7]
for i in a:
    for j in range(1,11):
        print(i,'x',j,'=',i*j)
    print()

#accessing tables of 4 and 6 only
a=[4,5,6,7]
for i in a:
    if i==4 or i==6:
        for j in range(1,11):
            print(i,'x',j,'=',i*j)
        print()

for x in [5,10,15]:
    count=0
    count=count+1
print(count)

emails=[1,2,3]
for m in emails:
    print("New mail arrived")
print("No new mail")

points=[1,2,3]
for p in points:
    print(p*2)

friends=["Aman","Sara","John"]
for f in friends:
    if f=="Sara":
        continue
    print("Hello",f)

a=[3,5,7,13]
sum=0
c=2
for i in range(4):
    sum=sum+a[c]
print(sum)