#data structures
#list tuple set dictionary
items1=[1,2,3]
items1.extend([4,5,6])
print(items1)

items2=[1,2,3]
items2.append([4,5,6])
print(items2)

items2=[1,2,3]
items2.insert(1,4)
print(items2)

items3=['Ram','1',3]
a=items3.pop(0)
print(items3)
print(a)

items4=['Ram','1',3]
items4.insert(0,items4.pop(2))
print(items4)

items1+=items2
print(items1)

items1=items1+items2
print(items1)

items=1,2,3,4
items=list(items)
items[3] = '4'
print(tuple(items))

#set1
items=set([1,2,3])
print(items)
items.add(4)
print(items)
items.remove(1)
print(items)
items.discard(3)
print(items)

#set2
items=set([1,2,3])
items1=set([2,4,6])
items2=set([2])
x=set()
a=items.intersection(items1)
print(a)
b=items.difference(items1)
print(b)
c=items.isdisjoint(items1)
print(c)
d=items2.issubset(items)
print(d)
print(type(x))
x.add(4)
x.add(2)
x.update([8,10,6])
print(x)

#dictionary
d={'a':1,'b':2,'c':3,'d':4}
print(d)
print(d['a'])
print(d.get('b'))
print(d)
d.update({'e':5,'f':6})
print(dict(sorted(d.items())))
d.popitem()
del d['c']
print(d)
d.pop('d')
print(d)
print(d.keys())
print(d.values())
print(d.items())